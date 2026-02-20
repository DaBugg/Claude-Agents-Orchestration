# Webflow Pages — Reference

Supplementary reference for the `webflow-pages` skill. Contains JSON-LD schema templates, SEO cheat sheets, accessibility guidelines, and Webflow MCP tool mappings.

---

## JSON-LD Schema Templates

### Organization

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "{{brand_name}}",
  "url": "{{site_url}}",
  "logo": "{{logo_url}}",
  "description": "{{company_description}}",
  "foundingDate": "{{founding_year}}",
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "{{phone}}",
    "contactType": "customer service",
    "availableLanguage": "English"
  },
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "{{street}}",
    "addressLocality": "{{city}}",
    "addressRegion": "{{state}}",
    "postalCode": "{{zip}}",
    "addressCountry": "US"
  },
  "sameAs": [
    "{{facebook_url}}",
    "{{linkedin_url}}",
    "{{twitter_url}}"
  ]
}
```

### WebSite (with SearchAction)

```json
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "{{brand_name}}",
  "url": "{{site_url}}",
  "potentialAction": {
    "@type": "SearchAction",
    "target": "{{site_url}}/search?q={search_term_string}",
    "query-input": "required name=search_term_string"
  }
}
```

### LocalBusiness

```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "{{brand_name}}",
  "url": "{{site_url}}",
  "image": "{{business_image_url}}",
  "telephone": "{{phone}}",
  "email": "{{email}}",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "{{street}}",
    "addressLocality": "{{city}}",
    "addressRegion": "{{state}}",
    "postalCode": "{{zip}}",
    "addressCountry": "US"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "{{lat}}",
    "longitude": "{{lng}}"
  },
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
      "opens": "08:00",
      "closes": "17:00"
    }
  ],
  "priceRange": "$$"
}
```

### Service / ProfessionalService

```json
{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "name": "{{service_name}}",
  "description": "{{service_description}}",
  "provider": {
    "@type": "Organization",
    "name": "{{brand_name}}",
    "url": "{{site_url}}"
  },
  "areaServed": {
    "@type": "Country",
    "name": "United States"
  },
  "serviceType": "{{service_type}}",
  "url": "{{service_page_url}}"
}
```

### GovernmentService (Public Safety)

```json
{
  "@context": "https://schema.org",
  "@type": "GovernmentService",
  "name": "{{service_name}}",
  "description": "{{service_description}}",
  "serviceType": "Emergency Management Consulting",
  "provider": {
    "@type": "Organization",
    "name": "{{brand_name}}",
    "url": "{{site_url}}"
  },
  "areaServed": {
    "@type": "AdministrativeArea",
    "name": "{{jurisdiction}}"
  },
  "audience": {
    "@type": "Audience",
    "audienceType": "Government Agencies"
  },
  "isRelatedTo": {
    "@type": "GovernmentService",
    "name": "Emergency Services",
    "serviceType": "Public Safety"
  }
}
```

### EmergencyService (Public Safety)

```json
{
  "@context": "https://schema.org",
  "@type": "EmergencyService",
  "name": "{{service_name}}",
  "description": "{{service_description}}",
  "provider": {
    "@type": "Organization",
    "name": "{{brand_name}}"
  },
  "areaServed": "{{service_area}}",
  "availableChannel": {
    "@type": "ServiceChannel",
    "serviceUrl": "{{site_url}}/contact",
    "servicePhone": "{{emergency_phone}}"
  }
}
```

### Article / BlogPosting

```json
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "{{article_title}}",
  "description": "{{article_summary}}",
  "image": "{{featured_image_url}}",
  "datePublished": "{{publish_date_iso}}",
  "dateModified": "{{modified_date_iso}}",
  "author": {
    "@type": "Person",
    "name": "{{author_name}}",
    "url": "{{author_url}}"
  },
  "publisher": {
    "@type": "Organization",
    "name": "{{brand_name}}",
    "logo": {
      "@type": "ImageObject",
      "url": "{{logo_url}}"
    }
  },
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "{{article_url}}"
  },
  "wordCount": "{{word_count}}",
  "articleSection": "{{category}}"
}
```

### FAQPage

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "{{question_1}}",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "{{answer_1}}"
      }
    },
    {
      "@type": "Question",
      "name": "{{question_2}}",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "{{answer_2}}"
      }
    }
  ]
}
```

### BreadcrumbList

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "{{site_url}}"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "{{parent_page_name}}",
      "item": "{{parent_page_url}}"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "{{current_page_name}}",
      "item": "{{current_page_url}}"
    }
  ]
}
```

### Product + Offer (Pricing Pages)

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "{{product_name}}",
  "description": "{{product_description}}",
  "brand": {
    "@type": "Brand",
    "name": "{{brand_name}}"
  },
  "offers": [
    {
      "@type": "Offer",
      "name": "{{plan_name}}",
      "price": "{{price}}",
      "priceCurrency": "USD",
      "priceValidUntil": "{{valid_until_iso}}",
      "availability": "https://schema.org/InStock",
      "url": "{{pricing_page_url}}"
    }
  ]
}
```

### SoftwareApplication (SaaS)

```json
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "{{app_name}}",
  "description": "{{app_description}}",
  "applicationCategory": "{{category}}",
  "operatingSystem": "Web",
  "offers": {
    "@type": "Offer",
    "price": "{{starting_price}}",
    "priceCurrency": "USD"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "{{rating}}",
    "ratingCount": "{{review_count}}"
  },
  "author": {
    "@type": "Organization",
    "name": "{{brand_name}}"
  }
}
```

### CreativeWork (Portfolio)

```json
{
  "@context": "https://schema.org",
  "@type": "CreativeWork",
  "name": "{{project_name}}",
  "description": "{{project_description}}",
  "image": "{{project_image_url}}",
  "creator": {
    "@type": "Organization",
    "name": "{{brand_name}}"
  },
  "dateCreated": "{{project_date_iso}}",
  "genre": "{{project_category}}",
  "url": "{{project_page_url}}"
}
```

### AboutPage

```json
{
  "@context": "https://schema.org",
  "@type": "AboutPage",
  "name": "About {{brand_name}}",
  "description": "{{about_description}}",
  "url": "{{about_page_url}}",
  "mainEntity": {
    "@type": "Organization",
    "name": "{{brand_name}}",
    "foundingDate": "{{founding_year}}",
    "numberOfEmployees": {
      "@type": "QuantitativeValue",
      "value": "{{employee_count}}"
    }
  }
}
```

### ContactPage

```json
{
  "@context": "https://schema.org",
  "@type": "ContactPage",
  "name": "Contact {{brand_name}}",
  "description": "{{contact_description}}",
  "url": "{{contact_page_url}}",
  "mainEntity": {
    "@type": "Organization",
    "name": "{{brand_name}}",
    "telephone": "{{phone}}",
    "email": "{{email}}",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "{{street}}",
      "addressLocality": "{{city}}",
      "addressRegion": "{{state}}",
      "postalCode": "{{zip}}",
      "addressCountry": "US"
    }
  }
}
```

### HowTo (Process/Steps)

```json
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "{{process_title}}",
  "description": "{{process_description}}",
  "step": [
    {
      "@type": "HowToStep",
      "position": 1,
      "name": "{{step_1_title}}",
      "text": "{{step_1_description}}"
    },
    {
      "@type": "HowToStep",
      "position": 2,
      "name": "{{step_2_title}}",
      "text": "{{step_2_description}}"
    }
  ]
}
```

---

## Meta Tag Cheat Sheet

### Character Limits

| Tag | Min | Optimal | Max | Notes |
|-----|-----|---------|-----|-------|
| Meta Title | 30 | 50-60 | 60 | Google truncates at ~60 chars |
| Meta Description | 70 | 150-160 | 160 | Google truncates at ~160 chars |
| OG Title | 30 | 55-60 | 90 | Facebook truncates at ~90 |
| OG Description | 50 | 55-200 | 300 | Most platforms show ~200 |
| OG Image Alt | 10 | 50-100 | 125 | Descriptive, contextual |
| URL Slug | 3 | 3-5 words | 75 chars | Lowercase, hyphens, keywords |

### Meta Title Formulas

| Page Type | Formula | Example |
|-----------|---------|---------|
| Home | `Brand - Primary Value Prop` | "TS&L - Public Safety Consulting & Emergency Management" |
| Service | `Service - Specific Benefit \| Brand` | "Emergency Planning - Protect Your Community \| TS&L" |
| Blog | `Article Title \| Brand Blog` | "5 Emergency Management Best Practices \| TS&L Blog" |
| About | `About Brand - What We Do` | "About TS&L - Expert Public Safety Consultants" |
| Contact | `Contact Brand - CTA` | "Contact TS&L - Request a Free Safety Assessment" |
| Pricing | `Pricing - Plans Starting At $X \| Brand` | "Pricing - Plans Starting at $499/mo \| TS&L" |

### Meta Description Formulas

| Page Type | Formula |
|-----------|---------|
| Home | `[Value proposition]. [Key differentiator]. [CTA].` |
| Service | `[What you offer]. [Who it's for]. [Expected outcome]. [CTA].` |
| Blog | `[What the reader will learn]. [Why it matters]. Read more.` |
| About | `[Who you are]. [What you do]. [Why choose you].` |
| Contact | `[How to reach you]. [What happens next]. [Response time].` |

### Open Graph Image Specifications

| Platform | Recommended Size | Aspect Ratio | Max File Size |
|----------|-----------------|--------------|---------------|
| Facebook | 1200 x 630 px | 1.91:1 | 8 MB |
| Twitter | 1200 x 628 px | 1.91:1 | 5 MB |
| LinkedIn | 1200 x 627 px | 1.91:1 | 5 MB |
| General | 1200 x 630 px | 1.91:1 | 5 MB |

---

## Alt Text Decision Tree

```
Is the image purely decorative (border, spacer, background pattern)?
├── YES → alt="" (empty string, not omitted)
└── NO → Does the image contain text?
    ├── YES → Is the text also present in nearby page content?
    │   ├── YES → alt="" or brief contextual description
    │   └── NO → Include the full text in the alt attribute
    └── NO → Is it a simple photo or illustration?
        ├── YES → Describe the subject and its context in the page
        │         Example: "Fire chief reviewing emergency response plan with team"
        └── NO → Is it a complex image (chart, graph, infographic)?
            ├── YES → Provide a brief summary in alt, full description in adjacent text
            │         Example: alt="Response time trends 2020-2025 — see data table below"
            └── NO → Is it a functional image (icon as button, linked logo)?
                ├── YES → Describe the function, not the appearance
                │         Example: alt="Search" (not "magnifying glass icon")
                └── NO → Describe what is visually important for understanding the content
```

### Alt Text Quality Rules

| Rule | Good | Bad |
|------|------|-----|
| Be specific | "Firefighters evacuating residents during flood response drill" | "People outside" |
| State context | "Chart showing 40% reduction in response times after training" | "Chart" |
| Skip redundancy | "TS&L team at annual safety conference" | "Image of TS&L team photo at conference" |
| Keep it concise | "Emergency dispatch center with 12 active monitoring stations" | "This is a photograph of the inside of our state-of-the-art emergency dispatch center which has twelve monitoring stations each equipped with..." |
| Match page purpose | "Sarah Chen presenting emergency preparedness workshop" (on About page) | "Woman at podium" |

---

## WCAG 2.1 AA Quick Reference (Webflow-Relevant)

### Perceivable

| Criterion | Requirement | Webflow Implementation |
|-----------|-------------|----------------------|
| 1.1.1 Non-text Content | All images have alt text | `asset_tool` → update_asset with alt_text |
| 1.3.1 Info and Relationships | Semantic HTML structure | DOM elements with proper tags, heading levels |
| 1.3.2 Meaningful Sequence | Reading order matches visual order | Webflow element order = DOM order |
| 1.4.1 Use of Color | Color is not the only visual means | Add icons/text alongside color indicators |
| 1.4.3 Contrast (Minimum) | 4.5:1 for normal text, 3:1 for large | `style_tool` with proper color values |
| 1.4.4 Resize Text | Content usable at 200% zoom | Use relative units (rem, em, %) |
| 1.4.10 Reflow | No horizontal scroll at 320px width | Webflow responsive breakpoints |
| 1.4.11 Non-text Contrast | 3:1 for UI components and graphics | Focus rings, borders, icons |

### Operable

| Criterion | Requirement | Webflow Implementation |
|-----------|-------------|----------------------|
| 2.1.1 Keyboard | All functionality via keyboard | Native Webflow elements are keyboard accessible |
| 2.4.1 Bypass Blocks | Skip navigation link | DOM element with skip link as first child of body |
| 2.4.2 Page Titled | Descriptive page title | `de_page_tool` → create_page with meta_title |
| 2.4.3 Focus Order | Logical tab order | Matches Webflow element order |
| 2.4.4 Link Purpose | Link text describes destination | Descriptive link text, no "click here" |
| 2.4.6 Headings and Labels | Descriptive headings | Proper H1-H6 hierarchy |
| 2.4.7 Focus Visible | Visible focus indicator | `style_tool` with :focus pseudo styles |

### Understandable

| Criterion | Requirement | Webflow Implementation |
|-----------|-------------|----------------------|
| 3.1.1 Language of Page | `lang` attribute on html | Set via Webflow site settings |
| 3.2.3 Consistent Navigation | Same nav on every page | `de_component_tool` → reusable nav component |
| 3.3.1 Error Identification | Form errors clearly described | Webflow form validation messages |
| 3.3.2 Labels or Instructions | Form inputs have labels | Label elements associated with inputs |

### Robust

| Criterion | Requirement | Webflow Implementation |
|-----------|-------------|----------------------|
| 4.1.1 Parsing | Valid HTML | Webflow generates valid HTML by default |
| 4.1.2 Name, Role, Value | ARIA attributes on custom components | `element_tool` → add_or_update_attribute |

---

## Core Web Vitals Thresholds

| Metric | What It Measures | Good | Needs Work | Poor |
|--------|-----------------|------|------------|------|
| **LCP** | Largest Contentful Paint — when the largest visible element finishes rendering | < 2.5s | 2.5s - 4.0s | > 4.0s |
| **CLS** | Cumulative Layout Shift — visual stability, elements moving after initial render | < 0.1 | 0.1 - 0.25 | > 0.25 |
| **INP** | Interaction to Next Paint — responsiveness to user input | < 200ms | 200ms - 500ms | > 500ms |

### Webflow-Specific Optimization Actions

| Metric | Action | How in Webflow |
|--------|--------|---------------|
| LCP | Optimize hero image | Upload compressed image (< 200KB), Webflow auto-generates srcset |
| LCP | Preload critical fonts | `data_scripts_tool` → header script with `<link rel="preload">` |
| LCP | Reduce above-fold DOM depth | Keep hero section to 3 levels max in `element_builder` |
| CLS | Set image dimensions | `element_tool` → add_or_update_attribute with width/height |
| CLS | Font display swap | `style_tool` → set `font-display: swap` on @font-face |
| CLS | Avoid dynamic above-fold content | Place dynamic elements below the fold |
| INP | Footer scripts | `data_scripts_tool` → location: "footer" for analytics |
| INP | Use Webflow interactions | Prefer CSS animations over JavaScript |
| INP | Minimize custom JS | Keep inline scripts under 2000 chars per script |

---

## Webflow MCP Tool Quick Reference

### Workflow Order

```
1. webflow_guide_tool        ← ALWAYS call first
2. data_sites_tool           ← Get site ID
3. data_pages_tool           ← Audit existing pages
4. de_page_tool              ← Create new page
5. element_builder           ← Build element tree
6. element_tool              ← Modify existing elements
7. style_tool                ← Create/update styles
8. asset_tool                ← Manage images + alt text
9. data_pages_tool           ← Set SEO metadata + OG tags
10. data_scripts_tool        ← Inject JSON-LD schema
11. data_enterprise_tool     ← Redirects, robots.txt (Enterprise only)
12. data_sites_tool          ← Publish site
```

### Tool → Task Mapping

| I want to... | Use this tool | Action |
|--------------|--------------|--------|
| Get my site ID | `data_sites_tool` | list_sites |
| Create a new page | `de_page_tool` | create_page |
| Switch to an existing page | `de_page_tool` | switch_page |
| Add sections and elements | `element_builder` | (element_schema with children) |
| Change a heading level | `element_tool` | set_heading_level |
| Set text content | `element_tool` | set_text |
| Add ARIA attributes | `element_tool` | add_or_update_attribute |
| Create a CSS class | `style_tool` | create_style |
| Update styles for mobile | `style_tool` | update_style (breakpoint_id: "small") |
| Add hover effect | `style_tool` | update_style (pseudo: "hover") |
| Set meta title/description | `data_pages_tool` | update_page_settings |
| Set Open Graph tags | `data_pages_tool` | update_page_settings (openGraph) |
| Add image alt text | `asset_tool` | update_asset (alt_text) |
| List all images | `asset_tool` | get_all_assets_and_folders |
| Inject JSON-LD schema | `data_scripts_tool` | add_inline_site_script (header) |
| Add analytics script | `data_scripts_tool` | add_inline_site_script (footer) |
| Create a CMS collection | `data_cms_tool` | create_collection |
| Add CMS items | `data_cms_tool` | create_collection_items |
| Create design tokens | `variable_tool` | create_color_variable, create_size_variable |
| Make a reusable component | `de_component_tool` | transform_element_to_component |
| Set up 301 redirect | `data_enterprise_tool` | create_301_redirect |
| Update robots.txt | `data_enterprise_tool` | update_robots_txt |
| Publish the site | `data_sites_tool` | publish_site |

### Breakpoint IDs for Responsive Styles

| Breakpoint | ID | Min Width |
|-----------|-----|-----------|
| XXL | `xxl` | 1920px |
| XL | `xl` | 1440px |
| Large | `large` | 1280px |
| Main (Desktop) | `main` | 992px |
| Medium (Tablet) | `medium` | 768px |
| Small (Mobile Landscape) | `small` | 480px |
| Tiny (Mobile Portrait) | `tiny` | 0px |

### Context Parameter Examples

The `context` parameter (required on all tools) should be 15-25 words in third person:

| Action | Context Example |
|--------|----------------|
| Listing sites | "The user wants to retrieve their Webflow site ID to begin building a new landing page." |
| Creating page | "The user is creating a new public safety services page with SEO metadata for their consulting firm." |
| Building elements | "The user is building the hero section with H1 heading, subtitle, and CTA button for the landing page." |
| Setting alt text | "The user is updating image alt text across the site to improve accessibility and SEO compliance." |
| Injecting schema | "The user is adding Organization JSON-LD structured data to the site header for search engine rich results." |
