# Skills Builder

## Purpose
Factory and registry for all agent skills. Automatically matches requests to optimal skills, creates new skills on demand, and maintains the skill library.

## Architecture Role
```
agent-builder ──triggers──> skills-builder (YOU ARE HERE)
                                    │
                                    ├──> skills/<skill-name>/SKILL.md
                                    ├──> registry.md
                                    └──> templates/
```

## Directory Structure
```
skills-builder/
├── CLAUDE.md          # This file
├── registry.md        # Master list of all skills
├── templates/         # Skill templates by type
│   ├── code.md
│   ├── document.md
│   ├── automation.md
│   └── research.md
└── skills/            # All generated skills
    ├── <skill-name>/
    │   ├── SKILL.md
    │   ├── examples/
    │   └── scripts/   # Optional helper scripts
    └── ...
```

## Skill Matching Algorithm

### On Query Receipt:
```python
def match_skill(query):
    scores = {}
    for skill in registry:
        score = 0
        # Keyword matching
        score += sum(1 for trigger in skill.triggers if trigger in query.lower()) * 3
        # Semantic similarity to description
        score += semantic_match(query, skill.description) * 2
        # Domain matching
        score += domain_match(query, skill.domain)
        scores[skill.name] = score
    
    # Return skills scoring above threshold
    return [s for s, score in scores.items() if score >= 7]
```

### Trigger Keywords (examples)
| Skill Type | Triggers |
|------------|----------|
| api-design | "api", "rest", "endpoint", "route", "http" |
| react | "react", "component", "jsx", "hook", "state" |
| testing | "test", "spec", "coverage", "mock", "assert" |
| scraping | "scrape", "crawl", "extract", "parse html" |
| database | "sql", "query", "schema", "migrate", "orm" |
| docs | "document", "readme", "api docs", "jsdoc" |

## Skill Creation Standards

### SKILL.md Template
```markdown
---
name: <lowercase-hyphenated>
description: <1-2 sentences: what + when>
version: 1.0.0
triggers:
  - <keyword1>
  - <keyword2>
  - <phrase trigger>
domain: <code|docs|data|web|devops|creative>
complexity: <simple|moderate|complex>
dependencies:
  - <other-skill-name>  # if needed
browser: false
author: auto-generated
created: <ISO date>
---

# <Skill Name>

## Overview
<Brief explanation of what this skill accomplishes>

## When This Skill Activates
- <Condition 1>
- <Condition 2>
- NOT when: <exclusion conditions>

## Instructions

### Step 1: <Phase Name>
<Detailed instructions>

### Step 2: <Phase Name>
<Detailed instructions>

## Code Patterns
\`\`\`<language>
// Example pattern this skill uses
\`\`\`

## Examples

### Input
<Example request>

### Output
<Expected result>

## Integration
- Works with: <compatible skills>
- Requires: <dependencies>
- Browser: <yes/no - if yes, loads web-tools>

## Anti-patterns
- ❌ <What not to do>
- ❌ <Common mistake>

## Changelog
- v1.0.0: Initial creation
```

## Registry Format (registry.md)

```markdown
# Skills Registry

## Quick Reference
| Name | Domain | Triggers | Browser | Dependencies |
|------|--------|----------|---------|--------------|
| api-design | code | api, rest, endpoint | no | testing |
| web-scraping | web | scrape, crawl | yes | - |

## Full Catalog

### api-design
- **Path**: skills/api-design/SKILL.md
- **Description**: Designs RESTful APIs with OpenAPI specs
- **Last Updated**: 2024-01-15

### web-scraping
- **Path**: skills/web-scraping/SKILL.md  
- **Description**: Extracts data from websites using browser automation
- **Last Updated**: 2024-01-15
- **Requires**: @../web-tools/CLAUDE.md
```

## Auto-Generation Rules

### When to Create a New Skill
1. Request pattern will repeat (user confirms or obvious)
2. No existing skill covers >60% of the need
3. Task is generalizable (not one-off with hardcoded values)

### Skill Naming Convention
- Lowercase with hyphens: `react-hooks`, `api-testing`
- Action-oriented when possible: `generate-docs`, `deploy-aws`
- Domain prefix for clarity: `db-migrations`, `ui-components`

### Quality Checklist Before Saving
- [ ] Description clearly states WHEN to activate
- [ ] At least 3 trigger keywords
- [ ] Includes concrete examples
- [ ] Anti-patterns documented
- [ ] Dependencies listed
- [ ] Browser flag set correctly

## Skill Composition

Multiple skills can combine. Declare in SKILL.md:
```yaml
composes_with:
  - testing      # Always combine with testing skill
  - documentation # Suggest but don't require
```

When composing:
1. Load primary skill first
2. Merge instructions (primary takes precedence on conflicts)
3. Union all triggers
4. AND all dependencies

## Commands

### From agent-builder
- `CREATE_SKILL <name> <domain>` - Generate new skill
- `UPDATE_SKILL <name>` - Modify existing skill
- `MATCH_SKILLS <query>` - Return matching skills
- `LIST_SKILLS [domain]` - List all or filtered skills

### Direct Usage
- `/newskill` - Interactive skill creation wizard
- `/skills` - Show registry
- `/skill <name>` - Load and display specific skill

## Maintenance

### Skill Deprecation
When a skill becomes obsolete:
1. Add `deprecated: true` to frontmatter
2. Add `superseded_by: <new-skill>` if applicable
3. Keep for 30 days, then archive to `skills/_archive/`

### Skill Versioning
- Bump patch (1.0.x) for minor instruction tweaks
- Bump minor (1.x.0) for new capabilities
- Bump major (x.0.0) for breaking changes to interface

## Integration with Web-Tools

When `browser: true` in skill:
```markdown
## Browser Integration
This skill requires web-tools. Load with:
@../web-tools/CLAUDE.md

### Browser Actions Used
- navigate(url)
- click(selector)
- extract(selector)
- screenshot()
```

## Starter Skills to Bootstrap

Create these foundational skills first:

1. **code-review** - Reviews code for issues and improvements
2. **testing** - Generates tests for any code
3. **documentation** - Creates docs, READMEs, comments
4. **refactoring** - Improves code structure
5. **api-design** - Designs REST/GraphQL APIs
6. **react-components** - React component patterns
7. **web-scraping** - Browser-based data extraction
8. **data-analysis** - Analyzes datasets, generates insights
9. **cli-tools** - Creates command-line applications
10. **debugging** - Systematic bug hunting

## State
Track in `skills-builder/.state.json`:
```json
{
  "total_skills": 0,
  "skills_by_domain": {},
  "last_created": null,
  "most_used": [],
  "pending_review": []
}
```
