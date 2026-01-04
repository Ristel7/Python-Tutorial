# ---------------------------------------------------------
# Day 31: Object-Oriented Programming (Basics)
# ---------------------------------------------------------

# ---------------------------------------------------------
# 1. Defining a Class
# ---------------------------------------------------------

class Student:
    pass

print("Class created successfully")


# ---------------------------------------------------------
# 2. Creating an Object
# ---------------------------------------------------------

s1 = Student()
s2 = Student()

print("Objects created:", s1, s2)


# ---------------------------------------------------------
# 3. Adding Attributes to Objects
# ---------------------------------------------------------

s1.name = "Priyanshu"
s1.age = 21
s1.course = "Python"

s2.name = "Riya"
s2.age = 22
s2.course = "Data Science"

print("\nStudent 1:", s1.name, s1.age, s1.course)
print("Student 2:", s2.name, s2.age, s2.course)


# ---------------------------------------------------------
# 4. Using __init__() Constructor
# ---------------------------------------------------------

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

s3 = Student("Aman", 20, "AI")
s4 = Student("Sneha", 23, "ML")

print("\nUsing constructor:")
print(s3.name, s3.age, s3.course)
print(s4.name, s4.age, s4.course)


# ---------------------------------------------------------
# 5. Adding Methods to a Class
# ---------------------------------------------------------

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Course: {self.course}")

    def is_adult(self):
        return self.age >= 18

student = Student("Priyanshu", 21, "Python")

print("\nUsing methods:")
student.display()
print("Is adult?", student.is_adult())


# ---------------------------------------------------------
# 6. self keyword explained
# ---------------------------------------------------------

class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def accelerate(self):
        self.speed += 10
        print(f"{self.brand} speed is now {self.speed}")

car1 = Car("Tesla", 50)
car1.accelerate()
car1.accelerate()


# ---------------------------------------------------------
# 7. Multiple Objects from Same Class
# ---------------------------------------------------------

car2 = Car("BMW", 60)
car2.accelerate()


# ---------------------------------------------------------
# 8. Real-world Example: Bank Account
# ---------------------------------------------------------

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("Withdrawn:", amount)

    def show_balance(self):
        print("Balance:", self.balance)

account = BankAccount("Priyanshu", 5000)

print("\nBank account operations:")
account.deposit(2000)
account.withdraw(1000)
account.show_balance()


# ---------------------------------------------------------
# End of Day 31: OOP Basics
# ---------------------------------------------------------

