# -----------------------------------
# Day 13: Operators in Python
# -----------------------------------

# Operators are special symbols that perform actions on values or variables.

# Types of Operators:
# 1. Arithmetic Operators
# 2. Assignment Operators
# 3. Comparison Operators
# 4. Logical Operators
# 5. Identity Operators
# 6. Membership Operators
# 7. Bitwise Operators

# Let's explore each of them in detail

# -----------------------------------
# 1. Arithmetic Operators
# +, -, *, /, %, //, **
# -----------------------------------

print("== Arithmetic Operators ==")
a = 10
b = 3
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)     # normal division
print("a % b =", a % b)     # remainder
print("a // b =", a // b)   # floor division
print("a ** b =", a ** b)   # exponent (power)

# -----------------------------------
# 2. Assignment Operators
# =, +=, -=, *=, /=, //=, %=, **=
# -----------------------------------

print("\n== Assignment Operators ==")
x = 5
print("Initial x:", x)
x += 3
print("x += 3:", x)
x *= 2
print("x *= 2:", x)
x -= 4
print("x -= 4:", x)
x /= 2
print("x /= 2:", x)
x //= 2
print("x //= 2:", x)
x %= 3
print("x %= 3:", x)
x **= 2
print("x **= 2:", x)

# -----------------------------------
# 3. Comparison Operators
# ==, !=, >, <, >=, <=
# -----------------------------------

print("\n== Comparison Operators ==")
p = 10
q = 20
print("p == q:", p == q)
print("p != q:", p != q)
print("p > q:", p > q)
print("p < q:", p < q)
print("p >= q:", p >= q)
print("p <= q:", p <= q)

# -----------------------------------
# 4. Logical Operators
# and, or, not
# -----------------------------------

print("\n== Logical Operators ==")
t = True
f = False
print("t and f:", t and f)
print("t or f:", t or f)
print("not t:", not t)

# Combined example
age = 21
has_id = True
print("\nCan enter club:", age >= 18 and has_id)
print("Teenager:", age > 12 and age < 20)

# -----------------------------------
# 5. Identity Operators
# is, is not
# -----------------------------------

print("\n== Identity Operators ==")
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print("a is b:", a is b)          # False → different location
print("a == b:", a == b)          # True → same value
print("a is c:", a is c)          # True → same location
print("a is not b:", a is not b)

# -----------------------------------
# 6. Membership Operators
# in, not in
# -----------------------------------

print("\n== Membership Operators ==")
fruits = ["apple", "banana", "mango"]
print("'apple' in fruits:", "apple" in fruits)
print("'grape' not in fruits:", "grape" not in fruits)

# -----------------------------------
# 7. Bitwise Operators
# &, |, ^, <<, >>, ~ (rare for beginners)
# -----------------------------------

print("\n== Bitwise Operators ==")
x = 6  # binary: 110
y = 2  # binary: 010

print("Binary of x:", bin(x))
print("Binary of y:", bin(y))

print("x & y :", x & y)   # AND
print("x | y :", x | y)   # OR
print("x ^ y :", x ^ y)   # XOR
print("x << 1 :", x << 1) # Left shift
print("x >> 1 :", x >> 1) # Right shift

# -----------------------------------
# Short Quiz Section (for learning)
# -----------------------------------

print("\n== Quick Practice ==")
score = int(input("Enter your score (0-100): "))
if score >= 50:
    print("Pass ✅")
else:
    print("Fail ❌")

# -----------------------------------
# End of Day 13 Lesson ✅
# -----------------------------------
