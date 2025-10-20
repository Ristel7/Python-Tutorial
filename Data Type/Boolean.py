# -----------------------------------
# Day 8: Boolean (bool) Data Type
# -----------------------------------

# The Boolean data type represents only two values: True or False.
# Used mainly in conditional statements and logical operations.

# -----------------------------------
# Declaring Boolean Variables
# -----------------------------------
is_active = True
is_logged_in = False

print("is_active:", is_active)
print("is_logged_in:", is_logged_in)
print("Type of is_active:", type(is_active))

# -----------------------------------
# Boolean as a Result of Comparison
# -----------------------------------
a = 10
b = 7

print("\nComparisons:")
print("a > b:", a > b)
print("a < b:", a < b)
print("a == b:", a == b)
print("a != b:", a != b)
print("a >= 10:", a >= 10)
print("b <= 5:", b <= 5)

# -----------------------------------
# Boolean and Arithmetic
# -----------------------------------
# In Python, True behaves like 1 and False behaves like 0 in math operations.
print("\nArithmetic with Boolean values:")
print("True + True =", True + True)    # 1 + 1 = 2
print("True + False =", True + False)  # 1 + 0 = 1
print("False * 5 =", False * 5)        # 0 * 5 = 0
print("True * 10 =", True * 10)        # 1 * 10 = 10

# -----------------------------------
# Logical Operators
# -----------------------------------
# and, or, not

x = True
y = False

print("\nLogical Operations:")
print("x and y =", x and y)   # True if both are True
print("x or y =", x or y)     # True if at least one is True
print("not x =", not x)       # Inverts True to False
print("not y =", not y)       # Inverts False to True

# -----------------------------------
# Using bool() Constructor
# -----------------------------------
# The bool() function converts values to Boolean.
# It returns False for these: 0, 0.0, '', [], {}, None
# Everything else is True

print("\nType Conversion using bool():")
print("bool(10):", bool(10))
print("bool(0):", bool(0))
print("bool('Python'):", bool("Python"))
print("bool(''):", bool(""))
print("bool([]):", bool([]))
print("bool([1,2,3]):", bool([1, 2, 3]))
print("bool(None):", bool(None))

# -----------------------------------
# Conditional Statements
# -----------------------------------
print("\nConditional Example:")

is_student = True
has_paid_fee = False

if is_student and has_paid_fee:
    print("Access Granted: Welcome Student!")
elif is_student and not has_paid_fee:
    print("Fee pending. Please complete payment.")
else:
    print("Not a student. Access Denied.")

# -----------------------------------
# Practical Examples
# -----------------------------------

# Example 1: Checking if a number is even
num = 6
is_even = (num % 2 == 0)
print("\nIs", num, "even?", is_even)

# Example 2: Login validation
username = "admin"
password = "1234"
is_authenticated = (username == "admin" and password == "1234")
print("Login Successful?", is_authenticated)

# Example 3: Using bool in filtering
data = [0, "", 25, "Hello", [], None, True]
filtered_data = [item for item in data if bool(item)]
print("Filtered (truthy) data:", filtered_data)

# Example 4: Boolean as switches
is_dark_mode = True
print("\nDark Mode is", "Enabled" if is_dark_mode else "Disabled")

# -----------------------------------
# End of Day 8 Lesson
# -----------------------------------
