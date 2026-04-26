import random
import copy
import pandas as pd
import numpy as np
import math

# 1. DATA GENERATION
def generate_data(n=15):
    data = []
    for i in range(n):
        entry = {
            "zone": i + 1,
            "metrics": {
                "traffic": random.randint(50, 200),
                "pollution": random.randint(100, 300),
                "energy": random.randint(200, 500)
            },
            "history": [random.randint(50, 200) for _ in range(5)]
        }
        data.append(entry)
    return data

# 2. PERSONALIZATION (ODD → ROTATE)
def rotate_data(data, k=3):
    return data[k:] + data[:k]

# 3. COPY MECHANISM
def replicate_data(original):
    assigned = original
    shallow = copy.copy(original)
    deep = copy.deepcopy(original)
    return assigned, shallow, deep

# 4. CUSTOM RISK FUNCTION
def custom_risk_score(t, p, e):
    base = math.log(t + p + e)
    return base + math.sqrt(e) / 10

# 5. MUTATION
def modify_data(data):
    for zone in data:
        zone["metrics"]["traffic"] += 20
        zone["metrics"]["pollution"] += 30
        zone["metrics"]["energy"] += 10
        zone["history"].append(random.randint(100, 300))
        t = zone["metrics"]["traffic"]
        p = zone["metrics"]["pollution"]
        e = zone["metrics"]["energy"]

        zone["risk"] = custom_risk_score(t, p, e)

# 6. DATAFRAME CONVERSION
def to_dataframe(data):
    rows = []
    for d in data:
        row = {
            "zone": d["zone"],
            "traffic": d["metrics"]["traffic"],
            "pollution": d["metrics"]["pollution"],
            "energy": d["metrics"]["energy"],
            "risk": d.get("risk", 0)
        }
        rows.append(row)
    return pd.DataFrame(rows)

# 7. MANUAL CORRELATION
def manual_correlation(x, y):
    x_mean = np.mean(x)
    y_mean = np.mean(y)

    num = np.sum((x - x_mean) * (y - y_mean))
    den = math.sqrt(np.sum((x - x_mean)**2) * np.sum((y - y_mean)**2))

    return num / den

# 8. ANALYSIS
def analyze(df):
    mean = df["risk"].mean()
    var = df["risk"].var()
    std = df["risk"].std()
    anomalies = df[df["risk"] > mean + std]["zone"].tolist()
    corr = manual_correlation(df["traffic"].values, df["pollution"].values)
    return mean, var, std, anomalies, corr

# 9. PATTERN DETECTION
def detect_patterns(original_before, original_after, df, var):
    leakage = 0
    for i in range(len(original_before)):
        if original_before[i]["metrics"] != original_after[i]["metrics"]:
            leakage += 1

    high_risk = df[df["risk"] > df["risk"].mean()]["zone"].tolist()

    clusters = []
    temp = []

    for z in sorted(high_risk):
        if not temp or z == temp[-1] + 1:
            temp.append(z)
        else:
            if len(temp) > 1:
                clusters.append(temp)
            temp = [z]
    if len(temp) > 1:
        clusters.append(temp)

    stability_index = 1 / var if var != 0 else 0
    return leakage, high_risk, clusters, stability_index


# 10. FINAL DECISION
def final_decision(leakage, stability):
    if leakage > 10:
        return "Critical Failure"
    elif leakage > 5:
        return "High Corruption Risk"
    elif stability < 0.05:
        return "Moderate Risk"
    else:
        return "System Stable"

# MAIN
def main():
    original = generate_data()

    original = rotate_data(original, 3)

    original_before = copy.deepcopy(original)

    assigned, shallow, deep = replicate_data(original)

    print("===== BEFORE =====")
    print(original)

    modify_data(shallow)

    print("\n===== AFTER =====")
    print("Original:", original)
    print("Shallow:", shallow)
    print("Deep:", deep)

    df = to_dataframe(original)
    print("\n===== DATAFRAME =====")
    print(df)

    mean, var, std, anomalies, corr = analyze(df)

    leakage, high_risk, clusters, stability = detect_patterns(
        original_before, original, df, var
    )

    print("\n===== ANALYSIS =====")
    print("Anomalies:", anomalies)
    print("Correlation (manual):", corr)
    print("High Risk Zones:", high_risk)
    print("Clusters:", clusters)

    print("\n===== FINAL OUTPUT =====")
    print((df["risk"].max(), df["risk"].min(), stability))

    decision = final_decision(leakage, stability)
    print("Decision:", decision)

main()