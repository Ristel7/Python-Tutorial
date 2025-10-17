# -----------------------------------
# Day 5: Integer (int) Data Type
# -----------------------------------

# In Python, an integer (int) is a whole number — positive, negative, or zero.
# It does NOT contain decimals.

# Example: Declaring integers
num1 = 10
num2 = -25
num3 = 0

print("num1:", num1)
print("num2:", num2)
print("num3:", num3)

# Check the data type
print("Type of num1:", type(num1))
print("Type of num2:", type(num2))
print("Type of num3:", type(num3))

# -----------------------------------
# Arithmetic operations with integers
# -----------------------------------
a = 15
b = 4

print("\nAddition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division (float result):", a / b)
print("Floor Division (integer result):", a // b)
print("Modulus (remainder):", a % b)
print("Exponent (power):", a ** b)

# -----------------------------------
# Type conversion (Casting)
# -----------------------------------
# You can convert other data types into int using the int() function.

x = "50"
y = 12.7
z = True

print("\nType before conversion:", type(x), type(y), type(z))

x = int(x)     # converts string "50" to integer 50
y = int(y)     # converts float 12.7 to integer 12 (truncates decimals)
z = int(z)     # converts True to 1, False would become 0

print("After conversion:", x, y, z)
print("Types after conversion:", type(x), type(y), type(z))

# -----------------------------------
# Integer comparison operators
# -----------------------------------
p = 20
q = 15

print("\nComparison Results:")
print("p == q:", p == q)
print("p != q:", p != q)
print("p > q:", p > q)
print("p < q:", p < q)
print("p >= q:", p >= q)
print("p <= q:", p <= q)

# -----------------------------------
# Using int() for user input (optional interactive part)
# -----------------------------------
# Uncomment to try in terminal
# num = int(input("\nEnter a number: "))
# print("You entered:", num, "and its type is:", type(num))

# -----------------------------------
# Working with big integers
# -----------------------------------
# Python automatically handles large integers — no size limit like in other languages.
big_number = 999999999999999999999999999999999999999
print("\nBig Integer Example:", big_number)
print("Type of big_number:", type(big_number))

# -----------------------------------
# Practical Example: Calculate area of rectangle
# -----------------------------------
length = 12
width = 8
area = length * width
print("\nArea of rectangle =", area)

# -----------------------------------
# Practical Example: Convert days to hours
# -----------------------------------
days = 5
hours = days * 24
print("Total hours in", days, "days =", hours)

