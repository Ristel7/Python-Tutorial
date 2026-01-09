# ---------------------------------------------------------
# Day 36: Encapsulation in Python
# ---------------------------------------------------------

# ---------------------------------------------------------
# 1. Public Members
# ---------------------------------------------------------

class Student:
    def __init__(self, name, age):
        self.name = name     # public
        self.age = age      # public


student = Student("Priyanshu", 21)

print("Public access:")
print(student.name)
print(student.age)


# ---------------------------------------------------------
# 2. Protected Members (Single underscore)
# ---------------------------------------------------------

class Employee:
    def __init__(self, name, salary):
        self._name = name       # protected
        self._salary = salary  # protected


emp = Employee("Riya", 50000)

print("\nProtected access (allowed but discouraged):")
print(emp._name)
print(emp._salary)


# ---------------------------------------------------------
# 3. Private Members (Double underscore)
# ---------------------------------------------------------

class BankAccount:
    def __init__(self, holder, balance):
        self.holder = holder
        self.__balance = balance   # private

    def show_balance(self):
        print("Balance:", self.__balance)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")


account = BankAccount("Priyanshu", 10000)

print("\nUsing public methods:")
account.show_balance()
account.deposit(2000)
account.withdraw(3000)
account.show_balance()

# print(account.__balance)  # ❌ Error (private)


# ---------------------------------------------------------
# 4. Name Mangling (How private works internally)
# ---------------------------------------------------------

print("\nAccessing private variable using name mangling:")
print(account._BankAccount__balance)


# ---------------------------------------------------------
# 5. Getters and Setters (Controlled Access)
# ---------------------------------------------------------

class User:
    def __init__(self, username, password):
        self.__password = password
        self.username = username

    def get_password(self):
        return "Access Denied"

    def set_password(self, new_password):
        if len(new_password) >= 8:
            self.__password = new_password
        else:
            print("Password too short")


user = User("admin", "python123")

print("\nUsing getter & setter:")
print(user.get_password())
user.set_password("short")
user.set_password("NewStrongPass")


# ---------------------------------------------------------
# 6. Property Decorator (@property)
# ---------------------------------------------------------

class Product:
    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value > 0:
            self.__price = value
        else:
            print("Invalid price")


p = Product(500)

print("\nUsing property:")
print(p.price)
p.price = 1000
print(p.price)


# ---------------------------------------------------------
# 7. Real-world Example: ATM System
# ---------------------------------------------------------

class ATM:
    def __init__(self, balance):
        self.__balance = balance

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Transaction failed")
        else:
            self.__balance -= amount
            print("Please collect cash")

    def check_balance(self):
        print("Balance:", self.__balance)


atm = ATM(8000)

print("\nATM operations:")
atm.check_balance()
atm.withdraw(2000)
atm.check_balance()


# ---------------------------------------------------------
# End of Day 36: Encapsulation
# ---------------------------------------------------------
