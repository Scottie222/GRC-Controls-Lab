vendors = ["CloudStorage Inc", "DataVault LLC"]
risk_report = {}

for v in vendors:
    risk_report[v] = {"Risk Score": 7, "Action": "Review MFA and permissions"}

with open("../Demo-Data/vendor-report.txt", "w") as f:
    for vendor, info in risk_report.items():
        f.write(f"{vendor}: {info}\n")
