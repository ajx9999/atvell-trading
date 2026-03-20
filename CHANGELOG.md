# Changelog

## V2 Site Consolidation And Quality Update

### Main Site Updates
- Added the main website pages under `V2/`:
- `V2/index.html`
- `V2/about/index.html`
- `V2/products/index.html`
- `V2/contact/index.html`
- Added structured data to the main `V2` homepage, products, and contact pages.
- Improved the products page note to sound more professional for retail and wholesale customers.

### Product Gallery Updates
- Updated the main `V2/products/index.html` image viewer to fully cover the page.
- Kept image viewer closing behavior via outside click, `Esc`, and close button.
- Removed the visible close hint text from the main products page.

### Numismatic Updates
- Updated `V2/numismatic/index.html`, `V2/numismatic/products.html`, and `V2/numismatic/contact/index.html`.
- Pointed the numismatic home page `Contact Us` button to the actual contact page.
- Removed the extra SEO-heavy visible text block from the numismatic contact page.
- Improved metadata, canonical links, and schema on the numismatic pages.
- Improved inline link styling and image alt text on the numismatic pages.

### Mobile And Compatibility
- Improved mobile navigation behavior on the main `V2` Atvell pages.
- Tightened mobile spacing, header sizing, and floating WhatsApp button behavior across the site.
- Added `rel="noopener"` to external links that open in new tabs.
- Corrected the main homepage WhatsApp link format.

## V2 Numismatic Site Update

### Pages Added
- Added a dedicated `V2/numismatic` mini-site with:
- `V2/numismatic/index.html`
- `V2/numismatic/products.html`
- `V2/numismatic/contact/index.html`

### Contact Page Changes
- Removed the email button.
- Updated business hours to `Open Daily: 9:00 AM - 5:00 PM`.
- Removed appointment-only wording.
- Added the full address: `Shop No. 10, 42, Jalan Medan Batu Caves 1, Medan Batu Caves, 68100 Batu Caves, Selangor, Malaysia`.
- Added a clickable address that opens Google Maps.
- Embedded the map using exact coordinates.
- Added a floating WhatsApp button.

### Products Page Changes
- Created a dedicated products gallery page.
- Removed product captions from gallery cards.
- Added click-to-open full image viewing.
- Added left and right navigation in the image viewer.
- Improved mobile behavior for the gallery lightbox.

### Branding And Header Changes
- Updated visible branding to `Atvell Trading Numismatic & Philatelic Collectibles`.
- Matched the title color, header styling, and hamburger menu style more closely to the main `atvell.com` site.
- Added a mobile hamburger menu for the numismatic pages.

### Mobile Optimization
- Improved responsive layout across home, products, and contact pages.
- Reduced header space usage on mobile.
- Improved spacing, tap targets, image sizing, and footer wrapping.
- Switched layouts to mobile-friendly single-column sections where needed.

### SEO And Content Changes
- Improved page titles, meta descriptions, keywords, and structured data.
- Refined homepage copy to sound more professional.
- Removed overly SEO-heavy visible text from the products page.

### Image Updates
- Renamed product images to `numisproduct1.JPG` through `numisproduct10.JPG`.
- Added `V2/numismatic/resize_products.py` to resize and convert product images.
- Generated optimized WebP assets in `V2/assets/images/webp/`.
- Updated the numismatic pages to use optimized WebP images and logo assets.

### GitHub
- Commit pushed to `main`: `d9aaa4a`
- Commit message: `Add V2 numismatic site and optimized assets`
