# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A Claude-based AI agent framework for orchestrating skills and browser automation. The three-layer architecture:

```
agent-builder/    →  Orchestration: routes requests to appropriate skills
       ↓
skills-builder/   →  Skill factory: matches queries, creates/manages skills
       ↓
web-tools/        →  Browser automation: browser-use + CDP patterns
```

**Data flow**: User request → agent-builder matches keywords → triggers skill from registry → skill may invoke web-tools if `browser: true`

## Skill System

Skills are defined in `skills-builder/skills/<name>/SKILL.md` with YAML frontmatter containing triggers, domain, and dependencies. Skill matching uses: keyword match (×3) + semantic similarity (×2) + domain match (×1). Threshold: score ≥ 7 to activate. When creating skills, always update `skills-builder/registry.md`.

---

## Folder Structure
```
claude-ai-orchestration/
├── CLAUDE.md                    # This file
├── README.md                    # Project documentation
├── pyproject.toml               # Dependencies
├── .env.example                 # Environment template
├── agent-builder/
│   ├── CLAUDE.md                # Orchestration instructions
│   └── orchestrator.py          # Python automation script
├── skills-builder/
│   ├── CLAUDE.md                # Skill creation standards
│   ├── registry.md              # Skill index
│   ├── templates/               # Skill templates
│   └── skills/                  # Individual skills
│       ├── web-scraping/
│       ├── marketing-copy/
│       └── code-review/
└── web-tools/
    └── CLAUDE.md                # Browser automation
```

## Quick Start

```bash
# Install dependencies
uv sync

# Set up environment
cp .env.example .env
# Add your ANTHROPIC_API_KEY to .env

# Run orchestrator
uv run python agent-builder/orchestrator.py
```

## Commands

```bash
# Package management (uv only)
uv add <package>              # Add dependency
uv sync                       # Install dependencies
uv run python <file>          # Run with deps

# Orchestrator commands
/skills                       # List available skills
/quit                         # Exit
```

## Python Standards

- Python >= 3.11 with async/await
- Type hints required
- All functions need docstrings

## Routing

### When working at root level:
- File operations → Handle here
- "Help me build..." → Route to `agent-builder/CLAUDE.md`
- "Scrape/browse X" → Route to `agent-builder/CLAUDE.md`
- "Create a skill..." → Route to `skills-builder/CLAUDE.md`

## Commit Format

```
<type>: <description>

Types: feat, fix, docs, refactor, chore
```
