# ---------------------------------------------------------
# Day 42: NumPy Advanced
# Broadcasting | Axis | Performance
# ---------------------------------------------------------

import time
import numpy as np


# ---------------------------------------------------------
# 1. Broadcasting (Most Important Concept)
# ---------------------------------------------------------
# NumPy automatically expands smaller arrays to match larger ones

arr = np.array([1, 2, 3])
scalar = 10

print("Broadcasting with scalar:")
print(arr + scalar)


# ---------------------------------------------------------
# Broadcasting between arrays
# ---------------------------------------------------------

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

vector = np.array([10, 20, 30])

print("\nBroadcasting vector to matrix:")
print(matrix + vector)


# ---------------------------------------------------------
# Broadcasting rules demo
# ---------------------------------------------------------

col_vector = np.array([[1], [2], [3]])
row_vector = np.array([10, 20, 30])

print("\nBroadcasting column and row vectors:")
print(col_vector + row_vector)


# ---------------------------------------------------------
# 2. Axis (How NumPy moves)
# ---------------------------------------------------------
# axis=0 → column-wise
# axis=1 → row-wise

data = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("\nData:")
print(data)

print("\nSum axis=0 (columns):")
print(np.sum(data, axis=0))

print("\nSum axis=1 (rows):")
print(np.sum(data, axis=1))


# ---------------------------------------------------------
# Mean, max, min using axis
# ---------------------------------------------------------

print("\nMean by column:", np.mean(data, axis=0))
print("Max by row:", np.max(data, axis=1))


# ---------------------------------------------------------
# 3. Keep dimensions (keepdims)
# ---------------------------------------------------------

print("\nKeep dimensions:")
print(np.sum(data, axis=1, keepdims=True))


# ---------------------------------------------------------
# 4. Vectorization vs Python loops
# ---------------------------------------------------------

arr = np.arange(1_000_000)

# Vectorized
vectorized = arr * 2

# Loop-based (slow)
loop_result = []
for x in arr:
    loop_result.append(x * 2)

print("\nVectorization done (loop skipped)")


# ---------------------------------------------------------
# 5. Performance timing
# ---------------------------------------------------------


start = time.time()
arr * 2
print("Vectorized time:", time.time() - start)

start = time.time()
for x in arr:
    x * 2
print("Loop time:", time.time() - start)


# ---------------------------------------------------------
# 6. Universal Functions (ufuncs)
# ---------------------------------------------------------

values = np.array([1, 4, 9, 16])

print("\nUfunc examples:")
print("Square root:", np.sqrt(values))
print("Exponential:", np.exp(values))
print("Log:", np.log(values))


# ---------------------------------------------------------
# 7. Where vs Boolean masking
# ---------------------------------------------------------

nums = np.array([10, 25, 30, 5, 40])

print("\nBoolean masking:")
print(nums[nums > 20])

print("\nUsing where:")
print(np.where(nums > 20, nums, 0))


# ---------------------------------------------------------
# 8. Memory views (advanced pe
