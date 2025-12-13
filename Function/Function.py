# -----------------------------------------------------
# Day 24: Functions in Python
# -----------------------------------------------------

print("== Basic Function ==")

def greet():
    print("Hello! Welcome to Python learning.")

greet()


# -----------------------------------------------------
# Function with parameters
# -----------------------------------------------------

print("\n== Function with parameters ==")

def welcome(name):
    print(f"Hello {name}, good to see you learning Python!")

welcome("Priyanshu")
welcome("Riya")


# -----------------------------------------------------
# Function returning a value
# -----------------------------------------------------

print("\n== Function returning values ==")

def add(a, b):
    return a + b

result = add(10, 20)
print("Sum:", result)


# -----------------------------------------------------
# Function with default parameters
# -----------------------------------------------------

print("\n== Function with default parameters ==")

def greet_user(name="Student"):
    print(f"Hi {name}! Keep pushing forward.")

greet_user()
greet_user("Aman")


# -----------------------------------------------------
# Function with multiple return values
# -----------------------------------------------------

print("\n== Multiple return values ==")

def get_stats(a, b):
    return (a + b), (a - b), (a * b)

sum_val, diff, product = get_stats(10, 5)

print("Sum:", sum_val)
print("Difference:", diff)
print("Product:", product)


# -----------------------------------------------------
# Function with variable number of arguments (*args)
# -----------------------------------------------------

print("\n== Variable arguments (*args) ==")

def total(*numbers):
    s = 0
    for n in numbers:
        s += n
    return s

print("Total:", total(1, 2, 3, 4, 5))


# -----------------------------------------------------
# Function with keyword arguments (**kwargs)
# -----------------------------------------------------

print("\n== Keyword arguments (**kwargs) ==")

def info(**details):
    for key, value in details.items():
        print(key, ":", value)

info(name="Priyanshu", city="Bhopal", course="Python")


# -----------------------------------------------------
# Passing list to a function
# -----------------------------------------------------

print("\n== Passing list to a function ==")

def show_items(items):
    for item in items:
        print(item)

show_items(["apple", "banana", "grape"])


# -----------------------------------------------------
# Nested functions
# -----------------------------------------------------

print("\n== Nested functions ==")

def outer():
    print("Inside outer function")

    def inner():
        print("Inside inner function")

    inner()

outer()


# -----------------------------------------------------
# Lambda Functions (anonymous functions)
# -----------------------------------------------------

print("\n== Lambda (one-line function) ==")

square = lambda x: x * x
print("Square of 5 is:", square(5))


# -----------------------------------------------------
# Lambda with map, filter
# -----------------------------------------------------

print("\n== Using lambda with map & filter ==")

nums = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x*x, nums))
evens = list(filter(lambda x: x % 2 == 0, nums))

print("Squared:", squared)
print("Evens:", evens)


# -----------------------------------------------------
# Function with documentation (docstring)
# -----------------------------------------------------

print("\n== Docstring example ==")

def multiply(a, b):
    """
    Returns the product of a and b.
    Useful for basic math operations.
    """
    return a * b

print("Multiply:", multiply(6, 4))
print("Docstring:", multiply.__doc__)


# -----------------------------------------------------
# Real-world Example 1: Calculator function
# -----------------------------------------------------

print("\n== Calculator Function ==")

def calculator(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero."
    else:
        return "Invalid operator."

print("Calc 10 + 5 =", calculator(10, 5, "+"))
print("Calc 10 / 0 =", calculator(10, 0, "/"))


# -----------------------------------------------------
# Real-world Example 2: Checking strong password
# -----------------------------------------------------

print("\n== Password Checker ==")

def is_strong(password):
    if len(password) < 8:
        return False
    if not any(ch.isupper() for ch in password):
        return False
    if not any(ch.islower() for ch in password):
        return False
    if not any(ch.isdigit() for ch in password):
        return False
    return True

print("Strong?", is_strong("Python123"))
print("Strong?", is_strong("weak"))


# -----------------------------------------------------
# End of Day 24: Functions in Python
# -----------------------------------------------------
