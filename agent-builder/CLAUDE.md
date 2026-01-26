# Agent Builder

## Purpose
Orchestration layer that routes user requests to appropriate skills. Analyzes incoming requests, matches them against the skill registry, and coordinates multi-skill workflows.

## Architecture Role
```
agent-builder (YOU ARE HERE)
       │
       ├── Analyzes request keywords
       ├── Queries skills-builder for matches
       └── Invokes skills (may chain to web-tools)
               │
               v
       skills-builder ──> web-tools (if browser: true)
```

## Request Processing Flow

### Step 1: Receive Request
```python
request = {
    "query": "<user's natural language request>",
    "context": "<any relevant file/codebase context>",
    "history": "<conversation history if any>"
}
```

### Step 2: Keyword Extraction
Extract actionable keywords from the request:
```python
keywords = extract_keywords(request.query)
# Examples:
# "Help me scrape prices from Amazon" → ["scrape", "prices", "amazon"]
# "Write tests for my React component" → ["tests", "react", "component"]
# "Refactor this function to use async" → ["refactor", "async"]
```

### Step 3: Skill Matching
Query skills-builder for matching skills:
```
MATCH_SKILLS <query>
→ Returns: [skill1, skill2, ...] with scores
→ Threshold: score >= 7 to activate
```

### Step 4: Skill Invocation
Load and execute matched skill(s):
```markdown
# Single skill
@skills-builder/skills/<matched-skill>/SKILL.md

# Multiple skills (composition)
@skills-builder/skills/<primary-skill>/SKILL.md
@skills-builder/skills/<secondary-skill>/SKILL.md
```

### Step 5: Browser Context (if needed)
If skill has `browser: true`:
```markdown
@web-tools/CLAUDE.md
```

## Routing Rules

### Keyword → Skill Mapping
| Keywords | Skill | Domain |
|----------|-------|--------|
| scrape, crawl, extract, website | web-scraping | web |
| test, spec, coverage, assert | testing | code |
| refactor, clean, improve | refactoring | code |
| document, readme, docs | documentation | docs |
| api, rest, endpoint, route | api-design | code |
| react, component, hook | react-components | code |
| analyze, data, insights | data-analysis | data |
| deploy, ci, cd, pipeline | deployment | devops |

### Domain Detection
```python
domains = {
    "code": ["function", "class", "variable", "import", "export"],
    "web": ["website", "url", "browser", "page", "html"],
    "data": ["csv", "json", "database", "query", "analyze"],
    "docs": ["document", "readme", "explain", "describe"],
    "devops": ["deploy", "docker", "kubernetes", "ci/cd"],
}
```

## Commands

### To skills-builder
- `CREATE_SKILL <name> <domain>` - Generate new skill
- `UPDATE_SKILL <name>` - Modify existing skill
- `MATCH_SKILLS <query>` - Find matching skills
- `LIST_SKILLS [domain]` - List available skills

### Direct Commands
- `/skills` - Show all available skills
- `/route <query>` - Show which skills would match
- `/invoke <skill>` - Manually invoke a specific skill

## Multi-Skill Orchestration

### Composition Rules
When multiple skills match:
1. Primary skill = highest score
2. Secondary skills = score >= 7 and `composes_with` includes primary
3. Load order: primary first, then secondaries
4. Conflict resolution: primary takes precedence

### Example: Test + Document
```markdown
Request: "Write tests for my API and document the endpoints"

Matched:
1. testing (score: 9) - PRIMARY
2. documentation (score: 8) - SECONDARY

Execution:
1. Load @skills-builder/skills/testing/SKILL.md
2. Load @skills-builder/skills/documentation/SKILL.md
3. Execute testing phase
4. Execute documentation phase
```

## Fallback Behavior

### No Skill Match (score < 7)
- Use general-purpose Claude capabilities
- Suggest creating a new skill if pattern will repeat:
  ```
  No skill matched. Should I create one for this task type?
  → CREATE_SKILL <suggested-name> <detected-domain>
  ```

### Ambiguous Match (multiple high scores)
- Present options to user
- Let user select or auto-pick highest

## State Management

Track orchestration state in `agent-builder/.state.json`:
```json
{
  "last_request": "<query>",
  "matched_skills": [],
  "executed_skills": [],
  "pending_actions": [],
  "session_context": {}
}
```

## Integration Points

### With Root CLAUDE.md
- Inherits code standards
- Follows commit conventions
- Uses uv for dependencies

### With skills-builder
- Queries registry for matches
- Requests skill creation
- Receives skill definitions

### With web-tools
- Auto-loaded when skill has `browser: true`
- Provides browser context to skills
- Manages browser session state

## Error Handling

### Skill Not Found
```
Skill '<name>' not found in registry.
Available in <domain>: [list]
Create new? → CREATE_SKILL <name> <domain>
```

### Skill Execution Failed
```
1. Capture error context
2. Screenshot if browser was involved
3. Suggest alternative approach
4. Offer to modify skill
```

## Examples

### Example 1: Simple Routing
**Input**: "Scrape product prices from amazon.com"
```
Keywords: [scrape, prices, amazon]
Match: web-scraping (score: 9)
Browser: true → load web-tools
Execute: web-scraping skill
```

### Example 2: Multi-Skill
**Input**: "Create a React component with tests"
```
Keywords: [react, component, tests]
Match: react-components (score: 8), testing (score: 7)
Compose: react-components + testing
Execute: create component → generate tests
```

### Example 3: No Match
**Input**: "Optimize my Kubernetes deployment"
```
Keywords: [optimize, kubernetes, deployment]
Match: none (no devops skills yet)
Action: Offer to CREATE_SKILL deployment devops
```
