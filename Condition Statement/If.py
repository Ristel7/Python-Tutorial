# -----------------------------------
# Day 14: if Statement in Python
# -----------------------------------

# The if statement lets Python make decisions.
# Syntax:
# if condition:
#     code block (runs only if condition is True)

# -----------------------------------
# Basic if example
# -----------------------------------

age = 18

if age >= 18:
    print("You are eligible to vote.")

# -----------------------------------
# Using if with variables and expressions
# -----------------------------------

temperature = 30

if temperature > 25:
    print("It's a hot day!")

# -----------------------------------
# Using if with user input
# -----------------------------------

# Note: input() returns string, so convert if comparing numerically
marks = int(input("Enter your marks: "))

if marks >= 50:
    print("You passed the exam!")

# -----------------------------------
# if with Boolean variable
# -----------------------------------

is_raining = True

if is_raining:
    print("Take an umbrella.")

# -----------------------------------
# Multiple if statements
# (All are checked separately)
# -----------------------------------

number = 12

if number > 0:
    print("Positive number")
if number % 2 == 0:
    print("Even number")
if number > 10:
    print("Number greater than 10")

# -----------------------------------
# Nested if statements
# -----------------------------------

age = int(input("\nEnter your age: "))

if age >= 18:
    print("You can enter the club.")
    if age >= 21:
        print("You can also access the VIP section.")
else:
    print("Sorry, you are underage.")

# -----------------------------------
# if with logical operators
# -----------------------------------

income = 40000
credit_score = 720

if income >= 30000 and credit_score >= 700:
    print("\nLoan Approved.")
if income < 30000 or credit_score < 700:
    print("Loan may be rejected or reviewed.")
if not (income < 30000):
    print("Income meets minimum requirement.")

# -----------------------------------
# if used to check membership
# -----------------------------------

fruits = ["apple", "banana", "mango"]

if "apple" in fruits:
    print("\nApple is available in the basket.")

# -----------------------------------
# if with string comparison
# -----------------------------------

username = input("\nEnter your username: ")

if username == "admin":
    print("Welcome, Administrator!")
if username != "admin":
    print("Access limited to basic features.")

# -----------------------------------
# Real-world example 1: Temperature warning
# -----------------------------------

temp = float(input("\nEnter current temperature in °C: "))

if temp >= 40:
    print("Warning: Extreme Heat!")
if temp >= 30 and temp < 40:
    print("It’s a hot day.")
if temp >= 20 and temp < 30:
    print("Weather is pleasant.")
if temp < 20:
    print("It’s a bit cold today.")

# -----------------------------------
# Real-world example 2: Grading system
# -----------------------------------

score = int(input("\nEnter your exam score (0-100): "))

if score >= 90:
    print("Grade: A+")
if score >= 80 and score < 90:
    print("Grade: A")
if score >= 70 and score < 80:
    print("Grade: B")
if score >= 60 and score < 70:
    print("Grade: C")
if score >= 50 and score < 60:
    print("Grade: D")
if score < 50:
    print("Grade: F (Fail)")

# -----------------------------------
# Real-world example 3: Login validation
# -----------------------------------

print("\n--- Login System ---")
stored_username = "Priyanshu"
stored_password = "1234"

user = input("Enter username: ")
pwd = input("Enter password: ")

if user == stored_username and pwd == stored_password:
    print("Login successful ✅")
if user != stored_username or pwd != stored_password:
    print("Invalid credentials ❌")

# -----------------------------------
# Quick Note:
# Every `if` creates a new independent check.
# Next lesson will add `elif` and `else` for better control flow.
# -----------------------------------
