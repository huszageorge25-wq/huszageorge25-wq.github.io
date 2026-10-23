# Storefront Studio client sites

Netlify publishes this repository automatically on every push to `main`.

- One folder per client, named with a short lowercase slug: `legends-barber-shop/`.
- Each folder holds `index.html` plus an `assets/` folder (images, logo, css).
- Concept previews go in `concepts/<slug>/` and carry `<meta name="robots" content="noindex">`.
- The live address of a client is `https://<netlify-site>.netlify.app/<slug>/`.
- Never commit passwords, keys or client personal data beyond what is on their public site.
