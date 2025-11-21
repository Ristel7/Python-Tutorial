# --------------------------------------------
# Basic while loop
# --------------------------------------------

print("Basic while loop:")
count = 1

while count <= 5:
    print("Count:", count)
    count += 1


# --------------------------------------------
# Loop that stops when a condition becomes False
# --------------------------------------------

print("\nLoop decreasing until zero:")
num = 3

while num > 0:
    print("Number:", num)
    num -= 1

print("Stopped when num reached 0")


# --------------------------------------------
# Using break inside a while loop
# --------------------------------------------

print("\nUsing break to stop early:")
x = 1

while x <= 10:
    if x == 5:
        break
    print(x)
    x += 1


# --------------------------------------------
# Using continue inside a while loop
# --------------------------------------------

print("\nUsing continue to skip a value:")
y = 0

while y < 6:
    y += 1
    if y == 3:
        continue
    print(y)


# --------------------------------------------
# Infinite loop (with break)
# --------------------------------------------

print("\nSimple menu using an infinite loop:")

while True:
    print("1. Say Hello")
    print("2. Say Bye")
    print("3. Exit")
    
    choice = input("Enter choice: ")

    if choice == "1":
        print("Hello!")
    elif choice == "2":
        print("Bye!")
    elif choice == "3":
        print("Exiting menu...")
        break
    else:
        print("Invalid choice, try again.")


# --------------------------------------------
# While loop with else
# --------------------------------------------
# else runs only when the loop finishes normally (without break).

print("\nWhile loop with else:")
n = 1

while n <= 3:
    print("n:", n)
    n += 1
else:
    print("Loop completed normally")


# --------------------------------------------
# Using while to validate input
# --------------------------------------------

print("\nInput validation:")

age = input("Enter your age: ")

while not age.isdigit():
    print("Invalid input. Enter numbers only.")
    age = input("Enter your age: ")

print("Your age is:", age)


# --------------------------------------------
# While loop to sum numbers
# --------------------------------------------

print("\nSumming numbers until user enters 0:")

total = 0

while True:
    val = int(input("Enter a number (0 to stop): "))
    if val == 0:
        break
    total += val

print("Total sum:", total)


# --------------------------------------------
# Countdown program
# --------------------------------------------

print("\nCountdown:")
t = 5

while t > 0:
    print(t)
    t -= 1

print("Blast off!")


# --------------------------------------------
# While loop on a list
# --------------------------------------------

print("\nLooping through a list manually:")
nums = [10, 20, 30, 40]
i = 0

while i < len(nums):
    print(nums[i])
    i += 1


# --------------------------------------------
# Real-world Example: Password Check
# --------------------------------------------

print("\nPassword check example:")
correct = "python123"
attempts = 3

while attempts > 0:
    guess = input("Enter password: ")

    if guess == correct:
        print("Access granted.")
        break
    else:
        attempts -= 1
        print("Wrong password. Attempts left:", attempts)

if attempts == 0:
    print("Account locked.")


# --------------------------------------------
# End of While Loop Detailed Lesson
# --------------------------------------------
