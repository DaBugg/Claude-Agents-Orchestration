# Product Library Template Page – Setup Guide

The **Product Library Template** is the CMS template for individual product entries. Each Product Library item gets its own URL: `/product-library/{item-slug}` (e.g. `/product-library/blue-light-emergency-towers`).

## Current Configuration (Done via API)

- **Page**: Product Library Template  
- **Page ID**: `699898c2f45fd2339b4fe2a6`  
- **Collection**: Product Library (`699898c1f45fd2339b4fe233`)  
- **Published path**: `/product-library`  
- **SEO**: Meta title and description are set to use the collection fields **SEO Title** and **SEO Description** for each item. If those fields are empty on an item, set a default in Webflow Page Settings → SEO (e.g. title: “{{seo-title}}” with default “Product | TS&L”).

## Build the Template in Webflow Designer

1. **Open the template**
   - In [Webflow Designer](https://transportationdemo-a2fc94272c2a2feb0c45.design.webflow.com) (Live-TS&L), open **Pages** → **Product Library Template** (under the Product Library collection).

2. **Add layout structure**
   - Add a **Section** (e.g. “Product Detail Section”).
   - Inside it, add a **Container** (e.g. “Product Detail Container”).
   - Inside the container, add the blocks below. For each element that should show CMS data, add the element first, then bind the field in the right-hand panel.

3. **Elements and field bindings**

   | Element type   | Purpose           | Bind to collection field |
   |----------------|-------------------|---------------------------|
   | **Heading** (H1) | Product name      | **Name**                  |
   | **Image**      | Product image     | **Product Image**         |
   | **Paragraph / Text** | Short description | **Product Description** |
   | **Text**       | Category tag      | **Category**              |
   | **Text**       | Brand tag         | **Brand Partner**         |
   | **Text**       | System function   | **System Function**       |
   | **Button** or **Link** | “Read more” / “View product” | **Product Page Link** |

   To bind a field: select the element → in the right panel, open the **element settings** (or “CMS” / “Dynamic”) → set the text/source to the correct **Product Library** field.

4. **Optional layout**
   - Use a **Grid** or **Flex** for the container so you can show image on one side and text on the other.
   - Style the tags (Category, Brand, System Function) as pills or labels.
   - Make the “Read more” button/link open in the same tab if Product Page Link goes to an internal page, or in a new tab if it’s external.

5. **SEO fallback (optional)**
   - In **Page Settings** → **SEO**, if you use dynamic title/description, set a **default** for when the item’s SEO Title or SEO Description is empty (e.g. default title: “Product | TS&L”).

## Collection Fields Reference (Product Library)

| Field slug           | Display name       | Type   | Use on template      |
|----------------------|--------------------|--------|-----------------------|
| `name`               | Name               | PlainText | H1 / title         |
| `slug`               | Slug               | PlainText | URL only           |
| `product-description` | Product Description | PlainText | Body copy        |
| `product-image`      | Product Image      | Image  | Main image            |
| `product-page-link`  | Product Page Link  | Link   | “Read more” CTA      |
| `category`           | Category           | Option | Tag                   |
| `brand-partner`       | Brand Partner      | Option | Tag                   |
| `system-function`    | System Function    | Option | Tag                   |
| `seo-title`          | SEO Title          | PlainText | Page meta title   |
| `seo-description`    | SEO Description    | PlainText | Page meta description |

## After You Publish

- Each published Product Library item will have a live URL: `yoursite.com/product-library/{slug}`.
- The main Products page can link to these with “Read more” pointing to **Product Page Link** (existing detail page) or to the template URL (e.g. `/product-library/blue-light-tower`) if you want the template to be the main product page.
