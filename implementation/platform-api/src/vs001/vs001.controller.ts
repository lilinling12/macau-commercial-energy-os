import { Body, Controller, Post } from '@nestjs/common';
import { Vs001Service, type Vs001Result } from './vs001.service.js';

@Controller('v1/vs001')
export class Vs001Controller {
  constructor(private readonly service: Vs001Service) {}

  @Post('evaluate')
  evaluate(@Body() body: unknown): Promise<Vs001Result> {
    return this.service.evaluate(body);
  }
}
