import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from faker import Faker
from rich.console import Console
from rich.table import Table
import datetime

console = Console()
fake = Faker()

# --- Generate fake access log data ---
users = [fake.name() for _ in range(10)]
events = ["Login Success", "Login Failed", "Privilege Escalation", "Unauthorized Access"]
timestamps = [datetime.datetime.now() - datetime.timedelta(minutes=i*5) for i in range(10)]

log_data = pd.DataFrame({
    "Time": timestamps,
    "User": users,
    "Event": np.random.choice(events, size=10)
})

# --- Display in terminal using rich table ---
table = Table(title="🚨 Access Monitoring Dashboard")
table.add_column("Time", style="cyan")
table.add_column("User", style="magenta")
table.add_column("Event", style="red")

for _, row in log_data.iterrows():
    table.add_row(str(row["Time"]), row["User"], row["Event"])

console.print(table)

# --- Generate fake vendor risk scores ---
vendors = [fake.company() for _ in range(5)]
risk_scores = np.random.randint(1, 100, size=5)

# --- Plot risk scores ---
plt.figure(figsize=(8,5))
plt.bar(vendors, risk_scores, color='orange')
plt.title("📊 Vendor Risk Scores")
plt.ylabel("Risk Score")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("vendor-risk-dashboard.png")
plt.close()

console.print("\n[bold yellow]Vendor Risk Dashboard saved as 'vendor-risk-dashboard.png'[/bold yellow]")

# --- Generate incident summary ---
incident_counts = log_data["Event"].value_counts()
plt.figure(figsize=(6,4))
incident_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title("Incident Distribution")
plt.savefig("incident-summary-dashboard.png")
plt.close()

console.print("[bold yellow]Incident Summary Dashboard saved as 'incident-summary-dashboard.png'[/bold yellow]")
