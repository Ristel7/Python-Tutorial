# -----------------------------------
# Day 4: Python Data Types
# -----------------------------------

# In Python, every value has a specific data type.
# Common built-in types include:
# int, float, complex, str, bool, list, tuple, set, dict, NoneType

# Let's explore each one with examples.

# -----------------------------------
# 1. Integer (int)
# -----------------------------------
age = 21
year = 2025
quantity = -10
print("Integer Examples:", age, year, quantity)
print("Type of age:", type(age))

# -----------------------------------
# 2. Float (decimal numbers)
# -----------------------------------
pi = 3.14159
temperature = -4.6
print("\nFloat Examples:", pi, temperature)
print("Type of pi:", type(pi))

# -----------------------------------
# 3. Complex Numbers
# -----------------------------------
z = 2 + 3j
print("\nComplex Number Example:", z)
print("Real part:", z.real)
print("Imaginary part:", z.imag)
print("Type of z:", type(z))

# -----------------------------------
# 4. String (str)
# -----------------------------------
name = "Priyanshu"
message = 'Learning Python step by step!'
print("\nString Examples:", name, message)
print("Type of name:", type(name))

# String indexing and slicing
print("First letter of name:", name[0])
print("First five letters of message:", message[:5])

# -----------------------------------
# 5. Boolean (bool)
# -----------------------------------
is_student = True
is_graduated = False
print("\nBoolean Examples:", is_student, is_graduated)
print("Type of is_student:", type(is_student))

# -----------------------------------
# 6. List
# -----------------------------------
# Lists are ordered, changeable, and allow duplicates.
fruits = ["apple", "banana", "cherry", "banana"]
print("\nList Example:", fruits)
print("Type of fruits:", type(fruits))
print("First fruit:", fruits[0])

# Lists can be updated
fruits[1] = "blueberry"
print("Updated List:", fruits)

# -----------------------------------
# 7. Tuple
# -----------------------------------
# Tuples are ordered and unchangeable (immutable)
coordinates = (10.5, 20.8)
print("\nTuple Example:", coordinates)
print("Type of coordinates:", type(coordinates))
# coordinates[0] = 11.0  # ❌ This will cause an error

# -----------------------------------
# 8. Set
# -----------------------------------
# Sets are unordered, don’t allow duplicates
colors = {"red", "green", "blue", "red"}
print("\nSet Example:", colors)
print("Type of colors:", type(colors))

# Add and remove items
colors.add("yellow")
colors.remove("green")
print("Updated Set:", colors)

# -----------------------------------
# 9. Dictionary (dict)
# -----------------------------------
# Dictionaries store data in key-value pairs
student = {
    "name": "Priyanshu",
    "age": 21,
    "course": "Python",
    "score": 89.5
}
print("\nDictionary Example:", student)
print("Type of student:", type(student))
print("Student Name:", student["name"])
print("Course:", student["course"])

# -----------------------------------
# 10. NoneType
# -----------------------------------
# Represents a null or no value
value = None
print("\nNoneType Example:", value)
print("Type of value:", type(value))

# -----------------------------------
# End of Day 4 Lesson
# -----------------------------------
