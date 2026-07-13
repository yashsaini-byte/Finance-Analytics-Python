import pandas as pd
import numpy as np
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Relative path — works on any machine, as long as the CSV sits in /data
RAW_PATH = os.path.join(BASE_DIR, "..", "data", "financial_data.csv")
CLEAN_PATH = os.path.join(BASE_DIR, "..", "data", "financial_data_clean.csv")

df = pd.read_csv(RAW_PATH)

print(df.head())
print(df.describe())
print(df.isnull().sum())
print(df.info())

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Remove duplicates
df.drop_duplicates(inplace=True)

# Remove rows with missing values
df.dropna(inplace=True)

# Derived columns
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year
df['Quarter'] = df['Date'].dt.quarter
df['Profit Margin'] = (df['Profit'] / df['Revenue']) * 100
df['Expense Ratio'] = (df['Expenses'] / df['Revenue']) * 100

print(df.info())

# THIS WAS MISSING BEFORE — the cleaned data now actually persists
df.to_csv(CLEAN_PATH, index=False)
print(f"Cleaned data saved to {CLEAN_PATH}")
