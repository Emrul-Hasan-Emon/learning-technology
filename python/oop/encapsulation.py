"""
Python OOP - Encapsulation Examples
Encapsulation is the bundling of data and methods, with restricted access to internal details.
It uses private/protected attributes and public methods to control access.
"""

# Example 1: Basic Encapsulation with Private Attributes
class BankAccount:
    """A class demonstrating basic encapsulation with private attributes."""
    
    def __init__(self, account_holder, initial_balance=0):
        """Initialize a BankAccount with private balance attribute."""
        self.account_holder = account_holder
        self.__balance = initial_balance  # Private attribute (name mangling with __)
    
    def deposit(self, amount):
        """Public method to deposit money."""
        if amount > 0:
            self.__balance += amount
            return f"Deposited ${amount}. New balance: ${self.__balance}"
        return "Deposit amount must be positive."
    
    def withdraw(self, amount):
        """Public method to withdraw money."""
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew ${amount}. Remaining balance: ${self.__balance}"
        return "Invalid withdrawal amount."
    
    def get_balance(self):
        """Public method to check balance (read-only access)."""
        return self.__balance


# Example 2: Encapsulation with Properties (Getters and Setters)
class Temperature:
    """A class demonstrating encapsulation using @property decorators."""
    
    def __init__(self, celsius=0):
        """Initialize temperature in Celsius."""
        self._celsius = celsius  # Protected attribute (single underscore)
    
    @property
    def celsius(self):
        """Getter for Celsius temperature."""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Setter for Celsius temperature with validation."""
        if isinstance(value, (int, float)):
            self._celsius = value
        else:
            raise ValueError("Temperature must be a number.")
    
    @property
    def fahrenheit(self):
        """Getter for Fahrenheit temperature."""
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """Setter for Fahrenheit temperature (converts to Celsius)."""
        if isinstance(value, (int, float)):
            self._celsius = (value - 32) * 5/9
        else:
            raise ValueError("Temperature must be a number.")


# Example 3: Protected Attributes and Methods
class Vehicle:
    """A class demonstrating protected attributes and methods."""
    
    def __init__(self, brand, model, year):
        """Initialize a Vehicle."""
        self.brand = brand
        self.model = model
        self._year = year  # Protected attribute
        self._mileage = 0  # Protected attribute
    
    def drive(self, distance):
        """Public method to drive the vehicle."""
        if distance > 0:
            self._update_mileage(distance)
            return f"Drove {distance} miles."
        return "Distance must be positive."
    
    def _update_mileage(self, distance):
        """Protected method - should not be called directly from outside."""
        self._mileage += distance
    
    def get_info(self):
        """Public method to get vehicle info."""
        return f"{self._year} {self.brand} {self.model} ({self._mileage} miles)"


# Example 4: Encapsulation with Data Validation
class Student:
    """A class demonstrating encapsulation with validation."""
    
    def __init__(self, name, student_id, gpa=0.0):
        """Initialize a Student."""
        self._name = name
        self._student_id = student_id
        self._gpa = gpa
    
    @property
    def gpa(self):
        """Getter for GPA."""
        return self._gpa
    
    @gpa.setter
    def gpa(self, value):
        """Setter for GPA with validation."""
        if 0.0 <= value <= 4.0:
            self._gpa = value
        else:
            raise ValueError("GPA must be between 0.0 and 4.0")
    
    @property
    def name(self):
        """Getter for student name."""
        return self._name
    
    @property
    def student_id(self):
        """Getter for student ID."""
        return self._student_id
    
    def get_status(self):
        """Public method to get academic status."""
        if self._gpa >= 3.5:
            return "Excellent"
        elif self._gpa >= 3.0:
            return "Good"
        elif self._gpa >= 2.0:
            return "Satisfactory"
        else:
            return "Needs Improvement"


# Example 5: Encapsulation with Private Methods
class LibraryBook:
    """A class demonstrating encapsulation with private methods."""
    
    def __init__(self, title, author, isbn):
        """Initialize a LibraryBook."""
        self.title = title
        self.author = author
        self.__isbn = isbn  # Private attribute
        self.__is_checked_out = False
        self.__borrower = None
    
    def checkout(self, borrower_name):
        """Public method to checkout a book."""
        if self.__is_checked_out:
            return f"Book '{self.title}' is already checked out."
        
        self.__is_checked_out = True
        self.__borrower = borrower_name
        self.__log_transaction("checkout", borrower_name)
        return f"Book '{self.title}' checked out to {borrower_name}."
    
    def return_book(self):
        """Public method to return a book."""
        if not self.__is_checked_out:
            return f"Book '{self.title}' is not checked out."
        
        borrower = self.__borrower
        self.__is_checked_out = False
        self.__borrower = None
        self.__log_transaction("return", borrower)
        return f"Book '{self.title}' returned by {borrower}."
    
    def __log_transaction(self, transaction_type, person_name):
        """Private method - internal logging (not accessible from outside)."""
        print(f"[LOG] {transaction_type.upper()}: {person_name} - {self.title}")
    
    def get_status(self):
        """Public method to check book status."""
        if self.__is_checked_out:
            return f"'{self.title}' is checked out to {self.__borrower}"
        return f"'{self.title}' is available"


# Example 6: Encapsulation with Class Attributes
class Counter:
    """A class demonstrating encapsulation with shared class attributes."""
    
    _total_instances = 0  # Protected class attribute
    
    def __init__(self, start_value=0):
        """Initialize a Counter."""
        self.__value = start_value
        Counter._total_instances += 1
    
    def increment(self):
        """Increment the counter."""
        self.__value += 1
    
    def decrement(self):
        """Decrement the counter."""
        self.__value -= 1
    
    def get_value(self):
        """Get current value."""
        return self.__value
    
    @classmethod
    def get_total_instances(cls):
        """Get total number of Counter instances created."""
        return cls._total_instances


# ============================================================================
# EXAMPLES/DEMONSTRATIONS
# ============================================================================

if __name__ == "__main__":
    # Example 1: Basic Encapsulation
    print("=" * 60)
    print("Example 1: Basic Encapsulation with Private Attributes")
    print("=" * 60)
    account = BankAccount("Alice", 1000)
    print(account.deposit(500))
    print(account.withdraw(200))
    print(f"Current balance: ${account.get_balance()}")
    # account.__balance = 999999  # Cannot access directly (name mangling)
    
    # Example 2: Properties (Getters and Setters)
    print("\n" + "=" * 60)
    print("Example 2: Encapsulation with Properties")
    print("=" * 60)
    temp = Temperature(25)
    print(f"Temperature: {temp.celsius}°C = {temp.fahrenheit}°F")
    temp.fahrenheit = 86  # Set using Fahrenheit
    print(f"Temperature: {temp.celsius:.1f}°C = {temp.fahrenheit}°F")
    
    try:
        temp.celsius = "invalid"
    except ValueError as e:
        print(f"Error: {e}")
    
    # Example 3: Protected Attributes and Methods
    print("\n" + "=" * 60)
    print("Example 3: Protected Attributes and Methods")
    print("=" * 60)
    car = Vehicle("Toyota", "Camry", 2022)
    print(car.drive(50))
    print(car.drive(30))
    print(car.get_info())
    
    # Example 4: Validation
    print("\n" + "=" * 60)
    print("Example 4: Encapsulation with Data Validation")
    print("=" * 60)
    student1 = Student("Bob", "S001", 3.8)
    student2 = Student("Charlie", "S002", 2.5)
    print(f"{student1.name}: GPA {student1.gpa} - Status: {student1.get_status()}")
    print(f"{student2.name}: GPA {student2.gpa} - Status: {student2.get_status()}")
    
    student1.gpa = 3.9
    print(f"{student1.name}: GPA {student1.gpa} - Status: {student1.get_status()}")
    
    try:
        student1.gpa = 5.0  # Invalid GPA
    except ValueError as e:
        print(f"Error: {e}")
    
    # Example 5: Private Methods
    print("\n" + "=" * 60)
    print("Example 5: Encapsulation with Private Methods")
    print("=" * 60)
    book = LibraryBook("Python Programming", "John Doe", "ISBN-123")
    print(book.checkout("Diana"))
    print(book.get_status())
    print(book.return_book())
    print(book.get_status())
    
    # Example 6: Class Attributes
    print("\n" + "=" * 60)
    print("Example 6: Encapsulation with Class Attributes")
    print("=" * 60)
    counter1 = Counter(10)
    counter1.increment()
    counter1.increment()
    print(f"Counter 1 value: {counter1.get_value()}")
    
    counter2 = Counter(20)
    counter2.decrement()
    print(f"Counter 2 value: {counter2.get_value()}")
    
    print(f"Total Counter instances created: {Counter.get_total_instances()}")
