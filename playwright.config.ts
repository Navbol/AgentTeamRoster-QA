import { defineConfig } from '@playwright/test';

const python = process.platform === 'win32'
  ? '.venv\\Scripts\\python.exe'
  : '.venv/bin/python';

export default defineConfig({
  use: {
    baseURL: 'http://127.0.0.1:5000',
  },
  webServer: {
    command: `${python} app.py`,
    url: 'http://127.0.0.1:5000',
    reuseExistingServer: !process.env.CI,
    timeout: 30_000,
  },
});