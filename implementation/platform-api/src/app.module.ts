import { Module } from '@nestjs/common';
import { HealthController } from './health.controller.js';
import {
  FailClosedEnergyGraphAdapter,
  FailClosedOptimizerAdapter,
  FailClosedTariffAdapter,
  InMemoryEvidenceRepository,
} from './vs001/adapters.js';
import {
  ENERGY_GRAPH_PORT,
  EVIDENCE_REPOSITORY,
  OPTIMIZER_PORT,
  TARIFF_RESOLUTION_PORT,
} from './vs001/ports.js';
import { Vs001Controller } from './vs001/vs001.controller.js';
import { Vs001Service } from './vs001/vs001.service.js';

@Module({
  controllers: [HealthController, Vs001Controller],
  providers: [
    Vs001Service,
    {
      provide: ENERGY_GRAPH_PORT,
      useClass: FailClosedEnergyGraphAdapter,
    },
    {
      provide: TARIFF_RESOLUTION_PORT,
      useClass: FailClosedTariffAdapter,
    },
    {
      provide: OPTIMIZER_PORT,
      useClass: FailClosedOptimizerAdapter,
    },
    {
      provide: EVIDENCE_REPOSITORY,
      useClass: InMemoryEvidenceRepository,
    },
  ],
})
export class AppModule {}
