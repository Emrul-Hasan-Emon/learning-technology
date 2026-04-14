# Conditionals are used to perform different actions based on different conditions.
# Python supports the usual logical conditions from mathematics:
# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

# If Statement
# The if statement is used to execute code only if a specified condition is True.
a = 33
b = 200
if b > a:
    print("b is greater than a")  # Output - b is greater than a

# Indentation
# Python relies on indentation (whitespace at the beginning of a line) to define scope in the code.
a = 33
b = 200
if b > a:
    print("b is greater than a")

# If...Else Statement
# The else statement allows you to execute code when the condition is False.
a = 33
b = 200
if b > a:
    print("b is greater than a")  # Output - b is greater than a
else:
    print("a is greater than b")

a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("a is greater than b")  # Output - a is greater than b

# The elif Statement
# The elif keyword is pythonically named else if. It is used to execute code when the previous conditions are not true.
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")  # Output - a and b are equal

a = 200
b = 33
if a > b:
    print("a is greater than b")  # Output - a is greater than b
elif a == b:
    print("a and b are equal")
else:
    print("b is greater than a")

# If...Elif...Else
a = 200
b = 33
if a > b:
    print("a is greater than b")  # Output - a is greater than b
elif a == b:
    print("a and b are equal")
else:
    print("b is greater than a")

# Multiple Elif
x = 10
if x == 5:
    print("x is 5")
elif x == 10:
    print("x is 10")  # Output - x is 10
elif x == 15:
    print("x is 15")
else:
    print("x is something else")

# Short Hand If
# If you have only one statement to execute, you can put it on the same line as the if statement:
if 5 > 2:
    print("5 is greater than 2")  # Output - 5 is greater than 2

# Ternary Operator (Short Hand If...Else)
# If you have only one statement to execute, one for if, and one for else, you can use the ternary operator:
# Syntax: value_if_true if condition else value_if_false
a = 2
b = 330
print("A") if a > b else print("B")  # Output - B

# More comprehensive ternary example
x = 15
result = "x is greater than 10" if x > 10 else "x is less than or equal to 10"
print(result)  # Output - x is greater than 10

# Nested If
x = 41
if x > 10:
    print("Above 10,")  # Output - Above 10,
    if x > 20:
        print("and also above 20!")  # Output - and also above 20!
    else:
        print("but not above 20.")

# Multiple conditions with and keyword
# The and keyword is used to combine conditional statements:
a = 200
b = 15
c = 500
if a > b and c > a:
    print("Both conditions are True")  # Output - Both conditions are True

# Multiple conditions with or keyword
# The or keyword is used to combine conditional statements:
a = 200
b = 15
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")  # Output - At least one of the conditions is True

# Combining and / or
a = 200
b = 15
c = 500
if (a > b) and (c > a):
    print("Both conditions are True")  # Output - Both conditions are True

if (a > b) or (a > c):
    print("At least one condition is True")  # Output - At least one condition is True

# The not keyword
# The not keyword is used to reverse the result, returns True if the result is false:
a = 33
b = 200
if not a > b:
    print("a is NOT greater than b")  # Output - a is NOT greater than b

# Membership testing with in keyword
# Check if a value is in a list
fruits = ["apple", "banana", "cherry"]
if "apple" in fruits:
    print("Yes, apple is in the fruits list")  # Output - Yes, apple is in the fruits list

if "orange" in fruits:
    print("Orange is in the list")
else:
    print("Orange is not in the list")  # Output - Orange is not in the list

# Check if a value is NOT in a list
if "mango" not in fruits:
    print("mango is NOT in the fruits list")  # Output - mango is NOT in the fruits list

# Using conditionals with string comparison
name = "John"
if name == "John":
    print("Your name is John")  # Output - Your name is John

if len(name) > 3:
    print("Your name is longer than 3 characters")  # Output - Your name is longer than 3 characters

# Using conditionals with type checking
x = 100
if type(x) == int:
    print("x is an integer")  # Output - x is an integer

if isinstance(x, int):
    print("x is an instance of int")  # Output - x is an instance of int

# Case Study: Grading System
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"Score: {score}, Grade: {grade}")  # Output - Score: 85, Grade: B

# Case Study: Age Group Classification
age = 25
if age < 13:
    category = "Child"
elif age < 18:
    category = "Teenager"
elif age < 65:
    category = "Adult"
else:
    category = "Senior"
print(f"Age: {age}, Category: {category}")  # Output - Age: 25, Category: Adult

# Case Study: Login System
username = "admin"
password = "1234"
if username == "admin" and password == "1234":
    print("Login successful")  # Output - Login successful
else:
    print("Invalid credentials")

username = "user"
password = "5678"
if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid credentials")  # Output - Invalid credentials

# Case Study: Even or Odd
num = 7
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")  # Output - 7 is odd

# Case Study: Number Comparison
num1 = 10
num2 = 20
if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 < num2:
    print(f"{num1} is less than {num2}")  # Output - 10 is less than 20
else:
    print(f"{num1} is equal to {num2}")

# Case Study: Temperature Check
temperature = 35
if temperature > 30:
    print("It's hot outside")  # Output - It's hot outside
elif temperature > 20:
    print("It's warm outside")
elif temperature > 10:
    print("It's cool outside")
else:
    print("It's cold outside")

# Case Study: Pass or Fail
score = 45
if score >= 50:
    print("Pass")
else:
    print("Fail")  # Output - Fail

# Case Study: Discount Calculator
purchase_amount = 150
if purchase_amount > 200:
    discount = 0.20
elif purchase_amount > 100:
    discount = 0.10
elif purchase_amount > 50:
    discount = 0.05
else:
    discount = 0
final_price = purchase_amount * (1 - discount)
print(f"Original: ${purchase_amount}, Discount: {discount*100}%, Final: ${final_price}")  # Output - Original: $150, Discount: 10.0%, Final: $135.0

# Case Study: Multiple Conditions
age = 20
has_license = True
if age >= 18 and has_license:
    print("You can drive")  # Output - You can drive
else:
    print("You cannot drive")

age = 16
has_license = False
if age >= 18 and has_license:
    print("You can drive")
else:
    print("You cannot drive")  # Output - You cannot drive

# Case Study: Nested Conditions - Valid Triangle
side1 = 5
side2 = 5
side3 = 5
if side1 > 0 and side2 > 0 and side3 > 0:
    if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
        print("Valid triangle")  # Output - Valid triangle
    else:
        print("Invalid triangle")
else:
    print("Sides must be positive")

# Case Study: String Validation
text = "hello123"
if text.isalpha():
    print("Contains only alphabets")
elif text.isdigit():
    print("Contains only digits")
elif text.isalnum():
    print("Contains alphabets and digits")  # Output - Contains alphabets and digits
else:
    print("Contains special characters")

# Case Study: Check if list is empty
my_list = []
if my_list:
    print("List is not empty")
else:
    print("List is empty")  # Output - List is empty

my_list = [1, 2, 3]
if my_list:
    print("List is not empty")  # Output - List is not empty
else:
    print("List is empty")

# Case Study: String contains substring
text = "Python is awesome"
if "Python" in text:
    print("'Python' found in text")  # Output - 'Python' found in text
else:
    print("'Python' not found in text")

# Case Study: Multiple conditions with OR
day = "Sunday"
if day == "Saturday" or day == "Sunday":
    print("It's weekend")  # Output - It's weekend
else:
    print("It's weekday")

day = "Monday"
if day == "Saturday" or day == "Sunday":
    print("It's weekend")
else:
    print("It's weekday")  # Output - It's weekday

# Case Study: Range Check
x = 50
if 0 <= x <= 100:
    print("x is between 0 and 100")  # Output - x is between 0 and 100
else:
    print("x is outside the range")

# Conditional Expression (Ternary)
x = 5
y = 10
max_val = x if x > y else y
print(f"Maximum value: {max_val}")  # Output - Maximum value: 10

# Nested Ternary
x = 15
result = "x is small" if x < 10 else "x is medium" if x < 20 else "x is large"
print(result)  # Output - x is medium
