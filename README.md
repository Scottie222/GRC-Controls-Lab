# GRC Controls Implementation Lab

## Overview
This project demonstrates practical implementation of GRC controls using ISO 27001 and NIST CSF.

It is based on the Capital One 2019 breach and shows how real-world security failures can be prevented through proper controls.

---

## Objectives
- Implement access management controls
- Simulate vendor risk management
- Build incident detection and response
- Align with GDPR and POPIA

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

---

## Key Features

### Access Management
- IAM roles with Terraform
- Least privilege access
- MFA simulation

### Vendor Risk
- Risk scoring scripts
- Vendor audit logs

### Incident Response
- Simulated incident logs
- Monitoring dashboards
- Automated alerts

### Recovery
- IAM restoration
- Security improvements

---

## Compliance
- ISO 27001
- NIST CSF
- GDPR
- POPIA

---

## Why This Project Matters
This project shows the ability to move beyond audits and actually implement controls.

It demonstrates practical GRC skills required for real-world roles.

---

## How to Use

Run scripts:

python Scripts/incident-sim.py  
python Scripts/vendor-risk.py  

(Optional)
terraform init  
terraform apply  

---

## Incident Reference
Capital One Data Breach 2019  
https://www.cnet.com/tech/tech-industry/capital-one-breach-everything-you-need-to-know/
