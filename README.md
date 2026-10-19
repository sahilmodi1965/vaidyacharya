# vaidyacharya

The website of the **Vaidyacharya Trust**, rebuilt from the archive.

The Trust was set up by Vivek Ragavan and his cousin Malavika Muralidharan to collect, translate and publish the works of their grandfather, Pandit Duraiswami Aiyangar (1883 to 1956): Ayurveda, Sanskrit literature and Vedantic commentaries. The old WordPress site at vaidyacharya.org went offline and its backup would not restore, so this version was rebuilt from copies in the Internet Archive's Wayback Machine. The text is copied word for word from those copies. Nothing was made up.

**Live preview:** https://sahilmodi1965.github.io/vaidyacharya/ (marked `noindex`, so search engines leave it alone).

## Pages

- **Home**: portrait, his titles, the Welcome essay and the list of works.
- **About**: the story of the Trust, the two trustees and the other contributors.
- **Works**: every recovered work. Hamsa Sandesham (English translation) can be read in the browser or downloaded as a PDF.
- **Contact**: a link to email `info@vaidyacharya.org`. The old site had a form, but it sent messages through WordPress, so there's no form here.

What's still missing (other book PDFs, the Biography and Bibliography pages and so on) is listed in [`docs/content-gaps.md`](docs/content-gaps.md).

## Preview it on your computer

You need Node.js 22.22 or newer (`nvm use` picks it up from `.nvmrc`).

```sh
npm install
npm run dev       # open http://localhost:4321
npm run build     # builds the finished site into dist/
npm run preview   # serves dist/ so you can check the build
```

## Publish the preview

```sh
sh scripts/deploy-pages.sh
```

This builds the site under the `/vaidyacharya` path and pushes it to the `gh-pages` branch. GitHub Pages serves that branch at `https://<owner>.github.io/vaidyacharya/`. Give it a minute or two to update.

For the real domain, run `npm run build` with no extra settings and upload `dist/` to any static host. It assumes `https://www.vaidyacharya.org` at the root. Old WordPress addresses such as `/about-us/` and `/hamsa-sandeshamenglish-translation/` redirect to the new pages.

## Where things live

| Path | What |
|---|---|
| `src/data/content.json` | All the recovered text. Edit wording here. |
| `src/lib/site.ts` | Site name, email, menu, and the Hamsa Sandesham PDF details. |
| `src/assets/images/` | The photos and book images from the old site. Astro resizes them at build time. |
| `public/pdf/` | Book PDFs. Only Hamsa Sandesham so far. |
| `src/pages/` | One file per page. |
| `src/styles/global.css` | Colours, fonts (Fraunces for headings, Source Serif 4 for text) and shared styles. |
| `scripts/recovery/` | The scripts that pulled the text out of the archived pages, and a check that every paragraph is in the build. |

## Adding a book PDF

1. Put the file in `public/pdf/`, for example `public/pdf/kiratarjuniya-english.pdf`.
2. Add a download link to that work in `src/pages/works/index.astro`, using `link('/pdf/…')` so it works on the preview too.
3. Run `npm run build`, then tick it off in `docs/content-gaps.md`.
