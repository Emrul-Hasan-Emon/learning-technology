# Iterators in Python
# An iterator is an object that can be iterated upon (looped through).
# An iterator implements two methods: __iter__() and __next__().

# Basic Iterator Concept
# List is iterable
mylist = [1, 2, 3]
myiter = iter(mylist)
print(next(myiter))  # Output - 1
print(next(myiter))  # Output - 2
print(next(myiter))  # Output - 3
# print(next(myiter))  # Would raise StopIteration

# Iterator from String
mystring = "hello"
myiter = iter(mystring)
print(next(myiter))  # Output - h
print(next(myiter))  # Output - e
print(next(myiter))  # Output - l

# Using For Loop (Implicitly Uses Iterator)
# When we use a for loop, Python internally creates an iterator and calls next()
mylist = [1, 2, 3]
for item in mylist:
    print(item)  # Output - 1 2 3

# While Loop with Iterator and Exception Handling
mylist = [1, 2, 3]
myiter = iter(mylist)
while True:
    try:
        print(next(myiter))
    except StopIteration:
        break
# Output - 1 2 3

# Creating a Custom Iterator Class
class CountUp:
    def __init__(self, max):
        self.max = max
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.max:
            self.current += 1
            return self.current
        else:
            raise StopIteration

counter = CountUp(3)
for num in counter:
    print(num)  # Output - 1 2 3

# Custom Iterator - Range Alternative
class SimpleRange:
    def __init__(self, start, end):
        self.current = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.end:
            self.current += 1
            return self.current - 1
        else:
            raise StopIteration

for num in SimpleRange(1, 5):
    print(num, end=" ")  # Output - 1 2 3 4
print()

# Generator Function (Simpler Way to Create Iterators)
def simple_generator():
    yield 1
    yield 2
    yield 3

for value in simple_generator():
    print(value)  # Output - 1 2 3

# Generator with Range
def count_generator(max_value):
    current = 0
    while current < max_value:
        yield current
        current += 1

for num in count_generator(5):
    print(num, end=" ")  # Output - 0 1 2 3 4
print()

# Generator with Loop
def generate_squares(n):
    for i in range(n):
        yield i ** 2

for square in generate_squares(5):
    print(square, end=" ")  # Output - 0 1 4 9 16
print()

# Generator Expression (Like List Comprehension)
squares_gen = (x ** 2 for x in range(5))
print(next(squares_gen))  # Output - 0
print(next(squares_gen))  # Output - 1
for square in squares_gen:
    print(square, end=" ")  # Output - 4 9 16
print()

# Difference: List Comprehension vs Generator Expression
# List Comprehension - creates entire list in memory
list_comp = [x ** 2 for x in range(1000000)]
print(type(list_comp))  # Output - <class 'list'>

# Generator Expression - creates values on demand
gen_exp = (x ** 2 for x in range(1000000))
print(type(gen_exp))  # Output - <class 'generator'>

# Built-in Iterator: range()
for i in range(3):
    print(i, end=" ")  # Output - 0 1 2
print()

# Built-in Iterator: enumerate()
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# Output - 0: apple 1: banana 2: cherry

# Built-in Iterator: zip()
letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
for letter, number in zip(letters, numbers):
    print(f"{letter}: {number}")
# Output - a: 1 b: 2 c: 3

# Built-in Iterator: map()
def double(x):
    return x * 2

numbers = [1, 2, 3, 4, 5]
doubled = map(double, numbers)
print(list(doubled))  # Output - [2, 4, 6, 8, 10]

# Built-in Iterator: filter()
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
evens = filter(is_even, numbers)
print(list(evens))  # Output - [2, 4, 6]

# Built-in Iterator: reversed()
mylist = [1, 2, 3, 4, 5]
for item in reversed(mylist):
    print(item, end=" ")  # Output - 5 4 3 2 1
print()

# Built-in Iterator: iter() with Condition
def read_until_zero():
    while True:
        value = int(input("Enter a number (0 to stop): "))
        if value == 0:
            break
        yield value

# Skipped interactive example
# for num in read_until_zero():
#     print(num)

# Iterator with State
class Fibonacci:
    def __init__(self, max):
        self.max = max
        self.a, self.b = 0, 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.a <= self.max:
            value = self.a
            self.a, self.b = self.b, self.a + self.b
            return value
        else:
            raise StopIteration

fib = Fibonacci(20)
print("Fibonacci:", list(fib))  # Output - Fibonacci: [0, 1, 1, 2, 3, 5, 8, 13, 21]

# Generator with Fibonacci
def fibonacci_gen(max_value):
    a, b = 0, 1
    while a <= max_value:
        yield a
        a, b = b, a + b

print("Generator Fibonacci:", list(fibonacci_gen(20)))  # Output - Generator Fibonacci: [0, 1, 1, 2, 3, 5, 8, 13, 21]

# Generator with send() Method
def echo_generator():
    while True:
        value = yield
        print(f"Received: {value}")

gen = echo_generator()
next(gen)  # Start the generator
gen.send("Hello")  # Output - Received: Hello
gen.send("World")  # Output - Received: World

# Generator with try/finally
def generator_with_cleanup():
    print("Setup")
    try:
        yield 1
        yield 2
        yield 3
    finally:
        print("Cleanup")

gen = generator_with_cleanup()
print(next(gen))  # Output - Setup 1
print(next(gen))  # Output - 2
gen.close()  # Output - Cleanup

# infinite Iterator
def infinite_counter(start=0):
    count = start
    while True:
        yield count
        count += 1

counter = infinite_counter()
print(next(counter))  # Output - 0
print(next(counter))  # Output - 1
print(next(counter))  # Output - 2

# Chaining Iterators with itertools
from itertools import chain

iter1 = [1, 2, 3]
iter2 = [4, 5, 6]
for item in chain(iter1, iter2):
    print(item, end=" ")  # Output - 1 2 3 4 5 6
print()

# Using itertools.combinations
from itertools import combinations

items = ['a', 'b', 'c']
for combo in combinations(items, 2):
    print(combo, end=" ")  # Output - ('a', 'b') ('a', 'c') ('b', 'c')
print()

# Using itertools.permutations
from itertools import permutations

items = ['a', 'b', 'c']
for perm in permutations(items, 2):
    print(perm, end=" ")  # Output - ('a', 'b') ('a', 'c') ('b', 'a') ('b', 'c') ('c', 'a') ('c', 'b')
print()

# Using itertools.product
from itertools import product

set1 = [1, 2]
set2 = ['a', 'b']
for prod in product(set1, set2):
    print(prod, end=" ")  # Output - (1, 'a') (1, 'b') (2, 'a') (2, 'b')
print()

# Using itertools.cycle
from itertools import cycle

colors = ['red', 'green', 'blue']
color_cycle = cycle(colors)
for _ in range(9):
    print(next(color_cycle), end=" ")  # Output - red green blue red green blue red green blue
print()

# Using itertools.repeat
from itertools import repeat

repeated = repeat("x", 3)
for item in repeated:
    print(item, end="")  # Output - xxx
print()

# Case Study: Even Number Iterator
def even_iterator(start, end):
    current = start
    while current <= end:
        if current % 2 == 0:
            yield current
        current += 1

for num in even_iterator(1, 10):
    print(num, end=" ")  # Output - 2 4 6 8 10
print()

# Case Study: Prime Number Generator
def prime_generator(limit):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    for num in range(2, limit):
        if is_prime(num):
            yield num

primes = list(prime_generator(20))
print("Primes:", primes)  # Output - Primes: [2, 3, 5, 7, 11, 13, 17, 19]

# Case Study: File Line Iterator
def read_lines(filename):
    try:
        with open(filename, 'r') as f:
            for line in f:
                yield line.strip()
    except FileNotFoundError:
        print(f"File {filename} not found")

# Example: for line in read_lines('example.txt'):
#     print(line)

# Case Study: Batch Iterator
def batch_iterator(iterable, batch_size):
    batch = []
    for item in iterable:
        batch.append(item)
        if len(batch) == batch_size:
            yield batch
            batch = []
    if batch:
        yield batch

data = range(1, 11)
for batch in batch_iterator(data, 3):
    print(batch)
# Output - [1, 2, 3] [4, 5, 6] [7, 8, 9] [10]

# Case Study: Window Iterator (Sliding Window)
def window_iterator(iterable, window_size):
    iterator = iter(iterable)
    window = []
    
    for item in iterator:
        window.append(item)
        if len(window) == window_size:
            yield tuple(window)
            window.pop(0)

data = range(1, 6)
for window in window_iterator(data, 3):
    print(window, end=" ")  # Output - (1, 2, 3) (2, 3, 4) (3, 4, 5)
print()

# Case Study: Filter and Transform Iterator
def filter_transform(iterable, predicate, transform):
    for item in iterable:
        if predicate(item):
            yield transform(item)

numbers = range(1, 11)
result = list(filter_transform(numbers, lambda x: x % 2 == 0, lambda x: x ** 2))
print("Filtered and transformed:", result)  # Output - Filtered and transformed: [4, 16, 36, 64, 100]

# Case Study: Flatten Nested Iterator
def flatten(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            for sub_item in flatten(item):
                yield sub_item
        else:
            yield item

nested = [1, [2, 3, [4, 5]], 6, [7, [8, 9]]]
print("Flattened:", list(flatten(nested)))  # Output - Flattened: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Case Study: Dictionary Iterator
def dict_iterator(dictionary):
    for key, value in dictionary.items():
        yield (key, value)

data = {"a": 1, "b": 2, "c": 3}
for key, value in dict_iterator(data):
    print(f"{key}: {value}")
# Output - a: 1 b: 2 c: 3

# Case Study: Tree Iterator (In-order Traversal)
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class TreeIterator:
    def __init__(self, root):
        self.root = root
        self.stack = []
        self._push_left(root)
    
    def _push_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.stack:
            raise StopIteration
        node = self.stack.pop()
        if node.right:
            self._push_left(node.right)
        return node.value

# Example: Create tree and iterate
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
for value in TreeIterator(root):
    print(value, end=" ")  # Output - 1 2 3
print()

# Case Study: Pairwise Iterator
def pairwise(iterable):
    iterator = iter(iterable)
    a = next(iterator, None)
    for b in iterator:
        yield (a, b)
        a = b

items = [1, 2, 3, 4, 5]
for pair in pairwise(items):
    print(pair, end=" ")  # Output - (1, 2) (2, 3) (3, 4) (4, 5)
print()

# Case Study: Running Sum Iterator
def running_sum(iterable):
    total = 0
    for item in iterable:
        total += item
        yield total

numbers = [1, 2, 3, 4, 5]
print("Running sums:", list(running_sum(numbers)))  # Output - Running sums: [1, 3, 6, 10, 15]

# Case Study: Circular Iterator
def circular_iterator(iterable, times):
    for _ in range(times):
        for item in iterable:
            yield item

items = ['a', 'b', 'c']
for item in circular_iterator(items, 2):
    print(item, end="")  # Output - abcabc
print()

# Case Study: Limit Iterator
def limit_iterator(iterable, limit):
    count = 0
    for item in iterable:
        if count >= limit:
            break
        yield item
        count += 1

items = range(1, 11)
for item in limit_iterator(items, 5):
    print(item, end=" ")  # Output - 1 2 3 4 5
print()

# Case Study: Skip Iterator
def skip_iterator(iterable, skip_count):
    iterator = iter(iterable)
    for _ in range(skip_count):
        next(iterator, None)
    for item in iterator:
        yield item

items = range(1, 11)
for item in skip_iterator(items, 3):
    print(item, end=" ")  # Output - 4 5 6 7 8 9 10
print()

# Case Study: Group By Iterator
from itertools import groupby

def group_consecutive(iterable):
    for key, group in groupby(enumerate(iterable), lambda x: x[1] - x[0]):
        yield [item[1] for item in group]

items = [1, 2, 3, 5, 6, 7, 8, 10, 11]
for group in group_consecutive(items):
    print(group)
# Output - [1, 2, 3] [5, 6, 7, 8] [10, 11]

# Case Study: Dictionary Value Iterator
def dict_values_iter(dictionary):
    for value in dictionary.values():
        yield value

data = {"a": 1, "b": 2, "c": 3}
print("Values:", list(dict_values_iter(data)))  # Output - Values: [1, 2, 3]

# Case Study: Dictionary Key Iterator
def dict_keys_iter(dictionary):
    for key in dictionary.keys():
        yield key

data = {"a": 1, "b": 2, "c": 3}
print("Keys:", list(dict_keys_iter(data)))  # Output - Keys: ['a', 'b', 'c']

# Case Study: Unique Iterator
def unique_iterator(iterable):
    seen = set()
    for item in iterable:
        if item not in seen:
            seen.add(item)
            yield item

items = [1, 2, 2, 3, 3, 3, 4, 5, 5]
print("Unique:", list(unique_iterator(items)))  # Output - Unique: [1, 2, 3, 4, 5]

# Case Study: Map and Filter Combined
def map_filter(iterable, predicate, func):
    for item in iterable:
        if predicate(item):
            yield func(item)

numbers = range(1, 11)
result = list(map_filter(numbers, lambda x: x % 2 == 0, lambda x: x ** 2))
print("Mapped and filtered:", result)  # Output - Mapped and filtered: [4, 16, 36, 64, 100]

# Case Study: String Iterator
def char_iterator(text):
    for char in text:
        yield char

text = "hello"
for char in char_iterator(text):
    print(char, end="")  # Output - hello
print()

# Case Study: Recursion with Iterator
def countdown_iterator(n):
    if n > 0:
        yield n
        yield from countdown_iterator(n - 1)

for num in countdown_iterator(5):
    print(num, end=" ")  # Output - 5 4 3 2 1
print()

# Case Study: Tuple Iterator
def tuple_iterator(tup):
    for item in tup:
        yield item

items = (1, 2, 3, 4, 5)
print("Tuple items:", list(tuple_iterator(items)))  # Output - Tuple items: [1, 2, 3, 4, 5]

# Case Study: Lazy Evaluation
def expensive_operation(n):
    print(f"Computing {n}...")
    return n ** 2

# Lazy: operations not performed until needed
lazy_results = (expensive_operation(x) for x in range(5))
print("Lazy results created (no computation yet)")
print("First result:", next(lazy_results))  # Output - Computing 0... First result: 0

# Case Study: Python's iter() with Callable
def countdown_generator():
    n = 5
    while n > 0:
        yield n
        n -= 1

for num in countdown_generator():
    print(num, end=" ")  # Output - 5 4 3 2 1
print()
