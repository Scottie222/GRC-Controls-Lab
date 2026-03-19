def detect_incident(event):
    """
    Detects if an event is a security incident.
    Returns True if incident detected, False otherwise.
    """
    incident_keywords = [
        "unauthorized",
        "breach",
        "attack",
        "malware",
        "intrusion",
        "escalation"
    ]
    event_lower = event.lower()
    for keyword in incident_keywords:
        if keyword in event_lower:
            return True
    return False
