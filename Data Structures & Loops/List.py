# -----------------------------------------
# Day 20: Lists in Python (In-depth)
# -----------------------------------------

# A List in Python is an ordered, mutable (changeable) collection of items.
# Lists can store elements of different data types — int, float, string, or even other lists.

# -----------------------------------------
# List Creation
# -----------------------------------------
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True]
nested = [[1, 2, 3], ["a", "b", "c"]]

print("Numbers:", numbers)
print("Fruits:", fruits)
print("Mixed:", mixed)
print("Nested:", nested)

# Creating an empty list
empty_list = []
print("Empty list:", empty_list)

# -----------------------------------------
# Accessing List Elements (Indexing)
# -----------------------------------------
# Indexing starts from 0, and negative indexing starts from -1 (last item)

print("\n--- Indexing ---")
print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])
print("Last fruit:", fruits[-1])
print("Second last number:", numbers[-2])

# -----------------------------------------
# Slicing Lists
# -----------------------------------------
# Syntax: list[start:end:step]
# End index is excluded

print("\n--- Slicing ---")
print("First three numbers:", numbers[:3])        # [1, 2, 3]
print("Last two fruits:", fruits[-2:])            # ['banana', 'cherry']
print("Every second number:", numbers[::2])       # [1, 3, 5]
print("Reversed list:", numbers[::-1])            # [5, 4, 3, 2, 1]

# -----------------------------------------
# Modifying Lists (Mutable)
# -----------------------------------------
print("\n--- Modifying Lists ---")
numbers[0] = 10
print("After modification:", numbers)             # [10, 2, 3, 4, 5]

# -----------------------------------------
# List Methods
# -----------------------------------------

# append(): Add an element at the end
fruits.append("orange")
print("\nAfter append:", fruits)  # ['apple', 'banana', 'cherry', 'orange']

# extend(): Add multiple elements at once
fruits.extend(["grape", "mango"])
print("After extend:", fruits)

# insert(): Add at a specific position
fruits.insert(1, "kiwi")
print("After insert:", fruits)

# remove(): Remove specific element (first occurrence)
fruits.remove("banana")
print("After remove:", fruits)

# pop(): Remove by index (and returns the removed value)
removed = fruits.pop(2)
print("After pop:", fruits)
print("Removed item:", removed)

# clear(): Remove all items from list
temp = [1, 2, 3]
temp.clear()
print("After clear:", temp)

# -----------------------------------------
# Other Useful List Methods
# -----------------------------------------
nums = [4, 1, 3, 2, 5]
print("\nOriginal nums:", nums)
nums.sort()                 # Sort in ascending order
print("Sorted:", nums)
nums.reverse()              # Reverse the list
print("Reversed:", nums)

print("Length:", len(nums))  # Number of elements
print("Max:", max(nums))     # Largest element
print("Min:", min(nums))     # Smallest element
print("Sum:", sum(nums))     # Sum of all numbers
print("Count of 3:", nums.count(3))  # Count occurrences

# -----------------------------------------
# Looping Through Lists
# -----------------------------------------
print("\n--- Looping through Lists ---")
for fruit in fruits:
    print(fruit)

# Using index with range()
for i in range(len(fruits)):
    print(f"Index {i}: {fruits[i]}")

# -----------------------------------------
# Nested Lists (2D Lists)
# -----------------------------------------
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("\n--- 2D List (Matrix) ---")
print(matrix[0])         # [1, 2, 3]
print(matrix[1][1])      # 5

# Looping through nested list
for row in matrix:
    for value in row:
        print(value, end=" ")
    print()

# -----------------------------------------
# List Comprehension
# -----------------------------------------
# A compact way to create or transform lists.

print("\n--- List Comprehension ---")

# Example 1: Create list of squares
squares = [x**2 for x in range(1, 6)]
print("Squares:", squares)

# Example 2: List of even numbers
evens = [x for x in range(10) if x % 2 == 0]
print("Even numbers:", evens)

# Example 3: Convert to uppercase
names = ["priyanshu", "rajput", "python"]
upper_names = [n.upper() for n in names]
print("Uppercase:", upper_names)

# Example 4: Filtering data
ages = [12, 18, 20, 16, 25]
adults = [age for age in ages if age >= 18]
print("Adults:", adults)

# Example 5: Nested comprehension (flatten 2D list)
flat = [num for row in matrix for num in row]
print("Flattened matrix:", flat)

# Example 6: Conditional expression in comprehension
labels = ["Even" if x % 2 == 0 else "Odd" for x in range(1, 6)]
print("Labels:", labels)

# -----------------------------------------
# Copying Lists
# -----------------------------------------
a = [1, 2, 3]
b = a           # Shallow copy (changes affect both)
c = a.copy()    # Deep copy (independent copy)

a.append(4)
print("\nOriginal a:", a)
print("Shallow copy b:", b)
print("Deep copy c:", c)

# -----------------------------------------
# Membership Operator
# -----------------------------------------
print("\n--- Membership Check ---")
print(3 in a)       # True
print(10 not in a)  # True

# -----------------------------------------
# End of Day 20: Lists in Python
# -----------------------------------------
