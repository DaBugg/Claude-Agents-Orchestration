"""
Agent Builder Orchestrator

Automates the skill-loading workflow:
1. Scans registry for matching skills
2. Loads SKILL.md content
3. Calls Claude API with skill as system prompt
4. Returns generated output

Usage:
    uv run python agent-builder/orchestrator.py
"""
from __future__ import annotations

import os
import re
from pathlib import Path

from anthropic import Anthropic
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

# Paths
ROOT = Path(__file__).parent.parent
REGISTRY_PATH = ROOT / "skills-builder" / "registry.md"
SKILLS_PATH = ROOT / "skills-builder" / "skills"


def load_registry() -> list[dict]:
    """Parse skills-builder/registry.md and extract skill entries."""
    if not REGISTRY_PATH.exists():
        print(f"❌ Registry not found: {REGISTRY_PATH}")
        return []

    content = REGISTRY_PATH.read_text()
    skills = []

    # Parse the Full Catalog section
    # Each skill entry starts with ### skill-name
    pattern = r"### (\S+)\n(.*?)(?=\n### |\n---|\Z)"
    matches = re.findall(pattern, content, re.DOTALL)

    for name, details in matches:
        skill = {"name": name}

        # Extract fields
        if path_match := re.search(r"\*\*Path\*\*:\s*(.+)", details):
            skill["path"] = path_match.group(1).strip()
        if triggers_match := re.search(r"\*\*Triggers\*\*:\s*(.+)", details):
            skill["triggers"] = [t.strip() for t in triggers_match.group(1).split(",")]
        if domain_match := re.search(r"\*\*Domain\*\*:\s*(\w+)", details):
            skill["domain"] = domain_match.group(1).strip()
        if browser_match := re.search(r"\*\*Browser\*\*:\s*(\w+)", details):
            skill["browser"] = browser_match.group(1).strip().lower() == "yes"

        if "triggers" in skill:  # Only add valid skills
            skills.append(skill)

    return skills


def match_skill(query: str, registry: list[dict]) -> tuple[dict | None, int]:
    """
    Score and match skills to query.

    Scoring (from CLAUDE.md):
    - Keyword match: ×3 weight
    - Domain match: ×1 weight
    Threshold: score >= 4 to activate (adjusted for single keywords)
    """
    query_lower = query.lower()
    query_words = set(query_lower.split())

    best_skill = None
    best_score = 0

    for skill in registry:
        score = 0

        # Keyword matching (×3 weight)
        for trigger in skill.get("triggers", []):
            trigger_lower = trigger.lower()
            # Check if trigger is in query (phrase or word match)
            if trigger_lower in query_lower:
                score += 3
            # Also check word overlap
            elif any(word in query_words for word in trigger_lower.split()):
                score += 2

        # Domain keywords (×1 weight)
        domain = skill.get("domain", "")
        domain_keywords = {
            "creative": ["write", "copy", "marketing", "ad", "content", "script"],
            "web": ["scrape", "browse", "website", "extract", "crawl"],
            "code": ["function", "class", "code", "implement", "build"],
            "docs": ["document", "readme", "explain", "describe"],
            "data": ["analyze", "csv", "json", "data", "report"],
            "devops": ["deploy", "docker", "ci", "pipeline"],
        }

        for keyword in domain_keywords.get(domain, []):
            if keyword in query_lower:
                score += 1

        if score > best_score:
            best_score = score
            best_skill = skill

    return best_skill, best_score


def load_skill(skill_name: str) -> str | None:
    """Read SKILL.md content for the given skill."""
    skill_path = SKILLS_PATH / skill_name / "SKILL.md"

    if not skill_path.exists():
        print(f"❌ Skill file not found: {skill_path}")
        return None

    return skill_path.read_text()


def generate(skill_content: str, user_query: str) -> str:
    """Call Claude API with skill as system prompt."""
    api_key = os.getenv("ANTHROPIC_API_KEY")

    if not api_key:
        return "❌ Error: ANTHROPIC_API_KEY not set. Add it to your .env file."

    client = Anthropic(api_key=api_key)

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=2048,
        system=skill_content,
        messages=[{"role": "user", "content": user_query}]
    )

    return response.content[0].text


def run_query(query: str) -> str:
    """Process a single query through the orchestrator."""
    print("\n" + "=" * 60)
    print("🔍 AGENT BUILDER - Skill Orchestrator")
    print("=" * 60)

    # Step 1: Load registry
    print("\n📋 Loading registry...")
    registry = load_registry()
    print(f"   Found {len(registry)} skills")

    # Step 2: Match skill
    print(f"\n🎯 Matching query: \"{query}\"")
    skill, score = match_skill(query, registry)

    if not skill or score < 4:
        print(f"   ❌ No skill matched (best score: {score})")
        print("   → Using general Claude capabilities")
        return "No matching skill found. Please try a different query or create a new skill."

    print(f"   ✅ Matched: {skill['name']} (score: {score})")
    print(f"   📁 Domain: {skill.get('domain', 'unknown')}")
    print(f"   🔑 Triggers: {', '.join(skill.get('triggers', [])[:5])}")

    # Step 3: Load skill
    print(f"\n📖 Loading skill: skills-builder/skills/{skill['name']}/SKILL.md")
    skill_content = load_skill(skill["name"])

    if not skill_content:
        return "Failed to load skill file."

    print(f"   ✅ Loaded ({len(skill_content)} chars)")

    # Step 4: Check browser requirement
    if skill.get("browser"):
        print("\n🌐 Note: This skill requires browser automation (web-tools)")

    # Step 5: Generate with Claude
    print("\n🤖 Generating with Claude API...")
    print("-" * 60)

    result = generate(skill_content, query)

    print("\n" + "=" * 60)
    print("📤 OUTPUT")
    print("=" * 60)

    return result


async def main() -> None:
    """Interactive CLI loop."""
    print("\n" + "=" * 60)
    print("🚀 AGENT BUILDER - Skill Orchestrator")
    print("=" * 60)
    print("\nThis tool automatically matches your queries to skills")
    print("and generates output using the SKILL.md instructions.\n")
    print("Commands:")
    print("  /skills  - List available skills")
    print("  /quit    - Exit")
    print("-" * 60)

    while True:
        try:
            query = input("\n💬 Enter your request: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n\n👋 Goodbye!")
            break

        if not query:
            continue

        if query.lower() == "/quit":
            print("\n👋 Goodbye!")
            break

        if query.lower() == "/skills":
            registry = load_registry()
            print("\n📋 Available Skills:")
            print("-" * 40)
            for skill in registry:
                browser = "🌐" if skill.get("browser") else "  "
                print(f"  {browser} {skill['name']} ({skill.get('domain', '?')})")
                print(f"      Triggers: {', '.join(skill.get('triggers', [])[:4])}")
            continue

        result = run_query(query)
        print(result)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
