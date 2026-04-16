# Modules in Python
# A module is a file containing Python definitions and statements.
# The file name is the module name with the suffix .py added.
# Modules help organize code into files and can be reused across applications.

# Import Entire Module
import math
print(math.pi)  # Output - 3.141592653589793
print(math.sqrt(16))  # Output - 4.0

# Import Specific Function from Module
from math import sqrt, pi
print(sqrt(25))  # Output - 5.0
print(pi)  # Output - 3.141592653589793

# Import Multiple Items
from math import sqrt, ceil, floor
print(sqrt(10))  # Output - 3.1622776601683795
print(ceil(4.3))  # Output - 5
print(floor(4.7))  # Output - 4

# Import with Alias
import math as m
print(m.sin(m.pi / 2))  # Output - 1.0

# Import Specific Item with Alias
from math import sqrt as square_root
print(square_root(9))  # Output - 3.0

# Import All from Module (Not Recommended)
# from math import *  # Not recommended - pollutes namespace

# List Module Contents
print(dir(math))
# Output - ['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', ...]

# Module Documentation
print(math.__name__)  # Output - math
print(math.__file__)  # Different based on installation

# Random Module
import random
print(random.random())  # Output - random float between 0 and 1
print(random.randint(1, 10))  # Output - random integer between 1 and 10
print(random.choice([1, 2, 3, 4, 5]))  # Output - random element from list

# Random Module - Shuffle
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)  # Output - shuffled list

# Random Module - Sample
sample = random.sample(range(1, 11), 3)
print(sample)  # Output - 3 random elements from range

# DateTime Module
from datetime import datetime, date, time, timedelta

# Get current date and time
now = datetime.now()
print(now)  # Output - current date and time
print(now.year)  # Output - 2026
print(now.month)  # Output - current month
print(now.day)  # Output - current day

# Create specific date
specific_date = date(2025, 12, 25)
print(specific_date)  # Output - 2025-12-25

# Create specific time
specific_time = time(14, 30, 0)
print(specific_time)  # Output - 14:30:00

# Date arithmetic
today = date.today()
tomorrow = today + timedelta(days=1)
next_week = today + timedelta(weeks=1)
print(f"Today: {today}, Tomorrow: {tomorrow}, Next week: {next_week}")

# OS Module (Operating System)
import os
print(os.getcwd())  # Output - current working directory
print(os.listdir('.'))  # Output - list of files in current directory

# Check if path exists
if os.path.exists('.'):
    print("Current directory exists")  # Output - Current directory exists

# Create directory
# os.mkdir('new_folder')  # Creates a new directory
# os.makedirs('path/to/folder')  # Creates nested directories

# Remove files and directories
# os.remove('file.txt')  # Removes a file
# os.rmdir('folder')  # Removes an empty directory

# OS Module - Path Operations
print(os.path.join('folder', 'file.txt'))  # Output - folder/file.txt or folder\file.txt
print(os.path.dirname('/path/to/file.txt'))  # Output - /path/to
print(os.path.basename('/path/to/file.txt'))  # Output - file.txt
print(os.path.splitext('file.txt'))  # Output - ('file', '.txt')

# JSON Module
import json

# Dictionary to JSON string
data = {"name": "John", "age": 30, "city": "NYC"}
json_string = json.dumps(data)
print(json_string)  # Output - {"name": "John", "age": 30, "city": "NYC"}

# JSON string to Dictionary
parsed_data = json.loads(json_string)
print(parsed_data)  # Output - {'name': 'John', 'age': 30, 'city': 'NYC'}

# Write to JSON file
# with open('data.json', 'w') as f:
#     json.dump(data, f)

# Read from JSON file
# with open('data.json', 'r') as f:
#     data = json.load(f)

# Re Module (Regular Expressions)
import re

# Pattern matching
text = "The price is 19.99"
pattern = r'\d+\.\d+'
match = re.search(pattern, text)
if match:
    print(f"Found: {match.group()}")  # Output - Found: 19.99

# Find all matches
pattern = r'\d+'
numbers = re.findall(pattern, text)
print(numbers)  # Output - ['19', '99']

# Replace pattern
new_text = re.sub(r'\d+', '#', text)
print(new_text)  # Output - The price is ##.##

# Split by pattern
pattern = r'\s+'
words = re.split(pattern, text)
print(words)  # Output - ['The', 'price', 'is', '19.99']

# Collections Module
from collections import Counter, defaultdict, OrderedDict

# Counter - Count occurrences
items = [1, 2, 2, 3, 3, 3, 4, 5, 5]
counter = Counter(items)
print(counter)  # Output - Counter({3: 3, 2: 2, 5: 2, 1: 1, 4: 1})
print(counter.most_common(2))  # Output - [(3, 3), (2, 2)]

# defaultdict - Dictionary with default values
def_dict = defaultdict(list)
def_dict['a'].append(1)
def_dict['a'].append(2)
print(def_dict)  # Output - defaultdict(<class 'list'>, {'a': [1, 2]})

# OrderedDict - Maintains insertion order (Python 3.7+ dict maintains order anyway)
ordered = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(ordered)  # Output - OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# String Module
from string import ascii_letters, digits, punctuation

print(ascii_letters)  # Output - abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(digits)  # Output - 0123456789
print(punctuation)  # Output - !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

# Itertools Module
from itertools import combinations, permutations, product, chain

items = ['a', 'b', 'c']
print(list(combinations(items, 2)))  # Output - [('a', 'b'), ('a', 'c'), ('b', 'c')]
print(list(permutations(items, 2)))  # Output - [('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'c'), ('c', 'a'), ('c', 'b')]
print(list(product([1, 2], ['a', 'b'])))  # Output - [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]

# Functools Module
from functools import reduce

# reduce function
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(f"Product: {product}")  # Output - Product: 120

# @lru_cache decorator for memoization
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))  # Output - 55

# Typing Module (for Type Hints)
from typing import List, Dict, Tuple, Optional, Union

def process_list(items: List[int]) -> int:
    return sum(items)

def get_user(user_id: int) -> Optional[Dict[str, Union[str, int]]]:
    if user_id == 1:
        return {"name": "John", "age": 30}
    return None

result = process_list([1, 2, 3, 4, 5])
print(result)  # Output - 15

# Pickle Module (Serialization)
import pickle

# Serialize object to bytes
data = {"name": "John", "age": 30}
pickled = pickle.dumps(data)
print(pickled[:20])  # Output - first 20 bytes

# Deserialize bytes to object
unpickled = pickle.loads(pickled)
print(unpickled)  # Output - {'name': 'John', 'age': 30}

# Pickle to file
# with open('data.pkl', 'wb') as f:
#     pickle.dump(data, f)

# Unpickle from file
# with open('data.pkl', 'rb') as f:
#     data = pickle.load(f)

# Sys Module
import sys

print(sys.version)  # Output - Python version
print(sys.platform)  # Output - operating system
print(sys.argv)  # Output - command line arguments

# Check Python version
if sys.version_info >= (3, 8):
    print("Python 3.8 or higher")  # Output - Python 3.8 or higher

# Time Module
import time

# Current time in seconds since epoch
current_time = time.time()
print(current_time)  # Output - seconds since epoch

# Sleep for seconds
# time.sleep(2)  # Pauses execution for 2 seconds

# Get current time tuple
time_tuple = time.localtime()
print(time_tuple)  # Output - time.struct_time

# Format time
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(formatted_time)  # Output - 2026-04-15 HH:MM:SS

# shutil Module (Shell utilities)
import shutil

# Copy file
# shutil.copy('source.txt', 'destination.txt')

# Copy directory
# shutil.copytree('source_dir', 'dest_dir')

# Remove directory tree
# shutil.rmtree('directory')

# Case Study: Module-Based Calculator
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

print(f"Add: {add(10, 5)}")  # Output - Add: 15
print(f"Subtract: {subtract(10, 5)}")  # Output - Subtract: 5
print(f"Multiply: {multiply(10, 5)}")  # Output - Multiply: 50
print(f"Divide: {divide(10, 5)}")  # Output - Divide: 2.0

# Case Study: Using Multiple Modules Together
import random
from datetime import datetime, timedelta

def generate_random_dates(count):
    dates = []
    base_date = datetime(2026, 1, 1)
    for _ in range(count):
        random_days = random.randint(0, 365)
        date = base_date + timedelta(days=random_days)
        dates.append(date)
    return dates

random_dates = generate_random_dates(5)
for date in random_dates:
    print(date)
# Output - 5 random dates in 2026

# Case Study: Data Processing with Multiple Modules
import json
import re
from datetime import datetime

# Sample data
email_list = "john@example.com, jane@example.com, bob@test.org"

# Extract emails using regex
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email_list)
print(f"Extracted emails: {emails}")

# Convert to JSON
data = {
    "emails": emails,
    "count": len(emails),
    "extracted_at": datetime.now().isoformat()
}
json_output = json.dumps(data, indent=2)
print(json_output)

# Case Study: File Operations with Modules
import os
from datetime import datetime

# Create file information
file_info = {
    "current_dir": os.getcwd(),
    "files": os.listdir('.')[:5],  # First 5 files
    "timestamp": datetime.now().isoformat(),
    "separator": os.sep
}

print(f"Current directory: {file_info['current_dir']}")
print(f"File separator: {file_info['separator']}")

# Case Study: Performance Analysis
import time

def timed_function():
    start = time.time()
    total = sum(range(1000000))
    end = time.time()
    return end - start

execution_time = timed_function()
print(f"Execution time: {execution_time:.4f} seconds")

# Case Study: Dictionary Operations with Collections
from collections import Counter
from string import ascii_letters

text = "hello world"
char_count = Counter(char for char in text if char in ascii_letters)
print(f"Character frequency: {dict(char_count)}")

# Case Study: Pattern Matching Examples
import re

# Email validation
email = "user@example.com"
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
is_valid_email = bool(re.match(email_pattern, email))
print(f"Valid email: {is_valid_email}")  # Output - Valid email: True

# Phone number extraction
text = "Call me at 555-123-4567 or 555.987.6543"
phone_pattern = r'\d{3}[-.]?\d{3}[-.]?\d{4}'
phones = re.findall(phone_pattern, text)
print(f"Phones found: {phones}")

# Case Study: Type Checking with Typing Module
from typing import List, Dict, Callable

def process_items(items: List[str]) -> Dict[str, int]:
    return {item: len(item) for item in items}

result = process_items(["hello", "world", "python"])
print(result)  # Output - {'hello': 5, 'world': 5, 'python': 6}

# Case Study: Sorting with Key Functions
import operator
from functools import partial

students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78}
]

# Sort by grade
sorted_students = sorted(students, key=lambda x: x['grade'], reverse=True)
for student in sorted_students:
    print(f"{student['name']}: {student['grade']}")
# Output - Bob: 92 Alice: 85 Charlie: 78

# Case Study: Caching with functools
from functools import lru_cache
import time

@lru_cache(maxsize=128)
def compute_factorial(n):
    if n <= 1:
        return 1
    return n * compute_factorial(n - 1)

print(f"Factorial: {compute_factorial(10)}")  # Output - Factorial: 3628800
print(f"Cache info: {compute_factorial.cache_info()}")  # Output - shows cache statistics

# Case Study: Creating Statistics Summary
import math

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

summary = {
    "count": len(numbers),
    "sum": sum(numbers),
    "mean": sum(numbers) / len(numbers),
    "min": min(numbers),
    "max": max(numbers),
    "range": max(numbers) - min(numbers)
}

for key, value in summary.items():
    print(f"{key}: {value}")
# Output - statistics summary

# Case Study: Random Simulation
import random

def simulate_dice_rolls(rolls):
    results = []
    for _ in range(rolls):
        results.append(random.randint(1, 6))
    return results

dice_rolls = simulate_dice_rolls(10)
print(f"Dice rolls: {dice_rolls}")

from collections import Counter
roll_counts = Counter(dice_rolls)
print(f"Frequency: {dict(roll_counts)}")

# Creating Custom Module (Example)
# Create a file named 'mymodule.py' with the following:
# def greeting(name):
#     print(f"Hello, {name}!")
# 
# Then import it:
# import mymodule
# mymodule.greeting("Alice")  # Output - Hello, Alice!

# Re-importing Modules
import importlib
import math

# Reload a module
# importlib.reload(math)

# Check if module is imported
if 'math' in __import__('sys').modules:
    print("math module is loaded")  # Output - math module is loaded

# Module.__name__ variable
print(__name__)  # Output - __main__ (when run as script)
# Output - module_name (when imported as module)

# Case Study: Command Line Argument Processing
import sys
import argparse

# Note: argparse requires command line arguments
# parser = argparse.ArgumentParser(description='Process some integers.')
# parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                     help='an integer for the accumulator')
# args = parser.parse_args()

# Case Study: Environment Variables
import os

# Get environment variable
home = os.environ.get('HOME', '/default/path')
print(f"Home directory: {home}")

# Set environment variable
# os.environ['MY_VAR'] = 'value'

# Case Study: Creating and Using Generators
from itertools import count, islice

# Infinite counter
counter = count(1)
limited = islice(counter, 5)
print(f"First 5 numbers: {list(limited)}")  # Output - First 5 numbers: [1, 2, 3, 4, 5]

# Case Study: Logging Module
import logging

# Basic logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
# Output - formatted log messages

# Case Study: ZIP File Operations
# import zipfile
# 
# with zipfile.ZipFile('archive.zip', 'w') as zf:
#     zf.write('file1.txt')
#     zf.write('file2.txt')
# 
# with zipfile.ZipFile('archive.zip', 'r') as zf:
#     zf.extractall()

# Case Study: CSV Module
import csv
# from io import StringIO
# 
# csv_data = """name,age,city
# John,30,NYC
# Jane,25,LA"""
# 
# reader = csv.DictReader(StringIO(csv_data))
# for row in reader:
#     print(row)

# Case Study: Decimal Module for Precise Arithmetic
from decimal import Decimal

price = Decimal('19.99')
quantity = Decimal('3')
total = price * quantity
print(f"Total: {total}")  # Output - Total: 59.97
