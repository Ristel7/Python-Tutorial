# -----------------------------------
# Day 15: if-elif in Python
# -----------------------------------

# The if-elif structure is used when we have multiple conditions,
# but we don’t necessarily need a default (else) case.

# Syntax:
# if condition1:
#     block1
# elif condition2:
#     block2
# elif condition3:
#     block3
# (and so on...)

# -----------------------------------
# Basic Example
# -----------------------------------

num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num == 0:
    print("Number is zero")
elif num < 0:
    print("Negative number")

# Only one of these blocks will run — the first one that’s True.

# -----------------------------------
# Grading system without else
# -----------------------------------

marks = int(input("\nEnter your marks: "))

if marks >= 90:
    print("Outstanding Performance")
elif marks >= 75:
    print("Very Good")
elif marks >= 60:
    print("Good")
elif marks >= 50:
    print("Pass")
elif marks < 50:
    print("Fail")

# Notice: We don’t need `else` — the last elif acts like a catch for <50.

# -----------------------------------
# Weather condition example
# -----------------------------------

temp = float(input("\nEnter temperature (°C): "))

if temp >= 40:
    print("Extremely Hot")
elif temp >= 30:
    print("Hot Day")
elif temp >= 20:
    print("Pleasant Weather")
elif temp >= 10:
    print("Cool Day")
elif temp < 10:
    print("Cold Weather")

# -----------------------------------
# if-elif with strings
# -----------------------------------

day = input("\nEnter day name: ").lower()

if day == "monday":
    print("Back to work!")
elif day == "friday":
    print("Almost the weekend!")
elif day == "saturday":
    print("Weekend starts now!")
elif day == "sunday":
    print("Rest and recharge!")

# -----------------------------------
# if-elif with logical operators
# -----------------------------------

age = int(input("\nEnter your age: "))

if age >= 0 and age <= 12:
    print("Child")
elif age >= 13 and age <= 19:
    print("Teenager")
elif age >= 20 and age <= 59:
    print("Adult")
elif age >= 60:
    print("Senior Citizen")

# -----------------------------------
# if-elif used in menu selection
# -----------------------------------

print("\n--- Simple Calculator ---")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Result:", a + b)
elif choice == 2:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Result:", a - b)
elif choice == 3:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Result:", a * b)
elif choice == 4:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero!")

# -----------------------------------
# Real-world example: Speed warning system
# -----------------------------------

speed = int(input("\nEnter your car speed (km/h): "))

if speed <= 60:
    print("Safe driving.")
elif speed > 60 and speed <= 100:
    print("Caution: Maintain control.")
elif speed > 100 and speed <= 120:
    print("Warning: You’re overspeeding!")
elif speed > 120:
    print("Danger! Reduce speed immediately!")

# -----------------------------------
# End of Day 15 (if-elif only)
# -----------------------------------
