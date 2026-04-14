# While Loops
# With the while loop we can execute a set of statements as long as a condition is true.
# The while loop requires relevant variables to be ready, typically you will need to initialize a variable.

# Basic While Loop
i = 1
while i < 6:
    print(i)  # Output - 1 2 3 4 5
    i += 1

# While Loop with Break
i = 1
while i < 6:
    if i == 3:
        break
    print(i)  # Output - 1 2
    i += 1

# While Loop with Continue
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)  # Output - 1 2 4 5 6

# While Loop with Else
i = 1
while i < 6:
    print(i)  # Output - 1 2 3 4 5
    i += 1
else:
    print("i is no longer less than 6")  # Output - i is no longer less than 6

# While Loop with Input (do-while simulation)
# Python doesn't have do-while, but we can simulate it
user_input = None
while user_input != "quit":
    user_input = input("Enter a command (or 'quit' to exit): ")
    if user_input != "quit":
        print(f"You entered: {user_input}")

# While Loop with Flag
found = False
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
index = 0
target = 7
while index < len(numbers) and not found:
    if numbers[index] == target:
        print(f"Found {target} at index {index}")  # Output - Found 7 at index 6
        found = True
    index += 1

# While Loop with Counter
count = 0
while count < 5:
    print(f"Count: {count}")  # Output - Count: 0 1 2 3 4
    count += 1

# Nested While Loop
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(f"({i},{j})", end=" ")  # Output - (1,1) (1,2) (1,3) (2,1) ...
        j += 1
    print()
    i += 1

# While Loop with Multiple Conditions
x = 1
y = 10
while x < y and x != 5:
    print(x)  # Output - 1 2 3 4
    x += 1

# While Loop with OR Condition
status = "running"
iterations = 0
while status == "running" or iterations < 3:
    print(f"Iteration {iterations}")  # Output - Iteration 0 1 2
    iterations += 1
    if iterations == 2:
        status = "stopped"

# While Loop Countdown
countdown = 5
while countdown > 0:
    print(countdown)  # Output - 5 4 3 2 1
    countdown -= 1
print("Blastoff!")  # Output - Blastoff!

# While Loop with String
password = ""
while password != "secret":
    password = input("Enter password: ")
    if password != "secret":
        print("Wrong password, try again")
    else:
        print("Access granted!")  # Output - Access granted!

# Case Study: Sum of Numbers
n = 1
total = 0
while n <= 5:
    total += n
    n += 1
print(f"Sum: {total}")  # Output - Sum: 15

# Case Study: Multiplication Table with While
multiplier = 5
i = 1
while i <= 10:
    print(f"{multiplier} x {i} = {multiplier*i}")
    i += 1
# Output - 5x1=5, 5x2=10, ..., 5x10=50

# Case Study: Factorial Calculation
n = 5
factorial = 1
i = 1
while i <= n:
    factorial *= i
    i += 1
print(f"Factorial of {n}: {factorial}")  # Output - Factorial of 5: 120

# Case Study: Fibonacci Sequence
n = 10
a, b = 0, 1
count = 0
while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1
print()  # Output - 0 1 1 2 3 5 8 13 21 34

# Case Study: Average Calculation
numbers = []
i = 1
while i <= 5:
    num = int(input(f"Enter number {i}: "))
    numbers.append(num)
    i += 1
average = sum(numbers) / len(numbers)
print(f"Average: {average}")

# Case Study: Find Minimum in List
numbers = [5, 2, 9, 1, 7, 3]
min_val = numbers[0]
index = 1
while index < len(numbers):
    if numbers[index] < min_val:
        min_val = numbers[index]
    index += 1
print(f"Minimum: {min_val}")  # Output - Minimum: 1

# Case Study: Find Maximum in List
numbers = [5, 2, 9, 1, 7, 3]
max_val = numbers[0]
index = 1
while index < len(numbers):
    if numbers[index] > max_val:
        max_val = numbers[index]
    index += 1
print(f"Maximum: {max_val}")  # Output - Maximum: 9

# Case Study: Reverse a List
numbers = [1, 2, 3, 4, 5]
reversed_list = []
index = len(numbers) - 1
while index >= 0:
    reversed_list.append(numbers[index])
    index -= 1
print(reversed_list)  # Output - [5, 4, 3, 2, 1]

# Case Study: Search Element
search_list = [10, 20, 30, 40, 50]
target = 30
index = 0
found = False
while index < len(search_list):
    if search_list[index] == target:
        print(f"Found {target} at index {index}")  # Output - Found 30 at index 2
        found = True
        break
    index += 1
if not found:
    print(f"{target} not found")

# Case Study: Count Occurrences
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
target = 3
count = 0
index = 0
while index < len(numbers):
    if numbers[index] == target:
        count += 1
    index += 1
print(f"{target} appears {count} times")  # Output - 3 appears 3 times

# Case Study: Filter Elements
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = []
index = 0
while index < len(numbers):
    if numbers[index] % 2 == 0:
        evens.append(numbers[index])
    index += 1
print(evens)  # Output - [2, 4, 6, 8, 10]

# Case Study: Remove Duplicates
numbers = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique = []
index = 0
while index < len(numbers):
    if numbers[index] not in unique:
        unique.append(numbers[index])
    index += 1
print(unique)  # Output - [1, 2, 3, 4, 5]

# Case Study: String Reversal
text = "hello"
reversed_text = ""
index = len(text) - 1
while index >= 0:
    reversed_text += text[index]
    index -= 1
print(reversed_text)  # Output - olleh

# Case Study: Digit Sum
num = 12345
digit_sum = 0
while num > 0:
    digit_sum += num % 10
    num //= 10
print(f"Sum of digits: {digit_sum}")  # Output - Sum of digits: 15

# Case Study: Prime Number Check
n = 17
is_prime = True
divisor = 2
while divisor * divisor <= n:
    if n % divisor == 0:
        is_prime = False
        break
    divisor += 1
if is_prime:
    print(f"{n} is prime")  # Output - 17 is prime
else:
    print(f"{n} is not prime")

# Case Study: Generate Prime Numbers
limit = 20
num = 2
primes = []
while num <= limit:
    is_prime = True
    divisor = 2
    while divisor * divisor <= num:
        if num % divisor == 0:
            is_prime = False
            break
        divisor += 1
    if is_prime:
        primes.append(num)
    num += 1
print(primes)  # Output - [2, 3, 5, 7, 11, 13, 17, 19]

# Case Study: Binary Representation
n = 10
binary = ""
temp = n
while temp > 0:
    binary = str(temp % 2) + binary
    temp //= 2
print(f"Binary of {n}: {binary}")  # Output - Binary of 10: 1010

# Case Study: Number Reversal
n = 12345
reversed_num = 0
while n > 0:
    reversed_num = reversed_num * 10 + n % 10
    n //= 10
print(f"Reversed: {reversed_num}")  # Output - Reversed: 54321

# Case Study: Palindrome Check
text = "racecar"
left = 0
right = len(text) - 1
is_palindrome = True
while left < right:
    if text[left] != text[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1
if is_palindrome:
    print(f"'{text}' is a palindrome")  # Output - 'racecar' is a palindrome
else:
    print(f"'{text}' is not a palindrome")

# Case Study: GCD (Greatest Common Divisor)
a = 48
b = 18
while b != 0:
    temp = b
    b = a % b
    a = temp
print(f"GCD: {a}")  # Output - GCD: 6

# Case Study: Power Calculation
base = 2
exponent = 5
result = 1
count = 0
while count < exponent:
    result *= base
    count += 1
print(f"{base}^{exponent} = {result}")  # Output - 2^5 = 32

# Case Study: Division Algorithm
dividend = 17
divisor = 5
quotient = 0
while dividend >= divisor:
    quotient += 1
    dividend -= divisor
remainder = dividend
print(f"17 ÷ 5 = {quotient} remainder {remainder}")  # Output - 17 ÷ 5 = 3 remainder 2

# Case Study: Linear Search
data = [10, 20, 30, 40, 50, 60, 70]
search_key = 40
index = 0
while index < len(data) and data[index] != search_key:
    index += 1
if index < len(data):
    print(f"Found at index {index}")  # Output - Found at index 3
else:
    print("Not found")

# Case Study: Running Total
numbers = [5, 10, 15, 20, 25]
running_total = []
index = 0
total = 0
while index < len(numbers):
    total += numbers[index]
    running_total.append(total)
    index += 1
print(running_total)  # Output - [5, 15, 30, 50, 75]

# Case Study: Even/Odd Separation
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = []
odds = []
index = 0
while index < len(numbers):
    if numbers[index] % 2 == 0:
        evens.append(numbers[index])
    else:
        odds.append(numbers[index])
    index += 1
print(f"Evens: {evens}")  # Output - Evens: [2, 4, 6, 8, 10]
print(f"Odds: {odds}")  # Output - Odds: [1, 3, 5, 7, 9]

# Case Study: Merge Two Lists
list1 = [1, 3, 5]
list2 = [2, 4, 6]
merged = []
i = j = 0
while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
        merged.append(list1[i])
        i += 1
    else:
        merged.append(list2[j])
        j += 1
while i < len(list1):
    merged.append(list1[i])
    i += 1
while j < len(list2):
    merged.append(list2[j])
    j += 1
print(merged)  # Output - [1, 2, 3, 4, 5, 6]

# Case Study: Character Frequency
text = "mississippi"
char_freq = {}
index = 0
while index < len(text):
    char = text[index]
    char_freq[char] = char_freq.get(char, 0) + 1
    index += 1
print(char_freq)  # Output - {'m': 1, 'i': 4, 's': 4, 'p': 2}

# Case Study: Nested While Loops - Matrix Print
rows = 3
cols = 4
i = 1
while i <= rows:
    j = 1
    while j <= cols:
        print(f"{i*j:2d}", end=" ")
        j += 1
    print()
    i += 1
# Output - multiplication matrix

# Case Study: Alternating Pattern
i = 0
while i < 10:
    if i % 2 == 0:
        print("E", end=" ")
    else:
        print("O", end=" ")
    i += 1
print()  # Output - E O E O E O E O E O

# Case Study: Skip Pattern
i = 0
while i < 20:
    if i % 3 != 0:
        print(i, end=" ")
    i += 1
print()  # Output - 1 2 4 5 7 8 10 11 13 14 16 17 19

# Case Study: Accumulate Pattern
start = 1
end = 5
accumulated = []
current = start
while current <= end:
    accumulated.append(current)
    current += 1
print(accumulated)  # Output - [1, 2, 3, 4, 5]

# Case Study: Conditional Break
attempts = 0
max_attempts = 3
while attempts < max_attempts:
    attempts += 1
    if attempts == 2:
        print(f"Breaking at attempt {attempts}")
        break
    print(f"Attempt {attempts}")
# Output - Attempt 1 Breaking at attempt 2

# Case Study: Validation Loop
valid_input = False
while not valid_input:
    user_input = input("Enter a number between 1 and 10: ")
    if user_input.isdigit():
        num = int(user_input)
        if 1 <= num <= 10:
            valid_input = True
            print(f"Valid input: {num}")
        else:
            print("Out of range!")
    else:
        print("Please enter a valid number!")

# Case Study: Data Processing
data = [100, 200, 300, 400, 500]
processed = []
index = 0
while index < len(data):
    processed.append(data[index] * 1.1)  # 10% increase
    index += 1
print(processed)  # Output - [110.0, 220.0, 330.0, 440.0, 550.0]

# Case Study: State Machine Simulation
state = "start"
transitions = 0
max_transitions = 5
while transitions < max_transitions:
    if state == "start":
        print("State: start -> processing")
        state = "processing"
    elif state == "processing":
        print("State: processing -> done")
        state = "done"
    elif state == "done":
        print("State: done -> start")
        state = "start"
    transitions += 1
# Output - state transitions simulation

# Case Study: Temperature Monitoring
temperature = 20
while temperature < 100:
    print(f"Temperature: {temperature}°C")
    if temperature < 30:
        print("  Status: Cold")
    elif temperature < 60:
        print("  Status: Warm")
    else:
        print("  Status: Hot")
    temperature += 20
# Output - temperature status at different levels

# Case Study: Simulated Download Progress
progress = 0
while progress <= 100:
    print(f"Download progress: {progress}%", end="\r")
    progress += 10
print("\nDownload complete!")  # Output - 0%, 10%, ..., 100%, Download complete!
