# Day 40 — Pandas: CSV Handling at Scale

This lesson covers large-scale CSV handling using Pandas.
It focuses on real-world data analysis tasks like filtering,
grouping, cleaning, and exporting data.

## Topics Covered
- Reading CSV files
- Data inspection (head, tail, shape)
- Column selection
- Filtering and sorting
- Adding and updating columns
- Handling missing values
- GroupBy and aggregations
- Chunk-based reading for large files
- Writing cleaned data to CSV
- Real-world data cleaning pipeline

# Day 41 — NumPy Basics

This lesson introduces NumPy, the core library for numerical computing in Python.
It covers array creation, manipulation, mathematical operations, and real-world examples.

## Topics Covered
- Creating NumPy arrays
- Array properties
- Indexing and slicing
- Mathematical operations
- Statistical functions
- Matrix operations
- Random number generation
- Copy vs view
- Stacking arrays
- Data normalization

| Concept          | Why It Matters            |
| ---------------- | ------------------------- |
| NumPy arrays     | Faster than lists         |
| Shape & dtype    | Understand data structure |
| Vectorized ops   | No loops                  |
| Broadcasting     | Clean math                |
| Boolean indexing | Filtering                 |
| Stats functions  | Analysis                  |
| Matrix ops       | ML foundation             |
| Copy vs view     | Avoid bugs                |

# Day 42 — NumPy Advanced (Broadcasting, Axis, Performance)

This lesson covers advanced NumPy concepts that make numerical code fast and scalable.
It explains broadcasting rules, axis usage, and performance benefits of vectorization.

## Topics Covered
- Broadcasting with scalars and arrays
- Axis-based operations
- keepdims usage
- Vectorization vs loops
- Performance timing
- Universal functions (ufuncs)
- Boolean masking and where
- Memory views
- Flatten vs ravel
- Real-world feature scaling

# Day 43 — **Pandas Advanced**

This lesson covers advanced Pandas operations used in real-world data analysis,
including groupby analytics, merging datasets, window functions, and performance tips.

## Topics Covered
- Advanced filtering
- GroupBy with multiple aggregations
- transform vs apply
- map and applymap
- Sorting with multiple columns
- Merge and join operations
- Date handling
- Rolling window functions
- Ranking analytics
- Performance best practices
- Real-world department report

# Day 45 — Advanced Matplotlib

This lesson covers advanced Matplotlib techniques for creating professional,
publication-quality visualizations.

## Topics Covered
- Figure vs Axes
- Proper subplots layout
- Plot styles
- Line customization
- Legends and annotations
- Grid control
- Twin axes
- Log scaling
- Saving high-quality plots
- Performance optimization
- Real-world dashboard-style plots

# Day 46 — Seaborn (Statistical Visualization)

This lesson introduces Seaborn for statistical data visualization.
It focuses on distribution analysis, relationships, and category-based insights.

## Topics Covered
- Distribution plots
- Box and violin plots
- Count plots
- Scatter and regression plots
- Bar plots with aggregation
- Heatmaps
- Pair plots
- FacetGrid
- Themes and styling
- Real-world sales analysis

| Use Seaborn when  | Use Matplotlib when |
| ----------------- | ------------------- |
| Statistical plots | Full control        |
| Quick insights    | Custom dashboards   |
| Pandas data       | Low-level tuning    |

# Polars Library — Fast Data Processing

This module demonstrates data manipulation using Polars,
a high-performance DataFrame library designed for large datasets.

## Topics Covered
- DataFrame creation
- Column selection and filtering
- Expression-based transformations
- Conditional logic
- GroupBy aggregations
- Lazy execution
- CSV handling
- Real-world sales analysis

## Why Polars
- Faster than Pandas
- Memory efficient
- Optimized query execution


| Pandas              | Polars           |
| ------------------- | ---------------- |
| Row-based           | Columnar         |
| Eager               | Lazy by default  |
| Slower on big data  | Very fast        |
| Python loops common | Expression-based |
| Memory heavy        | Memory efficient |
