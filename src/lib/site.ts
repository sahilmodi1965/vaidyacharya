import content from '../data/content.json';

export const site = {
  name: 'Vaidyacharya Trust',
  subject: 'Pandit Duraiswami Aiyangar',
  url: 'https://www.vaidyacharya.org',
  email: content.contact.email,
};

export const nav = [
  { href: '/', label: 'Home' },
  { href: '/biography/', label: 'Biography' },
  { href: '/descendants/', label: 'Family' },
  { href: '/about/', label: 'About' },
  { href: '/works/', label: 'Works' },
  { href: '/contact/', label: 'Contact' },
];

export const hamsaPdf = {
  href: '/pdf/hamsa-sandesham-english-translation.pdf',
  pages: 42,
  size: '370 KB',
  // Verbatim from the title page of the PDF.
  titlePage: [
    'HAṀSASANDEŚA',
    'of Sri Vedantadesika',
    'An English Rendering of the Tamil Translation, Notes and Foreword by',
    'Ayurveda-bhushana, Ayurvedacharya, Desikadarsana-dhurandhara, Vaidyaratnam Pandit M Duraiswami Aiyangar',
  ],
  // From the About page: "At present, she has translated Hamsa Sandesham and the Presidential Address".
  translator: 'Dr. S. Usha',
};

// Display-only: the old site set some headings in capitals ("VIVEK RAGAVAN").
export function titleCase(s: string) {
  return s === s.toUpperCase() ? s.toLowerCase().replace(/\b\p{L}/gu, (c) => c.toUpperCase()) : s;
}

// Slug for an in-page anchor on the Works page.
export function slug(s: string) {
  return s.toLowerCase().normalize('NFD').replace(/[^\w\s-]/g, '').trim().replace(/\s+/g, '-');
}
