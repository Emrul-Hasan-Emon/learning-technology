"""
Regular Expressions (regex) and Pattern Matching in Python

The re module provides support for regular expressions and pattern matching.
It allows you to search, find, replace, and validate strings using patterns.
"""

import re


# ============================================================================
# 1. Basic Pattern Matching (re.search)
# ============================================================================

print("=" * 70)
print("1. BASIC PATTERN MATCHING (search)")
print("=" * 70)

text = "The phone number is 123-456-7890"
pattern = r"\d{3}-\d{3}-\d{4}"  # Pattern for phone number

match = re.search(pattern, text)
if match:
    print(f"Text: {text}")
    print(f"Pattern: {pattern}")
    print(f"Found: {match.group()}")
    print(f"Position: {match.start()}-{match.end()}")
else:
    print("Pattern not found")


# ============================================================================
# 2. Finding All Occurrences (re.findall)
# ============================================================================

print("\n" + "=" * 70)
print("2. FINDING ALL OCCURRENCES (findall)")
print("=" * 70)

text = "Contact us at email1@example.com or email2@domain.org"
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

emails = re.findall(pattern, text)
print(f"Text: {text}")
print(f"Pattern: Email addresses")
print(f"Found emails: {emails}")

# Find all numbers
text = "I have 2 apples, 5 oranges, and 12 bananas"
numbers = re.findall(r"\d+", text)
print(f"\nText: {text}")
print(f"All numbers found: {numbers}")


# ============================================================================
# 3. Finding with Groups (re.finditer)
# ============================================================================

print("\n" + "=" * 70)
print("3. FINDING WITH GROUPS (finditer)")
print("=" * 70)

text = "John: 25, Alice: 30, Bob: 28"
pattern = r"(\w+):\s*(\d+)"

print(f"Text: {text}")
print(f"Pattern: name: age")
print("Matches:")

for match in re.finditer(pattern, text):
    print(f"  Full match: {match.group()}")
    print(f"  Name (group 1): {match.group(1)}")
    print(f"  Age (group 2): {match.group(2)}")


# ============================================================================
# 4. String Substitution (re.sub)
# ============================================================================

print("\n" + "=" * 70)
print("4. STRING SUBSTITUTION (sub)")
print("=" * 70)

# Replace phone number format
text = "Call 123-456-7890 or 987-654-3210"
pattern = r"(\d{3})-(\d{3})-(\d{4})"
replacement = r"(\1) \2-\3"

result = re.sub(pattern, replacement, text)
print(f"Original: {text}")
print(f"Replaced: {result}")

# Remove all digits
text = "The code is abc123def456"
result = re.sub(r"\d", "", text)
print(f"\nOriginal: {text}")
print(f"After removing digits: {result}")

# Case-insensitive replacement
text = "Hello HELLO hello"
result = re.sub(r"hello", "hi", text, flags=re.IGNORECASE)
print(f"\nOriginal: {text}")
print(f"After case-insensitive replacement: {result}")


# ============================================================================
# 5. Splitting Strings (re.split)
# ============================================================================

print("\n" + "=" * 70)
print("5. SPLITTING STRINGS (split)")
print("=" * 70)

# Split by comma or semicolon
text = "apple,banana;orange,grape"
result = re.split(r"[,;]", text)
print(f"Text: {text}")
print(f"Split by comma or semicolon: {result}")

# Split by whitespace
text = "one   two  three    four"
result = re.split(r"\s+", text)
print(f"\nText: '{text}'")
print(f"Split by whitespace: {result}")


# ============================================================================
# 6. Pattern Matching Basics
# ============================================================================

print("\n" + "=" * 70)
print("6. PATTERN MATCHING BASICS")
print("=" * 70)

patterns = {
    r"^Hello": "Starts with 'Hello'",
    r"world$": "Ends with 'world'",
    r"o.o": "Contains 'o', any char, 'o'",
    r"a+": "One or more 'a's",
    r"ab?c": "Optional 'b' between 'a' and 'c'",
    r"(ab)+": "One or more 'ab' groups",
    r"[aeiou]": "Any vowel",
    r"[^0-9]": "Not a digit",
    r"\d+": "One or more digits",
    r"\w+": "Word characters (letters, digits, _)",
    r"\s+": "Whitespace characters"
}

print("Common regex patterns:")
for pattern, description in patterns.items():
    print(f"  {pattern:<20} - {description}")


# ============================================================================
# 7. Validating Email Addresses
# ============================================================================

print("\n" + "=" * 70)
print("7. VALIDATING EMAIL ADDRESSES")
print("=" * 70)

def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

emails = [
    "user@example.com",
    "john.doe@company.co.uk",
    "invalid.email@",
    "no-at-sign.com",
    "user+tag@domain.org"
]

for email in emails:
    valid = is_valid_email(email)
    print(f"  {email:<30} - {'Valid' if valid else 'Invalid'}")


# ============================================================================
# 8. Validating Phone Numbers
# ============================================================================

print("\n" + "=" * 70)
print("8. VALIDATING PHONE NUMBERS")
print("=" * 70)

def is_valid_phone(phone):
    # Pattern: (123) 456-7890 or 123-456-7890 or 1234567890
    pattern = r"^(?:\+?1[-.\s]?)?\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})$"
    return re.match(pattern, phone) is not None

phones = [
    "123-456-7890",
    "(123) 456-7890",
    "1234567890",
    "+1-123-456-7890",
    "(123)456-7890",
    "invalid-123"
]

for phone in phones:
    valid = is_valid_phone(phone)
    print(f"  {phone:<25} - {'Valid' if valid else 'Invalid'}")


# ============================================================================
# 9. Extracting Data
# ============================================================================

print("\n" + "=" * 70)
print("9. EXTRACTING DATA")
print("=" * 70)

# Extract date components
text = "Meeting on 2025-03-15 at 2:30 PM"
pattern = r"(\d{4})-(\d{2})-(\d{2})"

match = re.search(pattern, text)
if match:
    year, month, day = match.groups()
    print(f"Text: {text}")
    print(f"Year: {year}, Month: {month}, Day: {day}")

# Extract HTML tags
html = "<h1>Title</h1><p>Paragraph</p>"
tags = re.findall(r"<(\w+)>", html)
print(f"\nHTML: {html}")
print(f"Tags found: {tags}")


# ============================================================================
# 10. Named Groups
# ============================================================================

print("\n" + "=" * 70)
print("10. NAMED GROUPS")
print("=" * 70)

text = "John Smith, 25 years old, lives in New York"
pattern = r"(?P<name>\w+\s\w+),\s*(?P<age>\d+)\s*years old,\s*lives in\s*(?P<city>\w+\s\w+)"

match = re.search(pattern, text)
if match:
    print(f"Text: {text}")
    print(f"Name: {match.group('name')}")
    print(f"Age: {match.group('age')}")
    print(f"City: {match.group('city')}")
    print(f"All groups: {match.groupdict()}")


# ============================================================================
# 11. Case-Insensitive Matching
# ============================================================================

print("\n" + "=" * 70)
print("11. CASE-INSENSITIVE MATCHING")
print("=" * 70)

text = "Hello HELLO hello HeLLo"
pattern = r"hello"

# Case-sensitive (default)
matches_case = re.findall(pattern, text)
print(f"Text: {text}")
print(f"Case-sensitive matches: {matches_case}")

# Case-insensitive
matches_nocase = re.findall(pattern, text, re.IGNORECASE)
print(f"Case-insensitive matches: {matches_nocase}")


# ============================================================================
# 12. Multiline Matching
# ============================================================================

print("\n" + "=" * 70)
print("12. MULTILINE MATCHING")
print("=" * 70)

text = """The first line
The second line
The third line"""

# Without MULTILINE: ^ and $ match string start/end
pattern1 = r"^The"
matches1 = re.findall(pattern1, text)
print(f"Text:\n{text}")
print(f"\nWithout MULTILINE (^The): {len(matches1)} matches")

# With MULTILINE: ^ and $ match line start/end
matches2 = re.findall(pattern1, text, re.MULTILINE)
print(f"With MULTILINE (^The): {len(matches2)} matches (one per line)")


# ============================================================================
# 13. Substitution with Function
# ============================================================================

print("\n" + "=" * 70)
print("13. SUBSTITUTION WITH FUNCTION")
print("=" * 70)

def double_number(match):
    num = int(match.group())
    return str(num * 2)

text = "I have 2 apples, 5 oranges, and 10 bananas"
result = re.sub(r"\d+", double_number, text)

print(f"Original: {text}")
print(f"After doubling numbers: {result}")


# ============================================================================
# 14. Lookahead and Lookbehind
# ============================================================================

print("\n" + "=" * 70)
print("14. LOOKAHEAD AND LOOKBEHIND")
print("=" * 70)

# Lookahead: match digits followed by " dollars"
text = "I have 100 dollars and 50 euros"
pattern = r"\d+(?= dollars)"
matches = re.findall(pattern, text)
print(f"Text: {text}")
print(f"Lookahead (?= dollars): {matches}")

# Lookbehind: match word after "price: "
text = "price: $50, cost: $30"
pattern = r"(?<=\$)\d+"
matches = re.findall(pattern, text)
print(f"\nText: {text}")
print(f"Lookbehind (?<=\\$): {matches}")


# ============================================================================
# 15. URL Validation and Extraction
# ============================================================================

print("\n" + "=" * 70)
print("15. URL VALIDATION AND EXTRACTION")
print("=" * 70)

def is_valid_url(url):
    pattern = r"^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[^\s]*)?$"
    return re.match(pattern, url) is not None

urls = [
    "https://www.example.com",
    "http://example.com/page",
    "https://sub.domain.co.uk/path?query=value",
    "not a url",
    "ftp://example.com"
]

for url in urls:
    valid = is_valid_url(url)
    print(f"  {url:<45} - {'Valid' if valid else 'Invalid'}")


# ============================================================================
# 16. Compile and Reuse
# ============================================================================

print("\n" + "=" * 70)
print("16. COMPILE AND REUSE PATTERNS")
print("=" * 70)

# Compile pattern once, use multiple times
email_pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")

texts = [
    "Contact john@example.com",
    "Email alice@domain.org here",
    "No email here"
]

print("Using compiled pattern for multiple searches:")
for text in texts:
    match = email_pattern.search(text)
    if match:
        print(f"  {text:<40} - Found: {match.group()}")
    else:
        print(f"  {text:<40} - No match")


# ============================================================================
# 17. Common Regex Patterns (Cheat Sheet)
# ============================================================================

print("\n" + "=" * 70)
print("17. COMMON REGEX PATTERNS (CHEAT SHEET)")
print("=" * 70)

cheat_sheet = """
ANCHORS:
  ^pattern      - Start of string/line
  pattern$      - End of string/line
  \\bword\\b      - Word boundary

CHARACTER CLASSES:
  [abc]         - Any of a, b, or c
  [a-z]         - Any lowercase letter
  [^abc]        - Not a, b, or c
  \\d            - Any digit
  \\D            - Not a digit
  \\w            - Word character (letter, digit, _)
  \\W            - Not a word character
  \\s            - Whitespace
  \\S            - Not whitespace
  .             - Any character (except newline)

QUANTIFIERS:
  *             - Zero or more
  +             - One or more
  ?             - Zero or one
  {n}           - Exactly n times
  {n,}          - n or more times
  {n,m}         - Between n and m times

GROUPS:
  (pattern)     - Capture group
  (?P<name>...)- Named group
  (?:...)       - Non-capturing group
  (?=...)       - Lookahead
  (?!...)       - Negative lookahead
  (?<=...)      - Lookbehind
  (?<!...)      - Negative lookbehind

ALTERNATION:
  pattern1|pattern2 - pattern1 OR pattern2

FLAGS:
  re.IGNORECASE - Case-insensitive
  re.MULTILINE  - ^ and $ match line boundaries
  re.DOTALL     - . matches newlines
  re.VERBOSE    - Allow comments and whitespace
"""

print(cheat_sheet)


# ============================================================================
# 18. Password Validation (Complex Example)
# ============================================================================

print("\n" + "=" * 70)
print("18. PASSWORD VALIDATION (COMPLEX EXAMPLE)")
print("=" * 70)

def is_strong_password(password):
    """
    Strong password must have:
    - At least 8 characters
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one digit
    - At least one special character
    """
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"\d", password):
        return False
    if not re.search(r"[!@#$%^&*()_+\-=\[\]{}|;:,.<>?]", password):
        return False
    return True

passwords = [
    "weak",
    "WeakPassword123",
    "Strong@Pass123",
    "Verys3cur3P@ssw0rd",
]

for pwd in passwords:
    strong = is_strong_password(pwd)
    print(f"  {pwd:<25} - {'Strong' if strong else 'Weak'}")


# ============================================================================
# 19. Summary of Functions
# ============================================================================

print("\n" + "=" * 70)
print("19. SUMMARY OF RE MODULE FUNCTIONS")
print("=" * 70)

summary = """
Main Functions:
  re.search(pattern, string)       - Find first match
  re.match(pattern, string)        - Match at start of string
  re.findall(pattern, string)      - Find all matches (list)
  re.finditer(pattern, string)     - Find all matches (iterator)
  re.sub(pattern, repl, string)    - Replace matches
  re.split(pattern, string)        - Split string by pattern
  re.compile(pattern)              - Compile pattern for reuse

Match Object Methods:
  match.group()                    - Get matched string
  match.group(n)                   - Get group n
  match.groups()                   - Get all groups as tuple
  match.groupdict()                - Get named groups as dict
  match.start()                    - Get start position
  match.end()                      - Get end position
  match.span()                     - Get (start, end) tuple

Flags:
  re.IGNORECASE (re.I)             - Ignore case
  re.MULTILINE (re.M)              - ^ $ match lines
  re.DOTALL (re.S)                 - . matches newlines
  re.VERBOSE (re.X)                - Allow whitespace/comments
"""

print(summary)
