"""
GRC Controls Lab — Vendor Risk Management
Capital One 2019 breach case study
ISO 27001 A.5.19 / POPIA Section 21 aligned
Author: Bakithi Scott Ngcampalala
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import json
import csv
from datetime import datetime

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

VENDORS = [
    {
        "name": "CloudStorage Inc",
        "type": "Cloud Infrastructure",
        "data_access": "Customer PII, Financial Records",
        "popia_operator": True,
        "scores": {
            "access_control": 3,
            "encryption": 4,
            "incident_response": 2,
            "popia_compliance": 3,
            "penetration_testing": 2,
            "business_continuity": 3,
            "contractual_controls": 2
        }
    },
    {
        "name": "DataVault LLC",
        "type": "Data Processing",
        "data_access": "Customer PII, Credit Data",
        "popia_operator": True,
        "scores": {
            "access_control": 4,
            "encryption": 5,
            "incident_response": 3,
            "popia_compliance": 4,
            "penetration_testing": 3,
            "business_continuity": 4,
            "contractual_controls": 3
        }
    },
    {
        "name": "SecureNet SA",
        "type": "Network Security",
        "data_access": "Network Logs, System Events",
        "popia_operator": False,
        "scores": {
            "access_control": 5,
            "encryption": 5,
            "incident_response": 4,
            "popia_compliance": 4,
            "penetration_testing": 5,
            "business_continuity": 4,
            "contractual_controls": 5
        }
    },
    {
        "name": "PayProcess (Pty) Ltd",
        "type": "Payment Processing",
        "data_access": "Financial Data, Card Data",
        "popia_operator": True,
        "scores": {
            "access_control": 2,
            "encryption": 3,
            "incident_response": 2,
            "popia_compliance": 2,
            "penetration_testing": 2,
            "business_continuity": 2,
            "contractual_controls": 1
        }
    },
    {
        "name": "AuditTrail Systems",
        "type": "Compliance & Audit",
        "data_access": "Audit Logs, Access Records",
        "popia_operator": False,
        "scores": {
            "access_control": 4,
            "encryption": 4,
            "incident_response": 4,
            "popia_compliance": 5,
            "penetration_testing": 3,
            "business_continuity": 4,
            "contractual_controls": 4
        }
    },
]

DOMAIN_WEIGHTS = {
    "access_control": 0.20,
    "encryption": 0.18,
    "incident_response": 0.15,
    "popia_compliance": 0.18,
    "penetration_testing": 0.12,
    "business_continuity": 0.10,
    "contractual_controls": 0.07
}

def calculate_risk(vendor):
    weighted = sum(
        vendor["scores"][d] * DOMAIN_WEIGHTS[d]
        for d in vendor["scores"]
    )
    score = round(weighted, 2)
    if score >= 4.5:
        rating = "Low"
        action = "Annual review — maintain current controls"
    elif score >= 3.5:
        rating = "Medium"
        action = "Quarterly review — implement missing controls within 90 days"
    elif score >= 2.5:
        rating = "High"
        action = "Monthly review — remediation plan required within 30 days"
    else:
        rating = "Critical"
        action = "Immediate escalation — suspend or remediate before next processing cycle"
    return score, rating, action

def export_csv(results):
    path = os.path.join(OUTPUT_DIR, "vendor-risk-report.csv")
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "Vendor", "Type", "Data Access", "POPIA Operator",
            "Risk Score", "Risk Rating", "Recommended Action", "Assessment Date"
        ])
        for r in results:
            writer.writerow([
                r["name"], r["type"], r["data_access"],
                "Yes" if r["popia_operator"] else "No",
                r["score"], r["rating"], r["action"],
                datetime.now().strftime("%Y-%m-%d")
            ])
    print(f"  CSV saved: {path}")

def export_json(results):
    path = os.path.join(OUTPUT_DIR, "vendor-risk-report.json")
    with open(path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"  JSON saved: {path}")

def export_txt(results):
    path = os.path.join(OUTPUT_DIR, "vendor-risk-report.txt")
    with open(path, "w") as f:
        f.write("=" * 65 + "\n")
        f.write("  GRC CONTROLS LAB — VENDOR RISK REPORT\n")
        f.write(f"  Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        f.write(f"  Framework: ISO 27001 A.5.19 | POPIA Section 21\n")
        f.write("=" * 65 + "\n\n")
        for r in results:
            f.write(f"Vendor:       {r['name']}\n")
            f.write(f"Type:         {r['type']}\n")
            f.write(f"Data Access:  {r['data_access']}\n")
            f.write(f"POPIA Op:     {'Yes' if r['popia_operator'] else 'No'}\n")
            f.write(f"Risk Score:   {r['score']} / 5.00\n")
            f.write(f"Risk Rating:  {r['rating']}\n")
            f.write(f"Action:       {r['action']}\n")
            f.write("\nDomain Scores:\n")
            for domain, score in r["scores"].items():
                bar = "#" * score + "-" * (5 - score)
                f.write(f"  {domain:<25} [{bar}] {score}/5\n")
            f.write("\n" + "-" * 65 + "\n\n")
        critical = [r for r in results if r["rating"] == "Critical"]
        high = [r for r in results if r["rating"] == "High"]
        f.write("SUMMARY\n")
        f.write(f"  Total vendors assessed: {len(results)}\n")
        f.write(f"  Critical: {len(critical)}\n")
        f.write(f"  High:     {len(high)}\n")
        f.write(f"  POPIA operators: {sum(1 for r in results if r['popia_operator'])}\n")
    print(f"  TXT saved: {path}")

def main():
    print("=" * 65)
    print("  GRC CONTROLS LAB — VENDOR RISK ASSESSMENT")
    print("  ISO 27001 A.5.19 | POPIA Section 21")
    print("=" * 65)
    results = []
    for v in VENDORS:
        score, rating, action = calculate_risk(v)
        result = {**v, "score": score, "rating": rating, "action": action,
                  "assessment_date": datetime.now().strftime("%Y-%m-%d")}
        results.append(result)
        print(f"\n  {v['name']}")
        print(f"    Score:  {score}/5.00  |  Rating: {rating}")
        print(f"    Action: {action}")
    print("\n" + "=" * 65)
    print("  EXPORTING OUTPUTS")
    print("=" * 65)
    export_csv(results)
    export_json(results)
    export_txt(results)
    print("\n  Done. All outputs saved to outputs/")

if __name__ == "__main__":
    main()