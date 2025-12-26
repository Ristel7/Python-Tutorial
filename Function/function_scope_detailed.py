# ---------------------------------------------------------
# Day 26: Function Scope (local, global, nonlocal)
# ---------------------------------------------------------

# Python has 3 important scopes:
# 1. Local      → Inside a function
# 2. Global     → Outside all functions
# 3. Nonlocal   → Inside nested functions


# ---------------------------------------------------------
# 1. Local Scope
# ---------------------------------------------------------

def show_local():
    x = 10   # local variable
    print("Inside function, x =", x)

show_local()

# print(x)  # ❌ error: x is not defined outside the function


# ---------------------------------------------------------
# 2. Global Scope
# ---------------------------------------------------------

y = 50  # global variable

def display_global():
    print("Inside function, y =", y)

display_global()
print("Outside function, y =", y)


# ---------------------------------------------------------
# 3. Modifying a Global Variable (global keyword)
# ---------------------------------------------------------

count = 0

def increase():
    global count
    count = count + 1
    print("Inside function, count =", count)

increase()
increase()
print("Outside function, count =", count)


# ---------------------------------------------------------
# 4. Local variable with same name as global
# ---------------------------------------------------------

value = 100  # global

def test():
    value = 20  # local (different from global)
    print("Local value inside function =", value)

test()
print("Global value outside function =", value)


# ---------------------------------------------------------
# 5. Nonlocal Scope (variables inside nested functions)
# ---------------------------------------------------------

def outer():
    msg = "Hello"  # this belongs to outer scope

    def inner():
        nonlocal msg
        msg = "Hi from inner"  # modifies outer variable

    inner()
    print("Outer msg:", msg)

outer()


# ---------------------------------------------------------
# 6. When NOT using nonlocal
# ---------------------------------------------------------

def outer2():
    text = "Python"

    def inner2():
        text = "Inner text"  # local to inner2 only
        print("Inside inner2:", text)

    inner2()
    print("Inside outer2:", text)

outer2()


# ---------------------------------------------------------
# 7. Accessing global + local with same name
# ---------------------------------------------------------

score = 90

def check_scope():
    score = 50
    print("Local score:", score)
    print("Global score:", globals()['score'])

check_scope()


# ---------------------------------------------------------
# 8. Using global inside conditional logic
# ---------------------------------------------------------

flag = False

def toggle():
    global flag
    flag = not flag

toggle()
print("\nFlag after function call:", flag)


# ---------------------------------------------------------
# 9. Real-world example: Counter using nonlocal
# ---------------------------------------------------------

def create_counter():
    count = 0  # belongs to outer function

    def inc():
        nonlocal count
        count += 1
        return count

    return inc

counter = create_counter()

print("\nCounter example:")
print(counter())
print(counter())
print(counter())


# ---------------------------------------------------------
# 10. Real-world example: Tracking login attempts
# ---------------------------------------------------------

def login_system():
    attempts = 0

    def attempt():
        nonlocal attempts
        attempts += 1
        return attempts

    return attempt

track = login_system()

print("\nLogin attempts example:")
print("Attempt:", track())
print("Attempt:", track())
print("Attempt:", track())


# ---------------------------------------------------------
# End of Day 26: Function Scope
# ---------------------------------------------------------
