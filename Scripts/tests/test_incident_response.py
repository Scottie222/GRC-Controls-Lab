from Scripts.incident_response import detect_incident

def test_detect_incident():
    result = detect_incident("FAILED LOGIN ATTEMPTS")
    assert result == True
