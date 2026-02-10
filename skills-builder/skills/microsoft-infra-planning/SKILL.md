---
name: microsoft-infra-planning
description: Runs a structured discovery and planning workflow for Microsoft Active Directory, Microsoft Entra ID (Azure AD), or hybrid migrations, including admin-role design, server/database/storage sizing, and phased implementation plans.
version: 1.1.0
triggers:
  - active directory
  - azure migration
  - entra id
  - microsoft server setup
  - identity and access management
  - hybrid identity
  - admin roles
  - office infrastructure planning
domain: devops
complexity: complex
dependencies: []
browser: false
author: auto-generated
created: 2026-02-10
---

# Microsoft Infrastructure Planning

## Overview
Use this skill when a tech leader needs to move office users and workloads to Microsoft identity/infrastructure. The skill prioritizes discovery questions first, then recommends AD-first, Azure-first, or hybrid architecture with role-based governance and implementation phases.

## Auto-Activation Conditions
Activate when requests include:
- Active Directory, Microsoft Entra ID (Azure AD), or hybrid identity planning
- Office/user migration design and admin role planning
- Microsoft server, database, hosting, storage, backup, or security architecture

Do NOT activate when:
- User only wants one-off scripting with no architecture discovery
- Request is unrelated to Microsoft identity or infrastructure planning

## Workflow

### Phase 1: Discovery Intake (Required)
Use [references/discovery-questionnaire.md](references/discovery-questionnaire.md). Ask questions in **batches**:
1. Organization and identity baseline
2. Workloads and sizing/performance
3. Security/compliance and operations
4. Budget/timeline and success criteria

Do not recommend architecture until required inputs are gathered or explicitly marked as assumptions.

### Phase 2: Determine the Target Model
Choose one and justify:
- **AD-first (on-prem centric)**: heavy legacy dependencies, local auth required
- **Azure-first (cloud-first)**: remote/hybrid workforce, SaaS-first operations
- **Hybrid identity**: both legacy AD-dependent systems and cloud services are required

### Phase 3: Build the Recommendation
Always include all sections:
1. **Identity architecture**
   - Directory model, tenant/domain strategy
   - AD DS, Entra ID, and Entra Connect decision
   - MFA/Conditional Access baseline and join model (Entra join/hybrid join)
2. **Admin role design**
   - Number of admins and role separation (identity, endpoint, security, platform)
   - Privileged Identity Management (PIM) usage
   - Break-glass accounts and emergency access policy
3. **Server/database/storage strategy**
   - Web hosting: App Service vs VM/IIS vs containers
   - Database: Azure SQL vs SQL VM vs PostgreSQL/MySQL managed
   - Storage: Azure Files/Blob/SharePoint/OneDrive by use case
4. **Security and resilience baseline**
   - Network segmentation and secure connectivity
   - Logging/monitoring stack and alert ownership
   - Backup/DR strategy aligned to RPO/RTO
5. **Migration roadmap**
   - Pilot -> phased migration -> cutover -> post-cutover hardening
   - Rollback criteria and change-control gates
6. **Cost and licensing guardrails**
   - Licensing family assumptions (M365, Entra, Intune, Defender, Azure consumption)
   - Major cost drivers and optimization actions

### Phase 4: Output Contract
Return recommendations in this exact structure:

```markdown
## 1) Discovery Summary
- Organization profile:
- Current-state risks:
- Constraints and assumptions:

## 2) Recommended Target Architecture
- Model selected: AD-first | Azure-first | Hybrid
- Why this model:
- Identity stack:
- Hosting/database/storage stack:

## 3) Admin Roles and Governance
- Proposed admin roles (count + responsibilities):
- Privileged-access controls:
- Operating model (who owns what):

## 4) Sizing and Capacity Plan
- User/device scale assumptions:
- Workload sizing assumptions:
- 12/24-month growth plan:

## 5) Implementation Roadmap
- Phase 0 (assessment/prep):
- Phase 1 (pilot):
- Phase 2 (migration):
- Phase 3 (hardening/optimization):

## 6) Risk Register
- Risk:
- Impact:
- Mitigation:

## 7) Open Questions
- Data still needed to finalize:
```

## Guidance Rules
- Ask for user counts, device counts, workload profile, and growth before SKU sizing.
- Use least-privilege and zero-trust defaults (MFA, Conditional Access, role separation, logging).
- Keep recommendations practical for current team size and maturity.
- Separate **must-have now** from **phase-2 enhancements**.
- If data is missing, state assumptions explicitly and confidence level (high/medium/low).

## First Questions to Ask
1. How many employees/contractors need access now, and in 12/24 months?
2. How many offices and countries must be supported?
3. Do you have legacy apps that require AD/Kerberos/LDAP?
4. Which workloads are mandatory (web, SQL, file shares, backup/archive, internal apps)?
5. How many admins do you have, and how should roles be separated?
6. Any compliance requirements (SOC 2, HIPAA, ISO 27001, GDPR, etc.)?
7. What is your budget range and target timeline?

## Anti-patterns
- ❌ Jumping to products/SKUs without collecting discovery inputs
- ❌ Assigning Global Administrator to broad IT groups
- ❌ Ignoring backup/DR ownership, RPO/RTO, and incident processes
- ❌ Treating Entra ID and on-prem AD as interchangeable without workload mapping
