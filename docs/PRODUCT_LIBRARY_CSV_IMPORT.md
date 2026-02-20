# Product Library – CSV bulk import

## File

**`product-library-import.csv`** (in the project root) contains all **60 products** from `tsl-product-library-FINAL.txt`, ready for Webflow CMS bulk import.

## Columns (map to Product Library fields)

| CSV column         | Product Library field | Notes |
|--------------------|------------------------|--------|
| name               | Name                   | Required |
| slug               | Slug                   | Required; URL-safe |
| product-description | Product Description  | One-line description |
| category           | Category               | Must match Option exactly |
| brand-partner      | Brand Partner          | Must match Option exactly |
| system-function    | System Function        | Must match Option exactly |
| product-page-link   | Product Page Link      | Relative URLs (e.g. `/safety-and-emergency/blue-light-tower`); empty where no existing page |
| sort-order         | Sort Order             | 1–60 by category order |
| seo-title          | SEO Title              | Per-item meta title |
| seo-description    | SEO Description        | Per-item meta description |

**Product Image** is not in the CSV (add images in Webflow after import, or add a column and map it if you have image URLs).

## Import steps in Webflow

1. Open your **Live-TS&L** site in the **Designer**.
2. Go to **CMS** (left panel) → open the **Product Library** collection.
3. Click **Import** (or the bulk-import option).
4. Upload **`product-library-import.csv`**.
5. Map each CSV column to the matching **Product Library** field (ignore or skip **Product Image** if you leave it empty).
6. Run the import. Resolve any validation errors (e.g. slug format, required fields).
7. After import, add **Product Image** per item in the CMS or by re-importing a CSV that includes image URLs if your plan supports it.
8. **Publish** the collection items so they appear on `/products` and filter correctly.

## Option values (must match exactly)

- **Category:** Campus & Public Safety, Intelligent Infrastructure Platform, Smart Lighting & Connected Spaces, Traffic Control & Management, Traffic Calming & Perimeter, Managed Services & Support  
- **Brand Partner:** Acuity Brands, Aivia, Asylon, Bolide Technology Group, Centegix, EnGoPlanet, Juganu, Knightscope, Network Optix, NoTraffic, North America Traffic, Oriux, Rosehill Highways, Rotaid, TS&L, TraffiCalm / Eltec / K&K, Traffic Logix, Wanco  
- **System Function:** (28 options – see collection in Webflow; values in the CSV match the doc.)

## Product page links

Where an existing site page exists, **product-page-link** uses a relative path (e.g. `/safety-and-emergency/blue-light-tower`). Empty cells mean no link was mapped; you can fill those in the CMS or in a second CSV import.

## After import

- Confirm all 60 items appear in **Product Library**.
- Add **Product Image** for each item (upload in Webflow or via image URL column if supported).
- Publish items so they show on the **Products** page and filters work.
