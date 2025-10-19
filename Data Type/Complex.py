# -----------------------------------
# Day 7: Complex (complex) Data Type
# -----------------------------------

# In Python, a complex number is written as: a + bj
# where 'a' is the real part and 'b' is the imaginary part.

# -----------------------------------
# Creating Complex Numbers
# -----------------------------------

num1 = 3 + 5j
num2 = 7 - 2j
num3 = complex(2, 4)   # another way to create complex numbers

print("num1:", num1)
print("num2:", num2)
print("num3:", num3)

# Check the type
print("\nType of num1:", type(num1))

# -----------------------------------
# Accessing Real and Imaginary Parts
# -----------------------------------

print("\nReal part of num1:", num1.real)
print("Imaginary part of num1:", num1.imag)

# You can also access these as float values
print("Type of real part:", type(num1.real))
print("Type of imaginary part:", type(num1.imag))

# -----------------------------------
# Arithmetic Operations
# -----------------------------------

print("\nAddition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)

# Note: Floor division // and modulus % are not supported for complex numbers

# -----------------------------------
# Conjugate of a Complex Number
# -----------------------------------

# The conjugate of (a + bj) is (a - bj)
print("\nConjugate of num1:", num1.conjugate())
print("Conjugate of num2:", num2.conjugate())

# -----------------------------------
# Magnitude (Absolute Value)
# -----------------------------------

# Magnitude = sqrt(real^2 + imag^2)
print("\nMagnitude of num1:", abs(num1))
print("Magnitude of num2:", abs(num2))

# -----------------------------------
# Comparison (== and != only)
# -----------------------------------

num4 = 3 + 5j
print("\nnum1 == num4:", num1 == num4)
print("num1 != num2:", num1 != num2)

# -----------------------------------
# Using math and cmath modules
# -----------------------------------
import cmath  # specialized module for complex math

# Square root
z = 16 + 9j
print("\nComplex number z:", z)
print("Square root of z:", cmath.sqrt(z))

# Phase angle (in radians)
print("Phase angle of z:", cmath.phase(z))

# Convert from polar to rectangular form
r = 5
theta = cmath.pi / 4  # 45 degrees
polar_to_rect = cmath.rect(r, theta)
print("Polar to Rectangular (r=5, θ=45°):", polar_to_rect)

# Convert from rectangular to polar form
z2 = 3 + 4j
r, theta = cmath.polar(z2)
print("Rectangular to Polar (3+4j):", (r, theta))

# -----------------------------------
# Practical Example 1: AC Voltage
# -----------------------------------

# Represent AC voltage as a complex number
# V = Vrms∠θ = magnitude * (cosθ + jsinθ)
V1 = cmath.rect(230, cmath.pi / 6)  # 230∠30°
V2 = cmath.rect(230, -cmath.pi / 6) # 230∠-30°

# Adding voltages (as complex numbers)
V_total = V1 + V2
print("\nTotal Voltage (V1 + V2):", V_total)
print("Magnitude of total voltage:", abs(V_total))
print("Phase angle of total voltage:", cmath.phase(V_total))

# -----------------------------------
# Practical Example 2: Quadratic Equation
# -----------------------------------

# Solve x² + 4x + 13 = 0
a = 1
b = 4
c = 13

# Formula: (-b ± sqrt(b² - 4ac)) / 2a
d = cmath.sqrt(b**2 - 4*a*c)
root1 = (-b + d) / (2*a)
root2 = (-b - d) / (2*a)

print("\nRoots of x² + 4x + 13 = 0 are:")
print("Root 1:", root1)
print("Root 2:", root2)

# -----------------------------------
# End of Day 7 Lesson
# -----------------------------------
