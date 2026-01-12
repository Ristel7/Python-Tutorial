# ---------------------------------------------------------
# Day 39: CSV Handling in Python
# ---------------------------------------------------------

import csv


# ---------------------------------------------------------
# 1. Writing to a CSV file
# ---------------------------------------------------------

with open("students.csv", mode="w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["id", "name", "age"])
    writer.writerow([1, "Priyanshu", 21])
    writer.writerow([2, "Riya", 22])
    writer.writerow([3, "Aman", 20])

print("CSV file written successfully")


# ---------------------------------------------------------
# 2. Reading a CSV file (basic)
# ---------------------------------------------------------

with open("students.csv", mode="r") as file:
    reader = csv.reader(file)

    print("\nReading CSV file:")
    for row in reader:
        print(row)


# ---------------------------------------------------------
# 3. Skipping header row
# ---------------------------------------------------------

with open("students.csv", mode="r") as file:
    reader = csv.reader(file)
    header = next(reader)

    print("\nHeader:", header)
    for row in reader:
        print(row)


# ---------------------------------------------------------
# 4. Reading CSV as dictionary (DictReader)
# ---------------------------------------------------------

with open("students.csv", mode="r") as file:
    reader = csv.DictReader(file)

    print("\nReading CSV using DictReader:")
    for row in reader:
        print(row["name"], row["age"])


# ---------------------------------------------------------
# 5. Writing CSV using DictWriter
# ---------------------------------------------------------

data = [
    {"id": 1, "product": "Laptop", "price": 60000},
    {"id": 2, "product": "Phone", "price": 30000},
    {"id": 3, "product": "Tablet", "price": 20000}
]

with open("products.csv", mode="w", newline="") as file:
    fieldnames = ["id", "product", "price"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(data)

print("\nProducts CSV created")


# ---------------------------------------------------------
# 6. Appending data to a CSV file
# ---------------------------------------------------------

with open("students.csv", mode="a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([4, "Sneha", 24])

print("\nData appended to students.csv")


# ---------------------------------------------------------
# 7. Reading CSV and filtering data
# ---------------------------------------------------------

print("\nStudents older than 21:")

with open("students.csv", mode="r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if int(row["age"]) > 21:
            print(row)


# ---------------------------------------------------------
# 8. Updating CSV data (read → modify → rewrite)
# ---------------------------------------------------------

updated_rows = []

with open("students.csv", mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["name"] == "Priyanshu":
            row["age"] = "22"
        updated_rows.append(row)

with open("students.csv", mode="w", newline="") as file:
    fieldnames = ["id", "name", "age"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(updated_rows)

print("\nCSV file updated")


# ---------------------------------------------------------
# 9. Real-world example: Calculate average age
# ---------------------------------------------------------

total_age = 0
count = 0

with open("students.csv", mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        total_age += int(row["age"])
        count += 1

average_age = total_age / count
print("\nAverage age:", average_age)


# ---------------------------------------------------------
# 10. Real-world example: Export report CSV
# ---------------------------------------------------------

report_data = [
    ["Month", "Sales"],
    ["Jan", 12000],
    ["Feb", 18000],
    ["Mar", 15000]
]

with open("sales_report.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(report_data)

print("\nSales report CSV created")


# ---------------------------------------------------------
# End of Day 39: CSV Handling
# ---------------------------------------------------------
