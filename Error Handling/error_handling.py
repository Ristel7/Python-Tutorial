# ---------------------------------------------------------
# Day 28: Error Handling in Python
# ---------------------------------------------------------
# Error handling lets your program respond gracefully
# instead of crashing when something unexpected happens.


# ---------------------------------------------------------
# 1. Basic try-except
# ---------------------------------------------------------

print("Basic try-except example:")

try:
    x = int("10")
    print("Converted value:", x)
except ValueError:
    print("Conversion failed")


# ---------------------------------------------------------
# 2. Handling invalid input
# ---------------------------------------------------------

print("\nHandling invalid user input:")

try:
    age = int(input("Enter your age: "))
    print("Your age is:", age)
except ValueError:
    print("Please enter numbers only")


# ---------------------------------------------------------
# 3. Multiple except blocks
# ---------------------------------------------------------

print("\nMultiple except blocks:")

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = a / b
    print("Result:", result)
except ValueError:
    print("Invalid number entered")
except ZeroDivisionError:
    print("Cannot divide by zero")


# ---------------------------------------------------------
# 4. Using else with try-except
# ---------------------------------------------------------
# else runs only if NO exception occurs

print("\nUsing else block:")

try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input")
else:
    print("You entered:", num)


# ---------------------------------------------------------
# 5. finally block
# ---------------------------------------------------------
# finally always runs (error or not)

print("\nUsing finally block:")

try:
    f = open("sample.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("File not found")
finally:
    print("File operation completed")


# ---------------------------------------------------------
# 6. Catching multiple exceptions together
# ---------------------------------------------------------

print("\nCatching multiple exceptions together:")

try:
    value = int(input("Enter a number: "))
    print(10 / value)
except (ValueError, ZeroDivisionError):
    print("Invalid input or division by zero")


# ---------------------------------------------------------
# 7. Using Exception (generic handler)
# ---------------------------------------------------------

print("\nUsing generic exception:")

try:
    data = [1, 2, 3]
    print(data[5])
except Exception as e:
    print("Error occurred:", e)


# ---------------------------------------------------------
# 8. Raising custom exceptions
# ---------------------------------------------------------

print("\nRaising custom exceptions:")

def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient balance")
    return balance - amount

try:
    print("Remaining balance:", withdraw(5000, 6000))
except ValueError as e:
    print("Transaction failed:", e)


# ---------------------------------------------------------
# 9. Custom exception class
# ---------------------------------------------------------

class AgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise AgeError("Age must be 18 or above")

try:
    check_age(16)
except AgeError as e:
    print("Age check failed:", e)


# ---------------------------------------------------------
# 10. Real-world example: Login system
# ---------------------------------------------------------

print("\nLogin system example:")

correct_password = "python123"

try:
    pwd = input("Enter password: ")
    if pwd != correct_password:
        raise PermissionError("Wrong password")
    print("Login successful")
except PermissionError as e:
    print("Access denied:", e)


# ---------------------------------------------------------
# 11. Real-world example: Safe calculator
# ---------------------------------------------------------

print("\nSafe calculator:")

try:
    x = float(input("Enter number 1: "))
    y = float(input("Enter number 2: "))
    print("Result:", x / y)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid numeric input")
else:
    print("Calculation completed successfully")
finally:
    print("Calculator closed")


# ---------------------------------------------------------
# End of Day 28: Error Handling
# ---------------------------------------------------------
