# Next Steps Checklist – Product Catalog

Do these in order with **Webflow Designer** open and the **Live-TS&L** site loaded.

**Designer link:** [Open Live-TS&L in Webflow Designer](https://transportationdemo-a2fc94272c2a2feb0c45.design.webflow.com?app=dc8209c65e3ec02254d15275ca056539c89f6d15741893a0adf29ad6f381eb99)

---

## Step 1: Product Library Template (individual product pages)

1. In the **Pages** panel, open **Product Library Template** (under the Product Library collection).
2. Add a **Section** on the page.
3. Inside it, add a **Container**.
4. Inside the container, add and bind:
   - **Heading (H1)** → bind to **Name**
   - **Image** → bind to **Product Image**
   - **Paragraph** → bind to **Product Description**
   - **Text** (×3) → bind to **Category**, **Brand Partner**, **System Function** (style as tags)
   - **Link** or **Button** “Read more” / “View product” → bind to **Product Page Link**
5. (Optional) Set **Page Settings → SEO** default title/description for items that don’t have SEO fields filled.
6. **Save** (Ctrl/Cmd + S).

Detail: [PRODUCT_LIBRARY_TEMPLATE_PAGE.md](PRODUCT_LIBRARY_TEMPLATE_PAGE.md)

---

## Step 2: Products page – Collection List and item template

1. In **Pages**, open **Products**.
2. In the **Product grid** section, select the inner **container** (with `fs-cmsfilter-element="list"`).
3. Add a **Collection List** inside that container.
4. Set the list’s collection to **Product Library**.
5. Inside the **Collection List Item** (the repeating block), add and bind:
   - **Image** → **Product Image**
   - **Heading (H3)** → **Name**
   - **Text** → **Brand Partner** (and optionally Category, System Function)
   - **Text** → **Product Description**
   - **Link** or **Button** “Read more” → **Product Page Link**
6. **Save**.

Detail: [PRODUCTS_PAGE_IMPLEMENTATION.md](PRODUCTS_PAGE_IMPLEMENTATION.md)

---

## Step 3: Publish

1. Click **Publish** in Webflow (choose your domain).
2. Visit `/products` to confirm the grid and filters work.
3. Visit `/product-library/{any-item-slug}` to confirm the template page works.

---

## If filter buttons don’t work

- Ensure the **Finsweet CMS Filter** script is applied to the **Products** page (Site/Page Settings → Custom Code or Scripts).
- Ensure the list wrapper has `fs-cmsfilter-element="list"` and the filter container has `fs-cmsfilter-element="filters"`.

## If you need to add more System Function buttons

On the Products page, in the System Function row, add a **Link** with class **Filter Button**, set:
- `fs-cmsfilter-field` = `system-function`
- `fs-cmsfilter-value` = exact option name (e.g. `Mobile Surveillance`)

Option names must match the Product Library **System Function** field options exactly.
