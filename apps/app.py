import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("../final_output.csv")

st.set_page_config(page_title="AML Dashboard", layout="wide")

st.title("🇳🇬 Anti-Money Laundering Dashboard")

# --- KPIs ---
total_tx = len(df)
suspicious_tx = len(df[df["final_flag"] == "SUSPICIOUS"])
avg_risk = round(df["risk_score"].mean(), 2)

col1, col2, col3 = st.columns(3)

col1.metric("Total Transactions", total_tx)
col2.metric("Suspicious Transactions", suspicious_tx)
col3.metric("Average Risk Score", avg_risk)

# --- Filter ---
st.sidebar.header("Filters")

min_amount = st.sidebar.slider("Minimum Amount", 0, int(df["amount"].max()), 0)
selected_flag = st.sidebar.selectbox("Transaction Type", ["ALL", "NORMAL", "SUSPICIOUS"])

filtered_df = df[df["amount"] >= min_amount]

if selected_flag != "ALL":
    filtered_df = filtered_df[filtered_df["final_flag"] == selected_flag]

# --- Table ---
st.subheader("Transactions")
st.dataframe(filtered_df)

# --- High Risk Section ---
st.subheader("🚨 High Risk Transactions")
high_risk = df[df["risk_score"] >= 5]
st.dataframe(high_risk)

# --- Simple Chart ---
st.subheader("Risk Score Distribution")
st.bar_chart(df["risk_score"].value_counts())