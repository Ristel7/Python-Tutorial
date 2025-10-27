# -----------------------------------
# Day 12: Input() Function in Python
# -----------------------------------

# input() allows the user to enter data from the keyboard.
# It ALWAYS returns a string, so type conversion is often needed.

# -----------------------------------
# Basic usage of input()
# -----------------------------------

name = input("Enter your name: ")
print("Hello,", name)

# -----------------------------------
# Input with number conversion
# -----------------------------------

# Since input returns a string, convert to int/float when needed

age = input("Enter your age: ")
print("Type before conversion:", type(age))
age = int(age)  # converting to integer
print("Type after conversion:", type(age))
print("You will be", age + 1, "years old next year.")

# -----------------------------------
# Taking multiple inputs on the same line
# -----------------------------------

# Example: Input separated by space
x, y = input("Enter two numbers (space separated): ").split()
x = int(x)
y = int(y)
print("\nSum of numbers:", x + y)

# Taking multiple inputs and converting together using map()
a, b, c = map(int, input("Enter three integers: ").split())
print("Multiplication:", a * b * c)

# -----------------------------------
# Input with float numbers
# -----------------------------------

height = float(input("\nEnter your height in meters: "))
print("Height entered:", height)

# -----------------------------------
# Boolean from input
# -----------------------------------

# For boolean input, we must define our own logic
response = input("\nDo you like Python? (yes/no): ").lower()

like_python = response in ["yes", "y"]
print("You like Python:", like_python)

# -----------------------------------
# Using input inside a function
# -----------------------------------

def greet_user():
    username = input("\nWhat is your username? ")
    print("Welcome,", username)

greet_user()

# -----------------------------------
# Practical Example 1: Simple Calculator
# -----------------------------------

print("\n--- Mini Calculator ---")
num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print("Result:", num1 + num2)
elif operator == "-":
    print("Result:", num1 - num2)
elif operator == "*":
    print("Result:", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Cannot divide by zero")
else:
    print("Invalid operator")

# -----------------------------------
# Practical Example 2: Validating numeric input
# -----------------------------------

value = input("\nEnter a number: ")

if value.isdigit():  # checks if all characters are digits
    value = int(value)
    print("Conversion successful:", value, "| Type:", type(value))
else:
    print("Not a valid number.")

# -----------------------------------
# Practical Example 3: Asking Yes/No Multiple Times
# -----------------------------------

while True:
    confirm = input("\nDo you want to exit? (yes/no): ").lower()
    if confirm in ["yes", "y"]:
        print("Exiting program... Goodbye!")
        break
    elif confirm in ["no", "n"]:
        print("Okay! Continue...")
    else:
        print("Invalid choice. Please type yes or no.")

# -----------------------------------
# End of Day 12 Lesson
# -----------------------------------
