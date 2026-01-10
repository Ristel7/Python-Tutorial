# ---------------------------------------------------------
# Day 37: Polymorphism in Python
# ---------------------------------------------------------

# ---------------------------------------------------------
# 1. Polymorphism using same method name
# ---------------------------------------------------------

class Dog:
    def speak(self):
        print("Dog barks")


class Cat:
    def speak(self):
        print("Cat meows")


animals = [Dog(), Cat()]

print("Same method, different behavior:")
for animal in animals:
    animal.speak()


# ---------------------------------------------------------
# 2. Polymorphism without inheritance (Duck Typing)
# ---------------------------------------------------------
# If it looks like a duck and quacks like a duck, Python accepts it.

class FileLogger:
    def log(self):
        print("Logging to a file")


class DatabaseLogger:
    def log(self):
        print("Logging to a database")


def process_log(logger):
    logger.log()


print("\nDuck typing example:")
process_log(FileLogger())
process_log(DatabaseLogger())


# ---------------------------------------------------------
# 3. Polymorphism with inheritance
# ---------------------------------------------------------

class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def area(self):
        return self.l * self.w


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r


shapes = [Rectangle(4, 5), Circle(3)]

print("\nArea calculation using polymorphism:")
for shape in shapes:
    print("Area:", shape.area())


# ---------------------------------------------------------
# 4. Method overriding (runtime polymorphism)
# ---------------------------------------------------------

class Vehicle:
    def move(self):
        print("Vehicle is moving")


class Car(Vehicle):
    def move(self):
        print("Car is driving")


class Bike(Vehicle):
    def move(self):
        print("Bike is riding")


vehicles = [Vehicle(), Car(), Bike()]

print("\nMethod overriding:")
for v in vehicles:
    v.move()


# ---------------------------------------------------------
# 5. Polymorphism with function arguments
# ---------------------------------------------------------

class EmailService:
    def send(self):
        print("Sending email")


class SMSService:
    def send(self):
        print("Sending SMS")


def notify(service):
    service.send()


print("\nNotification system:")
notify(EmailService())
notify(SMSService())


# ---------------------------------------------------------
# 6. Operator Overloading (Compile-time style polymorphism)
# ---------------------------------------------------------

class Point:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return self.x + other.x


p1 = Point(10)
p2 = Point(20)

print("\nOperator overloading:")
print("Sum:", p1 + p2)


# ---------------------------------------------------------
# 7. Built-in polymorphism
# ---------------------------------------------------------

print("\nBuilt-in polymorphism examples:")
print(len("Python"))
print(len([1, 2, 3, 4]))
print(len({"a": 1, "b": 2}))


# ---------------------------------------------------------
# 8. Real-world example: Payment System
# ---------------------------------------------------------

class Payment:
    def pay(self, amount):
        pass


class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")


class UPI(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI")


class Cash(Payment):
    def pay(self, amount):
        print(f"Paid {amount} in Cash")


payments = [CreditCard(), UPI(), Cash()]

print("\nPayment processing:")
for method in payments:
    method.pay(500)


# ---------------------------------------------------------
# End of Day 37: Polymorphism
# ---------------------------------------------------------
