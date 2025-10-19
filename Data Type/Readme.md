# Day 4: Data Types in Python

This folder contains my Day 4 Python practice file — `Data_Types.py`.  
In this lesson, I explored all the **built-in data types** in Python and learned how to use them in real examples.

## 🧠 Topics Covered
- Integers (`int`)
- Floating-point numbers (`float`)
- Complex numbers (`complex`)
- Strings (`str`)
- Booleans (`bool`)
- Lists (`list`)
- Tuples (`tuple`)
- Sets (`set`)
- Dictionaries (`dict`)
- NoneType (`None`)

# Integer
age = 21

# Float
pi = 3.14159

# String
name = "Priyanshu"

# Boolean
is_student = True

# List
fruits = ["apple", "banana", "cherry"]

# Tuple
coordinates = (10.5, 20.8)

# Set
colors = {"red", "green", "blue"}

# Dictionary
student = {"name": "Priyanshu", "age": 21, "course": "Python"}

# NoneType
value = None


# Day 5: Integer (int) Data Type in Python

This folder contains my Day 5 Python practice file — `Int_DataType.py`.  
In this lesson, I learned everything about the **integer (`int`) data type** in Python, including how to use it, perform operations, convert between types, and apply it in real examples.

---

## 🧠 Topics Covered

- What is an integer (`int`) in Python  
- Declaring and printing integer values  
- Arithmetic operations  
  - Addition `+`  
  - Subtraction `-`  
  - Multiplication `*`  
  - Division `/`  
  - Floor Division `//`  
  - Modulus `%`  
  - Exponent `**`  
- Type conversion using `int()`  
- Integer comparisons (`==`, `!=`, `>`, `<`, `>=`, `<=`)  
- Working with very large integers  
- Real-world examples using integers  

---

## 💡 Example Snippet

```python
a = 15
b = 4

print("Addition:", a + b)
print("Floor Division:", a // b)
print("Modulus:", a % b)

x = "50"
y = 12.7
print("Converted:", int(x), int(y))


# Day 6: Float (float) Data Type in Python

This folder contains my Day 6 Python practice file — `Float_DataType.py`.  
In this lesson, I explored how Python handles **floating-point numbers (decimal values)** and how to perform arithmetic, conversions, rounding, and formatting operations with them.


##  Topics Covered

- What is a float in Python  
- Declaring and printing float variables  
- Arithmetic operations  
  - Addition `+`  
  - Subtraction `-`  
  - Multiplication `*`  
  - Division `/`  
  - Floor Division `//`  
  - Modulus `%`  
  - Exponent `**`  
- Type conversion to float using `float()`  
- Rounding and formatting float values  
- Float precision and accuracy issues  
- Comparison of float values  
- Real-world examples with floats  


# Day 7: Complex (complex) Data Type in Python

This folder contains my Day 7 Python practice file — `Complex_DataType.py`.  
In this lesson, I explored how Python handles **complex numbers**, how to perform arithmetic and mathematical operations on them, and how to use the `cmath` module for advanced calculations.

---

## 🧠 Topics Covered

- What is a complex number in Python  
- Creating complex numbers  
  - Using literals (`a + bj`)  
  - Using the `complex()` constructor  
- Accessing real and imaginary parts  
- Arithmetic operations on complex numbers  
- Conjugate and magnitude (`abs()`)  
- Comparison (`==`, `!=`)  
- Using the `cmath` module for:  
  - Square roots of complex numbers  
  - Phase angle (argument)  
  - Polar and rectangular conversions  
- Real-world examples  
  - Electrical voltage representation  
  - Solving quadratic equations with complex roots  

---

## 💡 Example Snippet

```python
num1 = 3 + 5j
num2 = 7 - 2j

print("Addition:", num1 + num2)
print("Conjugate of num1:", num1.conjugate())

import cmath
z = 16 + 9j
print("Square root of z:", cmath.sqrt(z))

# Solving a quadratic equation: x² + 4x + 13 = 0
a, b, c = 1, 4, 13
d = cmath.sqrt(b**2 - 4*a*c)
root1 = (-b + d) / (2*a)
root2 = (-b - d) / (2*a)
print("Roots:", root1, root2)
