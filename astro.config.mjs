import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

const base = process.env.BASE_PATH || '/';
// Astro does not prefix redirect targets with the base, so do it here.
const to = (path) => base.replace(/\/$/, '') + path;

// Production: https://www.vaidyacharya.org at the root.
// The GitHub Pages preview sets SITE_URL and BASE_PATH in scripts/deploy-pages.sh.
export default defineConfig({
  site: process.env.SITE_URL || 'https://www.vaidyacharya.org',
  base,
  trailingSlash: 'always',
  // Old WordPress URLs (from the archived wp-sitemap.xml) point to their new homes.
  redirects: {
    '/descendants/': to('/'),
    '/about-us/': to('/about/'),
    '/contact-us/': to('/contact/'),
    '/bibliography/': to('/biography/#bibliography'),
  },
  integrations: [sitemap({ filter: (page) => !page.includes('/404') })],
});
