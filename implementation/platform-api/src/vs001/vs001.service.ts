import { createHash } from 'node:crypto';
import { Inject, Injectable } from '@nestjs/common';
import { parseTelemetryEventV1, type TelemetryEventV1 } from './contracts.js';
import {
  ENERGY_GRAPH_PORT,
  EVIDENCE_REPOSITORY,
  OPTIMIZER_PORT,
  TARIFF_RESOLUTION_PORT,
} from './ports.js';
import type {
  EnergyGraphPort,
  EvidenceRecord,
  EvidenceRepository,
  OptimizerPort,
  ShadowRecommendation,
  TariffResolutionPort,
} from './ports.js';

export type Vs001Result =
  | {
      kind: 'COMPLETED';
      event: TelemetryEventV1;
      recommendation: ShadowRecommendation;
      evidence: EvidenceRecord;
      cost: {
        currency: string;
        amount: string;
        tariffVersionRef: string;
        calculationRef: string;
      };
    }
  | {
      kind: 'FAIL_CLOSED';
      event: TelemetryEventV1;
      code: string;
      message: string;
      evidence: EvidenceRecord;
    };

function stableEvidenceId(event: TelemetryEventV1, suffix: string): string {
  const material = [
    event.schemaVersion,
    event.tenantId,
    event.siteId,
    event.deviceId,
    event.pointId,
    event.metric,
    String(event.value),
    event.unit,
    event.observedAt,
    suffix,
  ].join('|');

  return `ev-${createHash('sha256').update(material).digest('hex').slice(0, 24)}`;
}

function evidenceTime(event: TelemetryEventV1): string {
  return new Date(event.observedAt).toISOString();
}

@Injectable()
export class Vs001Service {
  constructor(
    @Inject(ENERGY_GRAPH_PORT)
    private readonly energyGraph: EnergyGraphPort,
    @Inject(TARIFF_RESOLUTION_PORT)
    private readonly tariff: TariffResolutionPort,
    @Inject(OPTIMIZER_PORT)
    private readonly optimizer: OptimizerPort,
    @Inject(EVIDENCE_REPOSITORY)
    private readonly evidenceRepository: EvidenceRepository,
  ) {}

  async evaluate(input: unknown): Promise<Vs001Result> {
    const event = parseTelemetryEventV1(input);
    const context = await this.energyGraph.resolve(event);

    if (context === null) {
      const evidence: EvidenceRecord = {
        schemaVersion: '1.0',
        evidenceId: stableEvidenceId(event, 'ENERGY_GRAPH_UNRESOLVED'),
        status: 'UNKNOWN',
        subject: 'VS-001 Energy Graph resolution failed closed',
        recordedAt: evidenceTime(event),
        sourceRefs: ['docs/05-mvp/vertical-slices/VS-001-energy-intelligence-loop.md'],
        notes: 'No settlement context was resolved for this telemetry point.',
      };
      await this.evidenceRepository.save(evidence);
      return {
        kind: 'FAIL_CLOSED',
        event,
        code: 'ENERGY_GRAPH_UNRESOLVED',
        message: 'No Energy Graph settlement context resolved.',
        evidence,
      };
    }

    if (context.tenantId !== event.tenantId || context.siteId !== event.siteId) {
      const evidence: EvidenceRecord = {
        schemaVersion: '1.0',
        evidenceId: stableEvidenceId(event, 'TENANT_SITE_MISMATCH'),
        status: 'UNKNOWN',
        subject: 'VS-001 tenant/site boundary mismatch',
        recordedAt: evidenceTime(event),
        sourceRefs: ['docs/04-engineering/module-boundaries/README.md'],
        notes: 'Resolved context did not match telemetry tenant/site identity.',
      };
      await this.evidenceRepository.save(evidence);
      return {
        kind: 'FAIL_CLOSED',
        event,
        code: 'TENANT_SITE_MISMATCH',
        message: 'Resolved Energy Graph context violates tenant/site boundary.',
        evidence,
      };
    }

    const tariff = await this.tariff.evaluate(event, context);
    if (tariff.kind === 'UNRESOLVED') {
      const evidence: EvidenceRecord = {
        schemaVersion: '1.0',
        evidenceId: stableEvidenceId(event, tariff.code),
        status: tariff.evidenceStatus,
        subject: 'VS-001 tariff resolution failed closed',
        recordedAt: evidenceTime(event),
        sourceRefs: [
          'docs/00-authority/decisions/OPEN-QUESTIONS.md',
          'docs/00-authority/decisions/DECISIONS.md',
        ],
        notes: `${tariff.code}: ${tariff.message}`,
      };
      await this.evidenceRepository.save(evidence);
      return {
        kind: 'FAIL_CLOSED',
        event,
        code: tariff.code,
        message: tariff.message,
        evidence,
      };
    }

    const evidence: EvidenceRecord = {
      schemaVersion: '1.0',
      evidenceId: stableEvidenceId(event, tariff.cost.calculationRef),
      status: 'DERIVED',
      subject: 'VS-001 deterministic economic evaluation',
      recordedAt: evidenceTime(event),
      sourceRefs: [
        tariff.cost.tariffVersionRef,
        tariff.cost.calculationRef,
        'docs/05-mvp/vertical-slices/VS-001-energy-intelligence-loop.md',
      ],
      derivation: 'Tariff cost returned by the authoritative tariff-resolution port.',
    };

    await this.evidenceRepository.save(evidence);

    const recommendation = await this.optimizer.recommend({
      event,
      context,
      cost: tariff.cost,
      evidenceRef: evidence.evidenceId,
    });

    if (recommendation.mode !== 'SHADOW') {
      throw new Error('VS-001 optimizer must return SHADOW mode');
    }

    return {
      kind: 'COMPLETED',
      event,
      recommendation,
      evidence,
      cost: tariff.cost,
    };
  }
}
