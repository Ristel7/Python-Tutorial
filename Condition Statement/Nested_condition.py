# -----------------------------------
# Day 17: Nested Conditions in Python
# -----------------------------------

# Nested conditions mean placing one if-elif-else block inside another.
# They’re useful when a decision depends on a previous condition being true.

# Syntax:
# if condition1:
#     if condition2:
#         statement
#     else:
#         statement
# else:
#     statement

# -----------------------------------
# Basic Example
# -----------------------------------

num = int(input("Enter a number: "))

if num >= 0:
    if num == 0:
        print("The number is zero.")
    else:
        print("The number is positive.")
else:
    print("The number is negative.")

# -----------------------------------
# Nested if example with age and citizenship
# -----------------------------------

age = int(input("\nEnter your age: "))
citizen = input("Are you an Indian citizen? (yes/no): ").lower()

if age >= 18:
    if citizen == "yes":
        print("You are eligible to vote in India.")
    else:
        print("You are not eligible to vote (citizenship issue).")
else:
    print("You are underage and not eligible to vote.")

# -----------------------------------
# Nested conditions for student grading
# -----------------------------------

marks = int(input("\nEnter your marks: "))

if marks >= 50:
    print("You passed the exam.")
    if marks >= 90:
        print("Grade: A+ (Excellent!)")
    elif marks >= 75:
        print("Grade: A (Very Good)")
    elif marks >= 60:
        print("Grade: B (Good)")
    else:
        print("Grade: C (Average)")
else:
    print("You failed. Better luck next time!")

# -----------------------------------
# Nested if with logical operators
# -----------------------------------

salary = float(input("\nEnter your monthly salary: "))

if salary > 0:
    if salary >= 100000:
        print("High income category")
    elif salary >= 50000:
        print("Middle income category")
    else:
        print("Low income category")
else:
    print("Invalid salary entered.")

# -----------------------------------
# Nested conditions with multiple levels
# -----------------------------------

print("\n--- Banking System ---")
balance = 10000
withdraw = int(input("Enter amount to withdraw: "))

if withdraw > 0:
    if withdraw <= balance:
        print("Processing withdrawal...")
        if withdraw > 5000:
            print("Large withdrawal! OTP verification required.")
        else:
            print("Withdrawal successful.")
    else:
        print("Insufficient balance.")
else:
    print("Invalid amount entered.")

# -----------------------------------
# Real-world Example 1: Driving eligibility
# -----------------------------------

print("\n--- Driving License Check ---")
age = int(input("Enter your age: "))
has_license = input("Do you have a valid license? (yes/no): ").lower()

if age >= 18:
    if has_license == "yes":
        print("You can drive legally.")
    else:
        print("You are old enough but need to get a license.")
else:
    print("You are not old enough to drive.")

# -----------------------------------
# Real-world Example 2: Online shopping discount
# -----------------------------------

print("\n--- Discount Eligibility ---")
cart_value = float(input("Enter cart total (₹): "))
is_member = input("Are you a premium member? (yes/no): ").lower()

if cart_value >= 500:
    if is_member == "yes":
        print("You get a 20% discount!")
    else:
        print("You get a 10% discount!")
else:
    if is_member == "yes":
        print("You get a 5% discount as a loyal member.")
    else:
        print("No discount. Add more items to get one!")

# -----------------------------------
# Real-world Example 3: Exam eligibility system
# -----------------------------------

print("\n--- Exam Eligibility ---")
attendance = int(input("Enter attendance percentage: "))
internal_marks = int(input("Enter internal marks (out of 40): "))

if attendance >= 75:
    if internal_marks >= 20:
        print("You are eligible for the final exam ✅")
    else:
        print("Low internal marks. Improve your performance.")
else:
    if attendance >= 60:
        print("You may be allowed with special permission.")
    else:
        print("Not eligible due to low attendance ❌")

# -----------------------------------
# End of Day 17 Lesson
# -----------------------------------
