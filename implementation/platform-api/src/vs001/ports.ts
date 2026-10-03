export const ENERGY_GRAPH_PORT = Symbol('ENERGY_GRAPH_PORT');
export const TARIFF_RESOLUTION_PORT = Symbol('TARIFF_RESOLUTION_PORT');
export const OPTIMIZER_PORT = Symbol('OPTIMIZER_PORT');
export const EVIDENCE_REPOSITORY = Symbol('EVIDENCE_REPOSITORY');

import type { TelemetryEventV1 } from './contracts.js';

export interface EnergyGraphContext {
  tenantId: string;
  siteId: string;
  assetRef: string;
  meterRef: string;
  contractRef: string;
}

export interface EnergyGraphPort {
  resolve(event: TelemetryEventV1): Promise<EnergyGraphContext | null>;
}

export interface SettledCost {
  currency: string;
  amount: string;
  tariffVersionRef: string;
  calculationRef: string;
}

export interface TariffResolved {
  kind: 'RESOLVED';
  cost: SettledCost;
}

export interface TariffUnresolved {
  kind: 'UNRESOLVED';
  code: string;
  message: string;
  evidenceStatus: 'UNKNOWN' | 'PROJECT_ASSUMPTION';
}

export type TariffResolution = TariffResolved | TariffUnresolved;

export interface TariffResolutionPort {
  evaluate(
    event: TelemetryEventV1,
    context: EnergyGraphContext,
  ): Promise<TariffResolution>;
}

export interface ShadowRecommendation {
  schemaVersion: '1.0';
  recommendationId: string;
  tenantId: string;
  siteId: string;
  mode: 'SHADOW';
  createdAt: string;
  validFrom: string;
  validUntil: string;
  objective: {
    type: 'ECONOMIC_COST';
    estimatedValue?: number;
    currency?: string;
  };
  actions: Array<{
    assetRef: string;
    actionType: string;
    parameters?: Record<string, unknown>;
  }>;
  evidenceRefs: string[];
  safetyReviewRequired: true;
}

export interface OptimizerPort {
  recommend(input: {
    event: TelemetryEventV1;
    context: EnergyGraphContext;
    cost: SettledCost;
    evidenceRef: string;
  }): Promise<ShadowRecommendation>;
}

export type EvidenceStatus =
  | 'VERIFIED'
  | 'DERIVED'
  | 'HYPOTHESIS'
  | 'PROJECT_ASSUMPTION'
  | 'UNKNOWN'
  | 'CONTRACT_VERIFIED';

export interface EvidenceRecord {
  schemaVersion: '1.0';
  evidenceId: string;
  status: EvidenceStatus;
  subject: string;
  recordedAt: string;
  sourceRefs: string[];
  derivation?: string;
  notes?: string;
}

export interface EvidenceRepository {
  save(record: EvidenceRecord): Promise<void>;
}
