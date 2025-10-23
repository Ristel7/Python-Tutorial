# -----------------------------------
# Day 11: Type Checking and Type Conversion
# -----------------------------------

# Type checking: Using type() and isinstance()
# Type conversion: Changing one data type to another (int(), float(), str(), etc.)

# -----------------------------------
# TYPE CHECKING
# -----------------------------------

# type() tells you the exact data type of a variable
a = 10
b = 12.5
c = "Python"
d = True
e = None
f = 3 + 4j
g = [1, 2, 3]
h = (10, 20, 30)
i = {"name": "Priyanshu", "age": 21}

print("---- Type Checking using type() ----")
print("Type of a:", type(a))
print("Type of b:", type(b))
print("Type of c:", type(c))
print("Type of d:", type(d))
print("Type of e:", type(e))
print("Type of f:", type(f))
print("Type of g:", type(g))
print("Type of h:", type(h))
print("Type of i:", type(i))

# -----------------------------------
# isinstance() function
# -----------------------------------
# Checks if a variable belongs to a certain class/type
print("\n---- Type Checking using isinstance() ----")
print("Is a an int?", isinstance(a, int))
print("Is b a float?", isinstance(b, float))
print("Is c a str?", isinstance(c, str))
print("Is g a list?", isinstance(g, list))
print("Is f a complex number?", isinstance(f, complex))
print("Is e None?", e is None)
print("Is h a tuple?", isinstance(h, tuple))
print("Is i a dict?", isinstance(i, dict))

# Multiple type check
print("Is a either int or float?", isinstance(a, (int, float)))

# -----------------------------------
# TYPE CONVERSION (TYPE CASTING)
# -----------------------------------

# Converting one type into another using constructor functions
# int(), float(), str(), complex(), bool(), list(), tuple(), set(), dict()

print("\n---- Type Conversion Examples ----")

# Numeric conversions
x = 5
y = 3.8
z = "25"

print("int to float:", float(x))   # 5 → 5.0
print("float to int:", int(y))     # 3.8 → 3
print("string to int:", int(z))    # "25" → 25
print("int to string:", str(x))    # 5 → "5"
print("int to complex:", complex(x))  # 5 → (5+0j)

# -----------------------------------
# Converting between collections
# -----------------------------------
numbers = [1, 2, 3, 4]
tuple_data = (5, 6, 7)
set_data = {8, 9, 10}

print("\nList to tuple:", tuple(numbers))
print("Tuple to list:", list(tuple_data))
print("List to set (removes duplicates):", set([1, 2, 2, 3, 4]))

# -----------------------------------
# String conversions
# -----------------------------------
string_num = "12.75"
converted_float = float(string_num)
print("\nString to float:", converted_float)
print("Float back to string:", str(converted_float))

# -----------------------------------
# Boolean conversions
# -----------------------------------
# bool() returns False for 0, 0.0, '', [], {}, None — everything else is True
print("\nBoolean conversions:")
print("bool(0):", bool(0))
print("bool(5):", bool(5))
print("bool(''):", bool(''))
print("bool('Python'):", bool("Python"))
print("bool([]):", bool([]))
print("bool([1,2]):", bool([1, 2]))
print("bool(None):", bool(None))

# -----------------------------------
# Converting user input (string → number)
# -----------------------------------
# Example: Simulating user input (normally input() gives string)
user_input = "42"
print("\nConverting user input string to integer:")
converted_value = int(user_input)
print("Original:", user_input, "Type:", type(user_input))
print("Converted:", converted_value, "Type:", type(converted_value))

# -----------------------------------
# Practical Example 1: Summing numeric strings
# -----------------------------------
num1 = "10"
num2 = "20"
sum_result = int(num1) + int(num2)
print("\nSum of two numeric strings:", sum_result)

# -----------------------------------
# Practical Example 2: Handling conversion errors
# -----------------------------------
print("\nHandling invalid conversions with try-except:")

value = "abc"
try:
    number = int(value)
    print("Conversion successful:", number)
except ValueError:
    print("Error: Cannot convert 'abc' to integer")

# -----------------------------------
# Practical Example 3: Dynamic type check
# -----------------------------------
def describe_value(value):
    print(f"\nValue: {value} | Type: {type(value).__name__}")
    if isinstance(value, (int, float, complex)):
        print("→ This is a number.")
    elif isinstance(value, str):
        print("→ This is text/string data.")
    elif isinstance(value, list):
        print("→ This is a list (collection of items).")
    elif value is None:
        print("→ This represents nothing (NoneType).")
    else:
        print("→ This is some other data type.")

describe_value(123)
describe_value("Python")
describe_value([1, 2, 3])
describe_value(None)

# -----------------------------------
# End of Day 11 Lesson
# -----------------------------------
