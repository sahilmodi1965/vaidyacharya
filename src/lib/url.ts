// Prefix a root-relative path with the deploy base (e.g. /vaidyacharya on GitHub Pages).
const base = import.meta.env.BASE_URL.replace(/\/$/, '');

export function link(path: string) {
  return path.startsWith('/') ? base + path : path;
}

export function stripBase(pathname: string) {
  return base && pathname.startsWith(base) ? pathname.slice(base.length) || '/' : pathname;
}

export const isPreview = base !== '';
