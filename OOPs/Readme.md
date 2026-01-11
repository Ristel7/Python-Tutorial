# Day 31 — OOP Basics in Python

This lesson introduces Object-Oriented Programming from scratch.
It explains how to create classes, objects, attributes, and methods using clear examples.

## Topics Covered
- What is OOP
- Defining classes
- Creating objects
- Adding attributes
- Using constructors (__init__)
- Methods inside a class
- self keyword
- Multiple objects from same class
- Real-world example (Bank Account)

| Concept          | Meaning                    |
| ---------------- | -------------------------- |
| Class            | Blueprint of an object     |
| Object           | Instance of a class        |
| Attribute        | Data stored inside object  |
| Method           | Function inside a class    |
| `__init__()`     | Constructor                |
| `self`           | Refers to current object   |
| Multiple objects | Same class, different data |

# Day 32 — **Inheritance in Python**

This lesson explains inheritance, one of the core pillars of Object-Oriented Programming.
It shows how classes reuse and extend behavior through parent-child relationships.

## Topics Covered
- Single inheritance
- Inheriting constructors
- Method overriding
- super() keyword
- Multilevel inheritance
- Multiple inheritance
- Method Resolution Order (MRO)
- Real-world example (Bank system)

| Concept                | Meaning                                 |
| ---------------------- | --------------------------------------- |
| Inheritance            | Child class uses parent class features  |
| `super()`              | Access parent methods                   |
| Method overriding      | Child replaces parent behavior          |
| Single inheritance     | One parent, one child                   |
| Multilevel inheritance | Parent → Child → Grandchild             |
| Multiple inheritance   | Child with multiple parents             |
| MRO                    | Order Python follows to resolve methods |

# Day 36 — Encapsulation in Python

Encapsulation helps protect data and ensures controlled access to class attributes.
This lesson explains public, protected, and private members with practical examples.

## Topics Covered
- Public, protected, private members
- Name mangling
- Getter and setter methods
- @property decorator
- Real-world examples:
  - Bank account
  - ATM system


| Concept         | Meaning                         |
| --------------- | ------------------------------- |
| Encapsulation   | Protecting data                 |
| Public          | Accessible everywhere           |
| Protected       | Accessible within class & child |
| Private         | Hidden from outside             |
| Name Mangling   | How Python hides private data   |
| Getters/Setters | Controlled access               |
| `@property`     | Pythonic getter/setter          |

# Day 37 — Polymorphism in Python

Polymorphism allows the same method name to behave differently depending on the object.
This lesson demonstrates polymorphism using classes, inheritance, duck typing, and operator overloading.

## Topics Covered
- Same method, different behavior
- Duck typing
- Polymorphism with inheritance
- Method overriding
- Polymorphism via function arguments
- Operator overloading
- Built-in polymorphism
- Real-world examples:
  - Payment system
  - Notification service

| Concept               | Meaning                           |
| --------------------- | --------------------------------- |
| Polymorphism          | Same method, different behavior   |
| Duck typing           | Behavior matters, not type        |
| Method overriding     | Child changes parent behavior     |
| Function polymorphism | Same function, different objects  |
| Operator overloading  | Custom behavior for operators     |
| Built-in polymorphism | Same function works on many types |


# Day 38 — Abstraction in Python

Abstraction is one of the core pillars of Object-Oriented Programming.
It focuses on exposing only essential functionality and hiding internal logic.

## Topics Covered
- Abstract Base Classes (ABC)
- @abstractmethod decorator
- Concrete methods in abstract classes
- Enforcing structure using abstraction
- Why abstract classes cannot be instantiated
- Real-world examples:
  - Payment system
  - Notification system
  - Shape area calculation


