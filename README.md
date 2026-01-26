# Claude AI Orchestration

An open-source framework that turns Claude into a skill-based AI system. Instead of generic responses, Claude follows specialized "skills" - detailed instruction sets that produce consistent, high-quality output for specific tasks.

## What This Project Does

**Problem**: When you ask Claude to "write marketing copy" or "review my code", you get generic responses that vary in quality and format.

**Solution**: This framework loads specialized SKILL.md files that tell Claude exactly HOW to approach each task - with frameworks, templates, examples, and quality checklists.

```
Your Request: "Write SMS for my lead gen campaign"
                    │
                    ▼
         ┌─────────────────────┐
         │  Orchestrator       │
         │  "Which skill fits?"│
         └─────────────────────┘
                    │
                    ▼
         ┌─────────────────────┐
         │  marketing-copy     │
         │  SKILL.md loaded    │
         │  (AIDA framework,   │
         │   templates, etc.)  │
         └─────────────────────┘
                    │
                    ▼
         ┌─────────────────────┐
         │  Claude API         │
         │  Follows skill      │
         │  instructions       │
         └─────────────────────┘
                    │
                    ▼
         High-quality, consistent
         SMS copy with A/B variants
```

## Why Use This?

| Without Skills | With Skills |
|----------------|-------------|
| Generic marketing copy | AIDA framework applied, A/B variants included |
| Basic code feedback | Severity-rated issues, security checks, fix examples |
| Inconsistent format | Same structure every time |
| Have to re-explain context | Skills remember the approach |

## Quick Start

### 1. Clone & Install

```bash
git clone https://github.com/YOUR_USERNAME/claude-ai-orchestration.git
cd claude-ai-orchestration

# Install with uv (recommended)
uv sync

# Or with pip
pip install anthropic python-dotenv
```

### 2. Add Your API Key

```bash
cp .env.example .env
```

Edit `.env` and add your Anthropic API key:
```
ANTHROPIC_API_KEY=sk-ant-your-key-here
```

Get your API key at: https://console.anthropic.com/

### 3. Run the Orchestrator

```bash
uv run python agent-builder/orchestrator.py
```

### 4. Try These Examples

```
💬 Enter your request: Review this Python code for bugs: def get_user(id): return db.query(f"SELECT * FROM users WHERE id = {id}")

💬 Enter your request: Write SMS sequence for a SaaS free trial ending

💬 Enter your request: /skills
```

## Included Skills

### 1. `marketing-copy` (Creative)
**Triggers**: sms, lead gen, ad copy, drip campaign, nurture sequence

Creates SMS marketing messages and lead generation copy using:
- AIDA Framework (Attention → Interest → Desire → Action)
- 160-character SMS optimization
- A/B test variations
- Multi-day nurture sequences

### 2. `code-review` (Code)
**Triggers**: review, bugs, refactor, security review, improve code

Reviews code with:
- Severity levels (Critical → High → Medium → Low)
- Security vulnerability detection
- Performance analysis
- Fix examples with explanations

### 3. `web-scraping` (Web)
**Triggers**: scrape, crawl, extract, get data from website

Browser-based data extraction with:
- Pagination handling
- Selector strategies
- Rate limiting
- Error recovery

## How to Add Your Own Skills

### Option A: Ask Claude Code to Generate It (Recommended)

The easiest way to create a new skill is to ask Claude Code directly. It will generate the complete skill folder, SKILL.md file, and update the registry automatically.

**Workflow:**

```
┌─────────────────────────────────────────────────────────────────┐
│  YOU: "Create a skill for generating unit tests"               │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  CLAUDE CODE:                                                   │
│  1. Reads skills-builder/CLAUDE.md for skill standards         │
│  2. Uses templates from skills-builder/templates/              │
│  3. Creates new folder: skills-builder/skills/unit-tests/      │
│  4. Generates SKILL.md with:                                   │
│     - YAML frontmatter (triggers, domain, browser flag)        │
│     - Detailed instructions                                     │
│     - Examples and templates                                    │
│  5. Updates skills-builder/registry.md                         │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  OUTPUT: New skill ready to use                                 │
│                                                                 │
│  skills-builder/skills/unit-tests/                             │
│  └── SKILL.md    ← Complete skill with instructions            │
└─────────────────────────────────────────────────────────────────┘
```

**Example Prompts:**

```bash
# In Claude Code CLI or IDE extension
"Create a skill for generating unit tests"

"Build me a skill that writes API documentation"

"I need a skill for optimizing SQL queries - should detect N+1 problems"

"Create a resume-writer skill for professional resumes"
```

Claude Code will:
1. Create `skills-builder/skills/<skill-name>/SKILL.md`
2. Include proper YAML frontmatter with triggers and domain
3. Write detailed instructions Claude should follow
4. Add input/output examples
5. Register the skill in `skills-builder/registry.md`

---

### Option B: Create Manually

If you prefer to create skills by hand:

#### 1. Create a skill folder
```bash
mkdir skills-builder/skills/my-skill
```

#### 2. Create SKILL.md
```markdown
---
name: my-skill
description: What this skill does
triggers:
  - keyword1
  - keyword2
domain: code
browser: false
---

# My Skill

## Instructions
<What Claude should do step-by-step>

## Examples
<Input/output examples>
```

#### 3. Update the registry
Add to `skills-builder/registry.md`:
```markdown
### my-skill
- **Path**: skills/my-skill/SKILL.md
- **Triggers**: keyword1, keyword2
- **Domain**: code
```

## Project Structure

```
claude-ai-orchestration/
├── agent-builder/
│   ├── CLAUDE.md           # Orchestration docs
│   └── orchestrator.py     # Main script
├── skills-builder/
│   ├── registry.md         # Skill index
│   ├── templates/          # Templates for new skills
│   └── skills/
│       ├── code-review/
│       ├── marketing-copy/
│       └── web-scraping/
├── web-tools/
│   └── CLAUDE.md           # Browser automation docs
├── .env.example
├── pyproject.toml
└── README.md
```

## Alternative Usage Methods

### Use with Claude Code CLI
```bash
# Claude Code automatically reads CLAUDE.md files
cd claude-ai-orchestration
claude "Review my code for security issues"
```

### Use with Claude Web (Manual)
1. Copy contents of a SKILL.md file
2. Paste at start of Claude conversation
3. Enter your request

### Use in Your Own Code
```python
from anthropic import Anthropic

# Load any skill
skill = open("skills-builder/skills/code-review/SKILL.md").read()

client = Anthropic()
response = client.messages.create(
    model="claude-sonnet-4-20250514",
    system=skill,
    messages=[{"role": "user", "content": "Review this code: ..."}]
)
print(response.content[0].text)
```

## Commands

| Command | Description |
|---------|-------------|
| `/skills` | List all available skills |
| `/quit` | Exit the orchestrator |
| Any text | Match skill and generate output |

## Requirements

- Python 3.11+
- Anthropic API key
- `uv` or `pip` for package management

## Contributing

1. Fork this repository
2. Create a new skill in `skills-builder/skills/`
3. Add it to `registry.md`
4. Submit a pull request

Skill ideas welcome:
- `test-generator` - Generate unit tests
- `api-docs` - Create API documentation
- `sql-optimizer` - Optimize SQL queries
- `react-components` - Generate React code

## License

MIT License - use freely, modify, distribute.

## Links

- [Anthropic API](https://docs.anthropic.com/)
- [Get API Key](https://console.anthropic.com/)
- [Claude Code](https://claude.ai/code)
- [Skills-Repo] (https://github.com/skillcreatorai/Ai-Agent-Skills)
