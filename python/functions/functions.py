# Functions
# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

# Creating a Function
def my_function():
    print("Hello from a function")

# Calling a Function
my_function()  # Output - Hello from a function

# Function with Parameters
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Output - Hello, Alice!
greet("Bob")    # Output - Hello, Bob!

# Function with Multiple Parameters
def add(a, b):
    print(f"{a} + {b} = {a + b}")

add(5, 3)  # Output - 5 + 3 = 8

# Return Statement
def multiply(a, b):
    return a * b

result = multiply(4, 5)
print(result)  # Output - 20

# Return Multiple Values
def divide(a, b):
    quotient = a / b
    remainder = a % b
    return quotient, remainder

q, r = divide(17, 5)
print(f"Quotient: {q}, Remainder: {r}")  # Output - Quotient: 3.4, Remainder: 2

# Default Parameter Values
def greet_with_default(name="User"):
    print(f"Hello, {name}!")

greet_with_default()      # Output - Hello, User!
greet_with_default("Eva") # Output - Hello, Eva!

# Keyword Arguments
def describe_person(name, age, city):
    print(f"{name} is {age} years old and lives in {city}")

describe_person(name="John", age=30, city="NYC")    # Output - John is 30 years old and lives in NYC
describe_person(age=25, city="LA", name="Jane")     # Output - Jane is 25 years old and lives in LA

# Arbitrary Arguments (*args)
def print_args(*args):
    for arg in args:
        print(arg)

print_args(1, 2, 3, "hello")    # Output - 1 2 3 hello
print_args("apple", "banana")   # Output - apple banana

# Arbitrary Keyword Arguments (**kwargs)
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="John", age=30, city="NYC")
# Output - name: John age: 30 city: NYC

# Combining *args and **kwargs
def combined_args(*args, **kwargs):
    print("Positional arguments:")
    for arg in args:
        print(f"  {arg}")
    print("Keyword arguments:")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

combined_args(1, 2, 3, name="John", age=30)
# Output - Positional arguments: 1 2 3 Keyword arguments: name: John age: 30

# List as Argument
def modify_list(items):
    items.append(4)

numbers = [1, 2, 3]
modify_list(numbers)
print(numbers)  # Output - [1, 2, 3, 4]

# Dictionary as Argument
def update_dict(data):
    data["city"] = "NYC"

person = {"name": "John", "age": 30}
update_dict(person)
print(person)  # Output - {'name': 'John', 'age': 30, 'city': 'NYC'}

# Function with Docstring
def calculate_area(radius):
    """
    Calculate the area of a circle.
    
    Args:
        radius: The radius of the circle
        
    Returns:
        The area of the circle
    """
    import math
    return math.pi * radius ** 2

print(calculate_area(5))  # Output - 78.53981633974483
print(calculate_area.__doc__)  # Output - The docstring

# Lambda Functions (Anonymous Functions)
square = lambda x: x ** 2
print(square(5))  # Output - 25

add_lambda = lambda x, y: x + y
print(add_lambda(3, 4))  # Output - 7

# Lambda with Conditional
check_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check_even(4))  # Output - Even
print(check_even(5))  # Output - Odd

# Lambda with Map
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output - [1, 4, 9, 16, 25]

# Lambda with Filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output - [2, 4, 6, 8, 10]

# Lambda with Sort
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)  # Output - [('Charlie', 78), ('Alice', 85), ('Bob', 92)]

# Higher Order Functions - Function as Parameter
def apply_operation(a, b, operation):
    return operation(a, b)

def multiply_func(x, y):
    return x * y

result = apply_operation(5, 3, multiply_func)
print(result)  # Output - 15

# Higher Order Functions - Returning Functions
def get_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

times_5 = get_multiplier(5)
print(times_5(10))  # Output - 50

# Closure
def outer(x):
    def inner(y):
        return x + y
    return inner

add_5 = outer(5)
print(add_5(10))  # Output - 15
print(add_5(20))  # Output - 25

# Recursion - Factorial
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output - 120

# Recursion - Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))  # Output - 8

# Recursion - Sum of List
def sum_list(items):
    if len(items) == 0:
        return 0
    else:
        return items[0] + sum_list(items[1:])

print(sum_list([1, 2, 3, 4, 5]))  # Output - 15

# Type Hints
def add_typed(a: int, b: int) -> int:
    return a + b

print(add_typed(5, 3))  # Output - 8

# Type Hints with Multiple Types
from typing import Union, List

def process_data(data: Union[int, str]) -> str:
    return f"Processed: {data}"

print(process_data(42))      # Output - Processed: 42
print(process_data("hello")) # Output - Processed: hello

# Function with List Parameter and Type Hint
def sum_numbers(numbers: List[int]) -> int:
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_numbers([1, 2, 3, 4, 5]))  # Output - 15

# Case Study: Even or Odd
def is_even(n):
    return n % 2 == 0

print(is_even(5))   # Output - False
print(is_even(10))  # Output - True

# Case Study: Prime Number Check
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(17))  # Output - True
print(is_prime(10))  # Output - False

# Case Study: Find Maximum
def find_max(*args):
    if len(args) == 0:
        return None
    max_val = args[0]
    for num in args[1:]:
        if num > max_val:
            max_val = num
    return max_val

print(find_max(5, 2, 9, 1, 8))  # Output - 9

# Case Study: Calculate GCD
def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

print(gcd(48, 18))  # Output - 6

# Case Study: String Reversal
def reverse_string(s):
    return s[::-1]

print(reverse_string("hello"))  # Output - olleh

# Case Study: Palindrome Check
def is_palindrome(text):
    clean_text = text.lower().replace(" ", "")
    return clean_text == clean_text[::-1]

print(is_palindrome("racecar"))     # Output - True
print(is_palindrome("hello"))       # Output - False
print(is_palindrome("A man a plan a canal Panama"))  # Output - True

# Case Study: List Average
def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

print(calculate_average([10, 20, 30, 40]))  # Output - 25.0

# Case Study: Filter List by Condition
def filter_even(numbers):
    result = []
    for num in numbers:
        if num % 2 == 0:
            result.append(num)
    return result

print(filter_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # Output - [2, 4, 6, 8, 10]

# Case Study: Count Occurrences
def count_occurrences(items, target):
    count = 0
    for item in items:
        if item == target:
            count += 1
    return count

print(count_occurrences([1, 2, 2, 3, 2, 4], 2))  # Output - 3

# Case Study: Remove Duplicates
def remove_duplicates(items):
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result

print(remove_duplicates([1, 2, 2, 3, 3, 3, 4, 5, 5]))  # Output - [1, 2, 3, 4, 5]

# Case Study: Sort Dictionary by Value
def sort_dict_by_value(d):
    return dict(sorted(d.items(), key=lambda x: x[1]))

data = {"apple": 5, "banana": 2, "cherry": 8, "date": 3}
print(sort_dict_by_value(data))  # Output - {'banana': 2, 'date': 3, 'apple': 5, 'cherry': 8}

# Case Study: Merge Two Lists
def merge_lists(list1, list2):
    return list1 + list2

print(merge_lists([1, 2, 3], [4, 5, 6]))  # Output - [1, 2, 3, 4, 5, 6]

# Case Study: Binary Search
def binary_search(sorted_list, target):
    left, right = 0, len(sorted_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

print(binary_search([1, 3, 5, 7, 9, 11, 13], 7))  # Output - 3

# Case Study: Power Function with Default
def power(base, exponent=2):
    return base ** exponent

print(power(5))      # Output - 25
print(power(5, 3))   # Output - 125

# Case Study: Validate Email
def is_valid_email(email):
    return "@" in email and "." in email

print(is_valid_email("user@example.com"))  # Output - True
print(is_valid_email("invalid.email"))     # Output - False

# Case Study: Calculate Discount
def apply_discount(price, discount_percent):
    return price * (1 - discount_percent / 100)

print(apply_discount(100, 20))  # Output - 80.0

# Case Study: Generate Range
def number_range(start, end, step=1):
    result = []
    current = start
    while current <= end:
        result.append(current)
        current += step
    return result

print(number_range(1, 10, 2))  # Output - [1, 3, 5, 7, 9]

# Case Study: String Frequency
def char_frequency(text):
    freq = {}
    for char in text:
        if char != " ":
            freq[char] = freq.get(char, 0) + 1
    return freq

print(char_frequency("hello world"))  # Output - {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}

# Case Study: Age Classifier
def classify_age(age):
    if age < 13:
        return "Child"
    elif age < 18:
        return "Teenager"
    elif age < 65:
        return "Adult"
    else:
        return "Senior"

print(classify_age(10))   # Output - Child
print(classify_age(15))   # Output - Teenager
print(classify_age(30))   # Output - Adult

# Case Study: Grade Assignment
def assign_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print(assign_grade(85))  # Output - B
print(assign_grade(92))  # Output - A

# Case Study: Matrix Sum
def matrix_sum(matrix):
    total = 0
    for row in matrix:
        for element in row:
            total += element
    return total

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix_sum(matrix))  # Output - 45

# Case Study: Transpose Matrix
def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

matrix = [[1, 2, 3], [4, 5, 6]]
print(transpose_matrix(matrix))  # Output - [[1, 4], [2, 5], [3, 6]]

# Case Study: String to List of Words
def split_words(text):
    return text.split()

print(split_words("Hello world Python programming"))  # Output - ['Hello', 'world', 'Python', 'programming']

# Case Study: Capitalize Words
def capitalize_words(text):
    return " ".join([word.capitalize() for word in text.split()])

print(capitalize_words("hello world python"))  # Output - Hello World Python

# Case Study: Sum of Digits
def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

print(sum_of_digits(12345))  # Output - 15

# Case Study: Armstrong Number
def is_armstrong(n):
    digits = str(n)
    num_digits = len(digits)
    total = sum(int(digit) ** num_digits for digit in digits)
    return total == n

print(is_armstrong(153))  # Output - True
print(is_armstrong(100))  # Output - False

# Case Study: Dictionary to List of Tuples
def dict_to_tuples(d):
    return list(d.items())

data = {"name": "John", "age": 30, "city": "NYC"}
print(dict_to_tuples(data))  # Output - [('name', 'John'), ('age', 30), ('city', 'NYC')]

# Case Study: Nested Function for Validation
def validate_input(value, min_val, max_val):
    def is_in_range(val):
        return min_val <= val <= max_val
    return is_in_range(value)

print(validate_input(50, 0, 100))   # Output - True
print(validate_input(150, 0, 100))  # Output - False

# Case Study: Decorator Example
def timer_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"{func.__name__} completed")
        return result
    return wrapper

@timer_decorator
def slow_function():
    print("Processing...")
    return "Done"

slow_function()
# Output - Calling slow_function... Processing... slow_function completed Done

# Case Study: Memoization with Decorator
def memoize(func):
    cache = {}
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    return wrapper

@memoize
def fib_memo(n):
    if n <= 1:
        return n
    return fib_memo(n - 1) + fib_memo(n - 2)

print(fib_memo(10))  # Output - 55

# Case Study: Default Arguments for Configuration
def create_user(name, email, role="user", active=True):
    return {
        "name": name,
        "email": email,
        "role": role,
        "active": active
    }

print(create_user("John", "john@example.com"))
# Output - {'name': 'John', 'email': 'john@example.com', 'role': 'user', 'active': True}

print(create_user("Jane", "jane@example.com", role="admin"))
# Output - {'name': 'Jane', 'email': 'jane@example.com', 'role': 'admin', 'active': True}

# Case Study: Function Composition
def compose(*functions):
    def composed(x):
        for func in reversed(functions):
            x = func(x)
        return x
    return composed

def add_5(x):
    return x + 5

def multiply_2(x):
    return x * 2

def square(x):
    return x ** 2

operation = compose(square, multiply_2, add_5)
print(operation(10))  # Output - (10+5)*2)^2 = 30^2 = 900

# Case Study: Chained Comparisons
def in_range(value, low, high):
    return low <= value <= high

print(in_range(50, 0, 100))   # Output - True
print(in_range(150, 0, 100))  # Output - False

# Case Study: Any/All with Custom Function
def all_positive(*numbers):
    return all(num > 0 for num in numbers)

def any_negative(*numbers):
    return any(num < 0 for num in numbers)

print(all_positive(1, 2, 3, 4, 5))     # Output - True
print(all_positive(1, 2, -3, 4, 5))    # Output - False
print(any_negative(1, 2, 3, -4, 5))    # Output - True
print(any_negative(1, 2, 3, 4, 5))     # Output - False
