---
name: marketing-copy
description: Creates SMS marketing messages, lead generation copy, and automation sequences using the AIDA framework. Activates when user asks for marketing text, SMS campaigns, lead nurturing, or ad copy.
version: 1.0.0
triggers:
  - sms
  - text message
  - marketing copy
  - lead generation
  - lead gen
  - automation sequence
  - drip campaign
  - nurture sequence
  - ad copy
  - call to action
  - cta
  - promotional text
  - marketing message
domain: creative
complexity: moderate
dependencies: []
browser: false
author: auto-generated
created: 2025-01-25
---

# Marketing Copy

## Overview
Generates high-converting SMS marketing messages, lead generation copy, and automation sequences. Uses the AIDA framework (Attention → Interest → Desire → Action) to structure persuasive messaging that drives engagement and conversions.

## Auto-Activation Conditions
This skill activates when:
- ✅ User asks to write SMS or text marketing messages
- ✅ Request involves lead generation or nurturing copy
- ✅ Task mentions drip campaigns or automation sequences
- ✅ User needs ad copy, CTAs, or promotional text
- ✅ Keywords: sms, lead gen, marketing, automation, drip, nurture, cta

Does NOT activate when:
- ❌ Long-form content (blog posts, articles) → use documentation skill
- ❌ Technical documentation → use docs skill
- ❌ Code generation → use code skills
- ❌ Video scripts needing visual directions → different skill needed

## Instructions

### Phase 1: Gather Context
Before writing, extract these from the request:
```python
context = {
    "product_service": "<what are we selling?>",
    "target_audience": "<who are we talking to?>",
    "pain_point": "<what problem do they have?>",
    "desired_outcome": "<what do they want?>",
    "cta_goal": "<what action should they take?>",
    "tone": "<professional|casual|urgent|friendly>",
    "character_limit": 160  # SMS default, adjust if needed
}
```

If any context is missing, ask the user before proceeding.

### Phase 2: Apply AIDA Framework

#### A - Attention (Hook)
Grab attention in the first 5-10 words:
- Use personalization: "Hey {name},"
- Ask a question: "Tired of X?"
- State a bold claim: "Get X in just Y days"
- Create urgency: "Last chance:"

#### I - Interest (Problem/Benefit)
Connect to their pain point or desire:
- Acknowledge the problem they face
- Hint at the solution
- Use "you" language

#### D - Desire (Value Proposition)
Make them want what you're offering:
- Specific benefits, not features
- Social proof if available
- Overcome objections

#### A - Action (CTA)
Clear, single action to take:
- Reply YES
- Click link
- Call now
- Use code X

### Phase 3: Write the Copy

#### SMS Format (160 chars)
```
[HOOK] + [VALUE] + [CTA]

Example:
"Hey {name}! Your free consultation expires tonight. Get personalized advice worth $200 - Reply YES to claim before midnight"
```

#### Lead Gen Sequence (Multi-touch)
```
Day 1: Introduction + value hook
Day 3: Pain point agitation
Day 5: Solution presentation
Day 7: Urgency + final CTA
```

### Phase 4: Optimize & Variations
Always provide:
1. Primary version (recommended)
2. A/B test variation
3. Shorter alternative (if applicable)

## AIDA Templates

### Template 1: Problem-Solution SMS
```
[Pain point question]? [Solution teaser]. [Specific benefit]. [CTA + urgency]

Example:
"Struggling to get leads? Our clients avg 47 new leads/week. See how → [link] (offer ends Friday)"
```

### Template 2: Social Proof SMS
```
[Result achieved] for [similar customer]. [Implied benefit for reader]. [CTA]

Example:
"Sarah doubled her revenue in 60 days. Want the same playbook? Reply GROW for free access"
```

### Template 3: Urgency SMS
```
[Time-sensitive hook]: [Offer]. [Scarcity]. [CTA]

Example:
"FINAL HOURS: 50% off ends at midnight. Only 3 spots left. Grab yours → [link]"
```

### Template 4: Nurture Sequence Message
```
Day 1: "Welcome to [brand]! Here's your free [resource]: [link]. Reply with questions!"

Day 3: "Quick tip: [valuable insight related to their pain point]. More strategies in our guide → [link]"

Day 5: "Most [audience] struggle with [pain point]. Here's how our clients solve it: [brief solution]. Want details? Reply INFO"

Day 7: "Last chance: [offer] expires tomorrow. [Benefit recap]. Claim now → [link]"
```

## Examples

### Example 1: Real Estate Lead Gen
**Input**: "Write SMS for real estate leads who downloaded a home buying guide"

**AIDA Analysis**:
- A: Personalized follow-up
- I: Home buying is stressful
- D: Expert guidance, local knowledge
- A: Schedule call

**Output**:
```
Primary:
"Hi {name}! Thanks for downloading our home buying guide. Questions about the market? I specialize in [area] - reply CALL for a free 15-min chat"

Variation:
"{name}, ready to find your dream home? I've helped 50+ families this year. Reply YES and let's talk about what you're looking for"
```

### Example 2: SaaS Trial Expiring
**Input**: "SMS for users whose free trial ends in 24 hours"

**AIDA Analysis**:
- A: Urgency (24 hours)
- I: They've invested time learning the tool
- D: Don't lose progress/data
- A: Upgrade now

**Output**:
```
Primary:
"Your free trial ends tomorrow! Keep all your [data/work] - upgrade now and get 20% off your first month: [link]"

Variation:
"24 hours left on your trial. Questions before you decide? Reply HELP or upgrade here: [link]"
```

### Example 3: Appointment Reminder + Upsell
**Input**: "Reminder for dental appointment with teeth whitening upsell"

**Output**:
```
Primary:
"Reminder: Your cleaning is tomorrow at 2pm. Want a brighter smile? Add whitening for just $99 (reg $199). Reply YES to add!"

Variation:
"See you tomorrow at 2pm! Quick Q: interested in our $99 whitening special? Reply BRIGHT to add it to your visit"
```

## Quality Checklist
Before delivering copy, verify:
- [ ] Under character limit (160 for SMS, or specified limit)
- [ ] AIDA framework applied
- [ ] Clear single CTA
- [ ] Personalization tokens noted: {name}, {date}, etc.
- [ ] Urgency/scarcity if appropriate
- [ ] A/B variation provided
- [ ] No spam trigger words (FREE!!!, Act Now!!!, etc.)
- [ ] Compliant with SMS marketing guidelines

## Anti-Patterns
- ❌ ALL CAPS MESSAGES (looks like spam)
- ❌ Multiple CTAs in one message
- ❌ Vague CTAs like "Learn more"
- ❌ No personalization
- ❌ Features instead of benefits
- ❌ Messages over 160 chars without warning
- ❌ Missing urgency in time-sensitive offers

## SMS Compliance Notes
- Always include opt-out option in sequences
- Identify sender/brand
- Don't send outside business hours
- Respect frequency limits

## Integration
- **Works with**: data-analysis (for A/B test results), documentation (for longer content)
- **Browser**: Not required

## Changelog
- v1.0.0 (2025-01-25): Initial creation - SMS, lead gen, AIDA framework
