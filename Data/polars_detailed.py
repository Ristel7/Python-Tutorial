# ---------------------------------------------------------
# Polars Detailed Guide
# ---------------------------------------------------------

import polars as pl


# ---------------------------------------------------------
# 1. Creating a DataFrame
# ---------------------------------------------------------

df = pl.DataFrame({
    "name": ["Aman", "Riya", "Priyanshu", "Sneha"],
    "department": ["IT", "HR", "IT", "HR"],
    "salary": [50000, 40000, 60000, 45000],
    "experience": [2, 3, 5, 4]
})

print("Initial DataFrame:")
print(df)


# ---------------------------------------------------------
# 2. Basic Inspection
# ---------------------------------------------------------

print("\nShape:", df.shape)
print("\nColumns:", df.columns)
print("\nSchema:")
print(df.schema)


# ---------------------------------------------------------
# 3. Selecting Columns
# ---------------------------------------------------------

print("\nSelect single column:")
print(df.select("name"))

print("\nSelect multiple columns:")
print(df.select(["name", "salary"]))


# ---------------------------------------------------------
# 4. Filtering Rows
# ---------------------------------------------------------

print("\nEmployees from IT:")
print(df.filter(pl.col("department") == "IT"))

print("\nSalary greater than 45000:")
print(df.filter(pl.col("salary") > 45000))


# ---------------------------------------------------------
# 5. Creating New Columns (with_columns)
# ---------------------------------------------------------

df = df.with_columns(
    (pl.col("salary") * 0.10).alias("bonus"),
    (pl.col("salary") + pl.col("salary") * 0.10).alias("salary_with_bonus")
)

print("\nAfter adding new columns:")
print(df)


# ---------------------------------------------------------
# 6. Conditional Columns (when-then-otherwise)
# ---------------------------------------------------------

df = df.with_columns(
    pl.when(pl.col("salary") >= 55000)
      .then("High")
      .otherwise("Medium")
      .alias("salary_level")
)

print("\nSalary level column:")
print(df)


# ---------------------------------------------------------
# 7. GroupBy & Aggregation
# ---------------------------------------------------------

grouped = (
    df.group_by("department")
      .agg(
          pl.col("salary").mean().alias("avg_salary"),
          pl.col("salary").max().alias("max_salary"),
          pl.count().alias("employee_count")
    )
)

print("\nGroupBy result:")
print(grouped)


# ---------------------------------------------------------
# 8. Sorting
# ---------------------------------------------------------

print("\nSorted by salary (descending):")
print(df.sort("salary", descending=True))


# ---------------------------------------------------------
# 9. Handling Missing Values
# ---------------------------------------------------------

df_null = pl.DataFrame({
    "name": ["A", "B", "C"],
    "score": [80, None, 90]
})

print("\nNull handling:")
print(df_null.fill_null(0))


# ---------------------------------------------------------
# 10. Reading CSV (Eager)
# ---------------------------------------------------------

# df_csv = pl.read_csv("sales_data.csv")
# print(df_csv.head())


# ---------------------------------------------------------
# 11. Lazy API (MOST IMPORTANT FEATURE)
# ---------------------------------------------------------

lazy_df = (
    df.lazy()
      .filter(pl.col("salary") > 45000)
      .select(["name", "salary"])
)

print("\nLazy query plan:")
print(lazy_df.explain())

print("\nLazy execution result:")
print(lazy_df.collect())


# ---------------------------------------------------------
# 12. String Operations
# ---------------------------------------------------------

print("\nUppercase names:")
print(df.select(pl.col("name").str.to_uppercase()))


# ---------------------------------------------------------
# 13. Date Handling
# ---------------------------------------------------------

date_df = pl.DataFrame({
    "date": pl.date_range(
        start=pl.date(2024, 1, 1),
        end=pl.date(2024, 1, 5),
        interval="1d"
    )
})

print("\nDate DataFrame:")
print(date_df)


# ---------------------------------------------------------
# 14. Real-world Example: Sales Analysis
# ---------------------------------------------------------

sales = pl.DataFrame({
    "month": ["Jan", "Feb", "Mar", "Apr"],
    "sales": [12000, 15000, 14000, 18000],
    "expenses": [8000, 9000, 8500, 10000]
})

sales = sales.with_columns(
    (pl.col("sales") - pl.col("expenses")).alias("profit")
)

print("\nSales with profit:")
print(sales)

print("\nTotal Profit:", sales.select(pl.col("profit").sum()))


# ---------------------------------------------------------
# End of Polars Guide
# ---------------------------------------------------------
