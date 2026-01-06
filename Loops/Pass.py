# ---------------------------------------------------------
# Day 33: pass Statement in Python
# ---------------------------------------------------------

# ---------------------------------------------------------
# 1. pass in a function
# ---------------------------------------------------------

def future_function():
    pass

# The function exists but does nothing
future_function()
print("Function with pass executed successfully")


# ---------------------------------------------------------
# 2. pass in a class
# ---------------------------------------------------------

class EmptyClass:
    pass

obj = EmptyClass()
print("Empty class object created:", obj)


# ---------------------------------------------------------
# 3. pass in if statement
# ---------------------------------------------------------

x = 10

if x > 5:
    pass  # logic will be added later
else:
    print("x is 5 or less")

print("Program continues normally")


# ---------------------------------------------------------
# 4. pass in for loop
# ---------------------------------------------------------

print("\nUsing pass in a for loop:")

for i in range(5):
    if i == 2:
        pass   # placeholder, does nothing
    print("Value:", i)


# ---------------------------------------------------------
# 5. pass in while loop
# ---------------------------------------------------------

print("\nUsing pass in a while loop:")

count = 0
while count < 3:
    pass
    count += 1

print("While loop finished")


# ---------------------------------------------------------
# 6. pass vs continue vs break
# ---------------------------------------------------------

print("\nComparing pass, continue, and break:")

for i in range(5):
    if i == 1:
        pass        # does nothing, continues normally
    elif i == 2:
        continue    # skips rest of loop for this iteration
    elif i == 4:
        break       # exits loop completely
    print("Number:", i)


# ---------------------------------------------------------
# 7. pass in exception handling
# ---------------------------------------------------------

print("\nUsing pass in try-except:")

try:
    x = int("abc")
except ValueError:
    pass   # ignore the error silently

print("Program did not crash")


# ---------------------------------------------------------
# 8. pass while designing program structure
# ---------------------------------------------------------

def login():
    pass

def logout():
    pass

def register():
    pass

print("\nProgram structure defined using pass")


# ---------------------------------------------------------
# 9. pass in abstract-style design (before implementation)
# ---------------------------------------------------------

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

# Later, child classes will implement these methods


# ---------------------------------------------------------
# 10. Real-world example: Feature under development
# ---------------------------------------------------------

feature_enabled = False

if feature_enabled:
    print("Feature is running")
else:
    pass   # feature will be added in future

print("Application is stable")


# ---------------------------------------------------------
# End of Day 33: pass Statement
# ---------------------------------------------------------

