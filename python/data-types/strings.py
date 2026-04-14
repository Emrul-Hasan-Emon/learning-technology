# Strings in python are surrounded by either single quotation marks, or double quotation marks.
 # 'hello' is the same as "hello".
a = "Hello, World!"
print(a)

# Assign String to a Variable
a = "Hello, World!"
print(a)

# Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

# Strings are Arrays
a = "Hello, World!"
print(a[1])

# Looping Through a String
for x in "banana":
  print(x) # Output - b a n a n a

# String Length
a = "Hello, World!"
print(len(a))

# Check String - To check if a certain phrase or character is present in a string, we can use the keyword in.
txt = "The best things in life are free!"
print("free" in txt) # Output - True

# Use it in an if statement:
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.") # Output - Yes, 'free' is present.

# Check if NOT
txt = "The best things in life are free!"
print("expensive" not in txt) # Output - True

# Use it in an if statement:
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.") # Output - No, 'expensive' is NOT present.

# STRING SLICING
b = "Hello, World!"
print(b[2:5]) # Output - llo

b = "Hello, World!" # Slice From the Start
print(b[:5]) # Output - Hello

b = "Hello, World!" # Slice To the End
print(b[2:]) # Output - llo, World!

b = "Hello, World!" # Negative Indexing - Use negative indexes to start the slice from the end of the string
print(b[-5:-2]) # Output - rld

# MODIFY STRINGS
a = "Hello, World!" # Upper Case
print(a.upper()) # Output - HELLO, WORLD!

a = "Hello, World!" # Lower Case
print(a.lower()) # Output - hello, world!

a = " Hello, World! " # Remove Whitespace
print(a.strip()) # returns "Hello, World!" 

a = "Hello, World!" # Replace String
print(a.replace("H", "J")) # Output - Jello, World!

a = "Hello, World!" # Split String
print(a.split(",")) # returns ['Hello', ' World!'] 

# STRING CONCATENATION
a = "Hello"
b = "World"
c = a + " " + b
print(c) # Output - Hello World

# FORMAT STRINGS
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age)) # Output - My name is John, and I am 36

price = 59
txt = f"The price is {price} dollars"
print(txt) # Output - The price is 59 dollars

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt) # Output - The price is 59.00 dollars

txt = f"The price is {20 * 59} dollars"
print(txt) # Output - The price is 1180 dollars

# ESCAPE CHARACTER
txt = "We are the so-called \"Vikings\" from the north."
print(txt) # Output - We are the so-called "Vikings" from the north.
# \'	Single Quote
# \\	Backslash
# \n	New Line
# \r	Carriage Return
# \t	Tab
# \b	Backspace
# \f	Form Feed
# \ooo	Octal value
# \xhh	Hex value

# STRING METHODS
a = "Hello, World!" # capitalize() - Converts the first character to upper case
print(a.capitalize()) # Output - Hello, world!

a = "Hello, World!" # casefold() - Converts string into lower case
print(a.casefold()) # Output - hello, world!

a = "Hello, World!" # center() - Returns a centered string
print(a.center(20)) # Output - '   Hello, World!    '

a = "Hello, World!" # count() - Returns the number of times a specified value occurs in a string
print(a.count("o")) # Output - 2

a = "Hello, World!" # encode() - Returns an encoded version of the string
print(a.encode()) # Output - b'Hello, World!'

a = "Hello, World!" # endswith() - Returns true if the string ends with the specified value
print(a.endswith("!")) # Output - True

a = "Hello, World!" # expandtabs() - Sets the tab size of the string
txt = "H\te\tl\tl\to"
print(txt.expandtabs(2)) # Output - H e l l o

a = "Hello, World!" # find() - Searches the string for a specified value and returns the position of where it was found
print(a.find("W")) # Output - 7

a = "Hello, World!" # format() - Formats specified values in a string
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49)) # Output - For only 49.00 dollars!

a = "Hello, World!" # format_map() - Formats specified values in a string
my_dict = {"price": 49}
txt = "For only {price:.2f} dollars!"
print(txt.format_map(my_dict)) # Output - For only 49.00 dollars!

a = "Hello, World!" # index() - Searches the string for a specified value and returns the position of where it was found
print(a.index("W")) # Output - 7

a = "Hello, World!" # isalnum() - Returns True if all characters in the string are alphanumeric
print(a.isalnum()) # Output - False

a = "Hello, World!" # isalpha() - Returns True if all characters in the string are in the alphabet
print(a.isalpha()) # Output - False

a = "Hello, World!" # isdecimal() - Returns True if all characters in the string are decimals
print(a.isdecimal()) # Output - False

a = "Hello, World!" # isdigit() - Returns True if all characters in the string are digits
print(a.isdigit()) # Output - False

a = "Hello, World!" # isidentifier() - Returns True if the string is an identifier
print(a.isidentifier()) # Output - False

a = "Hello, World!" # islower() - Returns True if all characters in the string are lower case
print(a.islower()) # Output - False

a = "Hello, World!" # isnumeric() - Returns True if all characters in the string are numeric
print(a.isnumeric()) # Output - False

a = "Hello, World!" # isprintable() - Returns True if all characters in the string are printable
print(a.isprintable()) # Output - True

a = "Hello, World!" # isspace() - Returns True if all characters in the string are whitespaces
print(a.isspace()) # Output - False

a = "Hello, World!" # istitle() - Returns True if the string follows the rules of a title
print(a.istitle()) # Output - True

a = "Hello, World!" # isupper() - Returns True if all characters in the string are upper case
print(a.isupper()) # Output - False

a = "Hello, World!" # join() - Joins the elements of an iterable to the end of the string
my_tuple = ("a", "b", "c")
print(a.join(my_tuple)) # Output - aHello, World!baHello, World!

a = "Hello, World!" # ljust() - Returns a left justified version of the string
print(a.ljust(20)) # Output - 'Hello, World!     '

a = "Hello, World!" # lower() - Converts a string into lower case
print(a.lower()) # Output - hello, world!

a = "Hello, World!" # lstrip() - Returns a left trim version of the string
print(a.lstrip()) # Output - 'Hello, World!     '

a = "Hello, World!" # maketrans() - Returns a translation table to be used in translations
my_dict = {83: 80}
print(a.maketrans(my_dict)) # Output - {83: 80}

a = "Hello, World!" # partition() - Returns a tuple where the string is parted into three parts
print(a.partition("World")) # Output - ('Hello, ', 'World', '!')

a = "Hello, World!" # replace() - Returns a string where a specified value is replaced with a specified value
print(a.replace("H", "J")) # Output - Jello, World!
