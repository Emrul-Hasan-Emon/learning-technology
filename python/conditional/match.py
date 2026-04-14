# Match Statement
# The match statement is used for pattern matching in Python 3.10+.
# It compares a value against multiple patterns and executes code for the first matching pattern.
# This is similar to switch/case statements in other languages but with more powerful pattern matching.

# Basic Match Statement
status = 200
match status:
    case 200:
        print("OK")  # Output - OK
    case 404:
        print("Not Found")
    case 500:
        print("Internal Server Error")
    case _:
        print("Unknown status")

# Match with Default Case
status = 201
match status:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case 500:
        print("Internal Server Error")
    case _:
        print("Unknown status")  # Output - Unknown status

# Wildcard Pattern (_)
# The underscore (_) acts as a catch-all pattern (default case)
day = 3
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")  # Output - Wednesday
    case _:
        print("Unknown day")

# Multiple Patterns (OR Pattern)
# Use the | (pipe) operator to match multiple patterns
color = "blue"
match color:
    case "red" | "green" | "blue":
        print("Primary color")  # Output - Primary color
    case "orange" | "purple" | "yellow":
        print("Secondary color")
    case _:
        print("Unknown color")

# Match with Strings
command = "help"
match command:
    case "help":
        print("Displaying help information...")  # Output - Displaying help information...
    case "exit":
        print("Exiting the program...")
    case "status":
        print("System status: OK")
    case _:
        print("Unknown command")

# Match with Numbers
number = 5
match number:
    case 0:
        print("Zero")
    case 1 | 2 | 3 | 4 | 5:
        print("One to Five")  # Output - One to Five
    case 6 | 7 | 8 | 9 | 10:
        print("Six to Ten")
    case _:
        print("Greater than 10")

# Match with Guard (if clause)
# Add conditions to patterns using if
x = 25
match x:
    case 0:
        print("Zero")
    case x if x < 0:
        print("Negative number")
    case x if x < 10:
        print("Single digit")
    case x if x < 100:
        print("Two digits")  # Output - Two digits
    case _:
        print("Three or more digits")

# Match with Sequences (Lists/Tuples)
point = (1, 2)
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"On Y-axis at {y}")
    case (x, 0):
        print(f"On X-axis at {x}")
    case (x, y):
        print(f"At ({x}, {y})")  # Output - At (1, 2)

point = (0, 5)
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"On Y-axis at {y}")  # Output - On Y-axis at 5
    case (x, 0):
        print(f"On X-axis at {x}")
    case (x, y):
        print(f"At ({x}, {y})")

# Match with Unpacking
# Destructure sequences and dictionaries in patterns
data = [1, 2, 3]
match data:
    case [x]:
        print(f"Single element: {x}")
    case [x, y]:
        print(f"Two elements: {x}, {y}")
    case [x, y, z]:
        print(f"Three elements: {x}, {y}, {z}")  # Output - Three elements: 1, 2, 3
    case _:
        print("Other number of elements")

# Match with Variable-length Sequences
numbers = [1, 2, 3, 4, 5]
match numbers:
    case []:
        print("Empty list")
    case [first]:
        print(f"Single element: {first}")
    case [first, *middle, last]:
        print(f"First: {first}, Middle: {middle}, Last: {last}")  # Output - First: 1, Middle: [2, 3, 4], Last: 5
    case _:
        print("Other list")

# Match with Dictionaries
person = {"name": "John", "age": 30}
match person:
    case {"name": name, "age": age}:
        print(f"Name: {name}, Age: {age}")  # Output - Name: John, Age: 30
    case {"name": name}:
        print(f"Name: {name}")
    case _:
        print("Unknown format")

# Match with Class Types
# Check and destructure class instances
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(3, 4)
match p:
    case Point(x=0, y=0):
        print("Origin")
    case Point(x=x, y=0):
        print(f"On X-axis at {x}")
    case Point(x=0, y=y):
        print(f"On Y-axis at {y}")
    case Point(x=x, y=y):
        print(f"At ({x}, {y})")  # Output - At (3, 4)

# Case Study: HTTP Status Code Handler
def handle_status(status_code):
    match status_code:
        case 200 | 201 | 202:
            return "Success"
        case 301 | 302 | 304:
            return "Redirection"
        case 400 | 401 | 403:
            return "Client Error"
        case 404:
            return "Not Found"
        case 500 | 502 | 503:
            return "Server Error"
        case _:
            return "Unknown Status"

print(handle_status(200))  # Output - Success
print(handle_status(404))  # Output - Not Found
print(handle_status(500))  # Output - Server Error

# Case Study: Calculator
def calculate(operation, a, b):
    match operation:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            if b == 0:
                return "Error: Division by zero"
            return a / b
        case _:
            return "Unknown operation"

print(calculate("+", 10, 5))  # Output - 15
print(calculate("-", 10, 5))  # Output - 5
print(calculate("*", 10, 5))  # Output - 50
print(calculate("/", 10, 5))  # Output - 2.0

# Case Study: Traffic Light
def traffic_light(color):
    match color.lower():
        case "red":
            return "Stop"
        case "yellow" | "amber":
            return "Prepare to stop"
        case "green":
            return "Go"
        case _:
            return "Invalid traffic light color"

print(traffic_light("Red"))  # Output - Stop
print(traffic_light("Yellow"))  # Output - Prepare to stop
print(traffic_light("Green"))  # Output - Go

# Case Study: Content Type Handler
def handle_content_type(content_type):
    match content_type:
        case "text/html":
            return "Render as HTML"
        case "application/json":
            return "Parse as JSON"
        case "image/png" | "image/jpeg" | "image/gif":
            return "Display as image"
        case "application/pdf":
            return "Display as PDF"
        case _:
            return "Unknown content type"

print(handle_content_type("application/json"))  # Output - Parse as JSON
print(handle_content_type("image/png"))  # Output - Display as image

# Case Study: API Response Handler
def handle_response(response):
    match response:
        case {"status": "success", "data": data}:
            return f"Success: {data}"
        case {"status": "error", "message": msg}:
            return f"Error: {msg}"
        case {"status": "pending"}:
            return "Request is still processing"
        case _:
            return "Invalid response format"

print(handle_response({"status": "success", "data": [1, 2, 3]}))  # Output - Success: [1, 2, 3]
print(handle_response({"status": "error", "message": "Not found"}))  # Output - Error: Not found

# Case Study: Coordinate Validator
def validate_coordinate(coord):
    match coord:
        case (0, 0):
            return "Origin"
        case (x, 0) if x > 0:
            return f"Positive X-axis"
        case (x, 0) if x < 0:
            return f"Negative X-axis"
        case (0, y) if y > 0:
            return f"Positive Y-axis"
        case (0, y) if y < 0:
            return f"Negative Y-axis"
        case (x, y) if x > 0 and y > 0:
            return "Quadrant I"
        case (x, y) if x < 0 and y > 0:
            return "Quadrant II"
        case (x, y) if x < 0 and y < 0:
            return "Quadrant III"
        case (x, y) if x > 0 and y < 0:
            return "Quadrant IV"
        case _:
            return "Invalid coordinate"

print(validate_coordinate((0, 0)))  # Output - Origin
print(validate_coordinate((3, 4)))  # Output - Quadrant I
print(validate_coordinate((-3, 4)))  # Output - Quadrant II

# Case Study: Grade Assignment
def assign_grade(score):
    match score:
        case s if s >= 90:
            return "A"
        case s if s >= 80:
            return "B"
        case s if s >= 70:
            return "C"
        case s if s >= 60:
            return "D"
        case _:
            return "F"

print(assign_grade(95))  # Output - A
print(assign_grade(85))  # Output - B
print(assign_grade(55))  # Output - F

# Case Study: Command Parser
def parse_command(cmd):
    match cmd.split():
        case ["help"]:
            return "Help: Available commands are 'help', 'status', 'quit'"
        case ["status"]:
            return "System is running normally"
        case ["quit"]:
            return "Exiting system..."
        case ["echo", *args]:
            return f"Echo: {' '.join(args)}"
        case ["set", key, value]:
            return f"Setting {key} to {value}"
        case _:
            return "Unknown command"

print(parse_command("help"))  # Output - Help: Available commands are 'help', 'status', 'quit'
print(parse_command("echo hello world"))  # Output - Echo: hello world
print(parse_command("set debug true"))  # Output - Setting debug to true

# Case Study: Type-based Routing
def process_data(data):
    match data:
        case int(x) if x > 0:
            return f"Positive integer: {x}"
        case int(x) if x < 0:
            return f"Negative integer: {x}"
        case int(x):
            return f"Zero"
        case str(s):
            return f"String with {len(s)} characters"
        case list(items):
            return f"List with {len(items)} items"
        case dict(d):
            return f"Dictionary with {len(d)} keys"
        case _:
            return f"Unknown type: {type(data)}"

print(process_data(42))  # Output - Positive integer: 42
print(process_data("hello"))  # Output - String with 5 characters
print(process_data([1, 2, 3]))  # Output - List with 3 items

# Case Study: Configuration Parser
def parse_config(config):
    match config:
        case {"mode": "dev", "debug": debug_level}:
            return f"Development mode with debug level {debug_level}"
        case {"mode": "prod", "secure": secure}:
            return f"Production mode with secure={secure}"
        case {"mode": mode, **rest}:
            return f"Mode: {mode}, Additional settings: {rest}"
        case _:
            return "Invalid configuration"

print(parse_config({"mode": "dev", "debug": 3}))  # Output - Development mode with debug level 3
print(parse_config({"mode": "prod", "secure": True}))  # Output - Production mode with secure=True

# Case Study: Nested Pattern Matching
def process_nested(data):
    match data:
        case {"user": {"name": name, "age": age}, "action": action}:
            return f"{name} (age {age}) performed {action}"
        case {"user": {"name": name}, "message": msg}:
            return f"Message from {name}: {msg}"
        case [first, *rest]:
            return f"First: {first}, Rest: {rest}"
        case _:
            return "Unmatched pattern"

print(process_nested({"user": {"name": "Alice", "age": 30}, "action": "login"}))
# Output - Alice (age 30) performed login

# Case Study: Validation with Guards and OR patterns
def validate_input(value):
    match value:
        case str(s) if len(s) == 0:
            return "Error: Empty string"
        case str(s) if len(s) > 100:
            return "Error: String too long"
        case int(n) | float(n) if n < 0:
            return "Error: Negative number"
        case int(n) | float(n) if n > 1000:
            return "Error: Number too large"
        case int(n) | float(n):
            return f"Valid number: {n}"
        case str(s):
            return f"Valid string: {s}"
        case _:
            return "Invalid input type"

print(validate_input(50))  # Output - Valid number: 50
print(validate_input("hello"))  # Output - Valid string: hello
print(validate_input(""))  # Output - Error: Empty string
print(validate_input(-5))  # Output - Error: Negative number
