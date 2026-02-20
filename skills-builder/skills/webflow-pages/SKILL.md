---
name: webflow-pages
description: >
  Builds professional Webflow pages with proper HTML semantics, structured data,
  SEO metadata, accessibility, and performance optimization. Activates when user
  asks to create, design, or optimize Webflow pages, or needs schema markup,
  meta tags, alt text, or heading hierarchy for Webflow sites.
version: 1.0.0
triggers:
  - webflow
  - webflow page
  - build website
  - create page
  - landing page
  - seo optimization
  - schema markup
  - structured data
  - meta tags
  - heading hierarchy
  - alt text
  - web accessibility
  - core web vitals
  - open graph
domain: web
complexity: complex
dependencies: []
browser: false
author: auto-generated
created: 2026-02-20
---

# Webflow Pages

## Overview

Builds professional, SEO-optimized Webflow pages using the Webflow MCP tools (Designer API + Data API). Enforces proper HTML heading hierarchy, injects JSON-LD structured data, configures meta/Open Graph tags, applies descriptive alt text, and follows WCAG 2.1 AA accessibility standards. Targets Public Safety, SaaS/Tech, and general multi-industry sites.

## Auto-Activation Conditions

This skill activates when:
- ✅ User asks to create, build, or design a Webflow page
- ✅ Request mentions SEO optimization for a Webflow site
- ✅ Task involves adding schema markup or structured data
- ✅ User wants to fix heading hierarchy or HTML semantics
- ✅ Request asks for alt text on images
- ✅ User mentions Open Graph tags or social sharing
- ✅ Task involves Core Web Vitals or performance optimization
- ✅ User references a Webflow site URL or site ID

Does NOT activate when:
- ❌ Building static HTML/CSS outside Webflow (use general web dev)
- ❌ WordPress, Squarespace, or non-Webflow platforms
- ❌ Writing marketing copy only (use `marketing-copy` skill)
- ❌ Scraping data from websites (use `web-scraping` skill)

## Webflow MCP Integration

This skill uses the `user-Webflow` MCP server instead of browser automation. **Always call `webflow_guide_tool` first** before any other Webflow MCP tool.

### Tool Reference by Task

| Task | MCP Tool | Key Actions |
|------|----------|-------------|
| List/get sites | `data_sites_tool` | list_sites, get_site, publish_site |
| Create pages & folders | `de_page_tool` | create_page (meta_title, meta_description), create_page_folder |
| Build element trees | `element_builder` | Section, Heading, Image, Container, DivBlock, DOM (max 3 levels/call) |
| Modify elements | `element_tool` | add_or_update_attribute, set_heading_level, set_text, set_image_asset |
| Create/update styles | `style_tool` | create_style, update_style (per breakpoint + pseudo) |
| SEO & OG metadata | `data_pages_tool` | update_page_settings (title, description, OG, slug) |
| JSON-LD scripts | `data_scripts_tool` | add_inline_site_script (location: header) |
| Image alt text | `asset_tool` | update_asset (alt_text field) |
| Design tokens | `variable_tool` | create_color_variable, create_size_variable |
| Reusable components | `de_component_tool` | transform_element_to_component, insert_component_instance |
| Redirects & robots.txt | `data_enterprise_tool` | create_301_redirect, update_robots_txt |
| CMS content | `data_cms_tool` | create_collection, create_collection_items |
| Visual debugging | `element_snapshot_tool` | Capture element screenshot |
| CSS reference | `de_learn_more_about_styles` | Full property documentation |

Every tool requires a `context` parameter (15-25 word third-person description of intent).

## Instructions

### Phase 1: Discovery and Site Context

Gather project context before building anything.

```python
context = {
    "site_id": None,        # from data_sites_tool → list_sites
    "existing_pages": [],   # from data_pages_tool → list_pages
    "existing_styles": [],  # from style_tool → get_styles
    "existing_components": [],  # from de_component_tool → get_all_components
    "page_type": "",        # landing | about | services | blog | contact | pricing | portfolio
    "industry": "",         # public-safety | saas | general
    "brand_name": "",
    "primary_keyword": "",
    "reference_url": ""     # e.g. https://www.tsandl.us/home-new
}
```

1. Call `webflow_guide_tool` to get latest guidelines
2. Call `data_sites_tool` with action `list_sites` to get the site ID
3. Call `data_pages_tool` with action `list_pages` to map existing structure
4. Call `style_tool` with action `get_styles` (query: "all") to see existing design system
5. Call `de_component_tool` with action `get_all_components` to inventory reusable parts
6. Ask user for page type, industry, brand name, and primary keyword

### Phase 2: Page Architecture (HTML Semantics)

Apply correct semantic structure before adding content.

**Heading Hierarchy Rules:**
- Exactly ONE `<h1>` per page — the primary page topic
- `<h2>` for major sections (Features, About, Pricing, etc.)
- `<h3>` for subsections within an H2 block
- `<h4>`-`<h6>` for deeper nesting — never skip levels
- Headings must be nested logically: H1 → H2 → H3 (never H1 → H3)

**Semantic Element Mapping in Webflow:**

| HTML Semantic | Webflow Element | How to Create |
|---------------|----------------|---------------|
| `<header>` | DOM element | `element_builder` with `set_dom_config: {tag: "header"}` |
| `<nav>` | DOM element | `set_dom_config: {tag: "nav"}` + `set_attributes: [{name: "aria-label", value: "Main navigation"}]` |
| `<main>` | DOM element | `set_dom_config: {tag: "main"}` |
| `<footer>` | DOM element | `set_dom_config: {tag: "footer"}` |
| `<section>` | Section | Native Webflow Section element |
| `<article>` | DOM element | `set_dom_config: {tag: "article"}` |
| `<aside>` | DOM element | `set_dom_config: {tag: "aside"}` |
| `<h1>`-`<h6>` | Heading | `set_heading_level: 1` through `6` |

**ARIA Attributes for Accessibility:**
```json
{
  "set_attributes": [
    {"name": "role", "value": "banner"},
    {"name": "aria-label", "value": "Site header"}
  ]
}
```

### Phase 3: Page Creation and Structure

1. Create the page with SEO metadata from the start:
   - Use `de_page_tool` → `create_page` with `page_name`, `meta_title`, `meta_description`
   - Meta title: `Primary Keyword - Secondary Keyword | Brand` (50-60 chars)
   - Meta description: action-oriented summary with CTA (150-160 chars)

2. Build the element tree using `element_builder`:
   - Max 3 levels of nesting per call; chain multiple calls for deeper structures
   - Always set `creation_position: "append"` for sequential sections

3. Apply heading levels immediately during element creation:
   - Use `set_heading_level` on every Heading element
   - Verify H1 is used exactly once

**Landing Page Section Pattern:**
```
Section (Hero)
  ├── Container
  │   ├── Heading [H1] — Primary page headline
  │   ├── Paragraph — Subtitle / value proposition
  │   └── Button — Primary CTA
Section (Social Proof)
  ├── Container
  │   ├── Heading [H2] — "Trusted By"
  │   └── DivBlock (Logo Grid)
  │       ├── Image — Client logo 1
  │       └── Image — Client logo 2
Section (Features)
  ├── Container
  │   ├── Heading [H2] — "Our Services" / "Features"
  │   └── DivBlock (Card Grid)
  │       ├── DivBlock (Card)
  │       │   ├── Heading [H3] — Feature title
  │       │   └── Paragraph — Feature description
  │       └── DivBlock (Card) ...
Section (Testimonials)
  ├── Container
  │   ├── Heading [H2] — "What Clients Say"
  │   └── DivBlock (Testimonial Grid)
Section (CTA)
  ├── Container
  │   ├── Heading [H2] — Closing CTA headline
  │   ├── Paragraph — Reinforcement text
  │   └── Button — Final CTA
```

**About Page Section Pattern:**
```
Section (Hero)
  ├── Container
  │   ├── Heading [H1] — "About [Brand]"
  │   └── Paragraph — Mission statement
Section (Mission & Values)
  ├── Container
  │   ├── Heading [H2] — "Our Mission"
  │   └── DivBlock (Values Grid)
  │       ├── DivBlock (Value Card)
  │       │   ├── Heading [H3] — Value name
  │       │   └── Paragraph — Value description
Section (Team)
  ├── Container
  │   ├── Heading [H2] — "Our Team"
  │   └── DivBlock (Team Grid)
  │       ├── DivBlock (Member Card)
  │       │   ├── Image — Headshot
  │       │   ├── Heading [H3] — Name
  │       │   └── Paragraph — Title / Bio
```

**Services Page Section Pattern:**
```
Section (Hero)
  ├── Container
  │   ├── Heading [H1] — "Our Services"
  │   └── Paragraph — Overview
Section (Service Detail) × N
  ├── Container
  │   ├── Heading [H2] — Service name
  │   ├── Paragraph — Service description
  │   └── Button — "Learn More" / CTA
Section (Process)
  ├── Container
  │   ├── Heading [H2] — "How It Works"
  │   └── DivBlock (Steps)
  │       ├── DivBlock (Step)
  │       │   ├── Heading [H3] — Step title
  │       │   └── Paragraph — Step description
Section (FAQ)
  ├── Container
  │   ├── Heading [H2] — "Frequently Asked Questions"
  │   └── DivBlock (FAQ Items)
```

**Blog/Article Page Pattern:**
```
DOM [tag: article]
  ├── Container
  │   ├── Heading [H1] — Article title
  │   ├── DivBlock (Byline)
  │   │   ├── Image — Author photo
  │   │   ├── TextBlock — Author name
  │   │   └── TextBlock — Publish date
  │   ├── Image — Featured image
  │   ├── Paragraph — Intro
  │   ├── Heading [H2] — First section
  │   ├── Paragraph — Content
  │   ├── Heading [H3] — Subsection
  │   ├── Paragraph — Content
  │   └── DivBlock (Related Posts)
  │       ├── Heading [H2] — "Related Articles"
```

**Contact Page Pattern:**
```
Section (Hero)
  ├── Container
  │   ├── Heading [H1] — "Contact Us"
  │   └── Paragraph — Intro
Section (Contact Form + Info)
  ├── Container
  │   ├── DivBlock (Two Column)
  │   │   ├── DivBlock (Form Column)
  │   │   │   ├── Heading [H2] — "Send a Message"
  │   │   │   └── DivBlock (Form)
  │   │   └── DivBlock (Info Column)
  │   │       ├── Heading [H2] — "Get in Touch"
  │   │       ├── TextBlock — Address
  │   │       ├── TextLink — Phone
  │   │       └── TextLink — Email
```

**Pricing Page Pattern:**
```
Section (Hero)
  ├── Container
  │   ├── Heading [H1] — "Pricing"
  │   └── Paragraph — Value statement
Section (Plans)
  ├── Container
  │   └── DivBlock (Plan Grid)
  │       ├── DivBlock (Plan Card)
  │       │   ├── Heading [H2] — Plan name
  │       │   ├── TextBlock — Price
  │       │   ├── DivBlock (Features List)
  │       │   │   └── TextBlock — Feature item × N
  │       │   └── Button — CTA
Section (FAQ)
  ├── Container
  │   ├── Heading [H2] — "Frequently Asked Questions"
```

**Portfolio / Case Study Pattern:**
```
Section (Hero)
  ├── Container
  │   ├── Heading [H1] — "Our Work" / "Case Studies"
  │   └── Paragraph — Intro
Section (Project Grid)
  ├── Container
  │   └── DivBlock (Grid)
  │       ├── LinkBlock (Project Card)
  │       │   ├── Image — Project thumbnail
  │       │   ├── Heading [H2] — Project title
  │       │   └── Paragraph — Brief description
Section (Individual Case Study — if single page)
  ├── Container
  │   ├── Heading [H2] — "The Challenge"
  │   ├── Paragraph
  │   ├── Heading [H2] — "Our Solution"
  │   ├── Paragraph
  │   ├── Heading [H2] — "Results"
  │   └── DivBlock (Metrics)
  │       ├── DivBlock (Metric)
  │       │   ├── Heading [H3] — Metric value
  │       │   └── TextBlock — Metric label
```

### Phase 4: SEO Metadata and Open Graph

After page structure is built, configure all SEO signals.

**Meta Title Formula:**
```
[Primary Keyword] - [Secondary Keyword] | [Brand Name]
```
- 50-60 characters max (Google truncates at ~60)
- Front-load the primary keyword
- Include brand at the end after pipe

**Meta Description Formula:**
```
[Action verb] [value proposition]. [Benefit statement]. [CTA].
```
- 150-160 characters max
- Include primary keyword naturally
- End with a call-to-action

**Apply via `data_pages_tool` → `update_page_settings`:**
```json
{
  "page_id": "<page-id>",
  "body": {
    "title": "Public Safety Consulting - Emergency Management | TS&L",
    "description": "Protect your community with expert public safety consulting. Custom emergency management plans, training, and compliance. Request a free assessment today.",
    "slug": "public-safety-consulting",
    "openGraph": {
      "title": "Public Safety Consulting Services | TS&L",
      "description": "Expert emergency management and public safety consulting for government and private organizations.",
      "image": "<asset-url-1200x630>",
      "imageAlt": "TS&L public safety team conducting emergency management training"
    }
  }
}
```

**Open Graph Checklist:**
- `og:title` — can differ from meta title (optimized for social)
- `og:description` — compelling social share text
- `og:image` — 1200x630px minimum, high contrast, readable text
- `og:image:alt` — descriptive alt text for the OG image
- `og:type` — "website" for pages, "article" for blog posts

**Canonical URLs:**
- Set on every page to prevent duplicate content
- Self-referencing canonical for primary pages
- Point paginated content to the canonical collection page

### Phase 5: Structured Data / Schema Markup (JSON-LD)

Inject JSON-LD via `data_scripts_tool` → `add_inline_site_script` with `location: "header"`.

**Schema Selection by Page Type:**

| Page Type | Primary Schema | Additional |
|-----------|---------------|------------|
| Landing | Organization, WebSite | BreadcrumbList |
| About | AboutPage, Person | Organization |
| Services | Service, ProfessionalService | FAQPage, HowTo |
| Blog | Article, BlogPosting | BreadcrumbList |
| Contact | ContactPage, LocalBusiness | PostalAddress |
| Pricing | Product, Offer | AggregateRating |
| Portfolio | CreativeWork, ItemList | ImageGallery |
| Public Safety | GovernmentService, EmergencyService | LocalBusiness |

**Injection Pattern:**
```json
{
  "site_id": "<site-id>",
  "request": {
    "sourceCode": "<script type=\"application/ld+json\">{...schema...}</script>",
    "version": "1.0.0",
    "displayName": "Schema - Organization",
    "location": "header",
    "canCopy": false
  }
}
```

**Validation:** After injection, test with Google Rich Results Test (https://search.google.com/test/rich-results) to confirm schema parses correctly.

See `reference.md` for complete JSON-LD templates for every schema type.

### Phase 6: Accessibility and Image Optimization

**Alt Text Guidelines:**
- Descriptive: explain what the image shows and why it matters in context
- Max 125 characters (screen readers may truncate longer text)
- Never start with "Image of..." or "Photo of..." — screen readers already announce it as an image
- Decorative images: set alt text to empty string `""` (not omitted)
- Complex images (charts, infographics): provide detailed description in adjacent text

**Alt Text by Image Type:**

| Image Type | Alt Text Pattern | Example |
|------------|-----------------|---------|
| Hero/banner | `[Subject] [action/context]` | "Emergency response team coordinating disaster relief operations" |
| Team headshot | `[Name], [Title] at [Company]` | "Sarah Chen, Director of Operations at TS&L" |
| Logo | `[Company] logo` | "TS&L Consulting logo" |
| Icon/decorative | `""` (empty) | "" |
| Product screenshot | `[Product] [showing feature]` | "Dashboard showing real-time emergency dispatch metrics" |
| Infographic | `[Topic summary] — full description in text below` | "Public safety response time statistics 2025" |

**Apply via `asset_tool` → `update_asset`:**
```json
{
  "siteId": "<site-id>",
  "actions": [{
    "actionType": "update_asset",
    "asset_id": "<asset-id>",
    "alt_text": "Emergency response team coordinating disaster relief operations"
  }]
}
```

**WCAG 2.1 AA Compliance Checklist:**
- [ ] Color contrast: 4.5:1 minimum for normal text, 3:1 for large text (18px+ bold or 24px+)
- [ ] Focus indicators: visible focus ring on all interactive elements
- [ ] Keyboard navigation: all functionality reachable via keyboard alone
- [ ] Skip link: first focusable element jumps to `<main>` content
- [ ] Form labels: every input has a visible, associated `<label>`
- [ ] Link purpose: link text describes destination (no "click here")
- [ ] ARIA landmarks: header, nav, main, footer roles assigned
- [ ] Motion: respect `prefers-reduced-motion` media query
- [ ] Text resizing: content readable at 200% zoom without horizontal scroll

**Apply ARIA via `element_tool` → `add_or_update_attribute`:**
```json
{
  "actions": [{
    "actionType": "add_or_update_attribute",
    "id": {"component": null, "element": "<element-id>"},
    "attributes": [
      {"name": "role", "value": "navigation"},
      {"name": "aria-label", "value": "Main navigation"}
    ]
  }]
}
```

### Phase 7: Performance and Core Web Vitals

**Target Thresholds:**

| Metric | Good | Needs Improvement | Poor |
|--------|------|-------------------|------|
| LCP (Largest Contentful Paint) | < 2.5s | 2.5s - 4.0s | > 4.0s |
| CLS (Cumulative Layout Shift) | < 0.1 | 0.1 - 0.25 | > 0.25 |
| INP (Interaction to Next Paint) | < 200ms | 200ms - 500ms | > 500ms |

**LCP Optimization:**
- Hero images: use Webflow's responsive image srcset (auto-generated)
- Set explicit `width` and `height` attributes on images to prevent layout shift
- Preload critical fonts via custom code in header
- Minimize above-the-fold DOM depth (keep hero section shallow)

**CLS Prevention:**
- Always set image dimensions before the image loads
- Use `font-display: swap` for custom fonts (set via `style_tool`)
- Avoid dynamically injected content above the fold
- Set explicit heights on containers that load async content

**INP Optimization:**
- Place analytics and tracking scripts in footer (not header)
- Minimize custom JavaScript — leverage Webflow interactions instead
- Avoid heavy DOM manipulation on user interaction

**Script Placement via `data_scripts_tool`:**
- `location: "header"` — ONLY for JSON-LD schema markup
- `location: "footer"` — analytics, tracking, non-critical JS

**Webflow-Specific Performance:**
- Enable lazy loading via element attributes: `{"name": "loading", "value": "lazy"}`
- Use Webflow's built-in responsive images (auto srcset)
- Compress assets before upload (target < 200KB per image)
- Limit custom fonts to 2 families, 3-4 weights max
- Use `variable_tool` design tokens for consistent sizing (avoids redundant styles)

## Industry-Specific Guidance

### Public Safety (Primary)

**Schema Types:**
- `GovernmentService` — for government-contracted services
- `EmergencyService` — for emergency management offerings
- `LocalBusiness` — for physical office locations
- `ProfessionalService` — for consulting services

**Design Principles:**
- Trust signals: certifications, compliance badges, government logos in social proof
- Color palette: navy blue (#1B3A5C) for trust, red (#CC0000) for urgency, white for clarity
- High contrast everywhere — accessibility is legally required (Section 508, ADA Title II)
- Emergency contact prominently placed: phone number in header, visible on every page
- Clear hierarchy: critical information first, supporting details below

**Content Priorities:**
1. Emergency contact / immediate action CTA
2. Services overview with clear scope
3. Credentials, certifications, compliance
4. Case studies with measurable outcomes
5. Team expertise and qualifications

### SaaS / Tech Products

**Schema Types:**
- `SoftwareApplication` — for the product itself
- `Product` + `Offer` — for pricing pages
- `Organization` — for the company
- `FAQPage` — for feature/pricing questions

**Design Principles:**
- Feature-benefit pairing: every feature links to a user outcome
- Social proof: customer count, logos, testimonials with metrics
- Pricing transparency: clear tier comparison, no hidden fees
- Trial/demo CTA: prominent, repeated throughout the page
- Dark mode consideration: design tokens that support theme switching

**Content Priorities:**
1. Value proposition headline (H1) — what problem you solve
2. Product demo / screenshot
3. Key features with benefits
4. Social proof (logos + testimonials)
5. Pricing with clear CTA
6. FAQ addressing objections

## Examples

### Example 1: Create a Landing Page for Public Safety Consulting

**Input**: "Create a landing page for TS&L public safety consulting on our Webflow site"

**Execution**:

1. Call `webflow_guide_tool` with context
2. Call `data_sites_tool` → `list_sites` to get site ID
3. Call `de_page_tool` → `create_page`:
   ```json
   {
     "page_name": "Public Safety Consulting",
     "meta_title": "Public Safety Consulting - Emergency Management | TS&L",
     "meta_description": "Protect your community with expert public safety consulting. Emergency management plans, training, and compliance solutions. Request a free assessment."
   }
   ```
4. Call `element_builder` to create Hero section:
   ```json
   {
     "element_schema": {
       "type": "Section",
       "set_style": ["hero-section"],
       "children": [{
         "type": "Container",
         "children": [
           {"type": "Heading", "set_heading_level": 1, "set_text": "Protecting Communities Through Expert Public Safety Solutions"},
           {"type": "Paragraph", "set_text": "Comprehensive emergency management consulting for government agencies and private organizations."},
           {"type": "Button", "set_text": "Request Free Assessment", "set_link": {"type": "url", "url": "/contact"}}
         ]
       }]
     }
   }
   ```
5. Build remaining sections (Social Proof, Services, Testimonials, CTA) following the Landing Page pattern
6. Call `data_pages_tool` → `update_page_settings` for OG tags
7. Inject Organization + WebSite JSON-LD via `data_scripts_tool`
8. Set alt text on all images via `asset_tool`

**Output**: A fully structured landing page with:
- Proper H1-H3 heading hierarchy
- Meta title, description, and Open Graph tags
- Organization + WebSite JSON-LD schema
- Descriptive alt text on all images
- ARIA landmarks (header, nav, main, footer)

### Example 2: Add Schema Markup and Meta Tags to Existing Service Page

**Input**: "Add schema markup and fix the SEO on our services page"

**Execution**:

1. Call `webflow_guide_tool`
2. Call `data_pages_tool` → `get_page_metadata` to audit current meta tags
3. Call `element_tool` → `get_all_elements` to audit heading structure
4. Fix any heading hierarchy issues via `element_tool` → `set_heading_level`
5. Update meta tags via `data_pages_tool` → `update_page_settings`:
   ```json
   {
     "page_id": "<page-id>",
     "body": {
       "title": "Public Safety Services - Training & Compliance | TS&L",
       "description": "Expert public safety services including emergency planning, compliance audits, and staff training. Serving government and private sectors nationwide."
     }
   }
   ```
6. Inject ProfessionalService + FAQPage schema via `data_scripts_tool`
7. Verify all images have alt text via `asset_tool`

**Output**: Updated service page with corrected heading hierarchy, optimized meta tags, and valid JSON-LD structured data.

### Example 3: Fix Heading Hierarchy and Add Alt Text Across the Site

**Input**: "Audit and fix the heading hierarchy and missing alt text on all pages"

**Execution**:

1. Call `webflow_guide_tool`
2. Call `data_pages_tool` → `list_pages` to get all pages
3. For each page:
   a. Call `de_page_tool` → `switch_page`
   b. Call `element_tool` → `get_all_elements` to get full element tree
   c. Identify heading violations (multiple H1s, skipped levels)
   d. Fix via `element_tool` → `set_heading_level`
4. Call `asset_tool` → `get_all_assets_and_folders` to find images missing alt text
5. For each image without alt text:
   a. Call `get_image_preview` to see the image
   b. Write descriptive alt text
   c. Apply via `asset_tool` → `update_asset`

**Output**: Site-wide audit report listing all fixes made, with every page having correct heading hierarchy and every image having descriptive alt text.

## Quality Checklist

Before completing, verify:
- [ ] Exactly one H1 per page, logical H2-H6 nesting (no skipped levels)
- [ ] Meta title set (50-60 chars, keyword-first, brand at end)
- [ ] Meta description set (150-160 chars, action-oriented, includes CTA)
- [ ] Open Graph title, description, and image (1200x630px) configured
- [ ] JSON-LD structured data injected and validates in Rich Results Test
- [ ] All images have descriptive, contextual alt text (125 chars max)
- [ ] Color contrast meets WCAG AA (4.5:1 text, 3:1 large text)
- [ ] ARIA landmarks assigned (header, nav, main, footer)
- [ ] Responsive across all breakpoints (xxl, xl, large, main, medium, small, tiny)
- [ ] Scripts placed correctly (schema in header, analytics in footer)
- [ ] No orphaned pages — all linked in navigation
- [ ] LCP target < 2.5s (hero images optimized, critical path minimal)
- [ ] CLS target < 0.1 (explicit image dimensions, font-display: swap)

## Anti-Patterns

- ❌ Multiple H1 tags on a single page
- ❌ Skipping heading levels (H1 → H3, missing H2)
- ❌ Generic alt text ("image", "photo", "img_001.jpg", "screenshot")
- ❌ Starting alt text with "Image of..." or "Photo of..."
- ❌ Keyword stuffing in meta title or description
- ❌ Missing Open Graph tags (causes broken social sharing previews)
- ❌ Using inline styles instead of Webflow style classes
- ❌ Ignoring responsive breakpoints (designing only for desktop)
- ❌ Invalid JSON-LD schema (always validate before publishing)
- ❌ Placing analytics scripts in the header (blocks rendering, hurts LCP)
- ❌ Decorative images with descriptive alt text (use empty string instead)
- ❌ Using Webflow interactions for critical content (invisible to crawlers)

## Integration

- **Works with**: `marketing-copy` (page content generation), `web-scraping` (competitive analysis)
- **Browser**: Not required — uses Webflow MCP tools
- **MCP Server**: `user-Webflow` (required — call `webflow_guide_tool` first)
- **Reference**: See `reference.md` for complete JSON-LD templates and cheat sheets

## Changelog

- v1.0.0 (2026-02-20): Initial creation — page building, SEO, schema, accessibility, performance
