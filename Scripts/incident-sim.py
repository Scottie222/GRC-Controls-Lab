import json
from datetime import datetime

incident_logs = [
    {"timestamp": str(datetime.now()), "user": "analyst1", "event": "unauthorized login attempt", "severity": "high"},
    {"timestamp": str(datetime.now()), "user": "analyst2", "event": "suspicious file download", "severity": "medium"}
]

with open("../Demo-Data/incident-logs.json", "w") as f:
    json.dump(incident_logs, f, indent=4)
