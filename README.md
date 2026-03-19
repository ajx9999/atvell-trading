# Atvell Trading

Official website repository for Atvell Trading Sdn. Bhd.

## Overview

This repository contains the public website for Atvell Trading, including:

- the main corporate site for wholesale souvenirs, cultural products, and religious items
- the numismatic and philatelic section for coins, banknotes, and stamp collectibles
- static assets used by the public website

## Site Structure

- `index.html`
  Main homepage for Atvell Trading
- `about/`
  Company background and business profile
- `products/`
  Main products gallery
- `contact/`
  Main contact page
- `numismatic/`
  Dedicated numismatic and philatelic microsite
- `assets/images/`
  Shared site images and optimized assets

## Numismatic Section

The `numismatic/` section includes:

- `numismatic/index.html`
  Numismatic landing page
- `numismatic/products.html`
  Collectibles gallery with lightbox image viewing
- `numismatic/contact/index.html`
  Contact page with map, phone number, location, and WhatsApp access
- `numismatic/resize_products.py`
  Utility script for resizing product images and exporting WebP versions

## Image Handling

The repository includes optimized WebP assets for website delivery.

Source product images:

- `assets/images/numisproduct1.JPG` through `assets/images/numisproduct10.JPG`

Optimized website assets:

- `assets/images/webp/`

To regenerate optimized numismatic WebP files:

```bash
python3 numismatic/resize_products.py
```

## Deployment

The site is intended to be served directly from the repository root for static hosting.

Files such as `CNAME` and `wrangler.jsonc` support deployment and domain configuration for the published website.

## Recent Updates

Recent improvements include:

- promotion of the site to the repository root structure
- a dedicated numismatic and philatelic site section
- responsive mobile improvements and hamburger navigation
- optimized product images in WebP format
- image lightbox support on the numismatic products page
- improved metadata, branding, and contact details

## Repository Notes

- Keep generated cache files out of version control.
- Prefer optimized images for production-facing pages.
- Maintain root-relative site structure for smooth static hosting.
