# ---------------------------------------------------------
# Day 34: break Statement in Python
# ---------------------------------------------------------

# ---------------------------------------------------------
# 1. break in a for loop
# ---------------------------------------------------------

print("break in for loop:")

for i in range(1, 6):
    if i == 4:
        break
    print(i)

print("Loop ended\n")


# ---------------------------------------------------------
# 2. break in a while loop
# ---------------------------------------------------------

print("break in while loop:")

count = 1
while True:
    if count == 5:
        break
    print(count)
    count += 1

print("While loop stopped\n")


# ---------------------------------------------------------
# 3. break with user input
# ---------------------------------------------------------

print("User input example:")

while True:
    user_input = input("Type 'exit' to stop: ")
    if user_input.lower() == "exit":
        break
    print("You typed:", user_input)

print("Exited input loop\n")


# ---------------------------------------------------------
# 4. break inside nested loops
# ---------------------------------------------------------

print("break inside nested loops:")

for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            break
        print(f"i={i}, j={j}")
    print("Inner loop ended")

print("Nested loops done\n")


# ---------------------------------------------------------
# 5. Using break with for-else
# ---------------------------------------------------------

print("for-else with break:")

numbers = [2, 4, 6, 8]
target = 6

for n in numbers:
    if n == target:
        print("Found:", target)
        break
else:
    print("Target not found")

print()


# ---------------------------------------------------------
# 6. break when condition is met
# ---------------------------------------------------------

print("Stopping loop when sum exceeds limit:")

total = 0

for i in range(1, 10):
    total += i
    if total > 15:
        break
    print("Added:", i, "Total:", total)

print("Final total:", total, "\n")


# ---------------------------------------------------------
# 7. break vs continue
# ---------------------------------------------------------

print("break vs continue:")

for i in range(1, 6):
    if i == 3:
        continue
    if i == 5:
        break
    print(i)

print("Loop exited\n")


# ---------------------------------------------------------
# 8. Real-world example: Password attempts
# ---------------------------------------------------------

print("Password attempt system:")

correct_password = "python123"
attempts = 3

while attempts > 0:
    password = input("Enter password: ")

    if password == correct_password:
        print("Access granted")
        break
    else:
        attempts -= 1
        print("Wrong password. Attempts left:", attempts)

if attempts == 0:
    print("Account locked\n")


# ---------------------------------------------------------
# 9. Real-world example: Searching in a list
# ---------------------------------------------------------

print("Searching in list:")

items = ["apple", "banana", "mango", "orange"]
search = "mango"

for item in items:
    if item == search:
        print("Item found:", search)
        break
    print("Checking:", item)

print("Search completed\n")


# ---------------------------------------------------------
# 10. Using break to stop infinite loop safely
# ---------------------------------------------------------

print("Safe infinite loop:")

num = 1
while True:
    print(num)
    if num == 3:
        break
    num += 1

print("Infinite loop stopped safely\n")


# ---------------------------------------------------------
# End of Day 34: break Statement
# ---------------------------------------------------------

