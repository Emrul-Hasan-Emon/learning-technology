# For Loops
# A for loop is used to iterate over a sequence (list, tuple, dictionary, set, or string).
# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

# Basic For Loop with List
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)  # Output - apple banana cherry

# For Loop with String
for char in "banana":
    print(char)  # Output - b a n a n a

# For Loop with Range
# The range() function returns a sequence of numbers
for x in range(6):
    print(x)  # Output - 0 1 2 3 4 5

# Range with Starting Point
for x in range(2, 6):
    print(x)  # Output - 2 3 4 5

# Range with Step
for x in range(2, 10, 2):
    print(x)  # Output - 2 4 6 8

# For Loop with Negative Range
for x in range(5, 0, -1):
    print(x)  # Output - 5 4 3 2 1

# For Loop with Else
for x in range(6):
    print(x)  # Output - 0 1 2 3 4 5
else:
    print("Finally finished!")  # Output - Finally finished!

# For Loop with Break Statement
for x in range(6):
    if x == 3:
        break
    print(x)  # Output - 0 1 2

# For Loop with Continue Statement
for x in range(6):
    if x == 3:
        continue
    print(x)  # Output - 0 1 2 4 5

# For Loop with Enumerate
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")  # Output - 0: apple 1: banana 2: cherry

# For Loop with Enumerate and Custom Start
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")  # Output - 1: apple 2: banana 3: cherry

# Nested For Loop
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")  # Output - i=0, j=0 i=0, j=1 i=1, j=0 i=1, j=1 i=2, j=0 i=2, j=1

# For Loop with Zip
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
for num, letter in zip(list1, list2):
    print(f"{num}: {letter}")  # Output - 1: a 2: b 3: c

# For Loop with Zip (Multiple Lists)
list1 = [1, 2, 3, 4]
list2 = ["a", "b", "c", "d"]
list3 = [10, 20, 30, 40]
for num, letter, val in zip(list1, list2, list3):
    print(f"{num}, {letter}, {val}")  # Output - 1, a, 10 2, b, 20 3, c, 30 4, d, 40

# For Loop with Dictionary
person = {"name": "John", "age": 36, "country": "Norway"}
for key in person:
    print(f"{key}: {person[key]}")  # Output - name: John age: 36 country: Norway

# For Loop with Dictionary using items()
person = {"name": "John", "age": 36, "country": "Norway"}
for key, value in person.items():
    print(f"{key}: {value}")  # Output - name: John age: 36 country: Norway

# For Loop with Dictionary using keys()
person = {"name": "John", "age": 36, "country": "Norway"}
for key in person.keys():
    print(key)  # Output - name age country

# For Loop with Dictionary using values()
person = {"name": "John", "age": 36, "country": "Norway"}
for value in person.values():
    print(value)  # Output - John 36 Norway

# For Loop with Set
fruits = {"apple", "banana", "cherry"}
for fruit in fruits:
    print(fruit)  # Output - apple banana cherry (order may vary)

# For Loop with Tuple
colors = ("red", "green", "blue")
for color in colors:
    print(color)  # Output - red green blue

# List Comprehension (One-liner For Loop)
numbers = [1, 2, 3, 4, 5]
squared = [x**2 for x in numbers]
print(squared)  # Output - [1, 4, 9, 16, 25]

# List Comprehension with Condition
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in numbers if x % 2 == 0]
print(evens)  # Output - [2, 4, 6, 8, 10]

# List Comprehension with Transformation
words = ["hello", "world", "python"]
lengths = [len(word) for word in words]
print(lengths)  # Output - [5, 5, 6]

# List Comprehension with Nested Loop
matrix = [[i*j for j in range(3)] for i in range(3)]
print(matrix)  # Output - [[0, 0, 0], [0, 1, 2], [0, 2, 4]]

# For Loop - Break with Label (using function)
def outer_loop():
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                return  # Breaks out of both loops
        print(f"Outer loop: i={i}")

outer_loop()  # Output - Outer loop: i=0

# For Loop - Continue Example
for i in range(5):
    if i == 2:
        continue
    print(i)  # Output - 0 1 3 4

# Case Study: Print Multiplication Table
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i*j:2d}", end=" ")
    print()
# Output - multiplication table from 1-10

# Case Study: Sum of List
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print(f"Sum: {total}")  # Output - Sum: 15

# Case Study: Find Maximum in List
numbers = [3, 7, 2, 9, 1, 5]
max_val = numbers[0]
for num in numbers:
    if num > max_val:
        max_val = num
print(f"Maximum: {max_val}")  # Output - Maximum: 9

# Case Study: Find Minimum in List
numbers = [3, 7, 2, 9, 1, 5]
min_val = numbers[0]
for num in numbers:
    if num < min_val:
        min_val = num
print(f"Minimum: {min_val}")  # Output - Minimum: 1

# Case Study: Reverse a List
numbers = [1, 2, 3, 4, 5]
reversed_list = []
for num in reversed(numbers):
    reversed_list.append(num)
print(reversed_list)  # Output - [5, 4, 3, 2, 1]

# Case Study: Count Occurrences
text = "hello world"
letter_count = {}
for char in text:
    if char != " ":
        letter_count[char] = letter_count.get(char, 0) + 1
print(letter_count)  # Output - {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}

# Case Study: Filter Elements
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print(even_numbers)  # Output - [2, 4, 6, 8, 10]

# Case Study: Transform Elements
prices = [10, 20, 30, 40, 50]
discounted = []
for price in prices:
    discounted.append(price * 0.9)
print(discounted)  # Output - [9.0, 18.0, 27.0, 36.0, 45.0]

# Case Study: Nested List Processing
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for element in row:
        print(f"{element:2d}", end=" ")
    print()
# Output - 1  2  3  4  5  6  7  8  9

# Case Study: Flatten Nested List
nested = [[1, 2], [3, 4], [5, 6]]
flattened = []
for sublist in nested:
    for item in sublist:
        flattened.append(item)
print(flattened)  # Output - [1, 2, 3, 4, 5, 6]

# Case Study: String Pattern Printing
for i in range(1, 6):
    print("*" * i)
# Output - * ** *** **** *****

# Case Study: String Pattern - Pyramid
for i in range(1, 6):
    print(" " * (5-i) + "*" * (2*i-1))
# Output - Pyramid pattern

# Case Study: Duplicate Check
numbers = [1, 2, 3, 2, 4, 1]
duplicates = []
for i, num in enumerate(numbers):
    for j in range(i+1, len(numbers)):
        if num == numbers[j] and num not in duplicates:
            duplicates.append(num)
print(f"Duplicates: {duplicates}")  # Output - Duplicates: [1, 2]

# Case Study: Merge Two Lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged = []
for item in list1:
    merged.append(item)
for item in list2:
    merged.append(item)
print(merged)  # Output - [1, 2, 3, 4, 5, 6]

# Case Study: Create Dictionary from Lists
keys = ["name", "age", "city"]
values = ["John", 30, "NYC"]
dictionary = {}
for key, value in zip(keys, values):
    dictionary[key] = value
print(dictionary)  # Output - {'name': 'John', 'age': 30, 'city': 'NYC'}

# Case Study: Generate Fibonacci Sequence
n = 10
fib_list = []
a, b = 0, 1
for _ in range(n):
    fib_list.append(a)
    a, b = b, a + b
print(fib_list)  # Output - [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Case Study: Calculate Factorial
n = 5
factorial = 1
for i in range(1, n+1):
    factorial *= i
print(f"Factorial of {n}: {factorial}")  # Output - Factorial of 5: 120

# Case Study: Prime Numbers
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

for num in range(1, 20):
    if is_prime(num):
        print(num, end=" ")
print()  # Output - 2 3 5 7 11 13 17 19

# Case Study: Search Element
search_list = [10, 20, 30, 40, 50, 60]
target = 40
found = False
for item in search_list:
    if item == target:
        found = True
        break
print(f"Found: {found}")  # Output - Found: True

# Case Study: Remove Duplicates
numbers = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)
print(unique)  # Output - [1, 2, 3, 4, 5]

# Case Study: Case Conversion
strings = ["hello", "world", "python"]
upper_strings = []
for s in strings:
    upper_strings.append(s.upper())
print(upper_strings)  # Output - ['HELLO', 'WORLD', 'PYTHON']

# Case Study: Even/Odd Separation
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = []
odds = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)
    else:
        odds.append(num)
print(f"Evens: {evens}")  # Output - Evens: [2, 4, 6, 8, 10]
print(f"Odds: {odds}")  # Output - Odds: [1, 3, 5, 7, 9]

# Case Study: Multiple Condition Loop
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78},
    {"name": "Diana", "grade": 88}
]
for student in students:
    if student["grade"] >= 80:
        print(f"{student['name']} passed with grade {student['grade']}")
# Output - Alice passed with grade 85 Bob passed with grade 92 Diana passed with grade 88

# Case Study: Group Processing
data = [("A", 1), ("B", 2), ("A", 3), ("B", 4), ("A", 5)]
groups = {}
for key, value in data:
    if key not in groups:
        groups[key] = []
    groups[key].append(value)
print(groups)  # Output - {'A': [1, 3, 5], 'B': [2, 4]}

# Case Study: Alternating Pattern
for i in range(10):
    if i % 2 == 0:
        print(f"{i} is even", end=" | ")
    else:
        print(f"{i} is odd", end=" | ")
print()
# Output - 0 is even | 1 is odd | 2 is even | 3 is odd | ...

# Case Study: Conditional Break with Message
for i in range(1, 11):
    if i == 7:
        print(f"Breaking at {i}")
        break
    print(i, end=" ")
print()  # Output - 1 2 3 4 5 6 Breaking at 7

# Case Study: Skip Pattern
for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i, end=" ")
print()  # Output - 1 2 4 5 7 8 10

# Case Study: Accumulate Running Total
numbers = [1, 2, 3, 4, 5]
running_total = []
total = 0
for num in numbers:
    total += num
    running_total.append(total)
print(running_total)  # Output - [1, 3, 6, 10, 15]

# Case Study: Filter and Transform
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = []
for num in numbers:
    if num > 5:
        result.append(num * 2)
print(result)  # Output - [12, 14, 16, 18, 20]

# Case Study: Word Frequency Counter
text = "the quick brown fox jumps over the lazy dog the"
words = text.split()
word_freq = {}
for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1
for word, count in word_freq.items():
    print(f"{word}: {count}")
# Output - word frequency count
