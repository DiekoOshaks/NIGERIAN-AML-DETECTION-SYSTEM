import pandas as pd

df = pd.read_csv("transactions.csv")

df["flag"] = "NORMAL"

# Rule 1: Large transaction
df.loc[df["amount"] > 500000, "flag"] = "HIGH_VALUE"

# Rule 2: Very large transaction
df.loc[df["amount"] > 1000000, "flag"] = "VERY_HIGH"

# Rule 3: Same sender many times (smurfing)
transaction_counts = df["sender"].value_counts()

suspicious_users = transaction_counts[transaction_counts > 100].index

df.loc[df["sender"].isin(suspicious_users), "flag"] = "SMURFING"

df.to_csv("flagged_transactions.csv", index=False)

print("Rule-based detection complete!")