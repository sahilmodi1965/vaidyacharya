# Content gaps

What the rebuilt site is still missing, and what to ask Vivek Ragavan or Malavika Muralidharan for.
Everything on the live site came from Wayback Machine copies of vaidyacharya.org (captures from April 2022 to August 2025). Nothing was written from scratch.

## What was recovered

| Item | Source capture |
|---|---|
| Home page text, list of titles, 6 book entries | `/` @ 20250825200803, cross-checked with the WordPress JSON for page 11. Identical in all 7 home captures from 2022 to 2025. |
| About: the story, both trustees, other contributors | `/about-us/` @ 20250225151245 and WordPress JSON for page 132 |
| Contact heading and email `info@vaidyacharya.org` | `/contact-us/` @ 20250225151245. The page showed `[email protected]`; the address was decoded from its Cloudflare `data-cfemail` value and matches the plain address in the WordPress JSON for page 180. |
| Hamsa Sandesham English translation PDF (42 pages) | `wp-content/uploads/2020/12/Hamsasandesa-Complete-Translation_compressed1.pdf` @ 20250625062224 |
| 9 images: the portrait, 6 book images, 2 trustee photos, plus the favicon | `wp-content/uploads/` captures from February and June 2025 |

## TODO: book PDFs and book pages

- [ ] **TODO: PDFs for the six other works.** The old home page had download buttons for these, but the files sat behind the Download Monitor plugin (`/download/<id>/`) and none were archived. Vivek has the files.
  - Jivanandanam of Anandaraya Makhin (Sanskrit) — old download 2193
  - Kiratarjuniya (Sanskrit 2198, English 2200)
  - Ashtanga Hridayam — 2182
  - Madhava Nidanam — 2204
  - Tantrasarasangra Pandit — 2215
  - The Presidential Address (Tamil 2226, English 2228)
- [ ] **TODO: each book's own page.** The old site had a page per book (and per translation). None were archived. If they only held a flipbook of the PDF, the PDFs alone are enough.
- [ ] **TODO: works the old sitemap lists but no archived page describes.** These slugs are in `wp-sitemap-posts-page-1.xml` (February 2025). We have no text, image or file for any of them:
  - `kadambari`, `kadambarienglish-translation` (Kadambari, with an English translation)
  - `meghasandesam-sanskrit`, `meghasandesam-english` (Meghasandesam, Sanskrit and English)
  - `sri-pancharatra-raksha-of-sri-vedanta-desika` and its `-english-translation`
  - `rasaratna-samuchchaya` and its `-english-translation`
  - `sarngadhara-samhita`
  - `pillai-pani`
  - `hamsa-sandesham` (presumably the Sanskrit or Tamil edition; only the English one was archived)
  - `jivanandanam-of-anandaraya-makhin-english-translation` (an English translation of Jivanandanam)
- [ ] **TODO: Hamsa Sandesham's category and description.** The old Hamsa page held only the flipbook, so the site shows the PDF's own title page and credits Dr. S. Usha as translator (per the About page). A short description in the style of the other works would help.

## TODO: pages that existed but weren't archived

From the old sitemap and menu. No copy of any of them exists in the Wayback Machine.

- [x] **Biography** (`/biography/`). Not in the Wayback Machine; rebuilt from the family's Word document "Biography of Pandit Doraiswamy Aiyangar with bibliography" (November 2020). The text is the family's own, with only obvious typos fixed and the duplicate journal entries merged. The chapter headings were added for the web.
- [x] **Bibliography** (`/bibliography/`). From the same document; it's the second half of the Biography page, and `/bibliography/` redirects to `/biography/#bibliography`.
- [ ] **TODO: birth year.** The home page (from the old site) says 1883; the biography says 1888, and it says he was "barely twenty" in 1908 and died at sixty eight in 1956, which fits 1888. Confirm with the family.
- [ ] **TODO: category pages**: Ayurveda Books, Vedanta Books, Sanskrit Literature, General Books, Books for Download. No **Vedanta** work at all was recovered, though the About page says he wrote commentaries on Vedantic texts.
- [ ] **TODO: Privacy Policy** (`/privacy-policy/`). Only needed if the site collects anything; this one doesn't (no forms, no analytics).
- Not rebuilt on purpose: Shop, Basket, Checkout, My Account, Login, Registration, No Access, My Profile (WooCommerce and membership pages), Sample Page, `home_1`, and the default "Hello world!" post.

## TODO: confirm with the family

- [ ] **TODO: confirm `info@vaidyacharya.org` still receives mail.** It's the address the old site used. The rebuilt site links to it with `mailto:`.
- [ ] **TODO: photos.** Both trustee photos were recovered. There are no photos of Chandrika or Dr. S. Usha (the old site had none either). Send any if they'd like them shown.
- [ ] **TODO: possible typos kept as-is from the old site.** These were copied verbatim; fix them only if the family agrees:
  - "Diplomad Ayurvedic Medical Practioner"
  - "Editor of Vaiydya Kalannidhi"
  - "Vidyapitha" stands alone as the last title; it may be the end of another line
  - "Physician SKPD Hospital, Madras Sri Desika Dashana Dhurandhara" looks like two titles run together
  - About: "…decided to establish the Vaidyacharya Trust with" ends a paragraph and "The express purpose of…" starts the next. It is probably one sentence.
  - Home: the heading reads "Pandit Duraiswami aiyangar (1883 -1956)"; the site capitalises the name in CSS but leaves the text alone
- [ ] **TODO: the old PDF URL.** Links to `/wp-content/uploads/2020/12/Hamsasandesa-Complete-Translation_compressed1.pdf` will 404 on the new site. If anyone shared that link, add a host-level redirect to `/pdf/hamsa-sandesham-english-translation.pdf` at launch.
