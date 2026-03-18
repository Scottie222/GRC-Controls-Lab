# GRC Controls Implementation Lab – Implementation Plan

## Incident Reference
Capital One Data Breach 2019  
https://www.cnet.com/tech/tech-industry/capital-one-breach-everything-you-need-to-know/

## Overview
This project simulates the implementation of GRC controls using ISO 27001 and NIST CSF frameworks. It demonstrates how security controls can be operationalized in a cloud environment.

## Objective
- Implement access management controls
- Simulate vendor risk workflows
- Build incident detection and response processes
- Align controls with GDPR and POPIA requirements

---

## 1. Access Management

### Why it matters
The Capital One breach exploited weak access controls and misconfigured permissions.

### Controls
- ISO 27001: A.9.1, A.9.2
- NIST CSF: PR.AC-1
- GDPR: Article 32
- POPIA: Section 19

### Implementation
- Terraform IAM roles
- Least privilege enforcement
- MFA simulation
- Access logging

### Demo
See: Demo-Data/access-logs.csv

---

## 2. Vendor Risk Management

### Why it matters
Cloud vendors introduce risk if not properly monitored.

### Controls
- ISO 27001: A.15.1, A.15.2
- NIST CSF: ID.SC-1
- GDPR: Article 28
- POPIA: Sections 19–21

### Implementation
- Vendor risk scoring script
- GitHub Actions workflow
- Risk reporting logs

### Demo
See: Demo-Data/vendor-report.txt

---

## 3. Incident Response

### Why it matters
Delayed detection increases breach impact.

### Controls
- ISO 27001: A.16.1
- NIST CSF: DE.CM-1
- GDPR: Articles 33–34
- POPIA: Sections 22–23

### Implementation
- Python incident simulation
- Monitoring dashboard
- Automated alerts

### Demo
See: Demo-Data/incident-logs.json

---

## 4. Recovery

### Why it matters
Systems must be restored and improved after incidents.

### Controls
- NIST CSF: RC.RP-1, RC.IM-1

### Implementation
- Restore IAM roles
- Update configurations
- Document lessons learned

### Demo
See: Demo-Data/recovery-actions.json

---

## Conclusion
This lab demonstrates how GRC controls move from theory to implementation using real-world scenarios.
