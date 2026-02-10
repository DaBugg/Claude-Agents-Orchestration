# Discovery Questionnaire: Microsoft AD / Entra ID / Hybrid

Use this questionnaire to gather decision-grade requirements before recommending architecture.

## How to Ask (Operator Notes)
- Ask in 3-4 short batches, not all at once.
- If an answer is unknown, mark as `TBD` and continue.
- Capture both **current state** and **12/24 month target**.

---

## Batch 1 — Organization, Users, and Identity
1. How many employees need accounts today?
2. How many contractors/vendors need access?
3. What are your expected user counts at 12 and 24 months?
4. How many office locations/countries are in scope?
5. Current identity provider: AD, Entra ID, Google, Okta, none, other?
6. Are there legacy apps requiring LDAP/Kerberos/NTLM?
7. Do you need SSO for only Microsoft 365, or additional SaaS apps?

## Batch 2 — Devices and Workloads
8. Device counts by type: Windows, macOS, Linux, iOS, Android?
9. Corporate-owned vs BYOD split?
10. Need device management/compliance (Intune/MDM)?
11. What workloads must be hosted?
    - public website
    - internal apps/APIs
    - SQL workloads
    - file shares/collaboration
    - backup/archive
12. Database engines required (SQL Server, PostgreSQL, MySQL, other)?
13. Storage profile needed (shared files, object storage, long-term retention)?
14. Performance expectations (concurrent users, peak load windows, latency targets)?

## Batch 3 — Security, Compliance, and Operations
15. Required compliance frameworks (SOC 2, ISO 27001, HIPAA, GDPR, etc.)?
16. Data sensitivity categories handled (public/internal/confidential/restricted)?
17. Required logging/audit retention period?
18. Backup expectations and DR targets (RPO and RTO) for critical systems?
19. How many total admins will operate the environment?
20. How should admin responsibilities be split?
    - identity admins
    - security admins
    - endpoint/device admins
    - workload/platform admins
21. Is 24/7 support required? If yes, who owns on-call?
22. Who approves changes and who owns incident response?

## Batch 4 — Budget, Timeline, and Success
23. Budget range and preference: OpEx cloud-first vs mixed CapEx/OpEx?
24. Any existing Microsoft licensing commitments?
25. Target dates for pilot and full cutover?
26. Hard constraints (data residency, vendor restrictions, line-of-business deadlines)?
27. Top 3 success metrics (e.g., uptime, ticket reduction, secure sign-ins, cost/user)?
28. What outcomes are mandatory now vs acceptable in phase 2?

---

## Capture Template (Fill During Interview)

```markdown
## Org Snapshot
- Employees:
- Contractors:
- Offices/countries:
- 12/24-month growth:

## Identity Baseline
- Current IdP:
- Legacy auth dependencies:
- SSO scope:

## Workload Scope
- Hosting:
- Databases:
- Storage:
- Performance targets:

## Security & Compliance
- Frameworks:
- Data sensitivity:
- Audit retention:
- RPO/RTO:

## Admin & Operations
- Total admins:
- Role split:
- On-call/support model:
- Incident/change owners:

## Budget & Timeline
- Budget posture:
- Licensing baseline:
- Pilot date:
- Cutover date:
- Constraints:

## Success Criteria
- KPI 1:
- KPI 2:
- KPI 3:
- Phase-1 must-haves:
- Phase-2 enhancements:
```
