# ---------------------------------------------------------
# Day 32: Inheritance in Python
# ---------------------------------------------------------

# ---------------------------------------------------------
# 1. Single Inheritance
# ---------------------------------------------------------

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def study(self):
        print(f"{self.name} is studying {self.course}.")

student = Student("Priyanshu", 21, "Python")

student.introduce()
student.study()


# ---------------------------------------------------------
# 2. Inheriting without overriding __init__
# ---------------------------------------------------------

class Teacher(Person):
    def teach(self):
        print(f"{self.name} is teaching.")

teacher = Teacher("Riya", 30)

teacher.introduce()
teacher.teach()


# ---------------------------------------------------------
# 3. Method Overriding
# ---------------------------------------------------------

class Employee(Person):
    def introduce(self):
        print(f"I am {self.name} and I work as an employee.")

emp = Employee("Aman", 28)
emp.introduce()


# ---------------------------------------------------------
# 4. Using super() with overridden methods
# ---------------------------------------------------------

class Manager(Person):
    def introduce(self):
        super().introduce()
        print("I also manage a team.")

mgr = Manager("Sneha", 35)
mgr.introduce()


# ---------------------------------------------------------
# 5. Multilevel Inheritance
# ---------------------------------------------------------

class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def fuel(self):
        print("Car uses petrol")

class ElectricCar(Car):
    def battery(self):
        print("Electric car runs on battery")

ev = ElectricCar()
ev.move()
ev.fuel()
ev.battery()


# ---------------------------------------------------------
# 6. Multiple Inheritance
# ---------------------------------------------------------

class Writer:
    def write(self):
        print("Writing content")

class Speaker:
    def speak(self):
        print("Speaking to audience")

class Influencer(Writer, Speaker):
    pass

inf = Influencer()
inf.write()
inf.speak()


# ---------------------------------------------------------
# 7. MRO (Method Resolution Order)
# ---------------------------------------------------------

class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(A):
    def show(self):
        print("Class C")

class D(B, C):
    pass

d = D()
d.show()

print("\nMRO of class D:")
print(D.mro())


# ---------------------------------------------------------
# 8. Real-world Example: Bank System
# ---------------------------------------------------------

class Account:
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    def show_balance(self):
        print("Balance:", self.balance)

class SavingsAccount(Account):
    def add_interest(self):
        self.balance += self.balance * 0.05
        print("Interest added")

class CurrentAccount(Account):
    def overdraft(self):
        print("Overdraft facility available")

sa = SavingsAccount("Priyanshu", 10000)
sa.show_balance()
sa.add_interest()
sa.show_balance()

ca = CurrentAccount("Riya", 5000)
ca.show_balance()
ca.overdraft()


# ---------------------------------------------------------
# End of Day 32: Inheritance
# ---------------------------------------------------------

