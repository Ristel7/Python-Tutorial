# -----------------------------------
# Day 18: Shorthand If Statement in Python
# -----------------------------------

# A shorthand 'if' is used when there's only one statement to execute inside the if block.
# It allows writing an if condition in a single line for simplicity.

# Syntax:
# if condition: statement

# Example 1: Simple shorthand if
num = 10
if num > 5: print("Number is greater than 5")

# Output: Number is greater than 5


# -----------------------------------
# Example 2: Checking if a number is positive
x = 7
if x > 0: print("Positive number")

# Output: Positive number


# -----------------------------------
# Example 3: Checking for even number
number = 8
if number % 2 == 0: print(f"{number} is even")

# Output: 8 is even


# -----------------------------------
# Example 4: Inline if-else (Ternary Operator)
# Python allows if-else in one line — also called a conditional expression.

# Syntax:
# value_if_true if condition else value_if_false

age = 18
status = "Adult" if age >= 18 else "Minor"
print(status)
# Output: Adult


# -----------------------------------
# Example 5: Inline condition for comparison
a = 10
b = 20
print("a is greater") if a > b else print("b is greater")

# Output: b is greater


# -----------------------------------
# Example 6: Inline condition with equal values
a = 5
b = 5
print("Equal") if a == b else print("Not Equal")

# Output: Equal


# -----------------------------------
# Example 7: Multiple conditions in shorthand
marks = 85
print("Excellent") if marks >= 90 else print("Good") if marks >= 70 else print("Needs Improvement")

# Output: Good


# -----------------------------------
# Example 8: Checking even/odd using shorthand
num = int(input("Enter a number: "))
print("Even") if num % 2 == 0 else print("Odd")

# Output: Depends on user input


# -----------------------------------
# Example 9: Simple login check
username = input("Enter username: ")
print("Welcome, Admin!") if username == "admin" else print("Access Denied")

# Output:
# Enter username: admin
# Welcome, Admin!


# -----------------------------------
# Example 10: Using shorthand with logical operators
temperature = 38
print("Fever detected!") if temperature >= 37 else print("Normal temperature")

# Output: Fever detected!


# -----------------------------------
# Example 11: Nested shorthand if-else (chained)
score = 92
print("Excellent") if score > 90 else print("Good") if score > 75 else print("Average")

# Output: Excellent


# -----------------------------------
# Example 12: Compact check for multiple inputs
is_raining = True
has_umbrella = False

print("Go outside") if not is_raining else print("Take umbrella") if has_umbrella else print("Stay inside")

# Output: Stay inside


# -----------------------------------
# Example 13: Checking string condition
city = "Delhi"
print("Capital city") if city.lower() == "delhi" else print("Other city")

# Output: Capital city


# -----------------------------------
# Example 14: Checking list length
fruits = ["apple", "banana"]
print("List has items") if len(fruits) > 0 else print("List is empty")

# Output: List has items


# -----------------------------------
# Example 15: Shorthand if with f-string formatting
age = 25
print(f"You are {'an adult' if age >= 18 else 'a minor'}.")

# Output: You are an adult.


# -----------------------------------
# Summary:
# Shorthand if statements are perfect for concise decisions.
# They improve readability when your condition and result are short.
# But for complex logic, always prefer standard if-elif-else blocks.
# -----------------------------------
