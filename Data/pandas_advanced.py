# ---------------------------------------------------------
# Day 43: Pandas Advanced
# ---------------------------------------------------------

import pandas as pd
import numpy as np


# ---------------------------------------------------------
# 1. Creating Sample Data
# ---------------------------------------------------------

data = {
    "employee": ["Aman", "Riya", "Aman", "Priyanshu", "Riya"],
    "department": ["IT", "HR", "IT", "IT", "HR"],
    "salary": [50000, 40000, 55000, 60000, 42000],
    "experience": [2, 3, 4, 5, 3]
}

df = pd.DataFrame(data)
print("Initial DataFrame:")
print(df)


# ---------------------------------------------------------
# 2. Advanced Filtering
# ---------------------------------------------------------

print("\nEmployees from IT with salary > 52000:")
print(df[(df["department"] == "IT") & (df["salary"] > 52000)])


# ---------------------------------------------------------
# 3. GroupBy (Very Important)
# ---------------------------------------------------------

print("\nAverage salary by department:")
print(df.groupby("department")["salary"].mean())

print("\nMultiple aggregations:")
print(
    df.groupby("department")
    .agg(
        avg_salary=("salary", "mean"),
        max_salary=("salary", "max"),
        emp_count=("employee", "count")
    )
)


# ---------------------------------------------------------
# 4. Transform (broadcast group result back)
# ---------------------------------------------------------

df["dept_avg_salary"] = df.groupby("department")["salary"].transform("mean")

print("\nAfter transform:")
print(df)


# ---------------------------------------------------------
# 5. apply() vs map()
# ---------------------------------------------------------

df["salary_after_bonus"] = df["salary"].apply(lambda x: x * 1.10)

print("\nSalary after bonus:")
print(df)


# map() for single column replacement
dept_map = {"IT": "Technology", "HR": "Human Resources"}
df["department_full"] = df["department"].map(dept_map)

print("\nMapped department names:")
print(df)


# ---------------------------------------------------------
# 6. applymap() for full DataFrame
# ---------------------------------------------------------

num_df = df[["salary", "experience"]]
print("\napplymap (convert to string):")
print(num_df.applymap(lambda x: f"{x}"))


# ---------------------------------------------------------
# 7. Sorting with multiple columns
# ---------------------------------------------------------

print("\nSorting by department and salary:")
print(df.sort_values(by=["department", "salary"], ascending=[True, False]))


# ---------------------------------------------------------
# 8. Merging DataFrames
# ---------------------------------------------------------

dept_info = pd.DataFrame({
    "department": ["IT", "HR"],
    "manager": ["Rahul", "Sneha"]
})

merged = pd.merge(df, dept_info, on="department", how="left")

print("\nMerged DataFrame:")
print(merged)


# ---------------------------------------------------------
# 9. Joining using index
# ---------------------------------------------------------

dept_info_indexed = dept_info.set_index("department")

joined = df.join(dept_info_indexed, on="department")

print("\nJoined DataFrame:")
print(joined)


# ---------------------------------------------------------
# 10. Handling Dates
# ---------------------------------------------------------

dates = pd.date_range("2024-01-01", periods=5)

df["joining_date"] = dates

print("\nWith dates:")
print(df)

print("\nYear extracted:")
print(df["joining_date"].dt.year)


# ---------------------------------------------------------
# 11. Window Functions (rolling)
# ---------------------------------------------------------

df["rolling_salary_avg"] = df["salary"].rolling(window=2).mean()

print("\nRolling average salary:")
print(df)


# ---------------------------------------------------------
# 12. Rank and Sorting Analytics
# ---------------------------------------------------------

df["salary_rank"] = df["salary"].rank(ascending=False)

print("\nSalary ranking:")
print(df)


# ---------------------------------------------------------
# 13. Performance Tips
# ---------------------------------------------------------

# Vectorized operation (fast)
df["salary_fast"] = df["salary"] * 1.05

# Avoid loops (slow) - shown conceptually
print("\nVectorized operations applied")


# ---------------------------------------------------------
# 14. Real-world Example: Department Summary Report
# ---------------------------------------------------------

report = (
    df.groupby("department")
    .agg(
        total_salary=("salary", "sum"),
        avg_experience=("experience", "mean"),
        employees=("employee", "count")
    )
    .sort_values(by="total_salary", ascending=False)
)

print("\nDepartment Summary Report:")
print(report)


# ---------------------------------------------------------
# End of Day 43: Pandas Advanced
# ---------------------------------------------------------
