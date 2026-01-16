# ---------------------------------------------------------
# Day 41: NumPy Basics
# ---------------------------------------------------------

import numpy as np


# ---------------------------------------------------------
# 1. Creating NumPy Arrays
# ---------------------------------------------------------

arr1 = np.array([1, 2, 3, 4, 5])
print("1D array:", arr1)

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D array:\n", arr2)


# ---------------------------------------------------------
# 2. Array Properties
# ---------------------------------------------------------

print("\nArray shape:", arr2.shape)
print("Array size:", arr2.size)
print("Array dimensions:", arr2.ndim)
print("Data type:", arr2.dtype)


# ---------------------------------------------------------
# 3. Special Arrays
# ---------------------------------------------------------

zeros = np.zeros((2, 3))
ones = np.ones((3, 2))
identity = np.eye(3)

print("\nZeros array:\n", zeros)
print("\nOnes array:\n", ones)
print("\nIdentity matrix:\n", identity)


# ---------------------------------------------------------
# 4. Creating Arrays with Range
# ---------------------------------------------------------

range_arr = np.arange(1, 10, 2)
linspace_arr = np.linspace(0, 1, 5)

print("\nRange array:", range_arr)
print("Linspace array:", linspace_arr)


# ---------------------------------------------------------
# 5. Reshaping Arrays
# ---------------------------------------------------------

arr = np.arange(1, 13)
reshaped = arr.reshape(3, 4)

print("\nOriginal array:", arr)
print("Reshaped array:\n", reshaped)


# ---------------------------------------------------------
# 6. Indexing and Slicing
# ---------------------------------------------------------

print("\nIndexing:")
print(arr1[0])
print(arr2[1, 2])

print("\nSlicing:")
print(arr1[1:4])
print(arr2[:, 1])


# ---------------------------------------------------------
# 7. Boolean Indexing
# ---------------------------------------------------------

print("\nBoolean indexing:")
print(arr1[arr1 > 2])


# ---------------------------------------------------------
# 8. Mathematical Operations
# ---------------------------------------------------------

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("\nMath operations:")
print("Add:", a + b)
print("Subtract:", a - b)
print("Multiply:", a * b)
print("Divide:", a / b)
print("Square:", a ** 2)


# ---------------------------------------------------------
# 9. Statistical Functions
# ---------------------------------------------------------

data = np.array([10, 20, 30, 40, 50])

print("\nStatistics:")
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Std Dev:", np.std(data))
print("Min:", np.min(data))
print("Max:", np.max(data))


# ---------------------------------------------------------
# 10. Matrix Operations
# ---------------------------------------------------------

m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])

print("\nMatrix multiplication:")
print(np.dot(m1, m2))

print("\nTranspose:")
print(m1.T)


# ---------------------------------------------------------
# 11. Random Numbers
# ---------------------------------------------------------

random_arr = np.random.rand(3, 3)
random_int = np.random.randint(1, 10, size=5)

print("\nRandom float array:\n", random_arr)
print("Random integers:", random_int)


# ---------------------------------------------------------
# 12. Copy vs View (Very Important)
# ---------------------------------------------------------

original = np.array([1, 2, 3])
view = original.view()
copy = original.copy()

view[0] = 99
copy[1] = 88

print("\nOriginal after view change:", original)
print("Copy remains separate:", copy)


# ---------------------------------------------------------
# 13. Stacking Arrays
# ---------------------------------------------------------

x = np.array([1, 2])
y = np.array([3, 4])

print("\nHorizontal stack:", np.hstack((x, y)))
print("Vertical stack:\n", np.vstack((x, y)))


# ---------------------------------------------------------
# 14. Real-world Example: Normalizing Data
# ---------------------------------------------------------

scores = np.array([45, 50, 60, 80, 90])

normalized = (scores - np.min(scores)) / (np.max(scores) - np.min(scores))

print("\nOriginal scores:", scores)
print("Normalized scores:", normalized)


# ---------------------------------------------------------
# End of Day 41: NumPy Basics
# ---------------------------------------------------------
