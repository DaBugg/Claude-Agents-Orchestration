---
name: <skill-name>
description: <What this skill does and WHEN it should automatically activate>
version: 1.0.0
triggers:
  - <keyword1>
  - <keyword2>
  - <phrase trigger>
domain: code
complexity: moderate
dependencies: []
browser: false
author: auto-generated
created: <ISO-DATE>
---

# <Skill Name>

## Overview
<2-3 sentences explaining what this skill accomplishes>

## Auto-Activation Conditions
This skill activates when:
- [ ] Request contains triggers: `<keyword1>`, `<keyword2>`
- [ ] Task involves <specific code task>
- [ ] User is working on <specific file types or patterns>

Does NOT activate when:
- [ ] <Exclusion condition 1>
- [ ] <Exclusion condition 2>

## Instructions

### Phase 1: Analysis
1. Understand the current codebase context
2. Identify relevant files and patterns
3. Determine scope of changes needed

### Phase 2: Implementation
1. <Step-by-step instructions>
2. <Claude should follow these exactly>
3. <Be specific about patterns to use>

### Phase 3: Verification
1. Run relevant tests
2. Check for type errors
3. Verify no regressions

## Code Patterns

### Pattern: <Pattern Name>
```<language>
// Example code that this skill produces
// Be specific about style, naming, structure
```

### Anti-Pattern: <What to Avoid>
```<language>
// ❌ Don't do this
```

## Examples

### Example 1: <Scenario>
**Input**: "<User request>"

**Output**:
```<language>
// Expected code output
```

### Example 2: <Scenario>
**Input**: "<User request>"

**Output**:
```<language>
// Expected code output
```

## Integration

### Works Well With
- `testing` - Always run tests after using this skill
- `documentation` - Update docs for any public API changes

### Conflicts With
- `<skill>` - Don't use together because <reason>

## Quality Checklist
Before completing, verify:
- [ ] Code follows project style guide
- [ ] All functions have type hints
- [ ] Error handling is appropriate
- [ ] No hardcoded values that should be config
- [ ] Tests pass (if applicable)

## Changelog
- v1.0.0 (<date>): Initial creation
