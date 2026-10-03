import { Controller, Get } from '@nestjs/common';

@Controller('health')
export class HealthController {
  @Get()
  getHealth(): { status: 'UP'; component: 'platform-api' } {
    return {
      status: 'UP',
      component: 'platform-api',
    };
  }
}
