# -----------------------------------------
# Day 21: Tuples in Python
# -----------------------------------------

# Think of tuples as “read-only lists”.
# They’re ordered, allow duplicates, and you can mix data types inside them.

# Creating tuples
numbers = (1, 2, 3, 4, 5)
fruits = ("apple", "banana", "cherry")
mixed = (1, "Python", 3.14, True)
single = ("hello",)  # A single-element tuple must have a comma

print("Numbers:", numbers)
print("Fruits:", fruits)
print("Mixed:", mixed)
print("Single:", single)

# Tuples can be created without parentheses too (tuple packing)
coords = 10, 20, 30
print("\nPacked tuple:", coords)

# Accessing elements (just like lists)
print("\nFirst fruit:", fruits[0])
print("Last number:", numbers[-1])
print("Slice of numbers:", numbers[1:4])

# Trying to modify a tuple will cause an error
# numbers[0] = 100  # ❌ TypeError

# But you can convert it to a list, modify, then convert back
temp = list(numbers)
temp[0] = 100
numbers = tuple(temp)
print("\nModified tuple:", numbers)

# -----------------------------------------
# Tuple Methods
# -----------------------------------------
data = (10, 20, 10, 30, 10)
print("\nCount of 10:", data.count(10))
print("Index of 30:", data.index(30))

# -----------------------------------------
# Tuple Unpacking
# -----------------------------------------
# You can unpack tuples directly into variables.
person = ("Priyanshu", 21, "India")
name, age, country = person
print(f"\nName: {name}, Age: {age}, Country: {country}")

# You can also use * to grab multiple values
nums = (1, 2, 3, 4, 5)
first, *middle, last = nums
print("First:", first)
print("Middle:", middle)
print("Last:", last)

# -----------------------------------------
# Tuples in Loops
# -----------------------------------------
cities = ("Delhi", "Bhopal", "Mumbai")
for city in cities:
    print("City:", city)

# Nested tuples
nested = ((1, 2), (3, 4), (5, 6))
for x, y in nested:
    print(f"X: {x}, Y: {y}")

# -----------------------------------------
# Tuples as Dictionary Keys
# -----------------------------------------
# Tuples are hashable (since they’re immutable), which means they can be used as keys in dictionaries.
locations = {
    (28.6139, 77.2090): "Delhi",
    (19.0760, 72.8777): "Mumbai",
    (23.2599, 77.4126): "Bhopal"
}
print("\nDictionary using tuples as keys:")
for coords, city in locations.items():
    print(f"Coordinates {coords} → {city}")

# -----------------------------------------
# Tuple Operations
# -----------------------------------------
nums1 = (1, 2, 3)
nums2 = (4, 5, 6)
combined = nums1 + nums2
repeated = nums1 * 2

print("\nCombined:", combined)
print("Repeated:", repeated)
print("Length:", len(combined))
print("Check 3 in nums1:", 3 in nums1)

# -----------------------------------------
# Tuple vs List
# -----------------------------------------
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)

print("\nList memory:", my_list.__sizeof__())
print("Tuple memory:", my_tuple.__sizeof__())
print("Lists are mutable, Tuples are not.")

# -----------------------------------------
# Real-world Examples
# -----------------------------------------

# Example 1: Returning multiple values from a function
def get_student_info():
    return ("Priyanshu", "Data Science", 2025)

student = get_student_info()
print("\nStudent Info:", student)

# Example 2: Storing fixed data like coordinates
points = [(10, 20), (30, 40), (50, 60)]
for x, y in points:
    print(f"Point X={x}, Y={y}")

# Example 3: Sorting with tuples
students = [("Priyanshu", 21), ("Ravi", 20), ("Anjali", 22)]
sorted_students = sorted(students, key=lambda s: s[1])
print("\nStudents sorted by age:", sorted_students)

# -----------------------------------------
# End of Day 21: Tuples in Python
# -----------------------------------------
