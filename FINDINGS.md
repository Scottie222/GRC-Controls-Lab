# Capital One 2019 Breach — Findings & Control Mapping

## What Went Wrong

In 2019, Capital One suffered a data breach exposing over 100 million customer records.
A former AWS employee exploited a misconfigured Web Application Firewall (WAF) to obtain
AWS credentials via SSRF (Server-Side Request Forgery), then accessed S3 buckets containing
sensitive personal data.

---

## Root Cause Findings

| Finding | What Failed |
|--------|-------------|
| Misconfigured WAF | Allowed SSRF requests to AWS metadata service |
| Overprivileged IAM role | Role had excessive S3 read permissions |
| No least privilege enforcement | Single role accessed 700+ S3 buckets |
| Inadequate monitoring | Exfiltration went undetected for months |
| No vendor/cloud risk controls | AWS misconfiguration not caught in reviews |

---

## Control Mapping — How This Lab Addresses Each Finding

### Finding 1 — Overprivileged IAM role
**File:** `Scripts/terraform-iam.tf`
This Terraform configuration simulates least privilege IAM roles,
ensuring each role only has permissions it strictly needs.
Directly addresses Capital One's core failure.

### Finding 2 — No incident detection
**File:** `Scripts/incident_sim.py` + `Scripts/tests/test_incident_response.py`
The detect_incident() function identifies unauthorized access attempts
and privilege escalation events — the exact events that occurred in this breach.

### Finding 3 — No vendor/cloud risk assessment
**File:** `Scripts/vendor-risk.py` + `Demo-Data/vendor-report.txt`
Simulates a vendor risk scoring workflow that would flag high-risk
cloud configurations before they reach production.

### Finding 4 — Inadequate monitoring and logging
**File:** `Scripts/monitoring-dashboard.py` + `Demo-Data/access-logs.csv`
Access logs capture who accessed what and when.
The monitoring dashboard surfaces anomalies in real time.

### Finding 5 — No documented incident response process
**File:** `ISO27001/Incident-Response.md` + `NIST-CSF/Respond.md`
Formal incident response procedures aligned to ISO 27001 Annex A
and NIST CSF Respond function — ensuring breaches are contained quickly.

### Finding 6 — No recovery plan
**File:** `NIST-CSF/Recover.md` + `Demo-Data/recovery-actions.json`
Documents recovery steps including IAM reconfiguration and
lessons learned — aligned to NIST CSF Recover function.

---

## Compliance Gaps Addressed

| Gap | Framework | File in This Lab |
|-----|-----------|-----------------|
| Access control weakness | ISO 27001 A.9 | ISO27001/Access-Management.md |
| No incident management | ISO 27001 A.16 | ISO27001/Incident-Response.md |
| Vendor not assessed | ISO 27001 A.15 | ISO27001/Vendor-Risk.md |
| No identify function | NIST CSF — Identify | NIST-CSF/Identify.md |
| No protect function | NIST CSF — Protect | NIST-CSF/Protect.md |
| No detect function | NIST CSF — Detect | NIST-CSF/Detect.md |
| Personal data exposed | GDPR Art. 32 + POPIA | Implementation-Plan.md |

---

## Conclusion

Every control failure in the Capital One breach is directly addressed
by a file or script in this lab. This project demonstrates the ability
to translate real-world breach findings into implemented, tested,
and documented security controls.
