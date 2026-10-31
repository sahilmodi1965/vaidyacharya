import content from '../data/content.json';

export const site = {
  name: 'Vidvadacharya Trust',
  brand: 'Dr. P.T. SRINIVASA IYENGAR',
  url: 'https://www.vaidyacharya.org',
  email: content.contact.email,
};

export const nav = [
  { href: '/', label: 'Home' },
  { href: '/about/', label: 'About' },
  { href: '/contact/', label: 'Contact' },
];

// Display-only: the old site set some headings in capitals ("VIVEK RAGAVAN").
export function titleCase(s: string) {
  return s === s.toUpperCase() ? s.toLowerCase().replace(/\b\p{L}/gu, (c) => c.toUpperCase()) : s;
}

// Slug for an in-page anchor.
export function slug(s: string) {
  return s.toLowerCase().normalize('NFD').replace(/[^\w\s-]/g, '').trim().replace(/\s+/g, '-');
}
