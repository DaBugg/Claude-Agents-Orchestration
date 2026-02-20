# Complete the /products Page – Add Collection List & Item Template

Your **Products** page is published and has the hero + filter section. **This is the only remaining step:** add the **product grid** (Collection List) and the **card template** inside it. This must be done in **Webflow Designer** (the API cannot create Collection List components).

**Designer:** [Live-TS&L → open Products page](https://transportationdemo-a2fc94272c2a2feb0c45.design.webflow.com?app=dc8209c65e3ec02254d15275ca056539c89f6d15741893a0adf29ad6f381eb99)

---

## 1. Find the product grid area

- On the **Products** page, scroll below the three filter rows (Category, Brand / Partner, System Function).
- You should see a **Section** (and inside it a **Container**) that was added for the product grid. The inner container has the attribute **fs-cmsfilter-element="list"** (Finsweet uses this to know which list to filter).
- **Click that inner container** (the one with `fs-cmsfilter-element="list"`) so the next element you add will go inside it. If you see placeholder text like “Product grid — add CMS Collection List…”, that’s the right container.

---

## 2. Add the Collection List

- With that container selected, open the **Add elements** panel (left sidebar or + button).
- Find **Components** (or **CMS**) and add **Collection List**.
- In the right-hand panel, set **Collection** to **Product Library**.
- You should now see a **Collection List** wrapper and inside it a **Collection List Item** (the repeating block). The item might be empty or have default placeholder content.

---

## 3. Build the card inside Collection List Item

- **Select the Collection List Item** (the inner block that repeats for each product).
- Add these elements **inside** the Collection List Item, then bind each to the field listed:

| Add this element      | Bind to (Product Library field) |
|-----------------------|----------------------------------|
| **Image**             | Product Image                    |
| **Heading** (H3)      | Name                             |
| **Text block**        | Brand Partner                    |
| **Text block**        | Product Description              |
| **Link** or **Button** (e.g. “Read more”) | Product Page Link        |

**To bind:** Select the element → in the right panel, find **CMS** / **Dynamic** / field picker → choose the correct **Product Library** field.

**Optional:** Add more text blocks and bind to **Category** and **System Function** so the cards show tags and Finsweet can filter by them (values must match the filter buttons exactly).

---

## 4. Layout the card (optional but recommended)

- Select the **Collection List Item**.
- Set the layout to **Grid** or **Flex** (e.g. image on top, text below; or image left, text right).
- Give the image a fixed aspect ratio or max height so cards look even.
- Style the “Read more” link/button to match your site.

---

## 5. Save and publish

- **Save** (Ctrl/Cmd + S).
- **Publish** the site again.
- Open **yoursite.com/products** and confirm:
  - Product Library items appear in the grid.
  - Clicking Category, Brand / Partner, or System Function filters the grid.
  - “Read more” goes to the correct product or detail page.

---

## If the grid is empty

- **CMS:** In the **Product Library** collection, make sure items exist and are **Published** (not draft).
- **Collection List:** Confirm the list is bound to **Product Library** and the container with the list has **fs-cmsfilter-element="list"** (and the filter section has **fs-cmsfilter-element="filters"**).
- **Script:** The **Finsweet CMS Filter** script should be applied to the **Products** page (footer). Check **Site settings** or **Page settings** → Custom Code / Scripts.

---

## Quick reference – Product Library fields

| Field             | Use on card        |
|-------------------|--------------------|
| Product Image     | Card image         |
| Name              | Card title (H3)    |
| Brand Partner     | Subtitle / tag     |
| Product Description | Short description |
| Product Page Link | “Read more” link   |
| Category          | Optional tag       |
| System Function   | Optional tag       |

Once the Collection List and item template are added and bound as above, the /products page is complete.

---

## Completion checklist (tick as you go)

- [ ] **1** – Found the product grid container (`fs-cmsfilter-element="list"`) below the filters
- [ ] **2** – Added **Collection List** inside it and set collection to **Product Library**
- [ ] **3** – Inside **Collection List Item** added: Image (→ Product Image), H3 (→ Name), Text (→ Brand Partner), Text (→ Product Description), Link/Button (→ Product Page Link)
- [ ] **4** – Bound every element to the correct Product Library field
- [ ] **5** – Set card layout (Grid/Flex) and styled the “Read more” button
- [ ] **6** – Saved and published; verified `/products` shows the grid and filters work
