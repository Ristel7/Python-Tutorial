# ---------------------------------------------------------
# Day 35: continue Statement in Python
# ---------------------------------------------------------

# continue skips the current iteration of a loop
# and moves directly to the next iteration.


# ---------------------------------------------------------
# 1. continue in a for loop
# ---------------------------------------------------------

print("continue in for loop:")

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

print("Loop finished\n")


# ---------------------------------------------------------
# 2. continue in a while loop
# ---------------------------------------------------------

print("continue in while loop:")

num = 0
while num < 5:
    num += 1
    if num == 2:
        continue
    print(num)

print("While loop finished\n")


# ---------------------------------------------------------
# 3. Skipping specific values
# ---------------------------------------------------------

print("Skipping even numbers:")

for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

print()


# ---------------------------------------------------------
# 4. continue with user input
# ---------------------------------------------------------

print("Ignoring empty input:")

while True:
    text = input("Enter something (type exit to stop): ")

    if text == "":
        continue
    if text.lower() == "exit":
        break

    print("You entered:", text)

print("Input loop ended\n")


# ---------------------------------------------------------
# 5. continue in nested loops
# ---------------------------------------------------------

print("continue in nested loops:")

for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            continue
        print(f"i={i}, j={j}")
    print("Inner loop complete")

print()


# ---------------------------------------------------------
# 6. continue vs break comparison
# ---------------------------------------------------------

print("continue vs break:")

for i in range(1, 6):
    if i == 2:
        continue
    if i == 5:
        break
    print(i)

print("Loop exited\n")


# ---------------------------------------------------------
# 7. continue in for-else
# ---------------------------------------------------------

print("for-else with continue:")

for i in range(3):
    if i == 1:
        continue
    print("i:", i)
else:
    print("Loop completed normally")

print()


# ---------------------------------------------------------
# 8. Real-world example: Filtering invalid data
# ---------------------------------------------------------

print("Filtering invalid values:")

data = [10, -5, 20, -3, 15]

for value in data:
    if value < 0:
        continue
    print("Valid value:", value)

print()


# ---------------------------------------------------------
# 9. Real-world example: Skipping failed login attempts
# ---------------------------------------------------------

print("Login simulation:")

users = ["admin", "", "guest", "root"]

for user in users:
    if user == "":
        continue
    print("Processing login for:", user)

print()


# ---------------------------------------------------------
# 10. Using continue to clean data
# ---------------------------------------------------------

print("Cleaning numeric data:")

raw_data = ["10", "abc", "25", "?", "30"]

clean_data = []

for item in raw_data:
    if not item.isdigit():
        continue
    clean_data.append(int(item))

print("Clean data:", clean_data)


# ---------------------------------------------------------
# End of Day 35: continue Statement
# ---------------------------------------------------------
