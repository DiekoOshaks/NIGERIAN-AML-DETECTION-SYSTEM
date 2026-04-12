import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder

# Load data
df = pd.read_csv("transactions.csv")

# --- Feature Engineering ---

# Convert timestamp to useful features
df["timestamp"] = pd.to_datetime(df["timestamp"])
df["hour"] = df["timestamp"].dt.hour

# Encode categorical data
le_location = LabelEncoder()
le_type = LabelEncoder()

df["location_encoded"] = le_location.fit_transform(df["location"])
df["type_encoded"] = le_type.fit_transform(df["type"])

# Select features
features = df[[
    "amount",
    "hour",
    "location_encoded",
    "type_encoded"
]]

# --- Train Model ---
model = IsolationForest(contamination=0.05, random_state=42)
df["anomaly"] = model.fit_predict(features)

# Convert output: -1 = anomaly, 1 = normal
df["ml_flag"] = df["anomaly"].apply(lambda x: "ANOMALY" if x == -1 else "NORMAL")

df.to_csv("ml_flagged.csv", index=False)

print("ML anomaly detection complete!")