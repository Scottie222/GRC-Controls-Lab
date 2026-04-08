"""
GRC Controls Lab — Run All Scripts
Author: Bakithi Scott Ngcampalala
"""

import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SCRIPTS = os.path.join(ROOT, "Scripts")

print("=" * 65)
print("  GRC CONTROLS LAB — FULL RUN")
print("  Capital One 2019 | ISO 27001 | NIST CSF | POPIA")
print("=" * 65)

print("\n[1/3] Running vendor risk assessment...")
print("-" * 65)
exec(open(os.path.join(SCRIPTS, "vendor-risk.py")).read())

print("\n[2/3] Running incident simulation...")
print("-" * 65)
exec(open(os.path.join(SCRIPTS, "incident_sim.py")).read())

print("\n[3/3] Generating monitoring dashboard charts...")
print("-" * 65)
exec(open(os.path.join(SCRIPTS, "monitoring-dashboard.py")).read())

print("\n" + "=" * 65)
print("  ALL DONE — outputs saved to outputs/")
print("=" * 65)
print()
print("  outputs/vendor-risk-report.csv")
print("  outputs/vendor-risk-report.json")
print("  outputs/vendor-risk-report.txt")
print("  outputs/incident-simulation-log.csv")
print("  outputs/incident-simulation-log.json")
print("  outputs/incident-simulation-report.txt")
print("  outputs/access-logs-simulated.csv")
print("  outputs/chart-event-distribution.png")
print("  outputs/chart-vendor-risk.png")
print("  outputs/chart-control-status.png")
print("  outputs/chart-events-over-time.png")