"""
GRC Controls Lab — Monitoring Dashboard
Generates PNG charts from simulated access and incident log data
ISO 27001 A.8.15 / NIST CSF Detect
Author: Bakithi Scott Ngcampalala
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import json
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from datetime import datetime, timedelta
import random

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

random.seed(42)
np.random.seed(42)

USERS = ["admin_user", "svc_account_01", "john.smith", "api_gateway",
         "backup_svc", "sarah.jones", "root_user", "monitor_agent"]
EVENTS = ["Login Success", "Login Failed", "Privilege Escalation",
          "Unauthorized Access", "File Read", "File Write", "Policy Change"]
SYSTEMS = ["IAM Console", "EC2 Instance", "S3 Bucket",
           "RDS Database", "VPN Gateway", "WAF", "CloudTrail"]

def generate_access_logs(n=120):
    base = datetime.now() - timedelta(days=7)
    rows = []
    for _ in range(n):
        ts = base + timedelta(minutes=random.randint(0, 10080))
        rows.append({
            "timestamp": ts.strftime("%Y-%m-%d %H:%M:%S"),
            "user": random.choice(USERS),
            "event": random.choices(EVENTS, weights=[40, 20, 5, 5, 15, 10, 5])[0],
            "system": random.choice(SYSTEMS),
            "ip": f"192.168.{random.randint(1,10)}.{random.randint(1,254)}"
        })
    return pd.DataFrame(rows)

def generate_vendor_scores():
    return pd.DataFrame([
        {"vendor": "CloudStorage Inc",   "score": 3.18, "rating": "High"},
        {"vendor": "DataVault LLC",      "score": 3.86, "rating": "Medium"},
        {"vendor": "SecureNet SA",       "score": 4.65, "rating": "Low"},
        {"vendor": "PayProcess (Pty)",   "score": 2.05, "rating": "Critical"},
        {"vendor": "AuditTrail Systems", "score": 4.02, "rating": "Low"},
    ])

def generate_control_status():
    return pd.DataFrame([
        {"control": "Access Management",    "framework": "ISO 27001", "status": "Implemented",     "score": 85},
        {"control": "Encryption at Rest",   "framework": "ISO 27001", "status": "Implemented",     "score": 90},
        {"control": "Incident Response",    "framework": "ISO 27001", "status": "Partial",         "score": 60},
        {"control": "Vendor Risk Mgmt",     "framework": "ISO 27001", "status": "Partial",         "score": 55},
        {"control": "Security Awareness",   "framework": "ISO 27001", "status": "Not Implemented", "score": 30},
        {"control": "Identify",             "framework": "NIST CSF",  "status": "Implemented",     "score": 80},
        {"control": "Protect",              "framework": "NIST CSF",  "status": "Implemented",     "score": 75},
        {"control": "Detect",               "framework": "NIST CSF",  "status": "Partial",         "score": 65},
        {"control": "Respond",              "framework": "NIST CSF",  "status": "Partial",         "score": 55},
        {"control": "Recover",              "framework": "NIST CSF",  "status": "Not Implemented", "score": 35},
        {"control": "Data Minimisation",    "framework": "POPIA",     "status": "Partial",         "score": 60},
        {"control": "Operator Agreements",  "framework": "POPIA",     "status": "Not Implemented", "score": 25},
        {"control": "Breach Notification",  "framework": "POPIA",     "status": "Implemented",     "score": 80},
    ])

def chart_event_distribution(df):
    counts = df["event"].value_counts()
    colors = []
    for e in counts.index:
        if e in ["Unauthorized Access", "Privilege Escalation"]:
            colors.append("#E24B4A")
        elif e in ["Login Failed", "Policy Change"]:
            colors.append("#EF9F27")
        else:
            colors.append("#378ADD")
    fig, ax = plt.subplots(figsize=(9, 5))
    bars = ax.barh(counts.index, counts.values, color=colors, edgecolor="white", height=0.6)
    ax.set_xlabel("Event Count", fontsize=11)
    ax.set_title("Security Event Distribution — Last 7 Days", fontsize=13, fontweight="bold", pad=15)
    ax.bar_label(bars, padding=4, fontsize=10)
    ax.set_facecolor("#f8f7f2")
    fig.patch.set_facecolor("#ffffff")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    legend = [
        mpatches.Patch(color="#E24B4A", label="Critical events"),
        mpatches.Patch(color="#EF9F27", label="Warning events"),
        mpatches.Patch(color="#378ADD", label="Normal events"),
    ]
    ax.legend(handles=legend, fontsize=9, loc="lower right")
    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, "chart-event-distribution.png")
    plt.savefig(path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"  Saved: {path}")

def chart_vendor_risk(df):
    color_map = {"Critical": "#E24B4A", "High": "#EF9F27", "Medium": "#378ADD", "Low": "#639922"}
    colors = [color_map[r] for r in df["rating"]]
    fig, ax = plt.subplots(figsize=(9, 5))
    bars = ax.barh(df["vendor"], df["score"], color=colors, edgecolor="white", height=0.6)
    ax.axvline(x=2.5, color="#E24B4A", linestyle="--", linewidth=1, alpha=0.6, label="Critical threshold")
    ax.axvline(x=3.5, color="#EF9F27", linestyle="--", linewidth=1, alpha=0.6, label="High threshold")
    ax.axvline(x=4.5, color="#639922", linestyle="--", linewidth=1, alpha=0.6, label="Low threshold")
    ax.set_xlim(0, 5.5)
    ax.set_xlabel("Risk Score (1-5)", fontsize=11)
    ax.set_title("Vendor Risk Scores — ISO 27001 A.5.19 | POPIA S.21", fontsize=13, fontweight="bold", pad=15)
    ax.bar_label(bars, fmt="%.2f", padding=4, fontsize=10)
    ax.set_facecolor("#f8f7f2")
    fig.patch.set_facecolor("#ffffff")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.legend(fontsize=9)
    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, "chart-vendor-risk.png")
    plt.savefig(path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"  Saved: {path}")

def chart_control_status(df):
    status_colors = {"Implemented": "#639922", "Partial": "#EF9F27", "Not Implemented": "#E24B4A"}
    colors = [status_colors[s] for s in df["status"]]
    labels = [f"{r['control']}\n({r['framework']})" for _, r in df.iterrows()]
    fig, ax = plt.subplots(figsize=(10, 7))
    bars = ax.barh(labels, df["score"], color=colors, edgecolor="white", height=0.6)
    ax.set_xlim(0, 120)
    ax.set_xlabel("Implementation Score (%)", fontsize=11)
    ax.set_title("GRC Control Implementation Status", fontsize=13, fontweight="bold", pad=15)
    ax.bar_label(bars, fmt="%d%%", padding=4, fontsize=9)
    ax.set_facecolor("#f8f7f2")
    fig.patch.set_facecolor("#ffffff")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    legend = [mpatches.Patch(color=v, label=k) for k, v in status_colors.items()]
    ax.legend(handles=legend, fontsize=9, loc="lower right")
    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, "chart-control-status.png")
    plt.savefig(path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"  Saved: {path}")

def chart_events_over_time(df):
    df["date"] = pd.to_datetime(df["timestamp"]).dt.date
    daily = df.groupby(["date", "event"]).size().unstack(fill_value=0)
    fig, ax = plt.subplots(figsize=(11, 5))
    critical_cols = [c for c in daily.columns if c in ["Unauthorized Access", "Privilege Escalation"]]
    normal_cols = [c for c in daily.columns if c not in critical_cols]
    for col in normal_cols:
        ax.plot(daily.index, daily[col], marker="o", linewidth=1.5, markersize=4, alpha=0.7, label=col)
    for col in critical_cols:
        ax.plot(daily.index, daily[col], marker="o", linewidth=2, markersize=6,
                color="#E24B4A", linestyle="--", label=f"{col} (!)")
    ax.set_xlabel("Date", fontsize=11)
    ax.set_ylabel("Event Count", fontsize=11)
    ax.set_title("Security Events Over Time — Last 7 Days", fontsize=13, fontweight="bold", pad=15)
    ax.set_facecolor("#f8f7f2")
    fig.patch.set_facecolor("#ffffff")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.legend(fontsize=8, loc="upper left", ncol=2)
    plt.xticks(rotation=30)
    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, "chart-events-over-time.png")
    plt.savefig(path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"  Saved: {path}")

def main():
    print("=" * 65)
    print("  GRC CONTROLS LAB — MONITORING DASHBOARD")
    print("  ISO 27001 A.8.15 | NIST CSF Detect")
    print("=" * 65)
    print("\n  Generating simulated data...")
    access_df = generate_access_logs(120)
    vendor_df = generate_vendor_scores()
    control_df = generate_control_status()
    access_csv = os.path.join(OUTPUT_DIR, "access-logs-simulated.csv")
    access_df.to_csv(access_csv, index=False)
    print(f"  Access log CSV saved: {access_csv}")
    print("\n  Generating charts...")
    chart_event_distribution(access_df)
    chart_vendor_risk(vendor_df)
    chart_control_status(control_df)
    chart_events_over_time(access_df)
    print(f"\n{'=' * 65}")
    print("  ALL CHARTS SAVED TO outputs/")
    print("=" * 65)

if __name__ == "__main__":
    main()