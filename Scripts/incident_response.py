"""
GRC Controls Lab — Incident Response Engine
ISO 27001 A.5.24–A.5.28 | NIST CSF Respond/Recover
Author: Bakithi Scott Ngcampalala
"""

import json
import csv
import os
from datetime import datetime

OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

INCIDENT_KEYWORDS = [
    "unauthorized", "breach", "attack", "malware",
    "intrusion", "escalation"
]

SEVERITY_MAP = {
    "breach": "Critical",
    "malware": "Critical",
    "unauthorized": "High",
    "intrusion": "High",
    "escalation": "High",
    "attack": "Medium",
}

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
    "None": []
}

def detect_incident(event: str) -> bool:
    """Returns True if the event string matches any incident keyword."""
    event_lower = event.lower()
    return any(kw in event_lower for kw in INCIDENT_KEYWORDS)

def classify_severity(event: str) -> str:
    """Returns severity level based on keywords in the event string."""
    event_lower = event.lower()
    for keyword, severity in SEVERITY_MAP.items():
        if keyword in event_lower:
            return severity
    return "Medium"

def get_response_actions(severity: str) -> list:
    """Returns the response playbook for a given severity level."""
    return RESPONSE_PLAYBOOKS.get(severity, RESPONSE_PLAYBOOKS["Medium"])

def run_demo():
    """Runs a standalone demo of the incident response engine."""
    demo_events = [
        "Unauthorized access attempt on IAM console",
        "Breach of IMDS endpoint from EC2 role",
        "Malware detected on endpoint device",
        "Normal login from known user",
        "Escalation attempt on database role",
        "Login Success from new device",
        "Attack pattern in WAF logs",
    ]

    print("=" * 65)
    print("  GRC CONTROLS LAB — INCIDENT RESPONSE ENGINE")
    print("  ISO 27001 A.5.24-A.5.28 | NIST CSF Respond")
    print("=" * 65)

    results = []
    for event in demo_events:
        is_incident = detect_incident(event)
        severity = classify_severity(event) if is_incident else "None"
        actions = get_response_actions(severity) if is_incident else []
        results.append({
            "event": event,
            "incident": is_incident,
            "severity": severity,
            "actions": actions,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "iso_clause": "A.5.25" if is_incident else "N/A",
            "nist_function": "Respond" if is_incident else "Detect"
        })
        status = f"[{severity}]" if is_incident else "[No incident]"
        print(f"\n  {status} {event}")
        for a in actions:
            print(f"    -> {a}")

    # Export results
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    csv_path = os.path.join(OUTPUT_DIR, "incident-response-demo.csv")
    with open(csv_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "event", "incident", "severity", "timestamp", "iso_clause", "nist_function"
        ])
        writer.writeheader()
        for r in results:
            writer.writerow({k: v for k, v in r.items() if k != "actions"})

    json_path = os.path.join(OUTPUT_DIR, "incident-response-demo.json")
    with open(json_path, "w") as f:
        json.dump(results, f, indent=2)

    print(f"\n{'=' * 65}")
    print("  OUTPUTS SAVED")
    print(f"  {csv_path}")
    print(f"  {json_path}")
    print("=" * 65)

if __name__ == "__main__":
    run_demo()