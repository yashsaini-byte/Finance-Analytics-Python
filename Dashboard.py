import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

df = pd.read_csv(os.path.join(BASE_DIR, "..", "data", "financial_data_clean.csv"))

df["Date"] = pd.to_datetime(df["Date"])

df["Year"] = df["Date"].dt.year

st.set_page_config(
    page_title="Finance Analytics Dashboard",
    layout="wide"
)

st.title("📊 Finance Analytics Dashboard")


total_revenue = df["Revenue"].sum()

total_profit = df["Profit"].sum()

average_roi = df["ROI (%)"].mean()

investment = df["Investment"].sum()

col1,col2,col3,col4 = st.columns(4)

col1.metric("Revenue",f"${total_revenue:,.0f} M")

col2.metric("Profit",f"${total_profit:,.0f} M")

col3.metric("Average ROI",f"{average_roi:.2f}%")

col4.metric("Investment",f"${investment:,.0f} M")


st.sidebar.header("Filters")

company = st.sidebar.selectbox(
    "Company",
    ["All"] + sorted(df["Company"].unique().tolist())
)

year = st.sidebar.selectbox(
    "Year",
    ["All"] + sorted(df["Year"].unique().tolist())
)

sector = st.sidebar.selectbox(
    "Sector",
    ["All"] + sorted(df["Sector"].unique().tolist())
)

filtered_df = df.copy()

if company != "All":
    filtered_df = filtered_df[filtered_df["Company"] == company]

if year != "All":
    filtered_df = filtered_df[filtered_df["Year"] == year]

if sector != "All":
    filtered_df = filtered_df[filtered_df["Sector"] == sector]



st.subheader("Revenue Trend")

revenue = filtered_df.groupby("Date")["Revenue"].sum()

fig,ax = plt.subplots(figsize=(10,4))

ax.plot(revenue.index,revenue.values)

ax.set_title("Revenue Trend")

st.pyplot(fig)

st.subheader("Profit Trend")

profit = filtered_df.groupby("Date")["Profit"].sum()

fig,ax = plt.subplots(figsize=(10,4))

ax.plot(profit.index,profit.values)

ax.set_title("Profit Trend")

st.pyplot(fig)

st.subheader("Top Revenue Companies")

top = (
    filtered_df.groupby("Company")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

fig,ax = plt.subplots(figsize=(8,5))

top.plot(kind="bar",ax=ax)

st.pyplot(fig)


st.subheader("Sector Revenue")

sector = filtered_df.groupby("Sector")["Revenue"].sum()

fig,ax = plt.subplots(figsize=(6,6))

ax.pie(
    sector,
    labels=sector.index,
    autopct="%1.1f%%"
)

st.pyplot(fig)



st.subheader("Revenue vs Expenses")

company = (
    filtered_df.groupby("Company")[["Revenue","Expenses"]]
    .sum()
)

fig,ax = plt.subplots(figsize=(10,5))

company.plot(kind="bar",ax=ax)

st.pyplot(fig)

st.subheader("Risk vs Return")

risk = (
    filtered_df.groupby("Company")["ROI (%)"]
    .agg(["mean","std"])
)

risk.columns=["Return","Risk"]

fig,ax = plt.subplots(figsize=(8,6))

ax.scatter(
    risk["Risk"],
    risk["Return"]
)

for i in risk.index:
    ax.text(
        risk.loc[i,"Risk"],
        risk.loc[i,"Return"],
        i
    )

st.pyplot(fig)
