# ============================
# 1. FOR LOOP (basic)
# ============================

print("For loop over a list:")
fruits = ["apple", "banana", "mango"]

for item in fruits:
    print(item)


# ============================
# 2. FOR LOOP with range()
# ============================

print("\nFor loop using range:")
for i in range(1, 6):   # prints 1 to 5
    print(i)


# ============================
# 3. FOR LOOP to get index + value
# ============================

print("\nFor loop with index:")
colors = ["red", "green", "blue"]

for index, value in enumerate(colors):
    print("Index:", index, "Value:", value)


# ============================
# 4. WHILE LOOP (basic)
# ============================

print("\nWhile loop:")
count = 1

while count <= 5:
    print("Count is:", count)
    count += 1


# ============================
# 5. WHILE LOOP example where condition becomes False
# ============================

print("\nWhile loop stopping when number becomes 0:")
num = 3

while num > 0:
    print("Number:", num)
    num -= 1

print("Loop ended")


# ============================
# 6. Using BREAK inside a loop
# ============================

print("\nUsing break:")
for x in range(10):
    if x == 4:
        break
    print(x)


# ============================
# 7. Using CONTINUE inside a loop
# ============================

print("\nUsing continue:")
for x in range(6):
    if x == 3:
        continue
    print(x)


# ============================
# 8. Looping through a string
# ============================

print("\nLooping over a string:")
text = "Python"

for char in text:
    print(char)


# ============================
# 9. Looping through a dictionary (keys and values)
# ============================

print("\nLoop through dictionary:")
student = {"name": "Aarav", "age": 20, "course": "CS"}

for key, value in student.items():
    print(key, "→", value)
