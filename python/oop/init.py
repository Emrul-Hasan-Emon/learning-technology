"""
Python OOP - __init__ Method Examples
The __init__ method is a constructor that initializes objects when created.
"""

# Example 1: Basic __init__ Usage
class Person:
    """A simple class demonstrating basic __init__ usage."""
    
    def __init__(self, name, age):
        """Initialize a Person with name and age."""
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Hello, my name is {self.name} and I'm {self.age} years old."


# Example 2: __init__ with Default Parameters
class Car:
    """A class demonstrating __init__ with default parameters."""
    
    def __init__(self, brand, model, year=2024):
        """Initialize a Car with brand, model, and optional year."""
        self.brand = brand
        self.model = model
        self.year = year
    
    def get_info(self):
        return f"{self.year} {self.brand} {self.model}"


# Example 3: __init__ with List/Dictionary Initialization
class Student:
    """A class demonstrating __init__ with mutable objects."""
    
    def __init__(self, name, student_id, courses=None):
        """Initialize a Student with name, ID, and optional course list."""
        self.name = name
        self.student_id = student_id
        self.courses = courses if courses is not None else []
    
    def add_course(self, course):
        self.courses.append(course)
    
    def get_courses(self):
        return f"{self.name}'s courses: {', '.join(self.courses)}"


# Example 4: __init__ with Multiple Instances
class Circle:
    """A class demonstrating multiple instances with __init__."""
    
    PI = 3.14159
    
    def __init__(self, radius):
        """Initialize a Circle with a radius."""
        self.radius = radius
    
    def area(self):
        return self.PI * self.radius ** 2
    
    def circumference(self):
        return 2 * self.PI * self.radius


# Example 5: Inheritance with __init__
class Animal:
    """Base class with __init__."""
    
    def __init__(self, name, species):
        """Initialize an Animal."""
        self.name = name
        self.species = species
    
    def sound(self):
        return "Some sound"


class Dog(Animal):
    """Derived class that extends Animal's __init__."""
    
    def __init__(self, name, breed, age):
        """Initialize a Dog with additional breed and age."""
        super().__init__(name, "Canine")
        self.breed = breed
        self.age = age
    
    def sound(self):
        return "Woof!"
    
    def describe(self):
        return f"{self.name} is a {self.age}-year-old {self.breed} {self.species}."


# Example 6: __init__ with Validation
class BankAccount:
    """A class demonstrating __init__ with input validation."""
    
    def __init__(self, account_holder, balance=0):
        """Initialize a BankAccount with validation."""
        if balance < 0:
            raise ValueError("Balance cannot be negative!")
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
    
    def get_balance(self):
        return f"Account holder: {self.account_holder}, Balance: ${self.balance}"


# ============================================================================
# EXAMPLES/DEMONSTRATIONS
# ============================================================================

if __name__ == "__main__":
    # Example 1: Basic Usage
    print("=" * 50)
    print("Example 1: Basic __init__ Usage")
    print("=" * 50)
    person1 = Person("Alice", 30)
    person2 = Person("Bob", 25)
    print(person1.greet())
    print(person2.greet())
    
    # Example 2: Default Parameters
    print("\n" + "=" * 50)
    print("Example 2: __init__ with Default Parameters")
    print("=" * 50)
    car1 = Car("Toyota", "Camry")
    car2 = Car("Honda", "Civic", 2022)
    print(car1.get_info())
    print(car2.get_info())
    
    # Example 3: List/Dictionary Initialization
    print("\n" + "=" * 50)
    print("Example 3: __init__ with Mutable Objects")
    print("=" * 50)
    student1 = Student("Charlie", "S001")
    student1.add_course("Python")
    student1.add_course("JavaScript")
    print(student1.get_courses())
    
    student2 = Student("Diana", "S002", ["Math", "Physics"])
    print(student2.get_courses())
    
    # Example 4: Multiple Instances
    print("\n" + "=" * 50)
    print("Example 4: Multiple Instances")
    print("=" * 50)
    circle1 = Circle(5)
    circle2 = Circle(10)
    print(f"Circle 1 - Radius: {circle1.radius}, Area: {circle1.area():.2f}, Circumference: {circle1.circumference():.2f}")
    print(f"Circle 2 - Radius: {circle2.radius}, Area: {circle2.area():.2f}, Circumference: {circle2.circumference():.2f}")
    
    # Example 5: Inheritance with __init__
    print("\n" + "=" * 50)
    print("Example 5: Inheritance with __init__")
    print("=" * 50)
    dog1 = Dog("Max", "German Shepherd", 5)
    dog2 = Dog("Buddy", "Golden Retriever", 3)
    print(dog1.describe())
    print(dog2.describe())
    print(f"{dog1.name} says: {dog1.sound()}")
    
    # Example 6: Validation
    print("\n" + "=" * 50)
    print("Example 6: __init__ with Validation")
    print("=" * 50)
    account1 = BankAccount("John Doe", 1000)
    print(account1.get_balance())
    print(account1.deposit(500))
    
    try:
        account2 = BankAccount("Jane Smith", -100)
    except ValueError as e:
        print(f"Error: {e}")
