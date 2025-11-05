# -----------------------------------------
# Day 19: Strings (In-depth)
# -----------------------------------------

# A string in Python is a sequence of characters enclosed in single, double, or triple quotes.
# Strings are immutable — meaning they cannot be changed once created.

# -----------------------------------------
# String Creation
# -----------------------------------------
string1 = 'Hello'
string2 = "Python"
string3 = '''This is
a multi-line
string.'''

print(string1)
print(string2)
print(string3)

# -----------------------------------------
# String Indexing
# -----------------------------------------
# Indexing allows you to access characters using their position (starting from 0).
# Example: H  e  l  l  o
#          0  1  2  3  4

text = "Python"

print("\n--- Indexing ---")
print("First character:", text[0])      # P
print("Third character:", text[2])      # t
print("Last character:", text[-1])      # n (negative index counts from the end)
print("Second last character:", text[-2])  # o

# -----------------------------------------
# String Slicing
# -----------------------------------------
# Slicing allows extracting a portion of a string.
# Syntax: string[start:end:step]
# start = starting index (inclusive)
# end = stopping index (exclusive)
# step = number of characters to skip

print("\n--- Slicing ---")
print("text[0:4] =", text[0:4])   # Pyth
print("text[2:]  =", text[2:])    # thon
print("text[:3]  =", text[:3])    # Pyt
print("text[-3:] =", text[-3:])   # hon
print("text[::2] =", text[::2])   # Pto (every 2nd character)
print("text[::-1] =", text[::-1]) # Reverse string

# -----------------------------------------
# String Immutability
# -----------------------------------------
# You cannot change characters directly.
# Example (This will cause an error):
# text[0] = "J"  ❌
# Instead, you create a new string.

new_text = "J" + text[1:]
print("\nModified text:", new_text)   # Jython

# -----------------------------------------
# Common String Methods
# -----------------------------------------
sample = "  hello python learners  "

print("\n--- String Methods ---")
print("Original:", repr(sample))

# Remove whitespace
print("strip():", sample.strip())

# Convert case
print("upper():", sample.upper())
print("lower():", sample.lower())
print("title():", sample.title())
print("capitalize():", sample.capitalize())
print("swapcase():", sample.swapcase())

# Count occurrences
print("count('o'):", sample.count('o'))

# Find positions
print("find('python'):", sample.find("python"))
print("index('python'):", sample.index("python"))

# Replace words
print("replace('python', 'world'):", sample.replace("python", "world"))

# Check string type
print("startswith('h'):", sample.startswith("h"))
print("endswith('s'):", sample.endswith("s"))

# Check content type
alpha = "Hello"
num = "12345"
alnum = "Python3"

print("isalpha():", alpha.isalpha())    # True
print("isdigit():", num.isdigit())      # True
print("isalnum():", alnum.isalnum())    # True
print("isspace():", "   ".isspace())    # True

# Splitting and Joining
words = "Python is fun"
print("split():", words.split())                # ['Python', 'is', 'fun']
joined = "-".join(words.split())
print("join():", joined)                        # Python-is-fun

# -----------------------------------------
# String Formatting Methods
# -----------------------------------------
name = "Priyanshu"
age = 21
language = "Python"

print("\n--- String Formatting ---")

# Method 1: f-string (Modern and Preferred)
print(f"My name is {name}, I am {age} years old, and I love {language}.")

# Method 2: format() method
print("My name is {}, I am {} years old, and I love {}.".format(name, age, language))

# Method 3: format() with placeholders
print("My name is {0}, I am {1} years old, and I love {2}.".format(name, age, language))
print("My name is {name}, I am {age} years old.".format(name="Priyanshu", age=21))

# Method 4: Old-style formatting (%)
print("My name is %s, I am %d years old, and I love %s." % (name, age, language))

# Formatting numbers
pi = 3.1415926535
print(f"Pi rounded to 2 decimals: {pi:.2f}")     # 3.14
print(f"Pi rounded to 4 decimals: {pi:.4f}")     # 3.1416

# Alignment and width
print(f"|{'Left':<10}|{'Center':^10}|{'Right':>10}|")

# -----------------------------------------
# String Iteration
# -----------------------------------------
print("\n--- String Iteration ---")
for char in "DATA":
    print(char)

# -----------------------------------------
# String Concatenation and Repetition
# -----------------------------------------
a = "Hello"
b = "World"
print("\nConcatenation:", a + " " + b)
print("Repetition:", a * 3)

# -----------------------------------------
# Checking Substring Presence
# -----------------------------------------
sentence = "Learning Python is enjoyable"
print("\n--- Substring Checks ---")
print("Python" in sentence)    # True
print("Java" not in sentence)  # True

# -----------------------------------------
# Multiline f-string Example
# -----------------------------------------
person = "Priyanshu"
course = "Python Programming"
duration = "30 days"

info = f"""
Student Name: {person}
Course: {course}
Duration: {duration}
"""
print("\n--- Multiline f-string ---")
print(info)

# -----------------------------------------
# End of Day 19: Strings (In-depth)
# -----------------------------------------
