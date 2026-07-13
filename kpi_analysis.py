import os
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "financial_data_clean.csv")
VISUALS_DIR = os.path.join(BASE_DIR, "..", "visuals")

os.makedirs(VISUALS_DIR, exist_ok=True)

df = pd.read_csv(DATA_PATH)
df["Date"] = pd.to_datetime(df["Date"])


def save(fig, name):
    path = os.path.join(VISUALS_DIR, name)
    fig.savefig(path, bbox_inches="tight")
    print(f"Saved {path}")
    plt.close(fig)


# Q1: Top 10 Companies by Revenue
def top_revenue():
    top = df.groupby("Company")["Revenue"].sum().sort_values(ascending=False).head(10)
    print("\n--- Top 10 Companies by Revenue ---")
    print(top)

    fig, ax = plt.subplots(figsize=(10, 6))
    top.plot(kind="bar", color="steelblue", ax=ax)
    ax.set_title("Top 10 Companies by Revenue")
    ax.set_ylabel("Revenue")
    plt.xticks(rotation=45)
    plt.tight_layout()
    save(fig, "q1_top_revenue.png")


# Q2: Top Companies by Profit
def top_profit():
    profit = df.groupby("Company")["Profit"].sum().sort_values(ascending=False)
    print("\n--- Profit by Company ---")
    print(profit)

    fig, ax = plt.subplots(figsize=(10, 8))
    ax.pie(profit, labels=profit.index, autopct="%1.1f%%", startangle=90)
    ax.set_title("Top Companies by Profit")
    plt.tight_layout()
    save(fig, "q2_top_profit.png")


# Q3: Average ROI KPI card
def avg_roi():
    avg = df["ROI (%)"].mean()
    print(f"\n--- Average ROI: {avg:.2f}% ---")

    fig, ax = plt.subplots(figsize=(5, 3))
    ax.text(0.5, 0.6, f"{avg:.2f}%", fontsize=32, fontweight="bold", ha="center")
    ax.text(0.5, 0.25, "Average ROI", fontsize=16, ha="center")
    ax.axis("off")
    save(fig, "q3_avg_roi.png")


# Q4: Monthly Revenue Trend
def monthly_revenue():
    monthly = df.groupby("Date")["Revenue"].sum()

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(monthly.index, monthly.values)
    ax.set_title("Monthly Revenue Trend")
    ax.grid(True)
    save(fig, "q4_monthly_revenue.png")


# Q5: Yearly Profit Growth %
def yearly_profit_growth():
    profit = df.groupby("Year")["Profit"].sum()
    growth = profit.pct_change() * 100
    print("\n--- Yearly Profit Growth % ---")
    print(growth)

    fig, ax = plt.subplots(figsize=(8, 5))
    growth.plot(marker="o", ax=ax)
    ax.set_title("Yearly Profit Growth")
    ax.set_ylabel("%")
    ax.grid(True)
    save(fig, "q5_yearly_profit_growth.png")


# Q6: Sector Revenue
def sector_revenue():
    sector = df.groupby("Sector")["Revenue"].sum().sort_values()
    print("\n--- Sector Revenue ---")
    print(sector)

    fig, ax = plt.subplots(figsize=(8, 6))
    sector.plot(kind="bar", ax=ax)
    ax.set_title("Sector Revenue")
    plt.tight_layout()
    save(fig, "q6_sector_revenue.png")


# Q7: Sector Profit
def sector_profit():
    profit = df.groupby("Sector")["Profit"].sum()

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.pie(profit, labels=profit.index, autopct="%1.1f%%", startangle=90)
    ax.set_title("Sector Profit")
    plt.tight_layout()
    save(fig, "q7_sector_profit.png")


# Q8: Top Performing Stocks by average ROI
def top_stocks():
    stocks = df.groupby("Company")["ROI (%)"].mean().sort_values(ascending=False)
    print("\n--- Companies Ranked by Average ROI ---")
    print(stocks)

    fig, ax = plt.subplots(figsize=(10, 6))
    stocks.plot(kind="line", marker="o", color="orange", ax=ax)
    ax.set_title("Top Performing Stocks")
    plt.tight_layout()
    save(fig, "q8_top_stocks.png")


# Q9: Profit Margin Comparison
def profit_margin():
    margin = df.groupby("Company")["Profit Margin"].mean()
    print("\n--- Profit Margin by Company ---")
    print(margin)

    fig, ax = plt.subplots(figsize=(10, 6))
    margin.plot(kind="barh", color="green", ax=ax)
    ax.set_title("Profit Margin Comparison")
    plt.tight_layout()
    save(fig, "q9_profit_margin.png")


if __name__ == "__main__":
    top_revenue()
    top_profit()
    avg_roi()
    monthly_revenue()
    yearly_profit_growth()
    sector_revenue()
    sector_profit()
    top_stocks()
    profit_margin()
    print("\nAll KPI visuals generated and saved to /visuals")
