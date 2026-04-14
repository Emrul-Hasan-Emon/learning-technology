# Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first:
print((6 + 3) - (6 + 3)) # Output - 0
# Break down the expression:
# (6 + 3) - (6 + 3)
# 9 - 9
print(9 - 9) # Output - 0

# Multiplication * has higher precedence than addition +, and therefore multiplications are evaluated before additions:
print(10 + 5 * 2) # Output - 20
# Break down the expression:
# 10 + 5 * 2
# 10 + 10
print(10 + 10) # Output - 20

# Precedence Order
# 1. Parentheses ()
# 2. Exponentiation **
# 3. Unary plus and minus +x, -x
# 4. Multiplication *, Division /, Floor Division //, Modulus %
# 5. Addition +, Subtraction -
# 6. Comparison Operators ==, !=, >, <, >=, <=
# 7. Logical Operators and, or, not
# 8. Assignment Operators =, +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=, :=
# When operators have the same precedence, they are evaluated from left to right.
print(10 - 5 + 2) # Output - 7
# Break down the expression:
# 10 - 5 + 2
# 5 + 2
print(5 + 2) # Output - 7