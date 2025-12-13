# ---------------------------------------------
# Day 25: Defining Functions in Python
# ---------------------------------------------

# A function is a named block of code that runs only when called.
# It helps avoid repetition and keeps code organized.

# ---------------------------------------------
# 1. Basic function definition
# ---------------------------------------------

def greet():
    print("Hello! This is your first function.")

greet()


# ---------------------------------------------
# 2. Function with one parameter
# ---------------------------------------------

def greet_user(name):
    print("Hello", name)

greet_user("Priyanshu")
greet_user("Riya")


# ---------------------------------------------
# 3. Function with multiple parameters
# ---------------------------------------------

def introduce(name, age, city):
    print("Name:", name)
    print("Age:", age)
    print("City:", city)

introduce("Aman", 22, "Bhopal")


# ---------------------------------------------
# 4. Function returning a value
# ---------------------------------------------

def add_numbers(a, b):
    return a + b

result = add_numbers(10, 20)
print("Result:", result)


# ---------------------------------------------
# 5. Function returning multiple values
# ---------------------------------------------

def calculate(a, b):
    return a + b, a - b, a * b

sum_val, diff, product = calculate(8, 4)

print("Sum:", sum_val)
print("Difference:", diff)
print("Product:", product)


# ---------------------------------------------
# 6. Function with default parameters
# ---------------------------------------------

def welcome(name="Student"):
    print("Welcome", name)

welcome()
welcome("Priyanshu")


# ---------------------------------------------
# 7. Keyword arguments
# ---------------------------------------------

def profile(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)

profile(age=21, name="Priyanshu", course="Python")


# ---------------------------------------------
# 8. Function with *args
# ---------------------------------------------

def total_sum(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total

print("Total:", total_sum(1, 2, 3, 4, 5))


# ---------------------------------------------
# 9. Function with **kwargs
# ---------------------------------------------

def show_details(**info):
    for key, value in info.items():
        print(key, ":", value)

show_details(name="Priyanshu", city="Bhopal", skill="Python")


# ---------------------------------------------
# 10. Function with a docstring
# ---------------------------------------------

def multiply(a, b):
    """
    Returns the multiplication of two numbers.
    """
    return a * b

print("Multiply:", multiply(6, 7))
print("Docstring:", multiply.__doc__)


# ---------------------------------------------
# 11. Nested function definition
# ---------------------------------------------

def outer_function():
    print("Inside outer function")

    def inner_function():
        print("Inside inner function")

    inner_function()

outer_function()


# ---------------------------------------------
# 12. Function calling another function
# ---------------------------------------------

def square(n):
    return n * n

def cube(n):
    return n * n * n

print("Square:", square(4))
print("Cube:", cube(4))


# ---------------------------------------------
# 13. Function returning a function
# ---------------------------------------------

def power_function(power):
    def calculate(n):
        return n ** power
    return calculate

square_func = power_function(2)
cube_func = power_function(3)

print("Square:", square_func(5))
print("Cube:", cube_func(5))


# ---------------------------------------------
# 14. Real-world example: eligibility check
# ---------------------------------------------

def check_eligibility(age):
    if age >= 18:
        return "Eligible"
    return "Not Eligible"

print("Eligibility:", check_eligibility(20))
print("Eligibility:", check_eligibility(16))


# ---------------------------------------------
# End of Day 25: Defining Functions
# ---------------------------------------------
