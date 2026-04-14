# =	    x = 5	        x = 5	
# +=	x += 3	        x = x + 3	
# -=	x -= 3	        x = x - 3	
# *=	x *= 3	        x = x * 3	
# /=	x /= 3	        x = x / 3	
# %=	x %= 3	        x = x % 3	
# //=	x //= 3	        x = x // 3	
# **=	x **= 3	        x = x ** 3	
# &=	x &= 3	        x = x & 3	
# |=	x |= 3	        x = x | 3	
# ^=	x ^= 3	        x = x ^ 3	
# >>=	x >>= 3	        x = x >> 3	
# <<=	x <<= 3	        x = x << 3	
# :=	print(x := 3)	x = 3
# print(x)

# The Walrus Operator
# The walrus operator (:=) assigns values to variables as part of a larger expression.
# Example
print(x := 3) # Output - 3

numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")