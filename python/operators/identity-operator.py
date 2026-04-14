# is 	    Returns True if both variables are the same object	    x is y	
# is not	Returns True if both variables are not the same object	x is not y

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z) # Output - True
print(x is y) # Output - False
print(x == y) # Output - True

x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y) # Output - True

# Difference Between is and ==
# The == operator compares the values of both the operands and checks for value equality.
# The is operator compares the identities of both the operands and checks for reference equality.

x = [1, 2, 3]
y = [1, 2, 3]

print(x == y) # Output - True (because the values are the same)
print(x is y) # Output - False (because x and y are different objects in memory)