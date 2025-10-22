# -----------------------------------
# Day 10: NoneType Data Type
# -----------------------------------

# In Python, NoneType is a special data type that has only one value — None.
# It represents the absence of a value or a null value.
# Example use cases:
# - Default values in variables or functions
# - Indicating missing or optional data
# - Resetting a variable’s value

# -----------------------------------
# Declaring NoneType
# -----------------------------------

a = None
print("Value of a:", a)
print("Type of a:", type(a))

# -----------------------------------
# Comparison with None
# -----------------------------------

# None is a singleton in Python — only one instance exists in memory.
# So we always compare using 'is' or 'is not', not '=='.

b = None
print("\nChecking identity:")
print("a is None:", a is None)
print("b is None:", b is None)
print("a == None (not preferred):", a == None)

# -----------------------------------
# None in Conditional Statements
# -----------------------------------

# None is treated as False in a boolean context
if a:
    print("\nVariable a has a value")
else:
    print("\nVariable a is None or considered False")

# -----------------------------------
# Functions Returning None
# -----------------------------------

def greet(name):
    print(f"Hello, {name}!")

result = greet("Priyanshu")
print("\nResult of greet function:", result)
print("Type of result:", type(result))

# The function doesn't return anything, so Python automatically returns None.

# -----------------------------------
# None as Default Argument
# -----------------------------------

def connect_to_db(db_name=None):
    if db_name is None:
        print("⚠️ No database name provided. Using default 'test_db'.")
    else:
        print(f"Connected to database: {db_name}")

print("\nUsing None as default argument:")
connect_to_db()
connect_to_db("Students_DB")

# -----------------------------------
# None in Lists or Dictionaries
# -----------------------------------

data = [12, 45, None, 78, None, 100]
print("\nList with None values:", data)

# Removing None values from a list
filtered_data = [x for x in data if x is not None]
print("Filtered list (without None):", filtered_data)

# Using None to represent missing dictionary data
student = {
    "name": "Priyanshu",
    "age": 21,
    "email": None  # email is missing
}

print("\nStudent dictionary:", student)
if student["email"] is None:
    print("Email not provided by the student.")

# -----------------------------------
# Assigning and Resetting Variables to None
# -----------------------------------

value = 100
print("\nBefore reset:", value)
value = None
print("After reset:", value)

# -----------------------------------
# Checking for None in Functions
# -----------------------------------

def safe_divide(a, b):
    if b == 0:
        return None
    return a / b

print("\nSafe divide function:")
print("10 / 2 =", safe_divide(10, 2))
print("10 / 0 =", safe_divide(10, 0))

result = safe_divide(10, 0)
if result is None:
    print("Division failed due to zero denominator.")

# -----------------------------------
# None vs. Empty Values
# -----------------------------------

# None is not the same as 0, False, or empty string/list/dict
print("\nDifference between None and empty values:")
print("None == 0:", None == 0)
print("None == False:", None == False)
print("None == '':", None == "")
print("bool(None):", bool(None))
print("bool(''):", bool(''))
print("bool([]):", bool([]))
print("bool(0):", bool(0))

# -----------------------------------
# Practical Use: Optional Function Return
# -----------------------------------

def find_item(items, target):
    for item in items:
        if item == target:
            return item
    return None  # Item not found

items = ["apple", "banana", "cherry"]
print("\nFinding items:")
print("Search 'banana' →", find_item(items, "banana"))
print("Search 'grapes' →", find_item(items, "grapes"))

# -----------------------------------
# End of Day 10 Lesson
# -----------------------------------
