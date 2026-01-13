# ---------------------------------------------------------
# Day 40: Pandas - CSV Handling at Scale
# ---------------------------------------------------------

import pandas as pd


# ---------------------------------------------------------
# 1. Reading a CSV file
# ---------------------------------------------------------

df = pd.read_csv("students.csv")

print("DataFrame loaded:")
print(df)


# ---------------------------------------------------------
# 2. Basic Data Inspection
# ---------------------------------------------------------

print("\nFirst 5 rows:")
print(df.head())

print("\nLast 5 rows:")
print(df.tail())

print("\nShape (rows, columns):", df.shape)

print("\nColumn names:")
print(df.columns)

print("\nData types:")
print(df.dtypes)


# ---------------------------------------------------------
# 3. Selecting Columns
# ---------------------------------------------------------

print("\nSelecting single column:")
print(df["name"])

print("\nSelecting multiple columns:")
print(df[["name", "age"]])


# ---------------------------------------------------------
# 4. Filtering Rows
# ---------------------------------------------------------

print("\nStudents older than 21:")
print(df[df["age"] > 21])

print("\nStudent named Priyanshu:")
print(df[df["name"] == "Priyanshu"])


# ---------------------------------------------------------
# 5. Sorting Data
# ---------------------------------------------------------

print("\nSorting by age:")
print(df.sort_values(by="age"))

print("\nSorting by age (descending):")
print(df.sort_values(by="age", ascending=False))


# ---------------------------------------------------------
# 6. Adding a New Column
# ---------------------------------------------------------

df["is_adult"] = df["age"] >= 18

print("\nAfter adding is_adult column:")
print(df)


# ---------------------------------------------------------
# 7. Updating Values
# ---------------------------------------------------------

df.loc[df["name"] == "Aman", "age"] = 22

print("\nAfter updating age of Aman:")
print(df)


# ---------------------------------------------------------
# 8. Removing Columns and Rows
# ---------------------------------------------------------

df_no_id = df.drop(columns=["id"])
print("\nAfter dropping id column:")
print(df_no_id)

df_removed = df[df["age"] >= 21]
print("\nAfter removing students younger than 21:")
print(df_removed)


# ---------------------------------------------------------
# 9. Handling Missing Values
# ---------------------------------------------------------

print("\nChecking missing values:")
print(df.isnull())

print("\nTotal missing values:")
print(df.isnull().sum())

df_filled = df.fillna(0)
print("\nAfter filling missing values:")
print(df_filled)


# ---------------------------------------------------------
# 10. GroupBy Operations (Very Important)
# ---------------------------------------------------------

print("\nAverage age:")
print(df["age"].mean())

print("\nGrouping by age:")
print(df.groupby("age").size())


# ---------------------------------------------------------
# 11. Aggregations
# ---------------------------------------------------------

print("\nAggregation summary:")
print(df.agg({
    "age": ["min", "max", "mean"]
}))


# ---------------------------------------------------------
# 12. Reading Large CSV in Chunks
# ---------------------------------------------------------
# Useful for very large files

print("\nReading CSV in chunks:")

chunks = pd.read_csv("students.csv", chunksize=2)

for chunk in chunks:
    print(chunk)
    print("---")


# ---------------------------------------------------------
# 13. Writing DataFrame to CSV
# ---------------------------------------------------------

df.to_csv("students_updated.csv", index=False)
print("\nUpdated CSV saved")


# ---------------------------------------------------------
# 14. Real-world Example: Data Cleaning Pipeline
# ---------------------------------------------------------

clean_df = (
    df
    .drop_duplicates()
    .assign(age=lambda x: x["age"].astype(int))
    .sort_values(by="age", ascending=False)
)

print("\nCleaned DataFrame:")
print(clean_df)


# ---------------------------------------------------------
# End of Day 40: Pandas CSV Handling
# ---------------------------------------------------------
