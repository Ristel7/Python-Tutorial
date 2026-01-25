# ---------------------------------------------------------
# Day 47: Dashboard-Style Visualization
# ---------------------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ---------------------------------------------------------
# 1. Sample Dataset (Sales Data)
# ---------------------------------------------------------

data = {
    "month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "sales": [12000, 15000, 14000, 18000, 20000, 22000],
    "expenses": [8000, 9000, 8500, 10000, 11000, 12000],
    "region": ["North", "North", "South", "South", "North", "South"]
}

df = pd.DataFrame(data)


# ---------------------------------------------------------
# 2. Global Styling
# ---------------------------------------------------------

sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (14, 8)


# ---------------------------------------------------------
# 3. Create Dashboard Layout
# ---------------------------------------------------------
# 2 rows x 2 columns dashboard

fig, axes = plt.subplots(2, 2)
fig.suptitle("Sales Performance Dashboard", fontsize=16, fontweight="bold")


# ---------------------------------------------------------
# Chart 1: Sales Trend (Line Chart)
# ---------------------------------------------------------

axes[0, 0].plot(df["month"], df["sales"], marker="o")
axes[0, 0].set_title("Monthly Sales Trend")
axes[0, 0].set_xlabel("Month")
axes[0, 0].set_ylabel("Sales")


# ---------------------------------------------------------
# Chart 2: Expenses Trend (Line Chart)
# ---------------------------------------------------------

axes[0, 1].plot(df["month"], df["expenses"], marker="o", color="orange")
axes[0, 1].set_title("Monthly Expenses Trend")
axes[0, 1].set_xlabel("Month")
axes[0, 1].set_ylabel("Expenses")


# ---------------------------------------------------------
# Chart 3: Sales by Region (Bar Chart)
# ---------------------------------------------------------

region_sales = df.groupby("region")["sales"].sum().reset_index()

sns.barplot(
    x="region",
    y="sales",
    data=region_sales,
    ax=axes[1, 0]
)
axes[1, 0].set_title("Total Sales by Region")
axes[1, 0].set_xlabel("Region")
axes[1, 0].set_ylabel("Total Sales")


# ---------------------------------------------------------
# Chart 4: Profit Distribution (Histogram)
# ---------------------------------------------------------

df["profit"] = df["sales"] - df["expenses"]

axes[1, 1].hist(df["profit"], bins=5)
axes[1, 1].set_title("Profit Distribution")
axes[1, 1].set_xlabel("Profit")
axes[1, 1].set_ylabel("Frequency")


# ---------------------------------------------------------
# 4. Layout Adjustment
# ---------------------------------------------------------

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()


# ---------------------------------------------------------
# End of Day 47: Dashboard Visualization
# ---------------------------------------------------------
