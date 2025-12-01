# ------------------------------------------------
# Basic nested loop
# ------------------------------------------------

print("Basic nested loop:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}")
    print("--- Row complete ---")


# ------------------------------------------------
# Looping through a 2D list (matrix)
# ------------------------------------------------

matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

print("\nMatrix traversal:")
for row in matrix:
    for val in row:
        print(val, end=" ")
    print()


# ------------------------------------------------
# Multiplication table
# ------------------------------------------------

print("\nMultiplication table (1–5):")
for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end="\t")
    print()


# ------------------------------------------------
# Nested loop with conditions
# ------------------------------------------------

print("\nChecking even & odd inside nested loops:")
for i in range(1, 4):
    for j in range(1, 6):
        if (i + j) % 2 == 0:
            print(f"{i}+{j} = Even")
        else:
            print(f"{i}+{j} = Odd")
    print("Row done")


# ------------------------------------------------
# Pattern Printing Examples
# ------------------------------------------------

print("\nPattern 1: Square of stars")
for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()

print("\nPattern 2: Right triangle")
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

print("\nPattern 3: Inverted triangle")
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()


# ------------------------------------------------
# Nested loops with lists inside lists
# ------------------------------------------------

students = [
    ["Priyanshu", 21, "Python"],
    ["Riya", 22, "AI/ML"],
    ["Aman", 19, "Data Science"]
]

print("\nStudent details:")
for student in students:
    for info in student:
        print(info, end=" | ")
    print()


# ------------------------------------------------
# Creating combinations using nested loops
# ------------------------------------------------

colors = ["Red", "Blue", "Green"]
sizes = ["S", "M", "L"]

print("\nCombinations of colors and sizes:")
for color in colors:
    for size in sizes:
        print(color, size)


# ------------------------------------------------
# Flattening a 2D list manually
# ------------------------------------------------

flat = []
print("\nFlattening matrix manually:")
for row in matrix:
    for val in row:
        flat.append(val)

print("Flattened list:", flat)


# ------------------------------------------------
# Nested while loops
# ------------------------------------------------

print("\nNested while loops:")
i = 1

while i <= 3:
    j = 1
    while j <= 3:
        print(f"i={i}, j={j}")
        j += 1
    i += 1


# ------------------------------------------------
# Real-world Example: Seating rows in a hall
# ------------------------------------------------

print("\nSeating arrangement rows:")
rows = 3
seats = 5

for r in range(1, rows + 1):
    for s in range(1, seats + 1):
        print(f"Row {r} Seat {s}")
    print("--- Row Completed ---")


# ------------------------------------------------
# Real-world Example: Searching in a matrix
# ------------------------------------------------

print("\nSearching for a value in a matrix:")
target = 50
found = False

for row in matrix:
    for value in row:
        if value == target:
            print("Found:", target)
            found = True
            break
    if found:
        break
else:
    print("Not found")


# ------------------------------------------------
# End of Nested Loops Detailed Lesson
# ------------------------------------------------
