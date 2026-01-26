# Web Tools

## Purpose
Browser automation layer that any skill or agent can invoke for web interactions. Built on browser-use patterns with CDP (Chrome DevTools Protocol).

## Architecture Role
```
agent-builder ────────────────────┐
       │                          │
       v                          v
skills-builder ──browser:true──> web-tools (YOU ARE HERE)
                                     │
                                     └──> Browser (Chromium via CDP)
```

## When This Loads
- Any skill with `browser: true` in frontmatter
- agent-builder detects web-related keywords
- Direct user request for browser interaction
- Keywords: browse, search, website, scrape, click, navigate, screenshot, form, login

## Core Capabilities

### Navigation
```python
await browser.goto(url)              # Navigate to URL
await browser.reload()               # Refresh page
await browser.go_back()              # Browser back
await browser.go_forward()           # Browser forward
await browser.wait_for_load()        # Wait for page load
```

### Interaction
```python
await browser.click(selector)        # Click element
await browser.type(selector, text)   # Type into input
await browser.select(selector, val)  # Select dropdown option
await browser.hover(selector)        # Hover over element
await browser.scroll(direction, px)  # Scroll page
await browser.press(key)             # Press keyboard key
```

### Extraction
```python
await browser.get_text(selector)     # Get element text
await browser.get_html(selector)     # Get element HTML
await browser.get_attribute(sel, attr) # Get attribute
await browser.get_all(selector)      # Get all matching elements
await browser.screenshot(path)       # Take screenshot
await browser.pdf(path)              # Save as PDF
```

### State
```python
await browser.get_url()              # Current URL
await browser.get_title()            # Page title
await browser.get_cookies()          # All cookies
await browser.set_cookie(cookie)     # Set cookie
await browser.local_storage_get(key) # Get localStorage
```

## Browser-Use Integration

### Setup (using uv, never pip)
```bash
uv add browser-use
uv sync
uvx browser-use install  # Install Chromium
```

### Basic Agent Pattern
```python
from browser_use import Agent, Browser, ChatBrowserUse
import asyncio

async def web_task(task_description: str):
    browser = Browser()
    llm = ChatBrowserUse()  # Optimized for browser tasks
    
    agent = Agent(
        task=task_description,
        llm=llm,
        browser=browser,
    )
    
    history = await agent.run()
    return history

# Execute
asyncio.run(web_task("Find the price of X on Amazon"))
```

### Custom Tools Pattern
```python
from browser_use import Tools

tools = Tools()

@tools.action(description='Extract all product prices from current page')
async def extract_prices(browser) -> list:
    elements = await browser.get_all('.price')
    return [e.text for e in elements]

@tools.action(description='Fill form with provided data')
async def fill_form(browser, data: dict) -> str:
    for field, value in data.items():
        await browser.type(f'[name="{field}"]', value)
    return "Form filled"

agent = Agent(
    task="...",
    llm=llm,
    browser=browser,
    tools=tools,  # Custom tools available
)
```

## Action Patterns

### Pattern: Login Flow
```python
async def login(browser, url, username, password):
    await browser.goto(url)
    await browser.type('#username', username)
    await browser.type('#password', password)
    await browser.click('[type="submit"]')
    await browser.wait_for_load()
    return await browser.get_url()  # Verify redirect
```

### Pattern: Data Scraping
```python
async def scrape_table(browser, url, table_selector):
    await browser.goto(url)
    rows = await browser.get_all(f'{table_selector} tr')
    data = []
    for row in rows:
        cells = await row.get_all('td')
        data.append([await c.get_text() for c in cells])
    return data
```

### Pattern: Form Submission
```python
async def submit_form(browser, url, form_data):
    await browser.goto(url)
    for selector, value in form_data.items():
        await browser.type(selector, value)
    await browser.click('[type="submit"]')
    await browser.wait_for_load()
    return await browser.screenshot('confirmation.png')
```

### Pattern: Multi-Page Navigation
```python
async def crawl_paginated(browser, start_url, next_selector, max_pages=10):
    await browser.goto(start_url)
    all_data = []
    
    for _ in range(max_pages):
        # Extract current page
        data = await browser.get_all('.item')
        all_data.extend(data)
        
        # Try next page
        next_btn = await browser.query(next_selector)
        if not next_btn:
            break
        await browser.click(next_selector)
        await browser.wait_for_load()
    
    return all_data
```

## Selector Strategies

### Priority Order
1. `#id` - ID selectors (most reliable)
2. `[data-testid="x"]` - Test IDs
3. `[name="x"]` - Form field names
4. `[aria-label="x"]` - Accessibility labels
5. `.class` - Class selectors
6. `tag` - Element tags (least specific)

### Robust Selectors
```python
# Prefer
await browser.click('[data-testid="submit-button"]')
await browser.type('[name="email"]', 'test@example.com')

# Avoid (fragile)
await browser.click('.btn-primary.mt-4.flex')
await browser.click('div > div > button:nth-child(3)')
```

## Error Handling

### Retry Pattern
```python
async def robust_action(browser, action, max_retries=3):
    for attempt in range(max_retries):
        try:
            return await action()
        except ElementNotFound:
            await browser.wait(1000)  # Wait 1s
        except TimeoutError:
            await browser.reload()
    raise ActionFailed(f"Failed after {max_retries} attempts")
```

### Screenshot on Failure
```python
async def safe_action(browser, action, name):
    try:
        return await action()
    except Exception as e:
        await browser.screenshot(f'error_{name}_{timestamp()}.png')
        raise
```

## Integration API

### Called by Skills
Skills with `browser: true` can invoke:
```markdown
<!-- In any SKILL.md -->
## Browser Actions
When this skill activates with browser context:

1. @web-tools:navigate(url)
2. @web-tools:extract(selector) 
3. @web-tools:click(selector)
```

### Called by Agent-Builder
```markdown
<!-- In agent-builder request -->
Load browser context: @../web-tools/CLAUDE.md
Execute: navigate to X, extract Y, return data
```

## Session Management

### Persistent Session
```python
# Reuse browser across tasks
browser = Browser(persistent=True, profile_path='./chrome-profile')
```

### Fresh Session
```python
# Clean session for each task
browser = Browser(headless=True, incognito=True)
```

### Authentication Persistence
```python
# Use existing Chrome profile with saved logins
browser = Browser(
    profile_path='~/.config/google-chrome/Default',
    persistent=True
)
```

## Configuration

### Browser Options
```python
Browser(
    headless=False,          # Show browser window
    proxy='http://...',      # Use proxy
    user_agent='...',        # Custom UA
    viewport=(1920, 1080),   # Window size
    timeout=30000,           # Default timeout ms
    extensions=[...],        # Chrome extensions
)
```

### Environment Variables
```bash
BROWSER_USE_API_KEY=xxx     # For cloud browsers
BROWSER_HEADLESS=true       # Default headless mode
BROWSER_TIMEOUT=30000       # Default timeout
```

## Anti-Detection

### Best Practices
- Use realistic viewport sizes
- Add random delays between actions
- Rotate user agents
- Use residential proxies for sensitive sites
- Respect robots.txt and rate limits

### Cloud Browsers (for CAPTCHAs)
```python
browser = Browser(use_cloud=True)  # Browser Use Cloud
```

## Commands

- `/browse <url>` - Open URL in browser
- `/screenshot` - Capture current page
- `/extract <selector>` - Get element content
- `/click <selector>` - Click element
- `/type <selector> <text>` - Type into element
- `/cookies` - Show all cookies
- `/close` - Close browser session

## Code Standards (from browser-use)
- Always use `uv` instead of pip
- Never create random example files
- Use descriptive names and docstrings for actions
- Return ActionResult with structured content
- Async/await for all browser operations
- Type hints required on all functions

## State
Track in `web-tools/.browser-state.json`:
```json
{
  "session_active": false,
  "current_url": null,
  "cookies_count": 0,
  "screenshots_taken": [],
  "last_action": null,
  "errors": []
}
```
