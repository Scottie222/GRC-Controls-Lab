# GRC Controls Implementation Lab

## Overview
This project demonstrates the practical implementation of Governance, Risk, and Compliance (GRC) controls using ISO 27001 and NIST Cybersecurity Framework (CSF).

It is based on the Capital One 2019 data breach and illustrates how real-world security failures can be prevented through properly designed and implemented controls.

---

## Objectives
- Implement access management controls
- Simulate vendor risk management workflows
- Build incident detection and response processes
- Align controls with GDPR and POPIA requirements

---

## Project Structure

GRC-Controls-Lab/

ISO27001/
- Access-Management.md
- Vendor-Risk.md
- Incident-Response.md

NIST-CSF/
- Identify.md
- Protect.md
- Detect.md
- Respond.md
- Recover.md

Scripts/
- terraform-iam.tf
- incident-sim.py
- vendor-risk.py

Demo-Data/
- access-logs.csv
- incident-logs.json
- vendor-report.txt
- recovery-actions.json

Implementation-Plan.md

---

## Key Features

### Access Management
- IAM roles simulated using Terraform
- Least privilege access enforcement
- Multi-factor authentication (MFA) simulation
- Access logging for monitoring

### Vendor Risk Management
- Vendor risk scoring simulation
- Basic workflow for vendor assessment
- Risk reporting outputs

### Incident Response & Monitoring
- Simulated incident detection logs
- Monitoring and alerting concepts
- Incident response workflow demonstration

### Recovery
- Simulated recovery actions
- IAM reconfiguration
- Lessons learned documentation

---

## Compliance Alignment

This project aligns with:

- ISO 27001 (Annex A Controls)
- NIST Cybersecurity Framework (CSF)
- GDPR (General Data Protection Regulation)
- POPIA (Protection of Personal Information Act)

---

## Why This Project Matters
This project demonstrates the ability to move beyond compliance assessments and implement practical security controls.

It reflects real-world GRC responsibilities, including control design, implementation, and monitoring aligned with industry frameworks.

---

## How to Use

### Run Simulations
Execute the scripts to simulate security operations:

python Scripts/incident-sim.py  
python Scripts/vendor-risk.py  

### (Optional) Infrastructure Simulation
To simulate IAM control deployment:

terraform init  
terraform apply  

---

## Incident Reference
Capital One Data Breach 2019  
https://www.capitalone.com/digital/facts2019/

---

## Conclusion
This project showcases the transition from theoretical GRC knowledge to practical implementation, demonstrating readiness for real-world GRC roles.
