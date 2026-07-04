---
name: canva-pitch-deck
description: >
  Builds investor pitch decks and product-launch presentations in Canva using
  the user-Canva MCP—structured slide plans, brand kits, assets, placeholders,
  and optional reads of existing Canva decks or off-Canva source material.
version: 1.0.0
triggers:
  - canva
  - pitch deck
  - investor deck
  - fundraising deck
  - product launch
  - launch presentation
  - presentation
  - slides
  - deck
  - keynote
  - slide deck
  - demo day
  - board deck
domain: creative
complexity: complex
dependencies: []
browser: false
composes_with:
  - marketing-copy
author: auto-generated
created: 2026-03-19
---

# Canva pitch deck and launch presentations

## Overview

Produces cohesive, presentable **multi-slide decks** in Canva for **pitch** and **product-launch** contexts. Uses AI generation (`generate-design` with `design_type: presentation`), optional **brand kits** and **ordered assets**, explicit **image placeholders** when media is missing, and structured workflows to **synthesize content** from off-Canva templates or existing Canva designs.

## Auto-Activation Conditions

This skill activates when:

- User asks to create, build, or generate a **pitch deck**, **launch deck**, **investor deck**, or **presentation** in **Canva**
- Request involves **slides**, **speaker notes**, **exporting** a Canva presentation, or **matching brand** colors/typography
- User wants to turn **outline / doc / pasted content** into slides

Does **not** activate when:

- Design work is **not** in Canva (Figma, Google Slides only, PowerPoint only with no Canva path)
- User only wants **copy** with no deck delivery (may use `marketing-copy` alone)
- User only wants **web pages** (use `webflow-pages`)

## Runtime: confirm available MCP tools

**Before** promising in-place editing (add/replace elements on an existing file), list the **actual** tools exposed by `user-Canva` in this session. The reference project includes design **read**, **generate**, **import/export**, **folder**, and **comment** tools; **`create-design-from-candidate`** may mention editing-transaction tools that **might** exist in a **newer** connector. If no editing/transaction tools appear, **do not** claim slide-level edits via API—use the **degraded** paths in [Workflow B](#workflow-b-edit-or-extend-an-existing-canva-deck).

Similarly, some Canva MCP builds document **`search-brand-templates`** for template pick + generation flows. If that tool is **absent**, use `generate-design` with an explicit **Style Guide** and Slide Plan, or ask the user to pick a starting style in Canva UI.

Always pass a concise `user_intent` string on every Canva MCP call when the schema requires it.

---

## Canva MCP integration (reference tool map)

Use this table as a guide; names match common `user-Canva` descriptors. **Verify** against the live tool list.

| Task | MCP tool(s) | Notes |
|------|-------------|--------|
| **AI-generate presentation** | `generate-design` | `design_type` **must** be `presentation`. `query` must follow the **exact** three-part structure below. |
| **Persist chosen candidate** | `create-design-from-candidate` | Needs `job_id` + `candidate_id` from generate step. Returns `design_id` for later reads/exports. |
| **Brand colors/fonts** | `list-brand-kits` → `generate-design` (`brand_kit_id`) | Ask if user wants on-brand; only set `brand_kit_id` after they confirm a kit. |
| **Images / video URLs** | `upload-asset-from-url` | If scope error (`asset:write`), ask user to reconnect Canva connector. Order matters for `asset_ids`. |
| **Resolve design** | `search-designs`, `get-design`, `resolve-shortlink` | `design_id` format: `D` + chars (11). Extract from `https://www.canva.com/design/{design_id}/...`. **Never** treat thumbnail or preview URL segments as `design_id`. |
| **Read slide structure** | `get-design-pages` | Pagination: `offset`, `limit`. |
| **Read slide text** | `get-design-content` | Pass `content_types: ["richtexts"]`. Charts/diagrams may need user-supplied numbers or screenshot assets. |
| **Read speaker notes** | `get-presenter-notes` | Optional per-page `pages`. |
| **Import external file** | `import-design-from-url` | Public **HTTPS** URL only; not `file://` or local paths. |
| **Export** | `get-export-formats`, `export-design` | After user approves. |
| **Organize** | `search-folders`, `list-folder-items`, `create-folder`, `move-item-to-folder` | Optional filing after creation. |
| **Review / async feedback** | `comment-on-design`, `list-comments`, `list-replies`, `reply-to-comment` | Optional collaboration. |

**Tool names verified** against this repository’s MCP descriptor folder (`mcps/user-Canva/tools`): `comment-on-design`, `create-design-from-candidate`, `create-folder`, `export-design`, `generate-design`, `get-design`, `get-design-content`, `get-design-pages`, `get-export-formats`, `get-presenter-notes`, `import-design-from-url`, `list-brand-kits`, `list-comments`, `list-folder-items`, `list-replies`, `move-item-to-folder`, `reply-to-comment`, `resolve-shortlink`, `search-designs`, `search-folders`, `upload-asset-from-url`. Anything else (e.g. `search-brand-templates`, editing transactions) must come from the **live** MCP tool list.

---

## `generate-design` query structure (presentations)

The `query` string **must** contain these sections **in order** with **these headers**:

1. **Presentation Brief** — Include **Title**; **Topic / Scope**; **Key Messages** (3–5); **Constraints & Assumptions**; **Style Guide** (tone, palette, typography, imagery), matching the `generate-design` tool wording.
2. **Narrative Arc** — One paragraph: e.g. Hook → Problem → Insight → Solution → Proof → Plan → CTA (explicit transitions).
3. **Slide Plan** — Numbered slides. **For each slide**, use **this exact subsection order**:
   - **Slide {N} — "{Exact Title}"**
   - **Goal:** one sentence.
   - **Bullets (3–6):** parallel, specific; avoid vague verbs.
   - **Visuals:** concrete layout + chart/diagram type if any; **include placeholder specs** when no image (see [Placeholders](#image-slots-and-placeholders)).
   - **Data/Inputs:** numbers, sources, or **example values** labeled as such (do not use bare `[TBD]`).
   - **Speaker Notes (2–4 sentences):**
   - **Asset Hint (optional):**
   - **Transition:** one sentence to next slide.

Self-check before sending: unique titles (≤ ~65 chars), cohesive arc, defined terms, consistent acronyms, concrete visuals, no empty placeholders without replacement strategy.

---

## Workflow A: New deck (primary)

1. **Intake** — Audience, ask length (slide count or minutes), CTA, taboo topics, language, deadline, competitor sensitivity.
2. **Brand** — Ask if they want a brand kit. If yes: `list-brand-kits`, user picks → pass `brand_kit_id` on `generate-design`.
3. **Assets** — If user has logos/product shots: `upload-asset-from-url` per file; collect **asset IDs**. For multi-slide decks, **`asset_ids` order = slide order** for image slots (tool description); only pass as many as there are real images to place.
4. **Build `query`** — Use [structure above](#generatedesign-query-structure-presentations). Merge in **synthesized** content from [Template intake](#template-intake-off-canva-and-canva).
5. **Generate** — `generate-design` with `design_type: presentation`, full `query`, optional `brand_kit_id`, optional `asset_ids`.
6. **Select** — Present candidates; user picks one → `create-design-from-candidate` (`job_id`, `candidate_id`).
7. **Handoff** — Share edit/view links from `get-design` if needed, offer export, optional folder move.

---

## Workflow B: Edit or extend an existing Canva deck

1. Resolve **`design_id`** (`search-designs`, URL parse, or `resolve-shortlink` for `canva.link`).
2. **If** the MCP exposes **editing / transaction** tools (e.g. start transaction, insert page, set text): follow **connector-specific** docs and keep changes minimal and reversible; prefer duplicating the design in UI if user is risk-averse.
3. **If not**:
   - **Read** existing copy: `get-design-content` (+ `get-presenter-notes`, `get-design-pages` for structure).
   - **Option i:** New `generate-design` **presentation** whose Slide Plan **reimplements** the deck (merged with user edits). Then `create-design-from-candidate`.
   - **Option ii:** User **duplicates** the design in Canva and edits manually; you only supply an updated Slide Plan / speaker notes as a doc.

Never fabricate `design_id` or continuation tokens.

---

## Template intake (off-Canva and Canva)

### Off-Canva (default expectation)

1. Ask for **structured paste**: section titles, bullets, metrics, quotes, must-keep legal lines.
2. If user has a **PDF / PPTX / Doc** on a **public HTTPS URL**, `import-design-from-url` can create a Canva design **for reference**—then **read** with `get-design-content` / `get-design-pages` if it becomes a normal multi-page design. Local paths cannot be imported; user must upload to a reachable URL.
3. **Synthesize** into the Slide Plan: one **main idea** per slide, 3–6 bullets, merge duplicate sections, promote numbers to **Data/Inputs**.

### Template already in Canva

1. `get-design-pages` for order and count; `get-design-content` with `richtexts` for text; optional `get-presenter-notes`.
2. Map pages → new Slide Plan bullets; preserve **user-marked** must-keep phrases.

---

## Image slots and placeholders

When an image is **not** available or generated yet, every affected slide’s **Visuals** line **must** still specify a **concrete** layout, for example:

- "Right 40%: **placeholder rectangle**, 2px dashed neutral border, centered label: `Insert: product UI screenshot`; left 60%: three bullets."
- "Full-bleed **photo slot** with semi-transparent overlay; caption bar for static text."

Avoid vague "add image here" without size/position language. For **external** generated images: create image → host at HTTPS → `upload-asset-from-url` → add to `asset_ids` in **slide order**.

---

## Animations and motion (v1 vs future)

**v1:** Use **Transition** sentences between slides in the Slide Plan and tight **Narrative Arc**; do not promise slide-build or element animations via MCP unless a tool explicitly supports them.

**Future:** When/if the connector exposes timeline or animation APIs, extend this skill with a short subsection per tool.

---

## Presentation quality checklist

Use alongside the self-check in the `generate-design` tool text:

- One **primary message** per slide; titles readable in isolation (story scan *via titles only*).
- **Contrast** and font sizes suitable for **projector** and **16:9** screens.
- **Data honesty** — label projections vs actuals; cite or mark example figures.
- **Timeboxing** — implied slide count matches meeting length; CTA slide present.
- **Launch-specific** — problem, solution, why-now, traction, ask, roadmap or GTM as appropriate.

---

## Integration

- **MCP Server:** `user-Canva` (enable in the agent environment).
- **Optional:** `marketing-copy` for sharper hooks and CTA language before building the Slide Plan.
- **Browser:** not required for this skill.

---

## Examples

### Input

"Canva pitch deck for our Series A: B2B scheduling SaaS, 12 slides, include traction chart placeholders and use our brand kit if I confirm."

### Output (agent behavior)

1. Confirm audience and brand kit → `list-brand-kits` if yes.
2. Build full **Presentation Brief / Narrative Arc / Slide Plan** (12 slides) with **Visuals** and placeholders for charts.
3. `generate-design` (`presentation`) → user picks candidate → `create-design-from-candidate` → offer `export-design`.

---

## Anti-patterns

- Using **IDs from preview or share links** that are **not** the canonical `design_id` path segment.
- Calling **`search-designs`** when the user asked to **search or pick Canva templates** for generation—use **`search-brand-templates`** **if** it exists in the MCP; otherwise clarify with the user.
- Omitting `design_type: presentation` or shrinking the **Slide Plan** so slides lack **Goal / Visuals / Transition**.
- Assuming **editing** APIs exist without checking the live tool list.
- Using **`import-design-from-url`** with **local** paths or non-HTTPS URLs.

---

## Changelog

- v1.0.0: Initial skill — generate, brand kit, assets, placeholders, off-Canva + Canva template paths, degraded edit path.
