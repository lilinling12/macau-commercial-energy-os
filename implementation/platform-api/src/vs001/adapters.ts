import { Injectable } from '@nestjs/common';
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

@Injectable()
export class FailClosedEnergyGraphAdapter implements EnergyGraphPort {
  async resolve(_event: TelemetryEventV1): Promise<EnergyGraphContext | null> {
    return null;
  }
}

@Injectable()
export class FailClosedTariffAdapter implements TariffResolutionPort {
  async evaluate(
    _event: TelemetryEventV1,
    _context: EnergyGraphContext,
  ): Promise<TariffResolution> {
    return {
      kind: 'UNRESOLVED',
      code: 'TARIFF_ADAPTER_NOT_BOUND',
      message:
        'No authoritative tariff-core adapter is configured. Settlement evaluation is blocked.',
      evidenceStatus: 'UNKNOWN',
    };
  }
}

@Injectable()
export class FailClosedOptimizerAdapter implements OptimizerPort {
  async recommend(_input: {
    event: TelemetryEventV1;
    context: EnergyGraphContext;
    cost: SettledCost;
    evidenceRef: string;
  }): Promise<ShadowRecommendation> {
    throw new Error('Optimizer adapter must not run without resolved tariff context');
  }
}

@Injectable()
export class InMemoryEvidenceRepository implements EvidenceRepository {
  private readonly records = new Map<string, EvidenceRecord>();

  async save(record: EvidenceRecord): Promise<void> {
    this.records.set(record.evidenceId, structuredClone(record));
  }

  get(evidenceId: string): EvidenceRecord | undefined {
    const record = this.records.get(evidenceId);
    return record === undefined ? undefined : structuredClone(record);
  }
}
