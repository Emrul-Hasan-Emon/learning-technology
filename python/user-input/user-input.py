"""
Python User Input Examples and Use Cases
==========================================

The input() function is used to get input from the user.
It displays a prompt and waits for the user to type and press Enter.
input() always returns a string, so type conversion may be needed.
"""

# ============================================================================
# 1. BASIC USER INPUT
# ============================================================================

# Example 1.1: Simple string input
def example_basic_string():
    """Get a simple string from the user"""
    name = input("What is your name? ")
    print(f"Hello, {name}!")


# Example 1.2: Getting multiple inputs
def example_multiple_inputs():
    """Get multiple inputs from the user"""
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    age = input("Enter age: ")
    print(f"Name: {first_name} {last_name}, Age: {age}")


# ============================================================================
# 2. TYPE CONVERSION
# ============================================================================

# Example 2.1: Converting input to integer
def example_int_conversion():
    """Convert string input to integer"""
    try:
        age = int(input("Enter your age: "))
        print(f"You are {age} years old")
        print(f"Next year you'll be {age + 1}")
    except ValueError:
        print("Error: Please enter a valid number")


# Example 2.2: Converting input to float
def example_float_conversion():
    """Convert string input to float for decimal numbers"""
    try:
        height = float(input("Enter your height in meters: "))
        print(f"Your height is {height}m")
    except ValueError:
        print("Error: Please enter a valid decimal number")


# Example 2.3: Converting input to boolean
def example_bool_conversion():
    """Convert string input to boolean"""
    response = input("Do you like Python? (yes/no): ").lower()
    if response in ['yes', 'y', 'true', '1']:
        print("Great! Welcome to Python!")
    elif response in ['no', 'n', 'false', '0']:
        print("Maybe you'll change your mind!")
    else:
        print("Invalid response")


# ============================================================================
# 3. INPUT VALIDATION
# ============================================================================

# Example 3.1: Validating number range
def example_validate_range():
    """Ensure input is within a specific range"""
    while True:
        try:
            score = int(input("Enter a score (0-100): "))
            if 0 <= score <= 100:
                print(f"Valid score: {score}")
                break
            else:
                print("Error: Score must be between 0 and 100")
        except ValueError:
            print("Error: Please enter a valid number")


# Example 3.2: Validating non-empty input
def example_validate_nonempty():
    """Ensure user doesn't submit empty input"""
    while True:
        name = input("Enter your name: ").strip()
        if name:
            print(f"Hello, {name}!")
            break
        else:
            print("Error: Name cannot be empty")


# Example 3.3: Validating input length
def example_validate_length():
    """Ensure input meets length requirements"""
    while True:
        password = input("Enter a password (min 8 characters): ")
        if len(password) >= 8:
            print("Password accepted!")
            break
        else:
            print("Error: Password must be at least 8 characters")


# Example 3.4: Validating against allowed values
def example_validate_choices():
    """Ensure input is one of allowed choices"""
    valid_choices = ['rock', 'paper', 'scissors']
    while True:
        choice = input(f"Choose one {valid_choices}: ").lower()
        if choice in valid_choices:
            print(f"You chose: {choice}")
            break
        else:
            print(f"Invalid choice. Please choose from {valid_choices}")


# ============================================================================
# 4. USE CASES
# ============================================================================

# USE CASE 1: Simple Calculator
def use_case_calculator():
    """Use case: Simple arithmetic calculator"""
    print("\n--- Simple Calculator ---")
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))
        
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("Error: Cannot divide by zero")
                return
            result = num1 / num2
        else:
            print("Error: Invalid operator")
            return
        
        print(f"{num1} {operator} {num2} = {result}")
    except ValueError:
        print("Error: Please enter valid numbers")


# USE CASE 2: Student Grade Management
def use_case_grade_calculator():
    """Use case: Calculate student grades and GPA"""
    print("\n--- Grade Calculator ---")
    try:
        student_name = input("Enter student name: ")
        num_subjects = int(input("How many subjects? "))
        
        total_marks = 0
        for i in range(num_subjects):
            marks = float(input(f"Enter marks for subject {i+1}: "))
            total_marks += marks
        
        average = total_marks / num_subjects
        
        if average >= 90:
            grade = 'A'
        elif average >= 80:
            grade = 'B'
        elif average >= 70:
            grade = 'C'
        else:
            grade = 'F'
        
        print(f"\nStudent: {student_name}")
        print(f"Average: {average:.2f}")
        print(f"Grade: {grade}")
    except ValueError:
        print("Error: Please enter valid numbers")


# USE CASE 3: Quiz Application
def use_case_quiz():
    """Use case: Simple quiz with scoring"""
    print("\n--- Quiz Application ---")
    questions = [
        ("What is the capital of France? ", "paris"),
        ("What is 2+2? ", "4"),
        ("What is the largest planet? ", "jupiter"),
    ]
    
    score = 0
    for question, answer in questions:
        user_answer = input(question).lower().strip()
        if user_answer == answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The answer is {answer}\n")
    
    print(f"Final Score: {score}/{len(questions)}")


# USE CASE 4: Shopping Cart
def use_case_shopping_cart():
    """Use case: Simple shopping cart system"""
    print("\n--- Shopping Cart ---")
    cart = {}
    
    while True:
        print("\n1. Add item\n2. View cart\n3. Checkout\n4. Exit")
        choice = input("Enter choice (1-4): ")
        
        if choice == '1':
            try:
                item_name = input("Item name: ")
                quantity = int(input("Quantity: "))
                price = float(input("Price per item: "))
                
                if item_name in cart:
                    cart[item_name]['quantity'] += quantity
                else:
                    cart[item_name] = {'quantity': quantity, 'price': price}
                
                print(f"Added {quantity} {item_name}(s) to cart")
            except ValueError:
                print("Error: Invalid input")
        
        elif choice == '2':
            print("\nCart Contents:")
            if not cart:
                print("Cart is empty")
            else:
                total = 0
                for item, details in cart.items():
                    subtotal = details['quantity'] * details['price']
                    print(f"{item}: {details['quantity']} x ${details['price']:.2f} = ${subtotal:.2f}")
                    total += subtotal
                print(f"Total: ${total:.2f}")
        
        elif choice == '3':
            total = sum(v['quantity'] * v['price'] for v in cart.values())
            print(f"\nChecking out... Total: ${total:.2f}")
            break
        
        elif choice == '4':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice")


# USE CASE 5: User Authentication
def use_case_login():
    """Use case: Simple login system"""
    print("\n--- Login System ---")
    
    # Hardcoded credentials (in real app, use secure database)
    valid_users = {
        'admin': 'password123',
        'user1': 'mypass456'
    }
    
    max_attempts = 3
    attempts = 0
    
    while attempts < max_attempts:
        username = input("Username: ")
        password = input("Password: ")
        
        if username in valid_users and valid_users[username] == password:
            print(f"Welcome, {username}!")
            return True
        else:
            attempts += 1
            remaining = max_attempts - attempts
            print(f"Invalid credentials. {remaining} attempts remaining")
    
    print("Login failed. Account locked.")
    return False


# USE CASE 6: To-Do List Manager
def use_case_todo_list():
    """Use case: Simple to-do list application"""
    print("\n--- To-Do List Manager ---")
    todos = []
    
    while True:
        print("\n1. Add task\n2. View tasks\n3. Mark complete\n4. Delete task\n5. Exit")
        choice = input("Enter choice (1-5): ")
        
        if choice == '1':
            task = input("Enter task: ")
            todos.append({'task': task, 'completed': False})
            print("Task added!")
        
        elif choice == '2':
            if not todos:
                print("No tasks")
            else:
                for i, todo in enumerate(todos, 1):
                    status = "✓" if todo['completed'] else "✗"
                    print(f"{i}. [{status}] {todo['task']}")
        
        elif choice == '3':
            if todos:
                try:
                    task_num = int(input("Task number to mark complete: "))
                    if 1 <= task_num <= len(todos):
                        todos[task_num - 1]['completed'] = True
                        print("Task marked complete!")
                except ValueError:
                    print("Invalid number")
        
        elif choice == '4':
            if todos:
                try:
                    task_num = int(input("Task number to delete: "))
                    if 1 <= task_num <= len(todos):
                        todos.pop(task_num - 1)
                        print("Task deleted!")
                except ValueError:
                    print("Invalid number")
        
        elif choice == '5':
            break
        
        else:
            print("Invalid choice")


# ============================================================================
# 5. ADVANCED PATTERNS
# ============================================================================

# Example 5.1: Loop until valid input
def example_loop_until_valid():
    """Keep asking until valid input is received"""
    while True:
        try:
            age = int(input("Enter your age: "))
            if age < 0:
                print("Age cannot be negative")
                continue
            if age > 150:
                print("Invalid age")
                continue
            print(f"Your age is {age}")
            break
        except ValueError:
            print("Please enter a valid number")


# Example 5.2: Using input with default values
def example_input_with_default():
    """Provide default values if user input is empty"""
    name = input("Enter name (default: Guest): ").strip() or "Guest"
    age = input("Enter age (default: 18): ").strip() or "18"
    print(f"Name: {name}, Age: {age}")


# ============================================================================
# MAIN FUNCTION - RUN EXAMPLES
# ============================================================================

def main():
    """Run interactive examples and use cases"""
    examples = {
        '1': ('Basic String Input', example_basic_string),
        '2': ('Multiple Inputs', example_multiple_inputs),
        '3': ('Integer Conversion', example_int_conversion),
        '4': ('Float Conversion', example_float_conversion),
        '5': ('Boolean Conversion', example_bool_conversion),
        '6': ('Validate Range', example_validate_range),
        '7': ('Validate Non-Empty', example_validate_nonempty),
        '8': ('Validate Length', example_validate_length),
        '9': ('Validate Choices', example_validate_choices),
        '10': ('Calculator', use_case_calculator),
        '11': ('Grade Calculator', use_case_grade_calculator),
        '12': ('Quiz', use_case_quiz),
        '13': ('Shopping Cart', use_case_shopping_cart),
        '14': ('Login System', use_case_login),
        '15': ('To-Do List', use_case_todo_list),
        '16': ('Loop Until Valid', example_loop_until_valid),
        '17': ('Input with Defaults', example_input_with_default),
    }
    
    while True:
        print("\n" + "="*50)
        print("Python User Input Examples")
        print("="*50)
        for key, (name, _) in examples.items():
            print(f"{key}. {name}")
        print("0. Exit")
        
        choice = input("\nSelect an example (0-17): ")
        
        if choice == '0':
            print("Goodbye!")
            break
        elif choice in examples:
            print(f"\n--- {examples[choice][0]} ---")
            examples[choice][1]()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
