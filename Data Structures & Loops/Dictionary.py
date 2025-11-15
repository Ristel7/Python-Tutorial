# -------------------------
# 1. Creating dictionaries
# -------------------------

student = {
    "name": "Riya",
    "age": 21,
    "course": "Computer Science",
    "skills": ["Python", "SQL", "Excel"],
    "is_active": True
}

print("Full dictionary:", student)


# -------------------------
# 2. Accessing values
# -------------------------

print("\nAccessing values:")
print("Name:", student["name"])          # direct access
print("Age:", student.get("age"))        # safer access using get()


# -------------------------
# 3. Updating values
# -------------------------

student["age"] = 22                       # change value
student["skills"].append("Git")           # update list inside dictionary

print("\nAfter updates:", student)


# -------------------------
# 4. Adding new key-value pairs
# -------------------------

student["email"] = "riya@example.com"
print("\nAfter adding email:", student)


# -------------------------
# 5. Removing items
# -------------------------

removed_item = student.pop("is_active")   # removes and returns value
print("\nRemoved 'is_active':", removed_item)
print("After pop:", student)

last_removed = student.popitem()          # removes last inserted pair
print("Last removed item:", last_removed)
print("After popitem:", student)


# -------------------------
# 6. Dictionary methods
# -------------------------

print("\nKeys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())


# -------------------------
# 7. Looping through dictionary
# -------------------------

print("\nLooping:")
for key in student:
    print("Key:", key)

for key, value in student.items():
    print("Key:", key, "Value:", value)


# -------------------------
# 8. Nested dictionaries
# -------------------------

company = {
    "employees": {
        "emp1": {"name": "Aarav", "salary": 50000},
        "emp2": {"name": "Siya", "salary": 60000}
    }
}

print("\nNested dictionary example:")
print(company["employees"]["emp1"]["name"])
print(company["employees"]["emp2"]["salary"])


# -------------------------
# 9. Dictionary from lists
# -------------------------

keys = ["name", "age", "city"]
values = ["Rohan", 25, "Delhi"]

person = dict(zip(keys, values))
print("\nDictionary created from lists:", person)


# -------------------------
# 10. Using dictionary as a counter
# -------------------------

text = "apple banana apple mango banana apple"
words = text.split()

counter = {}

for w in words:
    counter[w] = counter.get(w, 0) + 1

print("\nWord frequency:", counter)


# -------------------------
# 11. Checking if key exists
# -------------------------

print("\nKey 'name' exists?", "name" in student)
print("Key 'phone' exists?", "phone" in student)
