# -----------------------------------------
# Day 22: Sets and Frozensets in Python
# -----------------------------------------

# A set is a collection of unique elements.
# It doesn’t keep order, and it automatically removes duplicates.

# -----------------------------------------
# Creating Sets
# -----------------------------------------
numbers = {1, 2, 3, 4, 5}
mixed = {1, "Python", 3.14, True}
duplicates = {1, 2, 2, 3, 3, 3}

print("Numbers:", numbers)
print("Mixed:", mixed)
print("Duplicates removed:", duplicates)

# Creating an empty set
empty_set = set()
print("Empty set:", empty_set)

# You can also create a set from a list
from_list = set([1, 2, 3, 3, 4])
print("Set from list:", from_list)

# -----------------------------------------
# Adding and Removing Elements
# -----------------------------------------
fruits = {"apple", "banana"}

fruits.add("cherry")
print("\nAfter add:", fruits)

# update() adds multiple elements
fruits.update(["mango", "grape"])
print("After update:", fruits)

# remove() deletes an element; throws error if missing
fruits.remove("banana")
print("After remove:", fruits)

# discard() deletes but never throws error
fruits.discard("papaya")  # No error even if item doesn’t exist

# pop() removes a random element
removed = fruits.pop()
print("After pop:", fruits)
print("Removed:", removed)

# clear() empties the set
temp = {1, 2, 3}
temp.clear()
print("After clear:", temp)

# -----------------------------------------
# Set Operations
# -----------------------------------------
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("\nSet A:", a)
print("Set B:", b)

# Union: elements from both sets
print("Union:", a | b)
print("Union (method):", a.union(b))

# Intersection: common elements
print("Intersection:", a & b)
print("Intersection (method):", a.intersection(b))

# Difference: elements in A but not B
print("A - B:", a - b)
print("Difference:", a.difference(b))

# Symmetric Difference: elements NOT common
print("Symmetric Difference:", a ^ b)
print("Symmetric Difference method:", a.symmetric_difference(b))

# -----------------------------------------
# Set Membership
# -----------------------------------------
print("\nCheck 3 in A:", 3 in a)
print("Check 10 not in B:", 10 not in b)

# -----------------------------------------
# Looping Through a Set
# -----------------------------------------
colors = {"red", "green", "blue"}
for color in colors:
    print("Color:", color)

# -----------------------------------------
# Frozen Sets
# -----------------------------------------

# A frozenset is just like a set, but completely immutable.
# Once you create it, you can't add or remove anything.

normal_set = {1, 2, 3}
frozen = frozenset([1, 2, 3, 3, 4])

print("\nNormal Set:", normal_set)
print("Frozen Set:", frozen)

# normal_set.add(4)   # This works
# frozen.add(4)       # ❌ This will fail (frozensets cannot be modified)

# You CAN still perform set operations with frozensets
a = frozenset([1, 2, 3])
b = frozenset([3, 4, 5])

print("\nFrozen Union:", a | b)
print("Frozen Intersection:", a & b)
print("Frozen Symmetric Difference:", a ^ b)

# -----------------------------------------
# Frozenset as Dictionary Keys
# -----------------------------------------
# Since frozensets are immutable, they can be used as keys.

data = {
    frozenset(["python", "coding"]): "Skill Set",
    frozenset([1, 2]): "Numbers"
}

print("\nDictionary with frozenset keys:")
for key, value in data.items():
    print(key, "→", value)

# -----------------------------------------
# Real-world Example: Removing Duplicates
# -----------------------------------------
raw_data = ["apple", "apple", "banana", "orange", "banana"]
unique_data = list(set(raw_data))

print("\nRaw list:", raw_data)
print("Unique list:", unique_data)

# -----------------------------------------
# Real-world Example: Set Operations for Data Filtering
# -----------------------------------------
users_day1 = {"Priyanshu", "Anita", "Rahul", "Sneha"}
users_day2 = {"Anita", "Rohan", "Sneha"}

print("\nUsers on both days:", users_day1 & users_day2)
print("Only Day 1:", users_day1 - users_day2)
print("Only Day 2:", users_day2 - users_day1)
print("Visited any day:", users_day1 | users_day2)

# -----------------------------------------
# End of Day 22: Sets and Frozensets
# -----------------------------------------
