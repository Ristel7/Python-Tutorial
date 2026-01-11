# ---------------------------------------------------------
# Day 38: Abstraction in Python
# ---------------------------------------------------------

# Abstraction is implemented using the abc module
from abc import ABC, abstractmethod


# ---------------------------------------------------------
# 1. Abstract Base Class
# ---------------------------------------------------------

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


# ---------------------------------------------------------
# 2. Child class implementing abstract methods
# ---------------------------------------------------------

class Car(Vehicle):
    def start(self):
        print("Car engine started")

    def stop(self):
        print("Car engine stopped")


class Bike(Vehicle):
    def start(self):
        print("Bike started with kick")

    def stop(self):
        print("Bike stopped")


car = Car()
bike = Bike()

print("Vehicle actions:")
car.start()
car.stop()

bike.start()
bike.stop()


# ---------------------------------------------------------
# 3. Abstract class with concrete method
# ---------------------------------------------------------

class BankAccount(ABC):
    def __init__(self, balance):
        self.balance = balance

    @abstractmethod
    def withdraw(self, amount):
        pass

    def show_balance(self):
        print("Balance:", self.balance)


class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")


account = SavingsAccount(5000)
account.show_balance()
account.withdraw(2000)
account.show_balance()


# ---------------------------------------------------------
# 4. Enforcing structure using abstraction
# ---------------------------------------------------------

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class UPI(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI")


class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")


def process_payment(method, amount):
    method.pay(amount)


print("\nPayment processing:")
process_payment(UPI(), 1000)
process_payment(CreditCard(), 2000)


# ---------------------------------------------------------
# 5. Abstract class cannot be instantiated
# ---------------------------------------------------------

# v = Vehicle()   # ❌ This will raise an error
# p = Payment()  # ❌ Cannot create object of abstract class


# ---------------------------------------------------------
# 6. Real-world Example: Notification System
# ---------------------------------------------------------

class Notification(ABC):

    @abstractmethod
    def send(self, message):
        pass


class EmailNotification(Notification):
    def send(self, message):
        print("Email sent:", message)


class SMSNotification(Notification):
    def send(self, message):
        print("SMS sent:", message)


def notify_user(notification):
    notification.send("Welcome to the platform!")


print("\nNotification system:")
notify_user(EmailNotification())
notify_user(SMSNotification())


# ---------------------------------------------------------
# 7. Abstract class as a contract
# ---------------------------------------------------------

class Shape(ABC):

    @abstractmethod
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

print("\nArea calculation:")
for s in shapes:
    print("Area:", s.area())


# ---------------------------------------------------------
# End of Day 38: Abstraction
# ---------------------------------------------------------
