# Lists are used to store multiple items in a single variable.
# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
# Lists are created using square brackets:
mylist = ["apple", "banana", "cherry"]
print(mylist) # Output - ['apple', 'banana', 'cherry']

# List Length
mylist = ["apple", "banana", "cherry"]
print(len(mylist)) # Output - 3

# List Items - Data Types
# List items can be of any data type:
list1 = ["apple", "banana", "cherry"] # str
list2 = [1, 5, 7, 9, 3] # int
list3 = [True, False, False] # bool

# A list with strings, integers and boolean values:
list1 = ["abc", 34, True, 408, "male"]

mylist = ["apple", "banana", "cherry"]
print(type(mylist)) # Output - <class 'list'>

# The list() Constructor
# It is also possible to use the list() constructor to make a list.
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist) # Output - ['apple', 'banana', 'cherry']

# Access Items
mylist = ["apple", "banana", "cherry"]
print(mylist[0]) # Output - apple
print(mylist[1]) # Output - banana
print(mylist[2]) # Output - cherry
print(mylist[-1]) # Output - cherry
print(mylist[-2]) # Output - banana
print(mylist[-3]) # Output - apple

# Range of Indexes
mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(mylist[2:5]) # Output - ['cherry', 'orange', 'kiwi']
print(mylist[:4]) # Output - ['apple', 'banana', 'cherry', 'orange']
print(mylist[2:]) # Output - ['cherry', 'orange', 'kiwi', 'melon', 'mango']
print(mylist[-4:-1]) # Output - ['orange', 'kiwi', 'melon']

# Check if Item Exists
mylist = ["apple", "banana", "cherry"]
if "apple" in mylist:
    print("Yes, 'apple' is in the fruits list") # Output - Yes, 'apple' is in the fruits list

# Change Item Value
mylist = ["apple", "banana", "cherry"]
mylist[1] = "blackcurrant"
print(mylist) # Output - ['apple', 'blackcurrant', 'cherry']

# Change a Range of Item Values
mylist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
mylist[1:3] = ["blackcurrant", "watermelon"]
print(mylist) # Output - ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist) # Output - ['apple', 'watermelon']

# Insert Items
mylist = ["apple", "banana", "cherry"]
mylist.insert(2, "watermelon")
print(mylist) # Output - ['apple', 'banana', 'watermelon', 'cherry']

# Append Items
mylist = ["apple", "banana", "cherry"]
mylist.append("orange")
print(mylist) # Output - ['apple', 'banana', 'cherry', 'orange']

# Extend List
mylist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
mylist.extend(tropical)
print(mylist) # Output - ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

# Add Any Iterable
mylist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
mylist.extend(thistuple)
print(mylist) # Output - ['apple', 'banana', 'cherry', 'kiwi', 'orange']

# Remove Specified Item
mylist = ["apple", "banana", "cherry"]
mylist.remove("banana")
print(mylist) # Output - ['apple', 'cherry']

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana") # Only the first occurrence of "banana" will be removed
print(thislist) # Output - ['apple', 'cherry', 'banana', 'kiwi']

# Remove Specified Index
mylist = ["apple", "banana", "cherry"]
mylist.pop(1)
print(mylist) # Output - ['apple', 'cherry']

thislist = ["apple", "banana", "cherry"]
thislist.pop() # If we do not specify the index, the pop() method removes the last item.
print(thislist) 

thislist = ["apple", "banana", "cherry"]
del thislist[0] # The del keyword also removes the specified index, but it can also delete the list completely.
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist # The del keyword also removes the specified index, but it can also delete the list completely.

# Difference Between remove(), pop(), del and clear()
# The remove() method removes the specified item.
# The pop() method removes the specified index, (or the last item if index is not specified).
# The del keyword removes the specified index, or can delete the list completely.
# The clear() method empties the list.

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) # Output - []

# Loop Through a List
mylist = ["apple", "banana", "cherry"]
for x in mylist:
    print(x) # Output - apple banana cherry

# Loop Through the Index Numbers
mylist = ["apple", "banana", "cherry"]
for i in range(len(mylist)):
    print(mylist[i]) # Output - apple banana cherry

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1 # Output - apple banana cherry

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist] # Output - apple banana cherry

# List Comprehension
thislist = ["apple", "banana", "cherry"]
newlist = [x for x in thislist if "a" in x]
print(newlist) # Output - ['apple', 'banana']

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist) # Output - ['apple', 'banana', 'mango']

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x] 
print(newlist) # Output - ['apple', 'banana', 'mango']

# newlist = [expression for item in iterable if condition == True]
newlist = [x for x in fruits if x != "apple"]
print(newlist) # Output - ['banana', 'cherry', 'kiwi', 'mango']

newlist = [x for x in fruits]
print(newlist) # Output - ['apple', 'banana', 'cherry', 'kiwi', 'mango']

newlist = [x for x in range(10)]
print(newlist) # Output - [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

newlist = [x for x in range(10) if x < 5]
print(newlist) # Output - [0, 1, 2, 3, 4]

newlist = [x.upper() for x in fruits]
print(newlist) # Output - ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']

newlist = ['hello' for x in fruits]
print(newlist) # Output - ['hello', 'hello', 'hello', 'hello', 'hello']

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist) # Output - ['apple', 'orange', 'cherry', 'kiwi', 'mango']

# Sort List Alphanumerically
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist) # Output - ['Kiwi', 'Orange', 'banana', 'cherry']

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist) # Output - [23, 50, 65, 82, 100]

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True) # Sorts the list descending
print(thislist) # Output - ['pineapple', 'orange', 'mango', 'kiwi', 'banana']

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist) # Output - [100, 82, 65, 50, 23]

# Customize Sort Function
def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist) # Output - [50, 65, 82, 23, 100]

# Case Insensitive Sort
# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist) # Output - ['banana', 'cherry', 'Kiwi', 'Orange']

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist) # Output - ['banana', 'cherry', 'Kiwi', 'Orange']

# Reverse Order
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist) # Output - ['cherry', 'Kiwi', 'Orange', 'banana']

# Copy a List

# Make a copy of a list with the copy() method:
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist) # Output - ['apple', 'banana', 'cherry']

# Make a copy of a list with the built-in method list():
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist) # Output - ['apple', 'banana', 'cherry']

# Make a copy of a list with the built-in method slice():
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist) # Output - ['apple', 'banana', 'cherry']

# JOIN LISTS
# There are several ways to join, or concatenate, two or more lists in Python.
# The + operator is used to concatenate two lists:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3) # Output - ['a', 'b', 'c', 1, 2, 3]

# The extend() method does the same thing, but it does not create a new list:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1) # Output - ['a', 'b', 'c', 1, 2, 3]

# The extend() method does the same thing, but it does not create a new list:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1) # Output - ['a', 'b', 'c', 1, 2, 3]

# LIST METHODS
# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list
# The list() Constructor
# It is also possible to use the list() constructor to make a list.
thislist = list(("apple", "banana", "cherry")) # note the double round brackets
print(thislist) # Output - ['apple', 'banana', 'cherry']