# Classes and Objects in Python
# A class is a blueprint for objects, and objects are instances of a class

# ==============================================================================
# Example 1: Basic Class Definition and Object Creation
# ==============================================================================

class Dog:
    """A simple Dog class"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        return f"{self.name} says: Woof!"
    
    def get_age(self):
        return f"{self.name} is {self.age} years old"


# Creating objects (instances) of the Dog class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print("--- Example 1: Basic Class and Objects ---")
print(dog1.bark())
print(dog2.get_age())
print()


# ==============================================================================
# Example 2: Instance Variables and Methods
# ==============================================================================

class Car:
    """A Car class with instance variables and methods"""
    
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0
    
    def accelerate(self, increase):
        self.speed += increase
        return f"{self.brand} {self.model} accelerated to {self.speed} km/h"
    
    def brake(self, decrease):
        self.speed = max(0, self.speed - decrease)
        return f"{self.brand} {self.model} slowed down to {self.speed} km/h"
    
    def display_info(self):
        return f"{self.year} {self.brand} {self.model}, current speed: {self.speed} km/h"


print("--- Example 2: Instance Variables and Methods ---")
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Civic", 2023)

print(car1.accelerate(60))
print(car1.display_info())
print(car2.display_info())
print()


# ==============================================================================
# Example 3: Class Variables (Shared Across Instances)
# ==============================================================================

class Student:
    """A Student class with class and instance variables"""
    
    student_count = 0  # Class variable - shared by all instances
    
    def __init__(self, name, student_id):
        self.name = name  # Instance variable - unique to each object
        self.student_id = student_id
        Student.student_count += 1
    
    def display_info(self):
        return f"Student: {self.name}, ID: {self.student_id}"
    
    @classmethod
    def get_total_students(cls):
        """Class method that accesses class variables"""
        return f"Total students: {cls.student_count}"


print("--- Example 3: Class Variables ---")
student1 = Student("Alice", 101)
student2 = Student("Bob", 102)
student3 = Student("Charlie", 103)

print(student1.display_info())
print(student2.display_info())
print(Student.get_total_students())
print()


# ==============================================================================
# Example 4: Different Types of Methods
# ==============================================================================

class Calculator:
    """A Calculator class demonstrating different method types"""
    
    pi = 3.14159  # Class variable
    
    def __init__(self, name):
        self.name = name  # Instance variable
    
    # Instance method - operates on instance
    def add(self, a, b):
        return f"{self.name}: {a} + {b} = {a + b}"
    
    # Class method - operates on class
    @classmethod
    def multiply_by_pi(cls, value):
        return f"Value × π = {value * cls.pi}"
    
    # Static method - doesn't depend on instance or class
    @staticmethod
    def is_even(number):
        return f"{number} is {'even' if number % 2 == 0 else 'odd'}"


print("--- Example 4: Different Method Types ---")
calc = Calculator("MyCalc")
print(calc.add(5, 3))
print(Calculator.multiply_by_pi(2))
print(Calculator.is_even(7))
print()


# ==============================================================================
# Example 5: Multiple Objects with Different States
# ==============================================================================

class BankAccount:
    """A BankAccount class demonstrating object state"""
    
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
        self.transactions = []
    
    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposit: +{amount}")
        return f"{amount} deposited. New balance: {self.balance}"
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: -{amount}")
            return f"{amount} withdrawn. New balance: {self.balance}"
        else:
            return "Insufficient funds!"
    
    def get_statement(self):
        return f"Account: {self.account_holder}, Balance: {self.balance}"


print("--- Example 5: Multiple Objects with Different States ---")
account1 = BankAccount("John", 1000)
account2 = BankAccount("Jane", 500)

print(account1.deposit(500))
print(account2.deposit(1000))
print(account1.withdraw(200))
print(account2.withdraw(100))
print(account1.get_statement())
print(account2.get_statement())
print()


# ==============================================================================
# Example 6: Object Attributes and Accessing Them
# ==============================================================================

class Person:
    """A Person class demonstrating object attributes"""
    
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
    
    def update_city(self, new_city):
        self.city = new_city
    
    def __str__(self):
        return f"{self.name}, {self.age} years old, from {self.city}"


print("--- Example 6: Object Attributes ---")
person = Person("Alice", 30, "New York")
print(f"Name: {person.name}")
print(f"Age: {person.age}")
print(f"City: {person.city}")
print(f"Full info: {person}")

person.update_city("Los Angeles")
print(f"Updated city: {person.city}")
print()


# ==============================================================================
# Example 7: Comparing Objects
# ==============================================================================

class Book:
    """A Book class for demonstrating object comparison"""
    
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"
    
    def __eq__(self, other):
        """Check if two books are the same"""
        if isinstance(other, Book):
            return (self.title == other.title and 
                    self.author == other.author and 
                    self.year == other.year)
        return False


print("--- Example 7: Comparing Objects ---")
book1 = Book("Python 101", "John Doe", 2020)
book2 = Book("Python 101", "John Doe", 2020)
book3 = Book("Java Basics", "Jane Smith", 2021)

print(f"Book1: {book1}")
print(f"Book2: {book2}")
print(f"Book3: {book3}")
print(f"Book1 == Book2: {book1 == book2}")
print(f"Book1 == Book3: {book1 == book3}")
