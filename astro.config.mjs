import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// Production: https://www.vaidyacharya.org at the root.
// The GitHub Pages preview sets SITE_URL and BASE_PATH in scripts/deploy-pages.sh.
export default defineConfig({
  site: process.env.SITE_URL || 'https://www.vaidyacharya.org',
  base: process.env.BASE_PATH || '/',
  trailingSlash: 'always',
  integrations: [sitemap({ filter: (page) => !page.includes('/404') })],
});
