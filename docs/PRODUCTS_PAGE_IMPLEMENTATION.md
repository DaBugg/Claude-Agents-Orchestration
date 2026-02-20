# Products Page – Filtered Catalog Implementation

## What Was Built (via Webflow MCP / API)

- **Products page** (`/products`, Live-TS&L site) now has:
  1. **Hero** – “Our Products & Solutions” heading and subtitle (unchanged).
  2. **Filter section** – Three filter rows with Finsweet attributes:
     - **Category** – All + 6 categories (Campus & Public Safety, Intelligent Infrastructure, Smart Lighting, Traffic Control, Traffic Calming, Managed Services).
     - **Brand / Partner** – All + 17 brands (Acuity Brands, Aivia, Asylon, Bolide, Centegix, EnGoPlanet, Juganu, Knightscope, Network Optix, NoTraffic, North America Traffic, Oriux, Rosehill Highways, Rotaid, TS&L, TraffiCalm / Eltec / K&K, Traffic Logix, Wanco).
     - **System Function** – All + 28 system functions (partial set added via API; some may need to be added in Designer if timeouts occurred).
  3. **Product grid section** – A new section with a container that has `fs-cmsfilter-element="list"`. This div is the Finsweet “list” wrapper; the actual CMS Collection List must be added in Webflow Designer.
  4. **Finsweet CMS Filter** – Script registered on the site and applied to the Products page (footer). It loads the Finsweet CMS Filter from CDN so the filter buttons work.

## Complete the page (Collection List + cards)

**→ Step-by-step:** [COMPLETE_PRODUCTS_PAGE.md](COMPLETE_PRODUCTS_PAGE.md) — add the Collection List and item template so the grid shows Product Library items.

## What You Need to Do in Webflow Designer

1. **Open the Products page** in [Webflow Designer](https://transportationdemo-a2fc94272c2a2feb0c45.design.webflow.com) (Live-TS&L site).
2. **Add the CMS Collection List**
   - In the new “Product grid” section, select the inner container (the one with `fs-cmsfilter-element="list"`).
   - From the **Add elements** panel, add a **Collection List**.
   - Bind it to the **Product Library** collection.
3. **Build the collection item template** inside the Collection List:
   - **Product Image** ← bind to Product Image field.
   - **Heading (H3)** ← bind to Name.
   - **Text** ← Brand Partner (and/or Category, System Function if desired).
   - **Text** ← Product Description.
   - **Button or Link** “Read More” ← bind to Product Page Link.
4. **Finsweet attributes on CMS items**  
   So the filters can match items, the **dynamic text** elements that show Category, Brand Partner, and System Function inside each collection item must use the **same field values** as in the filter buttons (the buttons already use `fs-cmsfilter-field` and `fs-cmsfilter-value`). Optionally add `fs-cmsfilter-field="category"` (and `brand-partner`, `system-function`) to the corresponding text elements in the item template so Finsweet can hide/show items. (If the list wrapper has `fs-cmsfilter-element="list"` and the filter container has `fs-cmsfilter-element="filters"`, Finsweet usually discovers fields from the list content.)
5. **System Function buttons**  
   If any system function options are missing from the third row, add them in Designer with the same pattern: Link with class “Filter Button”, `fs-cmsfilter-field="system-function"`, `fs-cmsfilter-value="<exact option name>"` (must match the Product Library option exactly).
6. **Styling**  
   Adjust spacing, grid layout, and “Filter Button” / “Filter Row” styles as needed.

## Filter Attribute Reference

- **Filter container** (wraps all three rows): `fs-cmsfilter-element="filters"`.
- **List wrapper** (wraps the Collection List): `fs-cmsfilter-element="list"`.
- **Each filter link**: `fs-cmsfilter-field="category"` | `"brand-partner"` | `"system-function"`, and either `fs-cmsfilter-type="all"` (for “All”) or `fs-cmsfilter-value="<exact option label>"`.

Option labels must match the Product Library collection’s Option field values exactly (e.g. “Campus & Public Safety”, “TraffiCalm / Eltec / K&K”).

## Collection

- **Product Library** (slug: `product-library`, collection id: `699898c1f45fd2339b4fe233`) – used for the filtered list. Ensure CMS items are published so they appear on the live page.

## Related

- **Product Library Template** (individual product pages at `/product-library/{slug}`): see [PRODUCT_LIBRARY_TEMPLATE_PAGE.md](PRODUCT_LIBRARY_TEMPLATE_PAGE.md) for configuring the CMS template page.
