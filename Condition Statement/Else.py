# -----------------------------------
# Day 16: else Statement in Python
# -----------------------------------

# The else statement runs when all if and elif conditions are False.
# It acts as a "default" or "catch-all" block.

# Syntax:
# if condition1:
#     block1
# elif condition2:
#     block2
# else:
#     default block

# -----------------------------------
# Basic Example
# -----------------------------------

num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Number is zero")

# -----------------------------------
# Using else for default outcomes
# -----------------------------------

age = int(input("\nEnter your age: "))

if age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
elif age < 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

# -----------------------------------
# else used in grading logic
# -----------------------------------

marks = int(input("\nEnter your marks (0-100): "))

if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 50:
    print("Grade: D")
else:
    print("Fail - Better luck next time.")

# -----------------------------------
# else in login validation
# -----------------------------------

print("\n--- Login System ---")
username = input("Enter username: ")
password = input("Enter password: ")

if username == "Priyanshu" and password == "1234":
    print("Login successful ✅")
else:
    print("Invalid username or password ❌")

# -----------------------------------
# else used in number checks
# -----------------------------------

number = int(input("\nEnter a number: "))

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# -----------------------------------
# else with logical operators
# -----------------------------------

income = float(input("\nEnter your annual income: "))

if income >= 1000000:
    print("Tax Rate: 30%")
elif income >= 500000:
    print("Tax Rate: 20%")
elif income >= 250000:
    print("Tax Rate: 10%")
else:
    print("No tax applicable")

# -----------------------------------
# else for menu selection fallback
# -----------------------------------

print("\n--- Simple Menu ---")
print("1. View Profile")
print("2. Edit Profile")
print("3. Logout")

choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    print("Displaying profile...")
elif choice == 2:
    print("Editing profile...")
elif choice == 3:
    print("Logging out...")
else:
    print("Invalid option selected!")

# -----------------------------------
# else inside nested if
# -----------------------------------

print("\n--- Student Result System ---")
marks = int(input("Enter marks: "))

if marks >= 50:
    print("You passed.")
    if marks >= 90:
        print("Outstanding performance!")
    elif marks >= 75:
        print("Great job!")
    else:
        print("Good effort.")
else:
    print("You failed. Please try again next time.")

# -----------------------------------
# Real-world example: ATM withdrawal
# -----------------------------------

print("\n--- ATM Simulation ---")
balance = 5000
withdraw = int(input("Enter withdrawal amount: "))

if withdraw <= balance:
    print("Transaction successful. Remaining balance:", balance - withdraw)
else:
    print("Insufficient balance. Transaction declined.")

# -----------------------------------
# End of Day 16 Lesson
# -----------------------------------
