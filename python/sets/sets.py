# Sets are used to store multiple items in a single variable.
# Sets are one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
# Sets are created using curly braces:
myset = {"apple", "banana", "cherry"}
print(myset)  # Output - {'apple', 'banana', 'cherry'} (order may vary)

# Set Length
myset = {"apple", "banana", "cherry"}
print(len(myset))  # Output - 3

# Set Items - Data Types
# Set items can be of any data type:
set1 = {"apple", "banana", "cherry"}  # str
set2 = {1, 5, 7, 9, 3}  # int
set3 = {True, False, False}  # bool

# A set with strings, integers and boolean values:
set1 = {"abc", 34, True, 408, "male"}

myset = {"apple", "banana", "cherry"}
print(type(myset))  # Output - <class 'set'>

# Sets are Unordered
# Sets are unordered, so you cannot be sure in which order the items will appear.
myset = {"apple", "banana", "cherry"}
print(myset)  # Output may vary on order - {'apple', 'banana', 'cherry'}

# Duplicate Values
# Sets cannot have two items with the same value.
myset = {"apple", "banana", "cherry", "apple"}
print(myset)  # Output - {'apple', 'banana', 'cherry'} (only one apple)
print(len(myset))  # Output - 3

# The set() Constructor
# It is also possible to use the set() constructor to make a set.
thisset = set(("apple", "banana", "cherry"))  # note the double round-brackets
print(thisset)  # Output - {'apple', 'banana', 'cherry'}

# Access Items
# You cannot access items in a set by referring to an index or a key.
# But you can loop through the set items using a for loop,
# or ask if a specified value exists in a set, by using the in keyword.

myset = {"apple", "banana", "cherry"}
for x in myset:
    print(x)  # Output - apple banana cherry (order may vary)

# Check if Item Exists
myset = {"apple", "banana", "cherry"}
if "apple" in myset:
    print("Yes, 'apple' is in the fruits set")  # Output - Yes, 'apple' is in the fruits set

# Add Items
# Once a set is created, you cannot change its items, but you can add new items.

# Add one item to a set, use the add() method:
myset = {"apple", "banana", "cherry"}
myset.add("orange")
print(myset)  # Output - {'apple', 'banana', 'cherry', 'orange'} (order may vary)

# Add Multiple Items to a Set
# To add multiple items to a set, use the update() method:
myset = {"apple", "banana", "cherry"}
myset.update(["orange", "mango", "grapes"])
print(myset)  # Output - {'apple', 'banana', 'cherry', 'orange', 'mango', 'grapes'} (order may vary)

# Add Any Iterable
myset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
myset.update(mylist)
print(myset)  # Output - {'apple', 'banana', 'cherry', 'kiwi', 'orange'} (order may vary)

# Remove Items
# To remove an item in a set, use the remove(), or the discard() method.

# Remove an item by using the remove() method:
myset = {"apple", "banana", "cherry"}
myset.remove("banana")
print(myset)  # Output - {'apple', 'cherry'} (order may vary)

# Note: If the item to remove does not exist, remove() will raise an error.

# Remove an item by using the discard() method:
myset = {"apple", "banana", "cherry"}
myset.discard("banana")
print(myset)  # Output - {'apple', 'cherry'} (order may vary)

# Note: If the item to remove does not exist, discard() will NOT raise an error.

# You can also use the pop(), method to remove an item, but this method will remove a random item,
# so you cannot be sure which item that gets removed.
myset = {"apple", "banana", "cherry"}
x = myset.pop()
print(x)  # Output - removed item (random)
print(myset)  # Output - remaining set (order may vary)

# The clear() method empties the set:
myset = {"apple", "banana", "cherry"}
myset.clear()
print(myset)  # Output - set()

# The del keyword will delete the set completely:
myset = {"apple", "banana", "cherry"}
del myset
# print(myset)  # This will cause an error because the set no longer exists

# Loop Through a Set
myset = {"apple", "banana", "cherry"}
for x in myset:
    print(x)  # Output - apple banana cherry (order may vary)

# JOIN SETS
# There are several ways to join two or more sets in Python.

# The union() method returns a new set with all items from both sets:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)  # Output - {'a', 'b', 'c', 1, 2, 3} (order may vary)

# The | operator also returns a new set with all items from both sets:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)  # Output - {'a', 'b', 'c', 1, 2, 3} (order may vary)

# The update() method inserts the items from one set into another:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)  # Output - {'a', 'b', 'c', 1, 2, 3} (order may vary)

# The intersection() method returns a new set, that only contains the items that exist in both sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)  # Output - {'apple'}

# The & operator returns a new set, that only contains the items that exist in both sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print(set3)  # Output - {'apple'}

# The intersection_update() method keeps only the items that are present in both sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)  # Output - {'apple'}

# The difference() method returns a new set with items in the first set that are not in the second set:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)  # Output - {'banana', 'cherry'} (order may vary)

# The - operator returns a new set with items in the first set that are not in the second set:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2
print(set3)  # Output - {'banana', 'cherry'} (order may vary)

# The difference_update() method removes items from the first set that are in the second set:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)  # Output - {'banana', 'cherry'} (order may vary)

# The symmetric_difference() method returns a new set, with items that are not present in both sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)  # Output - {'banana', 'cherry', 'google', 'microsoft'} (order may vary)

# The ^ operator returns a new set, with items that are not present in both sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 ^ set2
print(set3)  # Output - {'banana', 'cherry', 'google', 'microsoft'} (order may vary)

# The symmetric_difference_update() method keeps only the items that are not present in both sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)  # Output - {'banana', 'cherry', 'google', 'microsoft'} (order may vary)

# SET METHODS
# Method                       Description
# add()                         Adds an element to the set
# clear()                       Removes all elements from the set
# copy()                        Returns a copy of the set
# difference()                  Returns a set containing the difference between two or more sets
# difference_update()           Removes the items in this set that are also included in another, specified set
# discard()                     Remove the specified item
# intersection()                Returns a set, that is the intersection of two other sets
# intersection_update()         Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()                  Returns whether two sets have a intersection or not
# issubset()                    Returns whether another set contains this set or not
# issuperset()                  Returns whether this set contains another set or not
# pop()                         Removes an element from the set
# remove()                      Removes the specified element
# symmetric_difference()        Returns a set with the symmetric differences of two sets
# symmetric_difference_update() Removes the items in this set that are also included in another, specified set, and inserts the other items
# union()                       Returns a set containing the union of sets
# update()                      Update the set with the union of this set and others

# Copy a Set

# Make a copy of a set with the copy() method:
thisset = {"apple", "banana", "cherry"}
myset = thisset.copy()
print(myset)  # Output - {'apple', 'banana', 'cherry'} (order may vary)

# Make a copy of a set with the set() constructor:
thisset = {"apple", "banana", "cherry"}
myset = set(thisset)
print(myset)  # Output - {'apple', 'banana', 'cherry'} (order may vary)

# issubset() method
# Returns whether another set contains this set or not
set1 = {"a", "b", "c"}
set2 = {"f", "e", "d", "c", "b", "a"}
x = set1.issubset(set2)
print(x)  # Output - True

# issuperset() method
# Returns whether this set contains another set or not
set1 = {"f", "e", "d", "c", "b", "a"}
set2 = {"a", "b", "c"}
x = set1.issuperset(set2)
print(x)  # Output - True

# isdisjoint() method
# Returns whether two sets have a intersection or not
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "facebook"}
x = set1.isdisjoint(set2)
print(x)  # Output - True

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
x = set1.isdisjoint(set2)
print(x)  # Output - False

# The set() Constructor
# It is also possible to use the set() constructor to make a set.
thisset = set(("apple", "banana", "cherry"))  # note the double round brackets
print(thisset)  # Output - {'apple', 'banana', 'cherry'} (order may vary)
