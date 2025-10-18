# -----------------------------------
# Day 6: Float (Floating Point) Data Type
# -----------------------------------

# A float represents real numbers (numbers with decimal points).
# Example: 3.14, -7.5, 0.0

# Declaring float variables
num1 = 3.14
num2 = -7.5
num3 = 0.0

print("num1:", num1)
print("num2:", num2)
print("num3:", num3)

# Check type
print("Type of num1:", type(num1))

# -----------------------------------
# Arithmetic operations with floats
# -----------------------------------
a = 5.5
b = 2.0

print("\nAddition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus (remainder):", a % b)
print("Exponent (power):", a ** b)

# -----------------------------------
# Type Conversion (Casting)
# -----------------------------------
x = 10       # int
y = "25.8"   # str
z = True     # bool

print("\nBefore conversion:", type(x), type(y), type(z))

# Convert to float
x = float(x)
y = float(y)
z = float(z)

print("After conversion:", x, y, z)
print("Types after conversion:", type(x), type(y), type(z))

# -----------------------------------
# Rounding and Formatting Floats
# -----------------------------------
value = 10 / 3
print("\nOriginal Value:", value)
print("Rounded (2 decimal places):", round(value, 2))
print("Rounded (3 decimal places):", round(value, 3))

# Format method
print("Formatted using format(): {:.2f}".format(value))
print(f"Formatted using f-string: {value:.4f}")

# -----------------------------------
# Float precision issue
# -----------------------------------
# Due to how computers store decimals, some float results are not exact.
result = 0.1 + 0.2
print("\n0.1 + 0.2 =", result)  # You might expect 0.3, but get 0.30000000000000004

# Use round() to fix display
print("Rounded result:", round(result, 2))

# -----------------------------------
# Comparison with floats
# -----------------------------------
a = 0.1 + 0.2
b = 0.3
print("\nAre a and b equal (without rounding)?", a == b)
print("Are they equal (after rounding)?", round(a, 2) == round(b, 2))

# -----------------------------------
# Practical Examples
# -----------------------------------

# 1. Calculate average of 3 marks
mark1 = 89.5
mark2 = 76.25
mark3 = 92.75
average = (mark1 + mark2 + mark3) / 3
print("\nAverage Marks:", round(average, 2))

# 2. Convert Celsius to Fahrenheit
celsius = 36.6
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

# 3. Calculate total cost
item_price = 499.99
tax_rate = 0.18
total_price = item_price + (item_price * tax_rate)
print("Total Price (with tax):", round(total_price, 2))

# -----------------------------------
# End of Day 6 Lesson
# -----------------------------------
