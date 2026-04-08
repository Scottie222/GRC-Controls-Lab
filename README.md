# GRC Controls Implementation Lab

**Bakithi Scott Ngcampalala** Cybersecurity & GRC Professional  
[github.com/Scottie222](https://github.com/Scottie222) · [LinkedIn](https://www.linkedin.com/in/bakithi-scott-ngcampalala-0051a4105)

---

## What this project is

A simulated GRC controls implementation lab grounded in the **real Capital One data breach of 2019**, in which a misconfigured AWS IAM role and SSRF vulnerability allowed a former AWS employee to exfiltrate over 100 million customer records from an S3 bucket.

The lab implements practical controls across ISO 27001:2022 Annex A, NIST CSF 2.0, POPIA and GDPR moving beyond compliance documentation into working Python scripts that simulate access monitoring, vendor risk scoring, incident detection, and response playbook execution. Every script produces real output files.

---

## The real incident

On **19 July 2019**, Capital One disclosed that a former AWS engineer had exploited a misconfigured Web Application Firewall to perform Server-Side Request Forgery (SSRF), allowing her to query the EC2 instance metadata service and obtain temporary IAM credentials. Those credentials were used to list and download 106 million customer records from S3 buckets making it one of the largest financial data breaches in US history.

The root cause was a combination of overly permissive IAM roles, lack of S3 bucket access controls, and insufficient monitoring of credential usage and metadata service access.

### What failed

| Control | Failure |
|---|---|
| IAM least privilege | EC2 role had excessive S3 permissions |
| SSRF protection | WAF did not block metadata service requests |
| Access monitoring | Unusual IAM credential usage went undetected |
| S3 bucket controls | No resource-based policies to restrict access |
| Encryption | Data accessible without additional decryption layer |

---

## What the lab produces

Running the scripts generates the following outputs in the `outputs/` folder:

| Output file | Script | Description |
|---|---|---|
| `vendor-risk-report.csv` | vendor-risk.py | 5 vendors scored across 7 domains — ISO 27001 A.5.19 aligned |
| `vendor-risk-report.json` | vendor-risk.py | Full JSON with scores, ratings and remediation actions |
| `vendor-risk-report.txt` | vendor-risk.py | Human-readable vendor risk report with domain breakdowns |
| `incident-simulation-log.csv` | incident-sim.py | 20 simulated security events with detection results |
| `incident-simulation-log.json` | incident-sim.py | Full incident log with severity, response actions, ISO/NIST mapping |
| `incident-simulation-report.txt` | incident-sim.py | Summary report of all detected incidents |
| `incident-response-demo.csv` | incident_response.py | Demo of the detection and classification engine |
| `incident-response-demo.json` | incident_response.py | Full response playbook output per event |
| `access-logs-simulated.csv` | monitoring-dashboard.py | 120 simulated access log entries across 7 days |
| `chart-event-distribution.png` | monitoring-dashboard.py | Security event distribution bar chart |
| `chart-vendor-risk.png` | monitoring-dashboard.py | Vendor risk scores with threshold lines |
| `chart-control-status.png` | monitoring-dashboard.py | GRC control implementation status across ISO/NIST/POPIA |
| `chart-events-over-time.png` | monitoring-dashboard.py | Security events over time line chart |

---

## Framework alignment

| Framework | Coverage |
|---|---|
| ISO 27001:2022 | A.5.19 Vendor risk, A.5.24–A.5.28 Incident management, A.8.15 Logging, A.9 Access control |
| NIST CSF 2.0 | Identify, Protect, Detect, Respond, Recover |
| POPIA Act 4 of 2013 | Section 19 safeguards, Section 21 operator obligations, Section 22 breach notification |
| GDPR | Article 32 security of processing, Article 33 breach notification |

---

## Project structure

```
GRC-Controls-Lab/
├── Scripts/
│   ├── vendor-risk.py          # Vendor risk scoring engine
│   ├── incident-sim.py         # Incident simulation — 20 events
│   ├── incident_response.py    # Detection, classification, response playbooks
│   ├── monitoring-dashboard.py # PNG chart generation
│   └── terraform-iam.tf        # Simulated IAM control deployment
├── ISO27001/
│   ├── Access-Management.md
│   ├── Incident-Response.md
│   └── Vendor-Risk.md
├── NIST-CSF/
│   ├── Identify.md
│   ├── Protect.md
│   ├── Detect.md
│   ├── Respond.md
│   └── Recover.md
├── Demo-Data/
│   ├── access-logs.csv
│   ├── incident-logs.json
│   ├── vendor-report.txt
│   └── recovery-actions.json
├── run_all.py                  # Run everything in one command
├── Implementation-Plan.md
├── FINDINGS.md
├── requirements.txt
└── outputs/                    # All generated outputs (gitignored)
```

---

## How to run

### Step 1 Clone the repo

```bash
git clone https://github.com/Scottie222/GRC-Controls-Lab.git
cd GRC-Controls-Lab
```

### Step 2 Install dependencies

```bash
pip install -r requirements.txt
```

### Step 3 Run everything at once

```bash
python run_all.py
```

Or run individual scripts:

```bash
python Scripts/vendor-risk.py
python Scripts/incident_response.py
python Scripts/incident-sim.py
python Scripts/monitoring-dashboard.py
```

All outputs are saved to the `outputs/` folder.

---

## Requirements

```
pandas
numpy
matplotlib
faker
rich
python-dotenv
requests
```

Install with:

```bash
pip install -r requirements.txt
```

---

## References

1. Capital One breach disclosure https://www.capitalone.com/digital/facts2019/
2. ISO/IEC 27001:2022 https://www.iso.org/standard/82875.html
3. NIST CSF 2.0 https://www.nist.gov/cyberframework
4. POPIA Act 4 of 2013 https://www.justice.gov.za/inforeg/docs/InfoRegSA-POPIA-act4of2013.pdf

---

## Related GRC portfolio projects

All projects grounded in real breach incidents [github.com/Scottie222](https://github.com/Scottie222):

| Project | Domain | Real incident |
|---|---|---|
| [StandardBank-Risk-Assessment](https://github.com/Scottie222/StandardBank-Risk-Assessment) | Risk Assessment | Experian SA 2020 — 24M records. [Live demo](https://scottie222.github.io/StandardBank-Risk-Assessment/) |
| [CloudSec-Assessment-SA](https://github.com/Scottie222/CloudSec-Assessment-SA) | Cloud Security | Dis-Chem 2022, Experian SA 2020 |
| [RetailCo-Security-Awareness](https://github.com/Scottie222/RetailCo-Security-Awareness) | Security Awareness | R200M SA phishing losses 2023 |
| [VendorRisk-SA](https://github.com/Scottie222/VendorRisk-SA) | Third-Party Risk | Experian, Dis-Chem, MTN, TransUnion |
| [LifeHealthcare-BCP](https://github.com/Scottie222/LifeHealthcare-BCP) | BCP/DR | Life Healthcare ransomware 2020 |
| [MTN-ISMS-Audit](https://github.com/Scottie222/MTN-ISMS-Audit) | Internal Audit | MTN SA breach April 2025 |
| [POPIA-GDPR-Compliance-Tracker](https://github.com/Scottie222/POPIA-GDPR-Compliance-Tracker) | Data Privacy | WhatsApp 2024 enforcement |