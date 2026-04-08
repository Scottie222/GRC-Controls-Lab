"""
GRC Controls Lab — Incident Simulation
Capital One 2019 breach case study
ISO 27001 A.5.24-A.5.28 | NIST CSF Respond/Recover
Author: Bakithi Scott Ngcampalala
"""

import os
import sys
import json
import csv
import random
from datetime import datetime, timedelta

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPTS_DIR)

OUTPUT_DIR = os.path.join(SCRIPTS_DIR, "..", "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

INCIDENT_KEYWORDS = ["unauthorized", "breach", "attack", "malware", "intrusion", "escalation"]
SEVERITY_MAP = {"breach": "Critical", "malware": "Critical", "unauthorized": "High",
                "intrusion": "High", "escalation": "High", "attack": "Medium"}
RESPONSE_PLAYBOOKS = {
    "Critical": [
        "Immediately isolate affected system from network",
        "Escalate to CISO and executive team within 15 minutes",
        "Preserve all logs and evidence — do not power off",
        "Notify Information Regulator under POPIA Section 22 if PII involved",
        "Engage incident response retainer",
        "Begin forensic investigation",
        "Notify affected data subjects if required",
    ],
    "High": [
        "Contain affected account or system within 30 minutes",
        "Escalate to Security team lead",
        "Collect and preserve relevant logs",
        "Review access control logs for lateral movement",
        "Reset compromised credentials",
        "Document timeline and actions taken",
    ],
    "Medium": [
        "Investigate event within 4 hours",
        "Review system and access logs",
        "Apply relevant patches or configuration fixes",
        "Update incident log with findings",
        "Confirm no data exfiltration occurred",
    ],
}

def detect_incident(event):
    return any(kw in event.lower() for kw in INCIDENT_KEYWORDS)

def classify_severity(event):
    for kw, sev in SEVERITY_MAP.items():
        if kw in event.lower():
            return sev
    return "Medium"

def get_response_actions(severity):
    return RESPONSE_PLAYBOOKS.get(severity, RESPONSE_PLAYBOOKS["Medium"])

SIMULATED_EVENTS = [
    "Unauthorized access attempt on IAM console",
    "Login Failed from unusual IP",
    "Privilege Escalation detected on EC2 instance",
    "Malware signature detected on endpoint",
    "Intrusion attempt on firewall rule 443",
    "Login Success from new device",
    "Breach attempt on S3 bucket ACL",
    "Normal file access by admin user",
    "Attack pattern detected in WAF logs",
    "Unauthorized API call to metadata service",
    "Login Success from known device",
    "Escalation attempt on database role",
    "Normal batch job completed",
    "Malware quarantined by endpoint protection",
    "Normal scheduled backup completed",
    "Intrusion detected on VPN gateway",
    "Unauthorized S3 bucket policy change",
    "Login Failed — account locked after 5 attempts",
    "Normal user activity — file read",
    "Breach of IMDS endpoint from EC2 role",
]

USERS = ["admin_user", "svc_account_01", "john.smith", "api_gateway",
         "backup_svc", "sarah.jones", "root_user", "monitor_agent"]
SYSTEMS = ["IAM Console", "EC2 Instance i-0abc123", "S3 Bucket prod-data",
           "RDS Database prod-db", "VPN Gateway", "WAF", "CloudTrail", "Lambda Function"]

def generate_incidents(n=20):
    incidents = []
    base_time = datetime.now() - timedelta(hours=48)
    for i in range(n):
        event = random.choice(SIMULATED_EVENTS)
        is_incident = detect_incident(event)
        severity = classify_severity(event) if is_incident else "None"
        actions = get_response_actions(severity) if is_incident else []
        ts = base_time + timedelta(minutes=random.randint(0, 2880))
        incidents.append({
            "id": f"INC-{str(i+1).zfill(3)}",
            "timestamp": ts.strftime("%Y-%m-%d %H:%M:%S"),
            "event": event,
            "user": random.choice(USERS),
            "system": random.choice(SYSTEMS),
            "incident_detected": is_incident,
            "severity": severity,
            "response_actions": actions,
            "status": "Resolved" if not is_incident else random.choice(["Open", "In Progress", "Resolved"]),
            "iso_clause": "A.5.25" if is_incident else "N/A",
            "nist_function": "Respond" if is_incident else "N/A"
        })
    incidents.sort(key=lambda x: x["timestamp"])
    return incidents

def export_csv(incidents):
    path = os.path.join(OUTPUT_DIR, "incident-simulation-log.csv")
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "id", "timestamp", "event", "user", "system",
            "incident_detected", "severity", "status", "iso_clause", "nist_function"
        ])
        writer.writeheader()
        for inc in incidents:
            writer.writerow({k: v for k, v in inc.items() if k != "response_actions"})
    print(f"  CSV saved: {path}")

def export_json(incidents):
    path = os.path.join(OUTPUT_DIR, "incident-simulation-log.json")
    with open(path, "w") as f:
        json.dump(incidents, f, indent=2)
    print(f"  JSON saved: {path}")

def export_txt(incidents):
    path = os.path.join(OUTPUT_DIR, "incident-simulation-report.txt")
    detected = [i for i in incidents if i["incident_detected"]]
    critical = [i for i in detected if i["severity"] == "Critical"]
    high = [i for i in detected if i["severity"] == "High"]
    medium = [i for i in detected if i["severity"] == "Medium"]
    with open(path, "w") as f:
        f.write("=" * 65 + "\n")
        f.write("  GRC CONTROLS LAB — INCIDENT SIMULATION REPORT\n")
        f.write(f"  Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        f.write("  Framework: ISO 27001 A.5.24-A.5.28 | NIST CSF Respond\n")
        f.write("  Reference: Capital One data breach 2019\n")
        f.write("=" * 65 + "\n\n")
        f.write("SUMMARY\n")
        f.write(f"  Total events simulated: {len(incidents)}\n")
        f.write(f"  Incidents detected:     {len(detected)}\n")
        f.write(f"  Critical:               {len(critical)}\n")
        f.write(f"  High:                   {len(high)}\n")
        f.write(f"  Medium:                 {len(medium)}\n\n")
        f.write("INCIDENT DETAIL\n")
        f.write("-" * 65 + "\n")
        for inc in detected:
            f.write(f"\n{inc['id']} | {inc['timestamp']}\n")
            f.write(f"  Event:    {inc['event']}\n")
            f.write(f"  User:     {inc['user']} | System: {inc['system']}\n")
            f.write(f"  Severity: {inc['severity']} | Status: {inc['status']}\n")
            f.write(f"  ISO:      {inc['iso_clause']} | NIST: {inc['nist_function']}\n")
            if inc["response_actions"]:
                f.write("  Actions:\n")
                for a in inc["response_actions"]:
                    f.write(f"    - {a}\n")
    print(f"  TXT saved: {path}")

def main():
    print("=" * 65)
    print("  GRC CONTROLS LAB — INCIDENT SIMULATION")
    print("  ISO 27001 A.5.24-A.5.28 | NIST CSF Respond/Recover")
    print("=" * 65)
    print("\n  Simulating 20 security events...")
    incidents = generate_incidents(20)
    detected = [i for i in incidents if i["incident_detected"]]
    print(f"\n  Events simulated:   {len(incidents)}")
    print(f"  Incidents detected: {len(detected)}")
    for inc in detected:
        print(f"\n  [{inc['severity']}] {inc['id']} — {inc['event']}")
        for a in inc["response_actions"]:
            print(f"    -> {a}")
    print("\n" + "=" * 65)
    print("  EXPORTING OUTPUTS")
    print("=" * 65)
    export_csv(incidents)
    export_json(incidents)
    export_txt(incidents)
    print("\n  Done. All outputs saved to outputs/")

if __name__ == "__main__":
    main()