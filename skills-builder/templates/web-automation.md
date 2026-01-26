---
name: <skill-name>
description: <What this skill does and WHEN it should automatically activate>
version: 1.0.0
triggers:
  - <keyword1>
  - <keyword2>
  - scrape
  - browse
  - website
domain: web
complexity: moderate
dependencies: []
browser: true  # ← This skill requires web-tools
author: auto-generated
created: <ISO-DATE>
---

# <Skill Name>

## Overview
<2-3 sentences explaining the web automation this skill performs>

## Auto-Activation Conditions
This skill activates when:
- [ ] Request involves web browsing or scraping
- [ ] User mentions specific websites or URLs
- [ ] Task requires extracting data from web pages
- [ ] Form submission or web interaction needed

Does NOT activate when:
- [ ] Task can be done via API instead of browser
- [ ] Data is available locally
- [ ] Simple HTTP request would suffice (use `requests` instead)

## Browser Integration
**Requires**: `@../web-tools/CLAUDE.md`

This skill uses browser automation. The web-tools context will be auto-loaded.

## Instructions

### Phase 1: Setup
1. Initialize browser session
2. Configure any needed authentication
3. Set appropriate timeouts

```python
from browser_use import Agent, Browser
browser = Browser(headless=True)
```

### Phase 2: Navigation
1. Navigate to target URL
2. Wait for page load
3. Handle any popups/modals

```python
await browser.goto('<target-url>')
await browser.wait_for_load()
```

### Phase 3: Extraction/Interaction
1. <Specific steps for this skill>
2. Use robust selectors
3. Handle dynamic content

```python
# Example extraction
data = await browser.get_all('<selector>')
```

### Phase 4: Cleanup
1. Capture screenshot for verification
2. Close browser session
3. Return structured data

## Selectors Used

| Element | Selector | Fallback |
|---------|----------|----------|
| <element1> | `#primary-id` | `[data-testid="x"]` |
| <element2> | `.specific-class` | `[aria-label="y"]` |

## Error Handling

### Common Failures
| Error | Cause | Recovery |
|-------|-------|----------|
| ElementNotFound | Page structure changed | Try fallback selector |
| Timeout | Slow network | Increase timeout, retry |
| CAPTCHA | Bot detection | Use cloud browser |

### Recovery Pattern
```python
async def safe_extract(browser, selector, retries=3):
    for i in range(retries):
        try:
            return await browser.get_text(selector)
        except ElementNotFound:
            await browser.wait(1000)
            if i == retries - 1:
                await browser.screenshot('debug.png')
                raise
```

## Examples

### Example 1: <Scenario>
**Input**: "<User request like 'scrape prices from example.com'>"

**Execution**:
```python
await browser.goto('https://example.com/products')
prices = await browser.get_all('.product-price')
return [p.text for p in prices]
```

**Output**:
```json
["$19.99", "$29.99", "$39.99"]
```

### Example 2: <Scenario>
**Input**: "<User request>"

**Execution**: ...

## Rate Limiting
- Delay between requests: <X> seconds
- Max pages per session: <Y>
- Respect robots.txt: yes/no

## Anti-Detection
- [ ] Randomize delays
- [ ] Rotate user agents
- [ ] Use realistic viewport
- [ ] Mimic human scroll patterns

## Output Format
This skill returns:
```json
{
  "success": true,
  "data": [...],
  "source_url": "https://...",
  "timestamp": "ISO-8601",
  "screenshots": ["path/to/screenshot.png"]
}
```

## Quality Checklist
Before completing, verify:
- [ ] All data successfully extracted
- [ ] No CAPTCHA blocks encountered
- [ ] Screenshots captured for audit
- [ ] Structured data returned
- [ ] Browser session properly closed

## Changelog
- v1.0.0 (<date>): Initial creation
