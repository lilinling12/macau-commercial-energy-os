import assert from 'node:assert/strict';
import { access } from 'node:fs/promises';
import test from 'node:test';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import type { TelemetryEventV1 } from './contracts.js';
import type {
  EnergyGraphContext,
  EnergyGraphPort,
  EvidenceRecord,
  EvidenceRepository,
  OptimizerPort,
  SettledCost,
  ShadowRecommendation,
  TariffResolution,
  TariffResolutionPort,
} from './ports.js';
import { Vs001Service } from './vs001.service.js';

const EVENT: TelemetryEventV1 = {
  schemaVersion: '1.0',
  tenantId: 'tenant-demo',
  siteId: 'site-demo',
  deviceId: 'meter-001',
  pointId: 'energy-import',
  metric: 'energy_import',
  value: 10,
  unit: 'kWh',
  quality: 'GOOD',
  observedAt: '2026-10-03T00:00:00Z',
  source: 'synthetic-vs001',
};

const CONTEXT: EnergyGraphContext = {
  tenantId: 'tenant-demo',
  siteId: 'site-demo',
  assetRef: 'asset/site-import',
  meterRef: 'meter/settlement-001',
  contractRef: 'contract/synthetic-c1',
};

class StaticGraph implements EnergyGraphPort {
  constructor(private readonly context: EnergyGraphContext | null = CONTEXT) {}

  async resolve(_event: TelemetryEventV1): Promise<EnergyGraphContext | null> {
    return this.context;
  }
}

class StaticTariff implements TariffResolutionPort {
  constructor(
    private readonly result: TariffResolution = {
      kind: 'RESOLVED',
      cost: {
        currency: 'MOP',
        amount: '12.500000',
        tariffVersionRef: 'tariff/synthetic-v1',
        calculationRef: 'calc/vs001-fixture-v1',
      },
    },
  ) {}

  async evaluate(
    _event: TelemetryEventV1,
    _context: EnergyGraphContext,
  ): Promise<TariffResolution> {
    return this.result;
  }
}

class StaticOptimizer implements OptimizerPort {
  calls = 0;

  async recommend(input: {
    event: TelemetryEventV1;
    context: EnergyGraphContext;
    cost: SettledCost;
    evidenceRef: string;
  }): Promise<ShadowRecommendation> {
    this.calls += 1;
    return {
      schemaVersion: '1.0',
      recommendationId: 'rec/vs001-fixture-v1',
      tenantId: input.event.tenantId,
      siteId: input.event.siteId,
      mode: 'SHADOW',
      createdAt: input.event.observedAt,
      validFrom: input.event.observedAt,
      validUntil: '2026-10-03T00:30:00Z',
      objective: {
        type: 'ECONOMIC_COST',
        currency: input.cost.currency,
      },
      actions: [],
      evidenceRefs: [input.evidenceRef],
      safetyReviewRequired: true,
    };
  }
}

class MemoryEvidence implements EvidenceRepository {
  readonly records: EvidenceRecord[] = [];

  async save(record: EvidenceRecord): Promise<void> {
    this.records.push(structuredClone(record));
  }
}

test('VS-001 completes only after graph and tariff resolution', async () => {
  const evidence = new MemoryEvidence();
  const optimizer = new StaticOptimizer();
  const service = new Vs001Service(
    new StaticGraph(),
    new StaticTariff(),
    optimizer,
    evidence,
  );

  const result = await service.evaluate(EVENT);

  assert.equal(result.kind, 'COMPLETED');
  if (result.kind !== 'COMPLETED') {
    return;
  }

  assert.equal(result.cost.amount, '12.500000');
  assert.equal(result.recommendation.mode, 'SHADOW');
  assert.equal(result.recommendation.actions.length, 0);
  assert.equal(optimizer.calls, 1);
  assert.equal(evidence.records.length, 1);
  assert.equal(result.evidence.status, 'DERIVED');
});

test('VS-001 fails closed on unresolved tariff and never calls optimizer', async () => {
  const evidence = new MemoryEvidence();
  const optimizer = new StaticOptimizer();
  const service = new Vs001Service(
    new StaticGraph(),
    new StaticTariff({
      kind: 'UNRESOLVED',
      code: 'U-001',
      message: 'CEM Pu settlement interval is not verified.',
      evidenceStatus: 'UNKNOWN',
    }),
    optimizer,
    evidence,
  );

  const result = await service.evaluate(EVENT);

  assert.equal(result.kind, 'FAIL_CLOSED');
  if (result.kind !== 'FAIL_CLOSED') {
    return;
  }

  assert.equal(result.code, 'U-001');
  assert.equal(result.evidence.status, 'UNKNOWN');
  assert.equal(optimizer.calls, 0);
});

test('VS-001 rejects cross-tenant Energy Graph resolution', async () => {
  const evidence = new MemoryEvidence();
  const optimizer = new StaticOptimizer();
  const service = new Vs001Service(
    new StaticGraph({
      ...CONTEXT,
      tenantId: 'tenant-other',
    }),
    new StaticTariff(),
    optimizer,
    evidence,
  );

  const result = await service.evaluate(EVENT);

  assert.equal(result.kind, 'FAIL_CLOSED');
  if (result.kind !== 'FAIL_CLOSED') {
    return;
  }

  assert.equal(result.code, 'TENANT_SITE_MISMATCH');
  assert.equal(optimizer.calls, 0);
});

test('VS-001 evidence identifier is deterministic for identical replay input', async () => {
  const first = new Vs001Service(
    new StaticGraph(),
    new StaticTariff(),
    new StaticOptimizer(),
    new MemoryEvidence(),
  );
  const second = new Vs001Service(
    new StaticGraph(),
    new StaticTariff(),
    new StaticOptimizer(),
    new MemoryEvidence(),
  );

  const a = await first.evaluate(EVENT);
  const b = await second.evaluate(EVENT);

  assert.equal(a.evidence.evidenceId, b.evidence.evidenceId);
});


const repositoryRoot = resolve(dirname(fileURLToPath(import.meta.url)), '../../../../');

async function assertRepositorySourcesResolve(sourceRefs: readonly string[]): Promise<void> {
  for (const sourceRef of sourceRefs) {
    if (!(sourceRef.startsWith('docs/') || sourceRef.startsWith('mvp/'))) {
      continue;
    }
    await access(resolve(repositoryRoot, sourceRef));
  }
}

test('VS-001 emitted documentation source references resolve on the repository tree', async () => {
  const evidence = new MemoryEvidence();
  const optimizer = new StaticOptimizer();

  const unresolvedGraph = await new Vs001Service(
    new StaticGraph(null),
    new StaticTariff(),
    optimizer,
    evidence,
  ).evaluate(EVENT);
  assert.equal(unresolvedGraph.kind, 'FAIL_CLOSED');
  await assertRepositorySourcesResolve(unresolvedGraph.evidence.sourceRefs);

  const mismatchedGraph = await new Vs001Service(
    new StaticGraph({ ...CONTEXT, siteId: 'site-other' }),
    new StaticTariff(),
    optimizer,
    evidence,
  ).evaluate(EVENT);
  assert.equal(mismatchedGraph.kind, 'FAIL_CLOSED');
  await assertRepositorySourcesResolve(mismatchedGraph.evidence.sourceRefs);

  const unresolvedTariff = await new Vs001Service(
    new StaticGraph(),
    new StaticTariff({
      kind: 'UNRESOLVED',
      code: 'U-001',
      message: 'CEM Pu settlement interval is not verified.',
      evidenceStatus: 'UNKNOWN',
    }),
    optimizer,
    evidence,
  ).evaluate(EVENT);
  assert.equal(unresolvedTariff.kind, 'FAIL_CLOSED');
  await assertRepositorySourcesResolve(unresolvedTariff.evidence.sourceRefs);

  const completed = await new Vs001Service(
    new StaticGraph(),
    new StaticTariff(),
    optimizer,
    evidence,
  ).evaluate(EVENT);
  assert.equal(completed.kind, 'COMPLETED');
  await assertRepositorySourcesResolve(completed.evidence.sourceRefs);
});
