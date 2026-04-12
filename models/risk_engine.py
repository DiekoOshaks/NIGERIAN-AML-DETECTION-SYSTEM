import pandas as pd

rules_df = pd.read_csv("flagged_transactions.csv")
ml_df = pd.read_csv("ml_flagged.csv")

# Merge datasets
df = rules_df.copy()
df["ml_flag"] = ml_df["ml_flag"]

# Assign risk scores
def calculate_risk(row):
    score = 0

    # Rule-based scoring
    if row["flag"] == "HIGH_VALUE":
        score += 2
    elif row["flag"] == "VERY_HIGH":
        score += 3
    elif row["flag"] == "SMURFING":
        score += 3

    # ML anomaly
    if row["ml_flag"] == "ANOMALY":
        score += 4

    return score

df["risk_score"] = df.apply(calculate_risk, axis=1)

# Final decision
df["final_flag"] = df["risk_score"].apply(
    lambda x: "SUSPICIOUS" if x >= 4 else "NORMAL"
)

df.to_csv("final_output.csv", index=False)

print("Risk scoring complete!")