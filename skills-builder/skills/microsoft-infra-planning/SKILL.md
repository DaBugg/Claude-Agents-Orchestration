---
name: microsoft-infra-planning
description: Discovers requirements and designs Microsoft AD or Azure infrastructure plans for office migrations, admin role models, hosting, and storage. Activates when users need a structured questionnaire and recommendation framework for identity, server, database, and governance setup.
version: 1.0.0
triggers:
  - active directory
  - azure migration
  - office infrastructure
  - microsoft server setup
  - identity and access management
  - ad or azure
  - hosting and storage planning
  - admin roles
domain: devops
complexity: complex
dependencies: []
browser: false
author: auto-generated
created: 2026-02-10
---

# Microsoft Infrastructure Planning

## Overview
Use this skill to run a discovery-first consultation for organizations moving office users to on-prem Active Directory, Azure AD (Microsoft Entra ID), or hybrid identity. It produces a scoped plan for identity, servers, databases, storage, security, roles, migration phases, and budget alignment.

## Auto-Activation Conditions
Activate when the user asks to:
- Set up AD, Azure AD/Entra ID, or a hybrid model
- Plan Microsoft server/database/storage infrastructure
- Define admin roles, permissions, or governance models
- Collect sizing inputs (headcount, offices, workloads, growth)

Do NOT activate when:
- The user only wants low-level PowerShell scripting
- The request is unrelated to Microsoft infra or identity

## Workflow

### Phase 1: Discovery Interview (Ask Before Recommending)
Start with the concise questionnaire in [references/discovery-questionnaire.md](references/discovery-questionnaire.md). Ask in batches, not all at once.

Minimum required inputs before architecture recommendation:
1. Company size and growth forecast
2. Number of offices and geography
3. Device mix and OS distribution
4. Current identity state (none, AD, Google, Okta, etc.)
5. Target workloads (file storage, web hosting, SQL apps, VMs, backups)
6. Compliance/security requirements
7. Admin team size and role split
8. Budget posture and timeline

### Phase 2: Classify Target Architecture
After discovery, classify into one of:
- **AD-first (on-prem)**: Legacy apps, local auth dependencies, limited cloud adoption
- **Azure-first (cloud-native)**: SaaS-heavy stack, remote teams, cloud governance priority
- **Hybrid identity**: Needs both legacy AD + modern cloud services

Explain why the selected model best fits constraints.

### Phase 3: Build a Recommendation Pack
Output should include:
1. **Identity design**
   - Tenant/domain strategy
   - AD DS / Entra ID / Entra Connect choices
   - MFA/Conditional Access baseline
2. **Admin role model**
   - Global admin minimization
   - Privileged role separation (identity, security, endpoint, workload)
   - Break-glass emergency access accounts
3. **Server and workload design**
   - Web hosting path (App Service, IIS on VM, AKS optional)
   - Database path (Azure SQL, SQL Server VM, managed PostgreSQL/MySQL if needed)
   - File and archive storage (Azure Files/Blob/SharePoint/OneDrive)
4. **Network and security baseline**
   - Segmentation, VPN/ExpressRoute, NSGs/firewalls
   - Logging/monitoring (Defender, Sentinel, Log Analytics)
   - Backup/DR targets with RPO/RTO mapping
5. **Migration plan**
   - Pilot group -> phased rollout -> full cutover
   - Rollback controls and acceptance checkpoints
6. **Licensing and cost guardrails**
   - Required Microsoft licensing families
   - Primary cost drivers and optimization levers

### Phase 4: Output Format
Respond in this structure:

```markdown
## 1) Discovery Summary
- Org profile:
- Constraints:
- Required outcomes:

## 2) Proposed Architecture
- Model: AD-first | Azure-first | Hybrid
- Identity stack:
- Server/database/storage stack:

## 3) Admin & Governance Model
- Core admin roles:
- Privileged access controls:
- Operational ownership:

## 4) Implementation Roadmap
- Phase 0 (prep):
- Phase 1 (pilot):
- Phase 2 (migration):
- Phase 3 (hardening/optimization):

## 5) Risks and Mitigations
- Risk:
- Mitigation:

## 6) Open Questions
- Items still needed to finalize design:
```

## Guidance Rules
- Ask clarifying questions before naming specific SKU sizes.
- Avoid over-provisioning; right-size with growth ranges (current + 12/24 months).
- Keep security controls mandatory (MFA, least privilege, logging, backups).
- Flag assumptions explicitly when data is missing.
- Distinguish "must-have now" vs "phase-2 improvements."

## Example Prompt Starters
- "How many total users, and how many are expected in 12 months?"
- "Do you need legacy app authentication against on-prem AD?"
- "Which workloads are mandatory: web hosting, internal apps, SQL, file shares, backup archive?"
- "How many people need admin access, and what level of privileges do they need?"
- "Any compliance obligations (HIPAA, SOC 2, ISO 27001, GDPR)?"

## Anti-patterns
- ❌ Recommending a full architecture without discovery inputs
- ❌ Assigning Global Admin broadly to IT staff
- ❌ Ignoring backup/DR and incident-response ownership
- ❌ Treating AD and Entra ID as interchangeable without workload mapping
