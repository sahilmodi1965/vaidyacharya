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
    '/about-us/': to('/about/'),
    '/contact-us/': to('/contact/'),
    '/hamsa-sandeshamenglish-translation/': to('/works/hamsa-sandesham/'),
    '/hamsa-sandesham/': to('/works/hamsa-sandesham/'),
    '/biography/': to('/about/'),
    '/bibliography/': to('/works/'),
    '/books-for-download/': to('/works/'),
    '/ayurveda-books/': to('/works/'),
    '/vedanta-books/': to('/works/'),
    '/sanskrit-literature/': to('/works/'),
    '/general-books/': to('/works/'),
    '/jivanandanam-of-anandaraya-makhin-sanskrit/': to('/works/'),
    '/jivanandanam-of-anandaraya-makhin-english-translation/': to('/works/'),
    '/kiratarjuniya/': to('/works/'),
    '/kiratarjuniya-english-explaination/': to('/works/'),
    '/ashtanga-hridayam/': to('/works/'),
    '/madhava-nidanam/': to('/works/'),
    '/tantrasara-sangraha/': to('/works/'),
    '/the-presidential-address/': to('/works/'),
    '/the-presidential-address-english-translation/': to('/works/'),
  },
  integrations: [sitemap({ filter: (page) => !page.includes('/404') })],
});
