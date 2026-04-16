"""
Exception Handling in Python - Try-Except Examples

Exception handling allows you to handle errors gracefully instead of crashing your program.
Use try-except blocks to catch and handle different types of errors.
"""


# ============================================================================
# 1. Basic Try-Except Block
# ============================================================================

print("=" * 70)
print("1. BASIC TRY-EXCEPT BLOCK")
print("=" * 70)

# Example 1: Division by zero
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# Example 2: Index out of range
try:
    numbers = [1, 2, 3]
    print(numbers[5])
except IndexError:
    print("Error: Index out of range!")

# Example 3: Key not found in dictionary
try:
    person = {"name": "Alice", "age": 30}
    print(person["city"])
except KeyError:
    print("Error: Key 'city' not found in dictionary!")


# ============================================================================
# 2. Multiple Except Blocks
# ============================================================================

print("\n" + "=" * 70)
print("2. MULTIPLE EXCEPT BLOCKS")
print("=" * 70)

user_input = "abc"

try:
    number = int(user_input)
    result = 100 / number
except ValueError:
    print(f"Error: '{user_input}' is not a valid integer!")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except Exception as e:
    print(f"Unexpected error: {e}")

# Example 2: Different exception types
filename = "nonexistent.txt"

try:
    with open(filename, 'r') as f:
        content = f.read()
except FileNotFoundError:
    print(f"Error: File '{filename}' not found!")
except IOError:
    print(f"Error: Cannot read file '{filename}'!")
except Exception as e:
    print(f"Unexpected error: {e}")


# ============================================================================
# 3. Catching Multiple Exceptions in One Block
# ============================================================================

print("\n" + "=" * 70)
print("3. CATCHING MULTIPLE EXCEPTIONS IN ONE BLOCK")
print("=" * 70)

try:
    data = [1, 2, 3]
    index = 10
    result = 100 / int("abc")  # This will raise ValueError
    print(data[index])
except (ValueError, IndexError, ZeroDivisionError) as e:
    print(f"Error caught: {type(e).__name__} - {e}")

# Example 2: Multiple exception types with list operations
try:
    action = "divide"
    
    if action == "divide":
        result = 10 / 0
    elif action == "index":
        nums = [1, 2]
        print(nums[5])
    elif action == "convert":
        num = int("text")
except (ZeroDivisionError, IndexError, ValueError) as error:
    print(f"Caught exception: {error}")


# ============================================================================
# 4. Try-Except-Else Block
# ============================================================================

print("\n" + "=" * 70)
print("4. TRY-EXCEPT-ELSE BLOCK")
print("=" * 70)

# The else block runs if NO exception occurs

user_input = "42"

try:
    number = int(user_input)
except ValueError:
    print(f"Error: '{user_input}' is not a valid number!")
else:
    result = number * 2
    print(f"Success! Input: {user_input}, Result: {result}")

# Example 2: File reading with else
try:
    numbers_str = "1,2,3,4,5"
    numbers = [int(n) for n in numbers_str.split(",")]
except ValueError:
    print("Error: Invalid numbers in the list!")
else:
    print(f"Numbers: {numbers}")
    print(f"Sum: {sum(numbers)}")
    print(f"Average: {sum(numbers) / len(numbers)}")


# ============================================================================
# 5. Try-Except-Finally Block
# ============================================================================

print("\n" + "=" * 70)
print("5. TRY-EXCEPT-FINALLY BLOCK")
print("=" * 70)

# The finally block ALWAYS runs, whether exception occurs or not

# Example 1: File handling
print("Example 1: File handling with finally")
try:
    # Simulate file operations
    print("  Opening file...")
    # with open("data.txt", 'r') as f:
    #     content = f.read()
    print("  File opened successfully!")
except FileNotFoundError:
    print("  Error: File not found!")
finally:
    print("  Closing file and cleaning up resources...")

# Example 2: Database connection
print("\nExample 2: Database connection simulation")
try:
    print("  Connecting to database...")
    # db = connect_to_database()
    print("  Connected!")
    # query = "SELECT * FROM users"
    # Execute query
    print("  Query executed!")
except Exception as e:
    print(f"  Error: {e}")
finally:
    print("  Closing database connection...")


# ============================================================================
# 6. Raising Exceptions
# ============================================================================

print("\n" + "=" * 70)
print("6. RAISING EXCEPTIONS")
print("=" * 70)

def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age > 150:
        raise ValueError("Age seems invalid!")
    return f"Valid age: {age}"

# Test with valid age
try:
    print(validate_age(25))
except ValueError as e:
    print(f"Error: {e}")

# Test with invalid age
try:
    print(validate_age(-5))
except ValueError as e:
    print(f"Error: {e}")


# ============================================================================
# 7. Custom Exception Classes
# ============================================================================

print("\n" + "=" * 70)
print("7. CUSTOM EXCEPTION CLASSES")
print("=" * 70)

class InsufficientFundsError(Exception):
    """Custom exception for insufficient funds"""
    pass

class InvalidAccountError(Exception):
    """Custom exception for invalid account"""
    pass

def withdraw_money(balance, amount):
    if amount <= 0:
        raise ValueError("Amount must be positive!")
    if balance < amount:
        raise InsufficientFundsError(f"You only have ${balance}, but trying to withdraw ${amount}")
    return balance - amount

# Test custom exceptions
try:
    balance = 100
    withdraw = 150
    new_balance = withdraw_money(balance, withdraw)
except InsufficientFundsError as e:
    print(f"Transaction failed: {e}")
except ValueError as e:
    print(f"Invalid input: {e}")

# Test successful transaction
try:
    balance = 100
    withdraw = 30
    new_balance = withdraw_money(balance, withdraw)
    print(f"Withdrawal successful! New balance: ${new_balance}")
except Exception as e:
    print(f"Error: {e}")


# ============================================================================
# 8. Exception Chaining
# ============================================================================

print("\n" + "=" * 70)
print("8. EXCEPTION CHAINING")
print("=" * 70)

def read_config_file(filename):
    try:
        with open(filename, 'r') as f:
            data = f.read()
        return int(data)  # Try to convert to integer
    except FileNotFoundError as e:
        raise RuntimeError(f"Configuration file not found: {filename}") from e
    except ValueError as e:
        raise RuntimeError(f"Invalid configuration format in {filename}") from e

try:
    config = read_config_file("config.txt")
except RuntimeError as e:
    print(f"Error: {e}")
    print(f"Caused by: {e.__cause__}")


# ============================================================================
# 9. Using finally with return Statement
# ============================================================================

print("\n" + "=" * 70)
print("9. FINALLY WITH RETURN STATEMENT")
print("=" * 70)

def process_data(data):
    try:
        result = int(data) * 2
        return result
    except ValueError:
        print("Error: Invalid data!")
        return None
    finally:
        print("Processing complete (finally block always runs)")

print(f"Result: {process_data('10')}")
print(f"Result: {process_data('invalid')}")


# ============================================================================
# 10. Common Built-in Exceptions
# ============================================================================

print("\n" + "=" * 70)
print("10. COMMON BUILT-IN EXCEPTIONS")
print("=" * 70)

exceptions_dict = {
    "ZeroDivisionError": "Division by zero: 10 / 0",
    "ValueError": "Invalid value: int('abc')",
    "TypeError": "Wrong type: '5' + 5",
    "IndexError": "Index out of range: [1,2][5]",
    "KeyError": "Key not found: {'a': 1}['b']",
    "FileNotFoundError": "File not found: open('nonexistent.txt')",
    "AttributeError": "Attribute not found: object.nonexistent",
    "NameError": "Variable not defined: undefined_var",
    "ImportError": "Cannot import: from nonexistent import something",
    "RuntimeError": "Raised to indicate invalid operation",
}

for exc_name, description in exceptions_dict.items():
    print(f"  {exc_name:<20} - {description}")


# ============================================================================
# 11. Try-Except in Loops
# ============================================================================

print("\n" + "=" * 70)
print("11. TRY-EXCEPT IN LOOPS")
print("=" * 70)

# Convert list of strings to integers, skip invalid ones
numbers_str = ["1", "2", "abc", "4", "def", "6"]

converted = []
skipped = []

for num_str in numbers_str:
    try:
        converted.append(int(num_str))
    except ValueError:
        skipped.append(num_str)

print(f"Original: {numbers_str}")
print(f"Converted: {converted}")
print(f"Skipped (invalid): {skipped}")

# Example 2: Process list of items with partial failures
print("\nProcessing items:")
items = [10, 0, 5, -1, 8]

for i, item in enumerate(items):
    try:
        result = 100 / item
        print(f"  Item {i}: 100/{item} = {result}")
    except ZeroDivisionError:
        print(f"  Item {i}: Cannot divide by zero!")
    except ZeroDivisionError:
        print(f"  Item {i}: Invalid!")


# ============================================================================
# 12. Try-Except with Context Managers
# ============================================================================

print("\n" + "=" * 70)
print("12. TRY-EXCEPT WITH CONTEXT MANAGERS")
print("=" * 70)

# Example: Reading multiple files
print("Reading files (with graceful error handling):")
files = ["file1.txt", "file2.txt", "file3.txt"]

for filename in files:
    try:
        with open(filename, 'r') as f:
            content = f.read()
        print(f"  {filename}: Read successfully")
    except FileNotFoundError:
        print(f"  {filename}: Not found (skipped)")
    except IOError as e:
        print(f"  {filename}: Error reading - {e}")
    finally:
        print(f"  {filename}: Finished processing")


# ============================================================================
# 13. Real-World Example: Data Processing
# ============================================================================

print("\n" + "=" * 70)
print("13. REAL-WORLD EXAMPLE: DATA PROCESSING")
print("=" * 70)

def parse_user_data(data_list):
    """Parse user data from a list of dictionaries"""
    users = []
    errors = []
    
    for i, data in enumerate(data_list):
        try:
            # Validate required fields
            if not isinstance(data, dict):
                raise TypeError("Each item must be a dictionary")
            
            name = data.get("name")
            age = data.get("age")
            email = data.get("email")
            
            if not name:
                raise ValueError("Name is required")
            if not age:
                raise ValueError("Age is required")
            
            # Convert age to integer
            age = int(age)
            
            if age < 0 or age > 150:
                raise ValueError(f"Invalid age: {age}")
            
            # Create user object
            user = {
                "name": name,
                "age": age,
                "email": email or "N/A"
            }
            users.append(user)
            
        except (TypeError, ValueError, KeyError) as e:
            errors.append(f"Row {i}: {e}")
    
    return users, errors

# Test with mixed valid and invalid data
test_data = [
    {"name": "Alice", "age": 25, "email": "alice@example.com"},
    {"name": "Bob", "age": "thirty"},  # Invalid age
    {"name": "", "age": 30},  # Missing name
    {"name": "Charlie", "age": 35},  # No email (optional)
]

users, errors = parse_user_data(test_data)

print("Valid users:")
for user in users:
    print(f"  {user}")

if errors:
    print("\nErrors found:")
    for error in errors:
        print(f"  {error}")


# ============================================================================
# 14. Assert Statements (Alternative to Try-Except)
# ============================================================================

print("\n" + "=" * 70)
print("14. ASSERT STATEMENTS")
print("=" * 70)

def calculate_discount(price, discount_percent):
    assert price >= 0, "Price cannot be negative"
    assert 0 <= discount_percent <= 100, "Discount must be between 0 and 100"
    return price * (1 - discount_percent / 100)

# Valid case
try:
    result = calculate_discount(100, 20)
    print(f"Discounted price: ${result}")
except AssertionError as e:
    print(f"Assertion failed: {e}")

# Invalid case
try:
    result = calculate_discount(-50, 20)
except AssertionError as e:
    print(f"Assertion failed: {e}")


# ============================================================================
# 15. Best Practices for Exception Handling
# ============================================================================

print("\n" + "=" * 70)
print("15. BEST PRACTICES SUMMARY")
print("=" * 70)

best_practices = """
RULE 1: Catch Specific Exceptions
  ✓ Good:  except ValueError:
  ✗ Bad:   except:  (catches all, including system exits)

RULE 2: Don't Ignore Exceptions
  ✓ Good:  except ValueError as e: print(f"Error: {e}")
  ✗ Bad:   except ValueError: pass  (silently ignores error)

RULE 3: Use Finally for Cleanup
  ✓ Always use finally for resource cleanup (files, connections)

RULE 4: Create Custom Exceptions
  ✓ Create custom exception classes for domain-specific errors

RULE 5: Provide Context
  ✓ Include error messages that help understand what went wrong

RULE 6: Use Else Block
  ✓ Use else for code that should only run if no exception occurs

RULE 7: Re-raise Exceptions if Needed
  ✓ Re-raise exceptions after logging: raise

RULE 8: Don't Catch Too Broad
  ✗ except Exception:  (too broad, use specific exceptions)
  ✗ except:           (catches everything including KeyboardInterrupt)

RULE 9: Avoid Nested Try-Except
  ✓ Prefer helper functions over deeply nested exception handlers

RULE 10: Log Exceptions
  ✓ Log exception details for debugging and monitoring
"""

print(best_practices)


# ============================================================================
# 16. Example: Defensive Programming
# ============================================================================

print("\n" + "=" * 70)
print("16. EXAMPLE: DEFENSIVE PROGRAMMING")
print("=" * 70)

def safe_divide(a, b, default=None):
    """Safely divide two numbers with error handling"""
    try:
        # Type checking
        if not isinstance(a, (int, float)):
            raise TypeError(f"First argument must be numeric, got {type(a).__name__}")
        if not isinstance(b, (int, float)):
            raise TypeError(f"Second argument must be numeric, got {type(b).__name__}")
        
        # Division
        return a / b
    
    except ZeroDivisionError:
        print("Warning: Division by zero, returning default value")
        return default
    except TypeError as e:
        print(f"Type error: {e}")
        return default
    except Exception as e:
        print(f"Unexpected error: {e}")
        return default

# Test cases
print(f"10 / 2 = {safe_divide(10, 2)}")
print(f"10 / 0 = {safe_divide(10, 0, default=0)}")
print(f"'10' / 2 = {safe_divide('10', 2)}")
print(f"10 / '2' = {safe_divide(10, '2')}")
