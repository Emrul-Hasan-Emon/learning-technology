# Tuples are used to store multiple items in a single variable.
# Tuples are one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
# Tuples are created using round brackets:
mytuple = ("apple", "banana", "cherry")
print(mytuple)  # Output - ('apple', 'banana', 'cherry')

# Tuple Length
mytuple = ("apple", "banana", "cherry")
print(len(mytuple))  # Output - 3

# Tuple Items - Data Types
# Tuple items can be of any data type:
tuple1 = ("apple", "banana", "cherry")  # str
tuple2 = (1, 5, 7, 9, 3)  # int
tuple3 = (True, False, False)  # bool

# A tuple with strings, integers and boolean values:
tuple1 = ("abc", 34, True, 408, "male")

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))  # Output - <class 'tuple'>

# A Tuple with One Item
# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
thistuple = ("apple",)
print(type(thistuple))  # Output - <class 'tuple'>

# NOT a tuple
thistuple = ("apple")
print(type(thistuple))  # Output - <class 'str'>

# The tuple() Constructor
# It is also possible to use the tuple() constructor to make a tuple.
thistuple = tuple(("apple", "banana", "cherry"))  # note the double round-brackets
print(thistuple)  # Output - ('apple', 'banana', 'cherry')

# Access Items
mytuple = ("apple", "banana", "cherry")
print(mytuple[0])  # Output - apple
print(mytuple[1])  # Output - banana
print(mytuple[2])  # Output - cherry
print(mytuple[-1])  # Output - cherry
print(mytuple[-2])  # Output - banana
print(mytuple[-3])  # Output - apple

# Range of Indexes
mytuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(mytuple[2:5])  # Output - ('cherry', 'orange', 'kiwi')
print(mytuple[:4])  # Output - ('apple', 'banana', 'cherry', 'orange')
print(mytuple[2:])  # Output - ('cherry', 'orange', 'kiwi', 'melon', 'mango')
print(mytuple[-4:-1])  # Output - ('orange', 'kiwi', 'melon')

# Check if Item Exists
mytuple = ("apple", "banana", "cherry")
if "apple" in mytuple:
    print("Yes, 'apple' is in the fruits tuple")  # Output - Yes, 'apple' is in the fruits tuple

# Tuples are Immutable
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
mytuple = ("apple", "banana", "cherry")
# mytuple[1] = "blackcurrant"  # This will raise a TypeError
# print(mytuple)

# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
mytuple = ("apple", "banana", "cherry")
mylist = list(mytuple)
mylist[1] = "blackcurrant"
mytuple = tuple(mylist)
print(mytuple)  # Output - ('apple', 'blackcurrant', 'cherry')

# Loop Through a Tuple
mytuple = ("apple", "banana", "cherry")
for x in mytuple:
    print(x)  # Output - apple banana cherry

# Loop Through the Index Numbers
mytuple = ("apple", "banana", "cherry")
for i in range(len(mytuple)):
    print(mytuple[i])  # Output - apple banana cherry

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1  # Output - apple banana cherry

# Using List Comprehension with Tuples
thistuple = ("apple", "banana", "cherry")
newlist = [x for x in thistuple if "a" in x]
print(newlist)  # Output - ['apple', 'banana']

fruits = ("apple", "banana", "cherry", "kiwi", "mango")
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)  # Output - ['apple', 'banana', 'mango']

fruits = ("apple", "banana", "cherry", "kiwi", "mango")
newlist = [x for x in fruits if "a" in x]
print(newlist)  # Output - ['apple', 'banana', 'mango']

# newlist = [expression for item in iterable if condition == True]
newlist = [x for x in fruits if x != "apple"]
print(newlist)  # Output - ['banana', 'cherry', 'kiwi', 'mango']

newlist = [x for x in fruits]
print(newlist)  # Output - ['apple', 'banana', 'cherry', 'kiwi', 'mango']

newlist = [x.upper() for x in fruits]
print(newlist)  # Output - ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']

newlist = ['hello' for x in fruits]
print(newlist)  # Output - ['hello', 'hello', 'hello', 'hello', 'hello']

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)  # Output - ['apple', 'orange', 'cherry', 'kiwi', 'mango']

# Unpacking a Tuple
# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
fruits = ("apple", "banana", "cherry")

# But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":
(green, yellow, red) = fruits
print(green)  # Output - apple
print(yellow)  # Output - banana
print(red)  # Output - cherry

# If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)  # Output - apple
print(yellow)  # Output - banana
print(red)  # Output - ['cherry', 'strawberry', 'raspberry']

# Adding an * before the variable name and assigning remaining values to it:
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, *yellow, red) = fruits
print(green)  # Output - apple
print(yellow)  # Output - ['banana', 'cherry', 'strawberry']
print(red)  # Output - raspberry

# Copy a Tuple

# Make a copy of a tuple with the built-in method tuple():
thistuple = ("apple", "banana", "cherry")
mytuple = tuple(thistuple)
print(mytuple)  # Output - ('apple', 'banana', 'cherry')

# Make a copy of a tuple with slicing:
thistuple = ("apple", "banana", "cherry")
mytuple = thistuple[:]
print(mytuple)  # Output - ('apple', 'banana', 'cherry')

# JOIN TUPLES
# There are several ways to join, or concatenate, two or more tuples in Python.
# The + operator is used to concatenate two tuples:
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)  # Output - ('a', 'b', 'c', 1, 2, 3)

# Multiply a Tuple
# If you want to repeat tuples, you can use the * operator:
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)  # Output - ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')

# TUPLE METHODS
# Tuples have only two built-in methods:
# Method       Description
# count()      Returns the number of times a specified value occurs in a tuple
# index()      Searches the tuple for a specified value and returns the position of where it was found

# count() method
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)  # Output - 2

# index() method
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)  # Output - 3

# The tuple() Constructor
# It is also possible to use the tuple() constructor to make a tuple.
thistuple = tuple(("apple", "banana", "cherry"))  # note the double round brackets
print(thistuple)  # Output - ('apple', 'banana', 'cherry')

# Nested Tuples
# Tuples can contain other tuples (nested tuples)
thistuple = ("apple", ("banana", "cherry"), "date")
print(thistuple)  # Output - ('apple', ('banana', 'cherry'), 'date')
print(thistuple[1][0])  # Output - banana

# Access nested tuple items
nestedtuple = ("apple", ("mango", "orange", "banana"), "kiwi")
print(nestedtuple[1][2])  # Output - banana
