import { readFile } from 'node:fs/promises';
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

class ReplayGraph implements EnergyGraphPort {
  async resolve(event: TelemetryEventV1): Promise<EnergyGraphContext> {
    return {
      tenantId: event.tenantId,
      siteId: event.siteId,
      assetRef: 'asset/site-import',
      meterRef: 'meter/settlement-001',
      contractRef: 'contract/synthetic-v1',
    };
  }
}

class ReplayTariff implements TariffResolutionPort {
  async evaluate(
    _event: TelemetryEventV1,
    _context: EnergyGraphContext,
  ): Promise<TariffResolution> {
    return {
      kind: 'RESOLVED',
      cost: {
        currency: 'MOP',
        amount: '12.500000',
        tariffVersionRef: 'tariff/synthetic-v1',
        calculationRef: 'calc/vs001-fixture-v1',
      },
    };
  }
}

class ReplayOptimizer implements OptimizerPort {
  async recommend(input: {
    event: TelemetryEventV1;
    context: EnergyGraphContext;
    cost: SettledCost;
    evidenceRef: string;
  }): Promise<ShadowRecommendation> {
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

class ReplayEvidence implements EvidenceRepository {
  async save(_record: EvidenceRecord): Promise<void> {
    // Replay output is returned by the domain service; persistence is intentionally
    // side-effect free in this fixture adapter.
  }
}

const fixtureUrl = new URL('../../fixtures/vs001/replay-input.json', import.meta.url);
const fixture = JSON.parse(await readFile(fixtureUrl, 'utf-8')) as unknown;

const service = new Vs001Service(
  new ReplayGraph(),
  new ReplayTariff(),
  new ReplayOptimizer(),
  new ReplayEvidence(),
);

const result = await service.evaluate(fixture);

process.stdout.write(`${JSON.stringify(result, null, 2)}\n`);
