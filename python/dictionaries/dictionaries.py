# Dictionaries are used to store multiple items in a single variable.
# Dictionaries are one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Set, all with different qualities and usage.
# Dictionaries are created using curly braces, and they have keys and values:
mydict = {"name": "John", "age": 36, "country": "Norway"}
print(mydict)  # Output - {'name': 'John', 'age': 36, 'country': 'Norway'}

# Dictionary Length
mydict = {"name": "John", "age": 36, "country": "Norway"}
print(len(mydict))  # Output - 3

# Dictionary Items - Data Types
# Dictionary values can be of any data type:
dict1 = {"name": "John", "age": 36}  # str and int
dict2 = {"apple": 1, "banana": 2, "cherry": 3}  # str and int
dict3 = {"active": True, "inactive": False}  # str and bool

# A dictionary with strings, integers and boolean values:
dict1 = {"abc": "xyz", 34: 289, True: "test"}

mydict = {"name": "John", "age": 36, "country": "Norway"}
print(type(mydict))  # Output - <class 'dict'>

# The dict() Constructor
# It is also possible to use the dict() constructor to make a dictionary.
thisdict = dict(name="John", age=36, country="Norway")
print(thisdict)  # Output - {'name': 'John', 'age': 36, 'country': 'Norway'}

# Access Items
mydict = {"name": "John", "age": 36, "country": "Norway"}
print(mydict["name"])  # Output - John
print(mydict["age"])  # Output - 36
print(mydict["country"])  # Output - Norway

# You can also use the get() method to access items in a dictionary:
mydict = {"name": "John", "age": 36, "country": "Norway"}
print(mydict.get("name"))  # Output - John
print(mydict.get("age"))  # Output - 36

# If the key does not exist, the get() method returns None, but you can specify a default value:
mydict = {"name": "John", "age": 36, "country": "Norway"}
print(mydict.get("address"))  # Output - None
print(mydict.get("address", "Not found"))  # Output - Not found

# Get the Keys
mydict = {"name": "John", "age": 36, "country": "Norway"}
print(mydict.keys())  # Output - dict_keys(['name', 'age', 'country'])

# Get the Values
mydict = {"name": "John", "age": 36, "country": "Norway"}
print(mydict.values())  # Output - dict_values(['John', 36, 'Norway'])

# Get the Items
mydict = {"name": "John", "age": 36, "country": "Norway"}
print(mydict.items())  # Output - dict_items([('name', 'John'), ('age', 36), ('country', 'Norway')])

# Check if Key Exists
mydict = {"name": "John", "age": 36, "country": "Norway"}
if "name" in mydict:
    print("Yes, 'name' is one of the keys in the mydict dictionary")  # Output - Yes, 'name' is one of the keys in the mydict dictionary

# Change Items
mydict = {"name": "John", "age": 36, "country": "Norway"}
mydict["age"] = 37
print(mydict)  # Output - {'name': 'John', 'age': 37, 'country': 'Norway'}

# You can also use the update() method to change the value of an item:
mydict = {"name": "John", "age": 36, "country": "Norway"}
mydict.update({"age": 37})
print(mydict)  # Output - {'name': 'John', 'age': 37, 'country': 'Norway'}

# Add Items
mydict = {"name": "John", "age": 36, "country": "Norway"}
mydict["color"] = "red"
print(mydict)  # Output - {'name': 'John', 'age': 36, 'country': 'Norway', 'color': 'red'}

# You can also use the update() method to add multiple items:
mydict = {"name": "John", "age": 36, "country": "Norway"}
mydict.update({"color": "red", "brand": "Ford"})
print(mydict)  # Output - {'name': 'John', 'age': 36, 'country': 'Norway', 'color': 'red', 'brand': 'Ford'}

# Remove Items
# The pop() method removes the item with the specified key name:
mydict = {"name": "John", "age": 36, "country": "Norway"}
mydict.pop("age")
print(mydict)  # Output - {'name': 'John', 'country': 'Norway'}

# The popitem() method removes the item that was last inserted (in Python 3.7+):
mydict = {"name": "John", "age": 36, "country": "Norway"}
mydict.popitem()
print(mydict)  # Output - {'name': 'John', 'age': 36}

# The del keyword removes the item with the specified key name:
mydict = {"name": "John", "age": 36, "country": "Norway"}
del mydict["age"]
print(mydict)  # Output - {'name': 'John', 'country': 'Norway'}

# The del keyword can also delete the dictionary completely:
mydict = {"name": "John", "age": 36, "country": "Norway"}
del mydict
# print(mydict)  # This will cause an error because the dictionary no longer exists

# The clear() method empties the dictionary:
mydict = {"name": "John", "age": 36, "country": "Norway"}
mydict.clear()
print(mydict)  # Output - {}

# Loop Through a Dictionary
mydict = {"name": "John", "age": 36, "country": "Norway"}
for x in mydict:
    print(x)  # Output - name age country

# You can also use the values() method to return values of a dictionary:
mydict = {"name": "John", "age": 36, "country": "Norway"}
for x in mydict.values():
    print(x)  # Output - John 36 Norway

# You can use the keys() method to return the keys of a dictionary:
mydict = {"name": "John", "age": 36, "country": "Norway"}
for x in mydict.keys():
    print(x)  # Output - name age country

# You can use the items() method to return both keys and values of a dictionary:
mydict = {"name": "John", "age": 36, "country": "Norway"}
for x, y in mydict.items():
    print(x, y)  # Output - name John age 36 country Norway

# Copy a Dictionary

# Make a copy of a dictionary with the copy() method:
thisdict = {"name": "John", "age": 36, "country": "Norway"}
mydict = thisdict.copy()
print(mydict)  # Output - {'name': 'John', 'age': 36, 'country': 'Norway'}

# Make a copy of a dictionary with the dict() constructor:
thisdict = {"name": "John", "age": 36, "country": "Norway"}
mydict = dict(thisdict)
print(mydict)  # Output - {'name': 'John', 'age': 36, 'country': 'Norway'}

# Nested Dictionaries
# A dictionary can also contain dictionaries (nested dictionaries):
myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}

print(myfamily)  # Output - {'child1': {'name': 'Emil', 'year': 2004}, ...}

# Access nested dictionary items
print(myfamily["child1"]["name"])  # Output - Emil
print(myfamily["child2"]["year"])  # Output - 2007

# Create nested dictionaries
child1 = {
    "name": "Emil",
    "year": 2004
}
child2 = {
    "name": "Tobias",
    "year": 2007
}
myfamily = {
    "child1": child1,
    "child2": child2
}

print(myfamily)  # Output - {'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}}

# DICTIONARY METHODS
# Method           Description
# clear()          Removes all the elements from the dictionary
# copy()           Returns a copy of the dictionary
# fromkeys()       Returns a dictionary with the specified keys and value
# get()            Returns the value of the specified key
# items()          Returns a list containing a tuple for each key value pair
# keys()           Returns a list containing the dictionary's keys
# pop()            Removes the element with the specified key
# popitem()        Removes the last inserted key-value pair
# setdefault()     Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()         Updates the dictionary with the specified key-value pairs
# values()         Returns a list of all the values in the dictionary

# fromkeys() method
# Create a new dictionary with the specified keys and value:
x = ("key1", "key2", "key3")
mydict = dict.fromkeys(x, 0)
print(mydict)  # Output - {'key1': 0, 'key2': 0, 'key3': 0}

# setdefault() method
# Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
mydict = {"name": "John", "age": 36}
x = mydict.setdefault("country", "Norway")
print(x)  # Output - Norway
print(mydict)  # Output - {'name': 'John', 'age': 36, 'country': 'Norway'}

# The dict() Constructor
# It is also possible to use the dict() constructor to make a dictionary.
thisdict = dict(name="John", age=36, country="Norway")
print(thisdict)  # Output - {'name': 'John', 'age': 36, 'country': 'Norway'}
