# ---------------------------------------------------------
# Day 46: Seaborn - Statistical Data Visualization
# ---------------------------------------------------------

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# ---------------------------------------------------------
# 1. Load built-in dataset
# ---------------------------------------------------------

df = sns.load_dataset("tips")
print(df.head())


# ---------------------------------------------------------
# 2. Distribution Plot (hist + kde)
# ---------------------------------------------------------

sns.histplot(df["total_bill"], kde=True)
plt.title("Distribution of Total Bill")
plt.show()


# ---------------------------------------------------------
# 3. Box Plot (Outliers & Spread)
# ---------------------------------------------------------

sns.boxplot(x="day", y="total_bill", data=df)
plt.title("Total Bill by Day")
plt.show()


# ---------------------------------------------------------
# 4. Violin Plot (Distribution + Density)
# ---------------------------------------------------------

sns.violinplot(x="day", y="total_bill", data=df)
plt.title("Violin Plot of Total Bill")
plt.show()


# ---------------------------------------------------------
# 5. Count Plot (Category Frequency)
# ---------------------------------------------------------

sns.countplot(x="day", data=df)
plt.title("Customer Count by Day")
plt.show()


# ---------------------------------------------------------
# 6. Scatter Plot with Hue
# ---------------------------------------------------------

sns.scatterplot(
    x="total_bill",
    y="tip",
    hue="sex",
    data=df
)
plt.title("Tip vs Total Bill")
plt.show()


# ---------------------------------------------------------
# 7. Regression Plot
# ---------------------------------------------------------

sns.regplot(x="total_bill", y="tip", data=df)
plt.title("Regression: Tip vs Total Bill")
plt.show()


# ---------------------------------------------------------
# 8. Bar Plot with Aggregation
# ---------------------------------------------------------

sns.barplot(
    x="day",
    y="total_bill",
    data=df,
    estimator=np.mean
)
plt.title("Average Bill per Day")
plt.show()


# ---------------------------------------------------------
# 9. Heatmap (Correlation Matrix)
# ---------------------------------------------------------

corr = df.corr(numeric_only=True)

sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()


# ---------------------------------------------------------
# 10. Pair Plot (Very Important)
# ---------------------------------------------------------

sns.pairplot(df, hue="sex")
plt.show()


# ---------------------------------------------------------
# 11. FacetGrid (Split plots by category)
# ---------------------------------------------------------

g = sns.FacetGrid(df, col="time", row="sex")
g.map(sns.scatterplot, "total_bill", "tip")
plt.show()


# ---------------------------------------------------------
# 12. Styling with Themes
# ---------------------------------------------------------

sns.set_theme(style="darkgrid")

sns.boxplot(x="day", y="tip", data=df)
plt.title("Styled Boxplot")
plt.show()


# ---------------------------------------------------------
# 13. Real-world Example: Sales Analysis
# ---------------------------------------------------------

sales_data = pd.DataFrame({
    "month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "sales": [12000, 15000, 14000, 18000, 20000],
    "region": ["North", "North", "South", "South", "North"]
})

sns.lineplot(x="month", y="sales", hue="region", data=sales_data, marker="o")
plt.title("Sales Trend by Region")
plt.show()


# ---------------------------------------------------------
# End of Day 46: Seaborn
# ---------------------------------------------------------

