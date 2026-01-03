# ---------------------------------------------------------
# Day 30: File Handling in Python
# ---------------------------------------------------------
# File handling allows Python to read from and write to files.
# Common modes: r (read), w (write), a (append), x (create)


# ---------------------------------------------------------
# 1. Writing to a file (write mode)
# ---------------------------------------------------------

file = open("example.txt", "w")
file.write("Hello, this is the first line.\n")
file.write("Python file handling is powerful.\n")
file.close()

print("File written successfully.")


# ---------------------------------------------------------
# 2. Reading from a file
# ---------------------------------------------------------

file = open("example.txt", "r")
content = file.read()
print("\nReading full file:")
print(content)
file.close()


# ---------------------------------------------------------
# 3. Reading line by line
# ---------------------------------------------------------

file = open("example.txt", "r")

print("Reading line by line:")
for line in file:
    print(line.strip())

file.close()


# ---------------------------------------------------------
# 4. Appending to a file
# ---------------------------------------------------------

file = open("example.txt", "a")
file.write("This line was added later.\n")
file.close()

print("\nContent appended.")


# ---------------------------------------------------------
# 5. Using with statement (best practice)
# ---------------------------------------------------------
# Automatically closes the file

with open("example.txt", "r") as file:
    print("\nUsing with statement:")
    print(file.read())


# ---------------------------------------------------------
# 6. Writing multiple lines using writelines()
# ---------------------------------------------------------

lines = [
    "Line one\n",
    "Line two\n",
    "Line three\n"
]

with open("multiple_lines.txt", "w") as file:
    file.writelines(lines)

print("\nMultiple lines written.")


# ---------------------------------------------------------
# 7. Reading lines into a list
# ---------------------------------------------------------

with open("multiple_lines.txt", "r") as file:
    lines_list = file.readlines()

print("\nLines as list:", lines_list)


# ---------------------------------------------------------
# 8. File pointer position
# ---------------------------------------------------------

with open("example.txt", "r") as file:
    print("\nPointer position:", file.tell())
    file.read(5)
    print("Pointer after reading 5 chars:", file.tell())
    file.seek(0)
    print("Pointer reset:", file.tell())


# ---------------------------------------------------------
# 9. Checking if file exists
# ---------------------------------------------------------

import os

filename = "example.txt"

if os.path.exists(filename):
    print("\nFile exists:", filename)
else:
    print("\nFile does not exist")


# ---------------------------------------------------------
# 10. Deleting a file
# ---------------------------------------------------------

temp_file = "temp.txt"

with open(temp_file, "w") as file:
    file.write("Temporary data")

if os.path.exists(temp_file):
    os.remove(temp_file)
    print("Temporary file deleted")


# ---------------------------------------------------------
# 11. Handling file errors safely
# ---------------------------------------------------------

try:
    with open("missing_file.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("\nError: File not found")


# ---------------------------------------------------------
# 12. Real-world Example: Logging user activity
# ---------------------------------------------------------

def log_activity(message):
    with open("activity.log", "a") as file:
        file.write(message + "\n")

log_activity("User logged in")
log_activity("User updated profile")
log_activity("User logged out")

print("\nUser activity logged.")


# ---------------------------------------------------------
# 13. Real-world Example: Simple notes app
# ---------------------------------------------------------

def add_note(note):
    with open("notes.txt", "a") as file:
        file.write(note + "\n")

def read_notes():
    with open("notes.txt", "r") as file:
        return file.read()

add_note("Learn Python file handling")
add_note("Practice daily")

print("\nNotes:")
print(read_notes())


# ---------------------------------------------------------
# End of Day 30: File Handling
# ---------------------------------------------------------

