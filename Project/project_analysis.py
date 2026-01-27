# ---------------------------------------------------------
# Mini Data Analysis Project
# Sales Performance Analysis
# ---------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ---------------------------------------------------------
# 1. Load Data
# ---------------------------------------------------------

df = pd.read_csv("sales_data.csv")
print("Raw Data:")
print(df)


# ---------------------------------------------------------
# 2. Data Overview
# ---------------------------------------------------------

print("\nDataset Info:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())


# ---------------------------------------------------------
# 3. Feature Engineering
# ---------------------------------------------------------

df["profit"] = df["sales"] - df["expenses"]

print("\nData with Profit Column:")
print(df)


# ---------------------------------------------------------
# 4. Key Analysis
# ---------------------------------------------------------

total_sales = df["sales"].sum()
total_profit = df["profit"].sum()

print("\nTotal Sales:", total_sales)
print("Total Profit:", total_profit)

region_summary = (
    df.groupby("region")
    .agg(
        total_sales=("sales", "sum"),
        total_profit=("profit", "sum"),
        avg_profit=("profit", "mean")
    )
)

print("\nRegion-wise Summary:")
print(region_summary)


# ---------------------------------------------------------
# 5. Dashboard Visualization
# ---------------------------------------------------------

sns.set_theme(style="whitegrid")
plt.figure(figsize=(14, 8))

# Sales Trend
plt.subplot(2, 2, 1)
plt.plot(df["month"], df["sales"], marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

# Expenses Trend
plt.subplot(2, 2, 2)
plt.plot(df["month"], df["expenses"], marker="o", color="orange")
plt.title("Monthly Expenses Trend")
plt.xlabel("Month")
plt.ylabel("Expenses")

# Sales by Region
plt.subplot(2, 2, 3)
sns.barplot(
    x=region_summary.index,
    y=region_summary["total_sales"]
)
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")

# Profit Distribution
plt.subplot(2, 2, 4)
plt.hist(df["profit"], bins=6)
plt.title("Profit Distribution")
plt.xlabel("Profit")
plt.ylabel("Frequency")

plt.tight_layout()
plt.savefig("dashboard.png", dpi=300)
plt.show()


# ---------------------------------------------------------
# End of Project
# ---------------------------------------------------------
