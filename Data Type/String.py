# -----------------------------------
# Day 9: String (str) Data Type
# -----------------------------------

# In Python, a string is a sequence of characters enclosed in quotes.
# You can use single (' '), double (" "), or triple quotes (''' ''' / """ """) for multiline strings.

# -----------------------------------
# Creating Strings
# -----------------------------------

single_quote = 'Hello'
double_quote = "World"
multi_line = """This is
a multi-line
string example."""

print("Single Quote String:", single_quote)
print("Double Quote String:", double_quote)
print("Multi-line String:\n", multi_line)

# -----------------------------------
# Checking Data Type
# -----------------------------------
print("\nType of single_quote:", type(single_quote))

# -----------------------------------
# String Indexing & Slicing
# -----------------------------------

# Strings are indexed like arrays — index starts from 0
text = "Python"

print("\nAccessing characters:")
print("First character:", text[0])
print("Last character:", text[-1])

print("\nSlicing examples:")
print("text[0:4] →", text[0:4])      # Pyth
print("text[2:] →", text[2:])        # thon
print("text[:3] →", text[:3])        # Pyt
print("text[::-1] →", text[::-1])    # Reverse string

# -----------------------------------
# String Concatenation & Repetition
# -----------------------------------
first = "Priyanshu"
last = "Rajput"
full_name = first + " " + last
print("\nFull Name:", full_name)

repeat_text = "Hi! " * 3
print("Repetition:", repeat_text)

# -----------------------------------
# String Methods
# -----------------------------------
sample = "  hello python learners  "

print("\nString Methods:")
print("Original:", sample)
print("Uppercase:", sample.upper())
print("Lowercase:", sample.lower())
print("Title Case:", sample.title())
print("Capitalized:", sample.capitalize())
print("Stripped:", sample.strip())
print("Replace:", sample.replace("python", "world"))
print("Count of 'l':", sample.count("l"))
print("Starts with '  he':", sample.startswith("  he"))
print("Ends with 'ners  ':", sample.endswith("ners  "))
print("Find 'python':", sample.find("python"))
print("Split:", sample.split())

# -----------------------------------
# String Formatting
# -----------------------------------

name = "Priyanshu"
age = 21
language = "Python"

print("\nString Formatting:")
# Using f-strings
print(f"My name is {name}, I am {age} years old, and I love {language}.")

# Using format() method
print("My name is {}, I am {} years old, and I love {}.".format(name, age, language))

# Using index-based placeholders
print("My name is {0}, and I love {2}!".format(name, age, language))

# -----------------------------------
# Escape Characters
# -----------------------------------

print("\nEscape Characters:")
print("Line break:\nThis is on a new line.")
print("Tab space:\tAfter tab")
print("Single quote: \'Hello\'")
print("Double quote: \"World\"")
print("Backslash: C:\\Users\\Python")

# -----------------------------------
# Iterating Through a String
# -----------------------------------
word = "Data"
print("\nIterating through:", word)
for char in word:
    print(char)

# -----------------------------------
# Membership Operators
# -----------------------------------
sentence = "Python is fun to learn"
print("\nMembership Tests:")
print("'Python' in sentence:", "Python" in sentence)
print("'Java' not in sentence:", "Java" not in sentence)

# -----------------------------------
# String Length
# -----------------------------------
print("\nLength of sentence:", len(sentence))

# -----------------------------------
# Practical Examples
# -----------------------------------

# 1. Validate Email
email = "user@example.com"
is_valid = "@" in email and "." in email
print("\nIs email valid?", is_valid)

# 2. Count vowels
vowels = "aeiouAEIOU"
text = "Data Science"
count = sum(1 for ch in text if ch in vowels)
print("Number of vowels in 'Data Science':", count)

# 3. Reverse a user input string
user_input = "Machine Learning"
reversed_input = user_input[::-1]
print("Reversed:", reversed_input)

# 4. Password strength check
password = "Priyanshu123"
is_strong = len(password) >= 8 and any(ch.isdigit() for ch in password) and any(ch.isupper() for ch in password)
print("Is password strong?", is_strong)

# -----------------------------------
# End of Day 9 Lesson
# -----------------------------------
