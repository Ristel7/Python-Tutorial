# -----------------------------------
# Day 3: Variables and Constants
# -----------------------------------

# A variable is like a container that stores data values.
# You can change its value anytime in your program.

# Example 1: Creating and printing variables
name = "Priyanshu"
age = 21
height = 5.9

print("Name:", name)
print("Age:", age)
print("Height:", height)

# Example 2: Updating variable values
age = 22  # You can reassign new data to the same variable
print("Updated Age:", age)

# Example 3: Performing operations with variables
a = 10
b = 5
sum_result = a + b
print("Sum:", sum_result)

# Example 4: Variables can hold different types of data
is_student = True
course = "Python Programming"
score = 89.5

print("Student:", is_student)
print("Course:", course)
print("Score:", score)

# -----------------------------------
# Constants in Python
# -----------------------------------
# Python doesn’t have built-in constant types like some other languages.
# By convention, we use ALL CAPS variable names to represent constants.

PI = 3.14159
GRAVITY = 9.8
MAX_STUDENTS = 50

print("\n--- Constants ---")
print("Value of PI:", PI)
print("Gravity:", GRAVITY)
print("Max Students Allowed:", MAX_STUDENTS)

# Even though you can technically change them...
PI = 3.14  # ...you should AVOID doing this in real projects
print("Modified PI (not recommended):", PI)

# -----------------------------------
# Example 5: Using Variables and Constants Together
# -----------------------------------

radius = 5
area = PI * radius ** 2
print("\nArea of Circle:", area)

# Using constant for conversion
METER_TO_KM = 0.001
distance_m = 5000
distance_km = distance_m * METER_TO_KM
print("Distance in Kilometers:", distance_km)
