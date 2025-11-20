# ----------------------------------------
# Basic for loop over a list
# ----------------------------------------

fruits = ["apple", "banana", "mango", "orange"]

print("Iterating through a simple list:")
for fruit in fruits:
    print(fruit)


# ----------------------------------------
# Looping with range()
# ----------------------------------------

print("\nUsing range() to generate numbers:")
for n in range(1, 6):  # 1 to 5
    print(n)

print("\nRange with step value:")
for n in range(0, 20, 5):  # 0, 5, 10, 15
    print(n)

print("\nReverse loop:")
for n in range(10, 0, -2):  # 10, 8, 6, 4, 2
    print(n)


# ----------------------------------------
# Looping through a string
# ----------------------------------------

print("\nIterating through a string:")
word = "PYTHON"
for ch in word:
    print(ch)


# ----------------------------------------
# Looping through a dictionary
# ----------------------------------------

student = {"name": "Priyanshu", "age": 21, "course": "Python"}

print("\nDictionary Keys:")
for key in student:
    print(key)

print("\nDictionary Values:")
for value in student.values():
    print(value)

print("\nDictionary Key + Value:")
for key, value in student.items():
    print(key, "→", value)


# ----------------------------------------
# Looping with enumerate()
# ----------------------------------------

colors = ["red", "green", "blue"]

print("\nUsing enumerate() to get both index and value:")
for index, color in enumerate(colors):
    print("Index:", index, "| Color:", color)


# ----------------------------------------
# Looping through a list of tuples
# ----------------------------------------

pairs = [(1, 10), (2, 20), (3, 30)]

print("\nUnpacking items inside the loop:")
for a, b in pairs:
    print("A =", a, "| B =", b)


# ----------------------------------------
# Looping through a nested list (2D list)
# ----------------------------------------

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("\nNested loops for 2D list:")
for row in matrix:
    for value in row:
        print(value, end=" ")
    print()


# ----------------------------------------
# break inside a loop
# ----------------------------------------

print("\nUsing break (stop loop when 5 appears):")
for num in range(1, 11):
    if num == 5:
        break
    print(num)


# ----------------------------------------
# continue inside a loop
# ----------------------------------------

print("\nUsing continue (skip number 3):")
for num in range(1, 6):
    if num == 3:
        continue
    print(num)


# ----------------------------------------
# for loop with else
# ----------------------------------------
# "else" runs when the loop finishes normally — NOT when break is used.

print("\nFor loop with else:")
for i in range(3):
    print("Iteration:", i)
else:
    print("Loop finished normally")


# ----------------------------------------
# Searching using for-else
# ----------------------------------------

numbers = [2, 4, 6, 8]

print("\nSearching for a number:")
target = 5

for num in numbers:
    if num == target:
        print("Found:", target)
        break
else:
    print("Not found in list")


# ----------------------------------------
# List comprehension (loop in one line)
# ----------------------------------------

print("\nUsing list comprehension:")
squares = [x * x for x in range(1, 6)]
print("Squares:", squares)


# ----------------------------------------
# Real-world example: Counting vowels
# ----------------------------------------

print("\nCounting vowels in a word:")
word = "programming"
vowels = "aeiou"
count = 0

for char in word:
    if char in vowels:
        count += 1

print("Total vowels:", count)


# ----------------------------------------
# Real-world example: Filtering numbers
# ----------------------------------------

nums = [12, 7, 34, 9, 50, 21]
even_nums = []

print("\nFiltering even numbers:")
for n in nums:
    if n % 2 == 0:
        even_nums.append(n)

print("Even numbers:", even_nums)


# ----------------------------------------
# End of For Loop Detailed Lesson
# ----------------------------------------
