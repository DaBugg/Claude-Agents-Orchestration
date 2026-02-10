# Discovery Questionnaire: AD / Azure / Hybrid Planning

Use these questions to collect decision-grade inputs before proposing architecture.

## 1) Organization & Growth
- How many employees today?
- How many contractors/vendors need access?
- Growth expectation at 6, 12, and 24 months?
- Number of office locations and countries?

## 2) Identity & Access Baseline
- Current identity provider (none, AD, Entra ID, Google, Okta, other)?
- Need single sign-on for Microsoft 365 only, or third-party SaaS too?
- Any legacy apps requiring LDAP/Kerberos/NTLM?
- MFA currently in place? Any exceptions?

## 3) Endpoint & Device Estate
- Device counts by platform: Windows, macOS, Linux, mobile?
- Corporate-owned vs BYOD split?
- Need Intune/MDM and compliance policies?

## 4) Workloads to Host
- Web hosting needed? (public website, internal portal, API)
- Database requirements? (SQL Server, MySQL, PostgreSQL, NoSQL)
- Storage use cases? (file shares, object storage, long-term archive)
- Performance expectations? (concurrent users, read/write profile, latency)

## 5) Security, Compliance, and Risk
- Compliance frameworks required (SOC 2, ISO 27001, HIPAA, GDPR, other)?
- Data classification levels (public/internal/confidential/restricted)?
- Required retention, legal hold, and audit logging periods?
- RPO/RTO targets for critical systems?

## 6) Admin Roles & Operations
- How many total IT admins?
- Need role separation for identity, security, endpoint, and workload admins?
- 24/7 support needed?
- Who owns change management and incident response?

## 7) Budget, Timeline, and Constraints
- Budget range (monthly/annual), and CapEx vs OpEx preference?
- Timeline for pilot and full migration?
- Existing Microsoft licensing commitments?
- Mandatory constraints (on-prem data residency, vendor lock-in concerns, etc.)?

## 8) Success Criteria
- What does success look like at 30/90/180 days?
- Which KPIs matter most? (uptime, login success rate, ticket reduction, cost/user)
- Must-have outcomes vs optional enhancements?
