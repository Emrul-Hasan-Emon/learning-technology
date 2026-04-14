# Arrays in Python
# Python doesn't have a built-in array type like some other languages.
# Instead, we use Lists which are dynamic arrays.
# Python also has an 'array' module for typed arrays similar to arrays in other languages.
# Note: Lists are more commonly used and flexible than arrays.

# Basic List (Array-like) Creation
arr = [1, 2, 3, 4, 5]
print(arr)  # Output - [1, 2, 3, 4, 5]

# Array Module - Typed Arrays
import array

# Creating a typed array (type 'i' for signed integers)
int_array = array.array('i', [1, 2, 3, 4, 5])
print(int_array)  # Output - array('i', [1, 2, 3, 4, 5])

# Array Module - Different Types
float_array = array.array('f', [1.1, 2.2, 3.3])
print(float_array)  # Output - array('f', [1.1000000238418579, 2.2000000476837158, 3.299999952316284])

# Array Module - Double Type
double_array = array.array('d', [1.1, 2.2, 3.3])
print(double_array)  # Output - array('d', [1.1, 2.2, 3.3])

# Array Length
arr = [1, 2, 3, 4, 5]
print(len(arr))  # Output - 5

# Access Array Elements
arr = [10, 20, 30, 40, 50]
print(arr[0])   # Output - 10
print(arr[2])   # Output - 30
print(arr[-1])  # Output - 50 (last element)
print(arr[-2])  # Output - 40

# Modify Array Elements
arr = [1, 2, 3, 4, 5]
arr[1] = 20
print(arr)  # Output - [1, 20, 3, 4, 5]

arr[-1] = 50
print(arr)  # Output - [1, 20, 3, 4, 50]

# Add Elements to Array
arr = [1, 2, 3]
arr.append(4)
print(arr)  # Output - [1, 2, 3, 4]

# Insert at Specific Position
arr = [1, 2, 4, 5]
arr.insert(2, 3)
print(arr)  # Output - [1, 2, 3, 4, 5]

# Extend Array with Multiple Elements
arr = [1, 2, 3]
arr.extend([4, 5, 6])
print(arr)  # Output - [1, 2, 3, 4, 5, 6]

# Remove Element by Value
arr = [1, 2, 3, 2, 4]
arr.remove(2)
print(arr)  # Output - [1, 3, 2, 4] (only first occurrence)

# Remove Element by Index
arr = [1, 2, 3, 4, 5]
removed = arr.pop(2)
print(f"Removed: {removed}, Array: {arr}")  # Output - Removed: 3, Array: [1, 2, 4, 5]

# Remove Last Element
arr = [1, 2, 3, 4, 5]
arr.pop()
print(arr)  # Output - [1, 2, 3, 4]

# Delete by Index
arr = [1, 2, 3, 4, 5]
del arr[2]
print(arr)  # Output - [1, 2, 4, 5]

# Clear Array
arr = [1, 2, 3, 4, 5]
arr.clear()
print(arr)  # Output - []

# Array Slicing
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(arr[2:5])      # Output - [3, 4, 5]
print(arr[:3])       # Output - [1, 2, 3]
print(arr[5:])       # Output - [6, 7, 8, 9, 10]
print(arr[-3:])      # Output - [8, 9, 10]
print(arr[::2])      # Output - [1, 3, 5, 7, 9] (step of 2)
print(arr[::-1])     # Output - [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] (reverse)

# Find Index of Element
arr = [10, 20, 30, 40, 30]
index = arr.index(30)
print(index)  # Output - 2 (first occurrence)

# Count Occurrences
arr = [1, 2, 2, 3, 3, 3, 4, 5, 5]
count = arr.count(3)
print(count)  # Output - 3

# Check if Element Exists
arr = [1, 2, 3, 4, 5]
if 3 in arr:
    print("3 exists in array")  # Output - 3 exists in array

# Sort Array
arr = [5, 2, 8, 1, 9, 3]
arr.sort()
print(arr)  # Output - [1, 2, 3, 5, 8, 9]

# Sort in Descending Order
arr = [5, 2, 8, 1, 9, 3]
arr.sort(reverse=True)
print(arr)  # Output - [9, 8, 5, 3, 2, 1]

# Sort with Custom Key
arr = ["apple", "pie", "zoo", "a"]
arr.sort(key=len)
print(arr)  # Output - ['a', 'pie', 'zoo', 'apple']

# Reverse Array
arr = [1, 2, 3, 4, 5]
arr.reverse()
print(arr)  # Output - [5, 4, 3, 2, 1]

# Copy Array (Shallow Copy)
arr1 = [1, 2, 3]
arr2 = arr1.copy()
arr2[0] = 10
print(f"arr1: {arr1}, arr2: {arr2}")  # Output - arr1: [1, 2, 3], arr2: [10, 2, 3]

# Copy Array (Alternative Method)
arr1 = [1, 2, 3]
arr2 = arr1[:]
arr2[0] = 10
print(f"arr1: {arr1}, arr2: {arr2}")  # Output - arr1: [1, 2, 3], arr2: [10, 2, 3]

# Concatenate Arrays
arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
arr3 = arr1 + arr2
print(arr3)  # Output - [1, 2, 3, 4, 5, 6]

# Repeat Array Elements
arr = [1, 2, 3]
repeated = arr * 3
print(repeated)  # Output - [1, 2, 3, 1, 2, 3, 1, 2, 3]

# Multi-dimensional Arrays (2D Array/Matrix)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[0])      # Output - [1, 2, 3]
print(matrix[1][2])   # Output - 6

# Access 2D Array Elements
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for element in row:
        print(element, end=" ")
print()  # Output - 1 2 3 4 5 6 7 8 9

# Create 2D Array Dynamically
rows = 3
cols = 3
matrix = [[0 for _ in range(cols)] for _ in range(rows)]
print(matrix)  # Output - [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Enumerate Array with Index
arr = ['a', 'b', 'c', 'd']
for index, value in enumerate(arr):
    print(f"{index}: {value}")
# Output - 0: a 1: b 2: c 3: d

# Array of Different Types (Heterogeneous)
mixed_array = [1, "hello", 3.14, True, None]
print(mixed_array)  # Output - [1, 'hello', 3.14, True, None]

# Array Comprehension
squares = [x ** 2 for x in range(1, 6)]
print(squares)  # Output - [1, 4, 9, 16, 25]

# Array Comprehension with Condition
evens = [x for x in range(1, 11) if x % 2 == 0]
print(evens)  # Output - [2, 4, 6, 8, 10]

# Array Comprehension - Nested
matrix = [[i + j for j in range(3)] for i in range(3)]
print(matrix)  # Output - [[0, 1, 2], [1, 2, 3], [2, 3, 4]]

# Case Study: Sum of Array
arr = [1, 2, 3, 4, 5]
total = sum(arr)
print(f"Sum: {total}")  # Output - Sum: 15

# Case Study: Average of Array
arr = [10, 20, 30, 40, 50]
average = sum(arr) / len(arr)
print(f"Average: {average}")  # Output - Average: 30.0

# Case Study: Find Maximum and Minimum
arr = [5, 2, 9, 1, 8, 3]
print(f"Max: {max(arr)}, Min: {min(arr)}")  # Output - Max: 9, Min: 1

# Case Study: Find Second Maximum
arr = [5, 2, 9, 1, 8, 3]
arr_sorted = sorted(set(arr), reverse=True)
print(f"Second Max: {arr_sorted[1]}")  # Output - Second Max: 8

# Case Study: Remove Duplicates
arr = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique = list(set(arr))
print(unique)  # Output - [1, 2, 3, 4, 5] (order may vary)

# Case Study: Merge Two Sorted Arrays
arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
merged = sorted(arr1 + arr2)
print(merged)  # Output - [1, 2, 3, 4, 5, 6]

# Case Study: Find Common Elements
arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7]
common = list(set(arr1) & set(arr2))
print(common)  # Output - [3, 4, 5]

# Case Study: Count Elements
arr = [1, 2, 2, 3, 3, 3, 4, 5, 5]
from collections import Counter
freq = Counter(arr)
print(dict(freq))  # Output - {1: 1, 2: 2, 3: 3, 4: 1, 5: 2}

# Case Study: Rotate Array
def rotate_array(arr, k):
    k = k % len(arr)
    return arr[-k:] + arr[:-k]

arr = [1, 2, 3, 4, 5]
print(rotate_array(arr, 2))  # Output - [4, 5, 1, 2, 3]

# Case Study: Flatten Nested Array
nested = [[1, 2], [3, 4], [5, 6]]
flattened = [item for sublist in nested for item in sublist]
print(flattened)  # Output - [1, 2, 3, 4, 5, 6]

# Case Study: Zip Arrays
arr1 = [1, 2, 3]
arr2 = ['a', 'b', 'c']
zipped = list(zip(arr1, arr2))
print(zipped)  # Output - [(1, 'a'), (2, 'b'), (3, 'c')]

# Case Study: Unzip Arrays
zipped = [(1, 'a'), (2, 'b'), (3, 'c')]
arr1, arr2 = zip(*zipped)
print(arr1, arr2)  # Output - (1, 2, 3) ('a', 'b', 'c')

# Case Study: Binary Search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = [1, 3, 5, 7, 9, 11]
print(binary_search(arr, 7))  # Output - 3

# Case Study: Linear Search
def linear_search(arr, target):
    for i, element in enumerate(arr):
        if element == target:
            return i
    return -1

arr = [10, 20, 30, 40, 50]
print(linear_search(arr, 30))  # Output - 2

# Case Study: Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(arr.copy()))  # Output - [11, 12, 22, 25, 34, 64, 90]

# Case Study: Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
print(selection_sort(arr.copy()))  # Output - [11, 12, 22, 25, 34, 64, 90]

# Case Study: Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
print(insertion_sort(arr.copy()))  # Output - [11, 12, 22, 25, 34, 64, 90]

# Case Study: Array Intersection
def array_intersection(arr1, arr2):
    set1 = set(arr1)
    return [x for x in arr2 if x in set1]

arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7]
print(array_intersection(arr1, arr2))  # Output - [3, 4, 5]

# Case Study: Array Difference
def array_difference(arr1, arr2):
    set2 = set(arr2)
    return [x for x in arr1 if x not in set2]

arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7]
print(array_difference(arr1, arr2))  # Output - [1, 2]

# Case Study: Array Union
def array_union(arr1, arr2):
    return list(set(arr1) | set(arr2))

arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7]
print(sorted(array_union(arr1, arr2)))  # Output - [1, 2, 3, 4, 5, 6, 7]

# Case Study: Majority Element
def majority_element(arr):
    count = {}
    for num in arr:
        count[num] = count.get(num, 0) + 1
    return max(count, key=count.get)

arr = [1, 1, 1, 2, 2, 3]
print(majority_element(arr))  # Output - 1

# Case Study: Check if Array is Sorted
def is_sorted(arr):
    return arr == sorted(arr)

arr1 = [1, 2, 3, 4, 5]
arr2 = [5, 2, 3, 4, 1]
print(f"arr1 sorted: {is_sorted(arr1)}")  # Output - arr1 sorted: True
print(f"arr2 sorted: {is_sorted(arr2)}")  # Output - arr2 sorted: False

# Case Study: Remove Duplicates Maintain Order
def remove_duplicates_ordered(arr):
    seen = set()
    result = []
    for item in arr:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

arr = [1, 2, 2, 3, 3, 3, 4, 5, 5]
print(remove_duplicates_ordered(arr))  # Output - [1, 2, 3, 4, 5]

# Case Study: Transpose Matrix
def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = transpose_matrix(matrix)
print(transposed)  # Output - [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# Case Study: Matrix Addition
def matrix_add(m1, m2):
    return [[m1[i][j] + m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))]

m1 = [[1, 2], [3, 4]]
m2 = [[5, 6], [7, 8]]
print(matrix_add(m1, m2))  # Output - [[6, 8], [10, 12]]

# Case Study: Matrix Multiplication
def matrix_multiply(m1, m2):
    result = [[0 for _ in range(len(m2[0]))] for _ in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                result[i][j] += m1[i][k] * m2[k][j]
    return result

m1 = [[1, 2], [3, 4]]
m2 = [[5, 6], [7, 8]]
print(matrix_multiply(m1, m2))  # Output - [[19, 22], [43, 50]]

# Case Study: Pascal's Triangle
def pascals_triangle(n):
    triangle = []
    for i in range(n):
        row = [1]
        if triangle:
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)
        triangle.append(row)
    return triangle

triangle = pascals_triangle(5)
for row in triangle:
    print(row)
# Output - [1] [1, 1] [1, 2, 1] [1, 3, 3, 1] [1, 4, 6, 4, 1]

# Case Study: Cumulative Sum
arr = [1, 2, 3, 4, 5]
cumsum = []
total = 0
for num in arr:
    total += num
    cumsum.append(total)
print(cumsum)  # Output - [1, 3, 6, 10, 15]

# Case Study: Prefix Sum
def prefix_sum(arr):
    prefix = [0]
    for num in arr:
        prefix.append(prefix[-1] + num)
    return prefix

arr = [1, 2, 3, 4, 5]
print(prefix_sum(arr))  # Output - [0, 1, 3, 6, 10, 15]

# Case Study: Move Zeros to End
def move_zeros_to_end(arr):
    zeros = 0
    for num in arr[:]:
        if num == 0:
            arr.remove(num)
            zeros += 1
    arr.extend([0] * zeros)
    return arr

arr = [1, 0, 2, 0, 3, 4, 0]
print(move_zeros_to_end(arr.copy()))  # Output - [1, 2, 3, 4, 0, 0, 0]

# Case Study: Array Rotation In-Place
def rotate_in_place(arr, k):
    k = k % len(arr)
    arr.reverse()
    arr[:k] = arr[:k][::-1]
    arr[k:] = arr[k:][::-1]
    return arr

arr = [1, 2, 3, 4, 5]
print(rotate_in_place(arr, 2))  # Output - [4, 5, 1, 2, 3]

# Case Study: Target Sum Pairs (Two Sum)
def two_sum(arr, target):
    seen = set()
    pairs = []
    for num in arr:
        complement = target - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    return pairs

arr = [1, 2, 3, 4, 5, 6]
print(two_sum(arr, 7))  # Output - [(1, 6), (2, 5), (3, 4)]
