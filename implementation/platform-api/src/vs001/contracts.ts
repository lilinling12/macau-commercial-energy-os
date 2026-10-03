export type TelemetryQuality = 'GOOD' | 'UNCERTAIN' | 'BAD' | 'UNKNOWN';

export interface TelemetryEventV1 {
  schemaVersion: '1.0';
  tenantId: string;
  siteId: string;
  deviceId: string;
  pointId: string;
  metric: string;
  value: number | boolean | string;
  unit: string;
  quality?: TelemetryQuality;
  observedAt: string;
  receivedAt?: string;
  source?: string;
}

const ALLOWED_FIELDS = new Set([
  'schemaVersion',
  'tenantId',
  'siteId',
  'deviceId',
  'pointId',
  'metric',
  'value',
  'unit',
  'quality',
  'observedAt',
  'receivedAt',
  'source',
]);

const QUALITY = new Set<TelemetryQuality>(['GOOD', 'UNCERTAIN', 'BAD', 'UNKNOWN']);

export class ContractValidationError extends Error {
  constructor(message: string) {
    super(message);
    this.name = 'ContractValidationError';
  }
}

function requireNonEmptyString(
  record: Record<string, unknown>,
  field: string,
): string {
  const value = record[field];
  if (typeof value !== 'string' || value.length === 0) {
    throw new ContractValidationError(`${field} must be a non-empty string`);
  }
  return value;
}

function requireDateTime(
  record: Record<string, unknown>,
  field: string,
): string {
  const value = requireNonEmptyString(record, field);
  if (Number.isNaN(Date.parse(value))) {
    throw new ContractValidationError(`${field} must be an ISO date-time`);
  }
  return value;
}

export function parseTelemetryEventV1(input: unknown): TelemetryEventV1 {
  if (typeof input !== 'object' || input === null || Array.isArray(input)) {
    throw new ContractValidationError('telemetry event must be an object');
  }

  const record = input as Record<string, unknown>;

  for (const key of Object.keys(record)) {
    if (!ALLOWED_FIELDS.has(key)) {
      throw new ContractValidationError(`unexpected field: ${key}`);
    }
  }

  if (record.schemaVersion !== '1.0') {
    throw new ContractValidationError('schemaVersion must equal 1.0');
  }

  const value = record.value;
  if (
    typeof value !== 'number' &&
    typeof value !== 'boolean' &&
    typeof value !== 'string'
  ) {
    throw new ContractValidationError('value must be number, boolean, or string');
  }

  if (typeof value === 'number' && !Number.isFinite(value)) {
    throw new ContractValidationError('numeric value must be finite');
  }

  const qualityValue = record.quality;
  if (
    qualityValue !== undefined &&
    (typeof qualityValue !== 'string' ||
      !QUALITY.has(qualityValue as TelemetryQuality))
  ) {
    throw new ContractValidationError('quality is invalid');
  }

  const event: TelemetryEventV1 = {
    schemaVersion: '1.0',
    tenantId: requireNonEmptyString(record, 'tenantId'),
    siteId: requireNonEmptyString(record, 'siteId'),
    deviceId: requireNonEmptyString(record, 'deviceId'),
    pointId: requireNonEmptyString(record, 'pointId'),
    metric: requireNonEmptyString(record, 'metric'),
    value,
    unit: typeof record.unit === 'string' ? record.unit : (() => {
      throw new ContractValidationError('unit must be a string');
    })(),
    observedAt: requireDateTime(record, 'observedAt'),
  };

  if (qualityValue !== undefined) {
    event.quality = qualityValue as TelemetryQuality;
  }
  if (record.receivedAt !== undefined) {
    event.receivedAt = requireDateTime(record, 'receivedAt');
  }
  if (record.source !== undefined) {
    event.source = requireNonEmptyString(record, 'source');
  }

  return event;
}
