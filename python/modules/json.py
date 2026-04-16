"""
JSON Module Examples in Python

The json module provides easy ways to encode and decode JSON data.
It's used for serializing Python objects to JSON and deserializing JSON to Python objects.
"""

import json
from datetime import datetime


# ============================================================================
# 1. Basic JSON Encoding (Python objects to JSON strings)
# ============================================================================

print("=" * 70)
print("1. JSON ENCODING (dumps)")
print("=" * 70)

# Convert Python dictionary to JSON string
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "coding", "hiking"]
}

json_string = json.dumps(person)
print("Original dictionary:")
print(person) # Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'hobbies': ['reading', 'coding', 'hiking']}
print("\nJSON string:") 
# Output: {"name": "Alice", "age": 30, "city": "New York", "hobbies": ["reading", "coding", "hiking"]}
print(json_string)
print(type(json_string))

# Convert Python list to JSON string
numbers = [1, 2, 3, 4, 5]
json_array = json.dumps(numbers)
print("\nList to JSON:")
print(json_array) # Output: [1, 2, 3, 4, 5]


# ============================================================================
# 2. Basic JSON Decoding (JSON strings to Python objects)
# ============================================================================

print("\n" + "=" * 70)
print("2. JSON DECODING (loads)")
print("=" * 70)

json_data = '{"name": "Bob", "age": 25, "city": "San Francisco"}'
print("JSON string:")
print(json_data) # Output: {"name": "Bob", "age": 25, "city": "San Francisco"}

parsed_data = json.loads(json_data)
print("\nParsed to Python dictionary:")
print(parsed_data) # Output: {'name': 'Bob', 'age': 25, 'city': 'San Francisco'}
print(f"Accessing name: {parsed_data['name']}") # Output: Accessing name: Bob
print(f"Accessing age: {parsed_data['age']}") # Output: Accessing age: 25


# ============================================================================
# 3. Pretty Printing JSON (with indentation)
# ============================================================================

print("\n" + "=" * 70)
print("3. PRETTY PRINTING JSON")
print("=" * 70)

company = {
    "name": "TechCorp",
    "employees": [
        {"id": 1, "name": "Alice", "position": "Manager"},
        {"id": 2, "name": "Bob", "position": "Developer"},
        {"id": 3, "name": "Charlie", "position": "Designer"}
    ],
    "location": "New York",
    "founded": 2015
}

# Normal dumps (compact)
print("Compact JSON:")
print(json.dumps(company))

# Pretty printed with indent
print("\nPretty printed JSON (indent=2):")
print(json.dumps(company, indent=2))

# With sort_keys
print("\nWith sorted keys:")
print(json.dumps(company, indent=2, sort_keys=True))


# ============================================================================
# 4. Writing to JSON Files (dump)
# ============================================================================

print("\n" + "=" * 70)
print("4. WRITING TO JSON FILES (dump)")
print("=" * 70)

# Sample data
students = [
    {"id": 101, "name": "Alice", "grade": "A"},
    {"id": 102, "name": "Bob", "grade": "B"},
    {"id": 103, "name": "Charlie", "grade": "A"}
]

# Write to file
filename = "students.json"
with open(filename, 'w') as f:
    json.dump(students, f, indent=2)

print(f"Data written to {filename}")

# Read the file to verify
with open(filename, 'r') as f:
    content = f.read()
    print(f"\nFile content:\n{content}")


# ============================================================================
# 5. Reading from JSON Files (load)
# ============================================================================

print("\n" + "=" * 70)
print("5. READING FROM JSON FILES (load)")
print("=" * 70)

with open(filename, 'r') as f:
    loaded_students = json.load(f)

print(f"Loaded data from {filename}:")
print(loaded_students)
print(f"\nFirst student: {loaded_students[0]}")
print(f"Second student's name: {loaded_students[1]['name']}")


# ============================================================================
# 6. Handling Different Data Types
# ============================================================================

print("\n" + "=" * 70)
print("6. HANDLING DIFFERENT DATA TYPES")
print("=" * 70)

# JSON supports: string, number, object, array, true, false, null
data_types = {
    "string": "Hello",
    "integer": 42,
    "float": 3.14,
    "boolean_true": True,
    "boolean_false": False,
    "null_value": None,
    "array": [1, 2, 3],
    "nested_object": {"key": "value"}
}

print("Python data types to JSON:")
json_output = json.dumps(data_types, indent=2)
print(json_output)

# Note: True/False in Python become true/false in JSON, None becomes null
print("\nJSON to Python mapping:")
print("- true -> True")
print("- false -> False")
print("- null -> None")


# ============================================================================
# 7. Custom Object Serialization (using default parameter)
# ============================================================================

print("\n" + "=" * 70)
print("7. CUSTOM OBJECT SERIALIZATION")
print("=" * 70)

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

def product_encoder(obj):
    """Convert custom objects to JSON-serializable format"""
    if isinstance(obj, Product):
        return {
            "name": obj.name,
            "price": obj.price,
            "quantity": obj.quantity
        }
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

# Create custom objects
product1 = Product("Laptop", 999.99, 5)
product2 = Product("Mouse", 29.99, 15)

products = [product1, product2]

print("Serializing custom objects:")
json_products = json.dumps(products, default=product_encoder, indent=2)
print(json_products)


# ============================================================================
# 8. Using JSONEncoder class (alternative approach)
# ============================================================================

print("\n" + "=" * 70)
print("8. CUSTOM JSONENCODER CLASS")
print("=" * 70)

class ProductEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Product):
            return {
                "name": obj.name,
                "price": obj.price,
                "quantity": obj.quantity
            }
        return super().default(obj)

product = Product("Keyboard", 79.99, 8)
json_output = json.dumps(product, cls=ProductEncoder, indent=2)
print("Using custom JSONEncoder class:")
print(json_output)


# ============================================================================
# 9. Error Handling
# ============================================================================

print("\n" + "=" * 70)
print("9. ERROR HANDLING")
print("=" * 70)

# Invalid JSON string
invalid_json = '{"name": "Alice", "age": 30,}'  # Trailing comma is invalid

try:
    result = json.loads(invalid_json)
except json.JSONDecodeError as e:
    print(f"JSONDecodeError: {e}")
    print(f"Error message: {e.msg}")
    print(f"Line: {e.lineno}, Column: {e.colno}")

# Non-serializable object
try:
    data = {"date": datetime.now()}
    json.dumps(data)
except TypeError as e:
    print(f"\nTypeError: {e}")
    print("Solution: Use custom encoder or convert to string first")


# ============================================================================
# 10. Using parse_float and parse_int parameters
# ============================================================================

print("\n" + "=" * 70)
print("10. CUSTOM PARSING")
print("=" * 70)

# Parse numbers as strings instead of floats
json_string = '{"price": 19.99, "quantity": 5}'

# Default parsing
default_parse = json.loads(json_string)
print("Default parsing:")
print(default_parse)
print(f"price type: {type(default_parse['price'])}")

# Custom parsing (numbers as strings)
custom_parse = json.loads(json_string, parse_float=str, parse_int=str)
print("\nCustom parsing (numbers as strings):")
print(custom_parse)
print(f"price type: {type(custom_parse['price'])}")


# ============================================================================
# 11. Summary and Best Practices
# ============================================================================

print("\n" + "=" * 70)
print("11. QUICK REFERENCE")
print("=" * 70)

reference = """
json.dumps(obj)      - Convert Python object to JSON string
json.loads(s)        - Convert JSON string to Python object
json.dump(obj, fp)   - Write Python object as JSON to file
json.load(fp)        - Read JSON from file and parse to Python object

Parameters:
- indent              - Pretty print with indentation
- sort_keys           - Sort dictionary keys in output
- default             - Custom serializer function
- cls                 - Custom JSONEncoder class
- parse_float         - Custom float parser
- parse_int           - Custom int parser

Type Mapping:
Python           JSON
dict      <->    object
list      <->    array
str       <->    string
int/float <->    number
True      <->    true
False     <->    false
None      <->    null
"""

print(reference)

# Clean up the test file
import os
if os.path.exists(filename):
    os.remove(filename)
    print(f"\nCleaned up: {filename}")
