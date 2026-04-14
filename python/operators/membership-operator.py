# in 	    Returns True if a sequence with the specified value is present in the object	    x in y	
# not in	Returns True if a sequence with the specified value is not present in the object	x not in y

fruits = ["apple", "banana", "cherry"]
print("banana" in fruits) # Output - True

fruits = ["apple", "banana", "cherry"]
print("pineapple" not in fruits) # Output - True

# Membership in Strings
txt = "Hello, welcome to my world."
print("welcome" in txt) # Output - True
txt = "Hello, welcome to my world."
print("goodbye" not in txt) # Output - True