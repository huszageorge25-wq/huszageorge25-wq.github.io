# Storefront Studio sites

GitHub Pages publishes this repository automatically on every push to `main`.
Address: https://huszageorge25-wq.github.io/

- The root `index.html` is the Storefront Studio website.
- One folder per client, named with a short lowercase slug: `legends-barber-shop/` (index.html plus `assets/`).
  Live address: https://huszageorge25-wq.github.io/<slug>/
- Concept previews go in `concepts/<slug>/` and carry `<meta name="robots" content="noindex">`.
- Never commit passwords, keys or client personal data beyond what is on their public site.

## SEO layer
`python3 _studio/seo.py` rebuilds the industry pages (`websites-for/`), guides (`guides/`), `start/`, `404.html`,
`robots.txt`, `sitemap.xml`, `llms.txt` and patches the homepage head/footer between `SEO` markers.
Content lives in `_studio/seo_data.py`. Re-run after changing prices in `_studio/extras.py` OFFER.
