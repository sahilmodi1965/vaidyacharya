import type { ImageMetadata } from 'astro';

const files = import.meta.glob<{ default: ImageMetadata }>('../assets/images/*.{jpg,png}', { eager: true });

export function img(name: string): ImageMetadata {
  const hit = files[`../assets/images/${name}`];
  if (!hit) throw new Error(`Missing image: ${name}`);
  return hit.default;
}
