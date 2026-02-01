# ---------------------------------------------------------
# Day 48: Polars vs Pandas Performance Comparison
# ---------------------------------------------------------

import pandas as pd
import polars as pl
import numpy as np
import time


# ---------------------------------------------------------
# 1. Create Large Dataset
# ---------------------------------------------------------

rows = 1_000_000

data = {
    "id": np.arange(rows),
    "category": np.random.choice(["A", "B", "C", "D"], size=rows),
    "value": np.random.randint(1, 100, size=rows),
    "sales": np.random.randint(1000, 10000, size=rows)
}


# ---------------------------------------------------------
# 2. Pandas DataFrame
# ---------------------------------------------------------

start = time.time()
pd_df = pd.DataFrame(data)
print("Pandas DataFrame creation time:", time.time() - start)


# ---------------------------------------------------------
# 3. Polars DataFrame
# ---------------------------------------------------------

start = time.time()
pl_df = pl.DataFrame(data)
print("Polars DataFrame creation time:", time.time() - start)


# ---------------------------------------------------------
# 4. Filtering Performance
# ---------------------------------------------------------

# Pandas
start = time.time()
pd_filtered = pd_df[pd_df["sales"] > 5000]
print("Pandas filtering time:", time.time() - start)

# Polars
start = time.time()
pl_filtered = pl_df.filter(pl.col("sales") > 5000)
print("Polars filtering time:", time.time() - start)


# ---------------------------------------------------------
# 5. GroupBy Aggregation Performance
# ---------------------------------------------------------

# Pandas
start = time.time()
pd_group = (
    pd_df.groupby("category")
    .agg(avg_sales=("sales", "mean"))
)
print("Pandas groupby time:", time.time() - start)

# Polars
start = time.time()
pl_group = (
    pl_df.group_by("category")
    .agg(pl.col("sales").mean())
)
print("Polars groupby time:", time.time() - start)


# ---------------------------------------------------------
# 6. Column Computation Performance
# ---------------------------------------------------------

# Pandas
start = time.time()
pd_df["profit"] = pd_df["sales"] - pd_df["value"]
print("Pandas column operation time:", time.time() - start)

# Polars
start = time.time()
pl_df = pl_df.with_columns(
    (pl.col("sales") - pl.col("value")).alias("profit")
)
print("Polars column operation time:", time.time() - start)


# ---------------------------------------------------------
# 7. Lazy Execution (Polars Only)
# ---------------------------------------------------------

start = time.time()
lazy_result = (
    pl_df.lazy()
    .filter(pl.col("sales") > 5000)
    .group_by("category")
    .agg(pl.col("profit").mean())
    .collect()
)
print("Polars lazy execution time:", time.time() - start)


# ---------------------------------------------------------
# End of Comparison
# ---------------------------------------------------------
