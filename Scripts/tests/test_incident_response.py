import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from Scripts.incident_response import detect_incident

def test_detect_unauthorized_access():
    assert detect_incident("Unauthorized access attempt") == True

def test_detect_privilege_escalation():
    assert detect_incident("Privilege escalation detected") == True

def test_no_incident():
    assert detect_incident("Normal system operation") == False

def test_detect_malware():
    assert detect_incident("Malware found on system") == True
