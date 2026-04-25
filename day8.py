import random
import pandas as pd
import numpy as np
import math

# STEP 1: SIMULATION FUNCTION
def simulate_data(n=18):
    data = []
    data.append({"zone": 1, "traffic": 95, "air_quality": 280, "energy": 450})  
    data.append({"zone": 2, "traffic": 0, "air_quality": 40, "energy": 120})   
    data.append({"zone": 3, "traffic": 60, "air_quality": 150, "energy": 490}) 

    for i in range(4, n+1):
        record = {
            "zone": i,
            "traffic": random.randint(0, 100),
            "air_quality": random.randint(0, 300),
            "energy": random.randint(0, 500)
        }
        data.append(record)

    return data

# STEP 2: CLASSIFICATION
def classify_zone(record):
    if record["air_quality"] > 200 or record["traffic"] > 80:
        return "High Risk"
    elif record["energy"] > 400:
        return "Energy Critical"
    elif record["traffic"] < 30 and record["air_quality"] < 100:
        return "Safe Zone"
    else:
        return "Moderate"

# STEP 3: CUSTOM RISK SCORE
def calculate_risk(record):
    risk = (record["traffic"] * 0.4 +
            record["air_quality"] * 0.4 +
            record["energy"] * 0.2)
    return math.sqrt(risk)

# STEP 4: CUSTOM SORT (NO sort_values)
def custom_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j]["traffic"] > data[j+1]["traffic"]:
                data[j], data[j+1] = data[j+1], data[j]
    return data

# STEP 5: ANALYSIS FUNCTIONS
def compute_statistics(df):
    mean_vals = df.mean(numeric_only=True)

    max_risk = df["risk_score"].max()
    min_risk = df["risk_score"].min()
    avg_risk = df["risk_score"].mean()

    return mean_vals, (max_risk, avg_risk, min_risk)


def top_3_zones(df):
    indices = np.argsort(-df["risk_score"].values)
    return df.iloc[indices[:3]]


def detect_patterns(df):
    patterns = {}
    threshold = df["risk_score"].mean()
    patterns["multi_factor"] = df[
        (df["risk_score"] > threshold) & (df["air_quality"].diff() > 0)
    ]
    if np.var(df["traffic"]) < 200:
        patterns["stability"] = "Stable Traffic"
    else:
        patterns["stability"] = "Unstable Traffic"
    clusters = []
    current_cluster = []

    for i in range(len(df)):
        if df.iloc[i]["risk_score"] > threshold:
            current_cluster.append(df.iloc[i]["zone"])
        else:
            if len(current_cluster) > 1:
                clusters.append(current_cluster)
            current_cluster = []

    patterns["clusters"] = clusters

    return patterns


def final_decision(avg_risk):
    if avg_risk < 10:
        return "City Stable"
    elif avg_risk < 15:
        return "Moderate Risk"
    elif avg_risk < 20:
        return "High Alert"
    else:
        return "Critical Emergency"

# MAIN EXECUTION
data = simulate_data()
categorized = {}
for record in data:
    category = classify_zone(record)
    categorized[record["zone"]] = category
data = custom_sort(data)
df = pd.DataFrame(data)
df["risk_score"] = df.apply(calculate_risk, axis=1)
mean_vals, risk_tuple = compute_statistics(df)
top_zones = top_3_zones(df)
patterns = detect_patterns(df)
decision = final_decision(risk_tuple[1])

# OUTPUT
print("\n--- DataFrame ---")
print(df)

print("\n--- Categorized Zones ---")
print(categorized)

print("\n--- Top 3 Risk Zones ---")
print(top_zones)

print("\n--- Risk Tuple (max, avg, min) ---")
print(risk_tuple)

print("\n--- Patterns Detected ---")
print(patterns)

print("\n--- Final Decision ---")
print(decision)
