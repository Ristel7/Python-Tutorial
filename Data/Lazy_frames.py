import polars as pl

df = pl.DataFrame({
    "name": ["Aman", "Riya", "Priyanshu", "Sneha"],
    "department": ["IT", "HR", "IT", "HR"],
    "salary": [50000, 40000, 60000, 45000]
})

lazy_df = df.lazy()
