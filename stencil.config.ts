import { Config } from '@stencil/core';

export const config: Config = {
  namespace: 'uptime-sla',
  globalScript: 'src/global/app.ts',
  srcDir: 'src',
  outputTargets: [
    {
      type: 'www',
      serviceWorker: null,
    },
  ],
};
