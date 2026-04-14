# & 	AND	Sets each bit to 1 if both bits are 1	x & y	
# |	    OR	Sets each bit to 1 if one of two bits is 1	x | y	
# ^	    XOR	Sets each bit to 1 if only one of two bits is 1	x ^ y	
# ~	    NOT	Inverts all the bits	~x	
# <<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2	
# >>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2

# The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:
x = 5  # 0101 in binary
y = 3  # 0011 in binary
print(x & y) # Output - 1 (0001 in binary)
print(x | y) # Output - 7 (0111 in binary)
print(x ^ y) # Output - 6 (0110 in binary)
print(~x)    # Output - -6 (inverts the bits of 5,
# which is 0101 in binary, resulting in 1010 in binary, which is -6 in decimal)
print(x << 2) # Output - 20 (shifts bits of 5 to
# the left by 2 positions, resulting in 10100 in binary, which is 20 in decimal)
print(x >> 2) # Output - 1 (shifts bits of 5 to
# the right by 2 positions, resulting in 0001 in binary, which is 1 in decimal)
print(y << 2) # Output - 12 (shifts bits of 3 to
# the left by 2 positions, resulting in 1100 in binary, which is
# 12 in decimal)
print(y >> 2) # Output - 0 (shifts bits of 3 to
# the right by 2 positions, resulting in 0000 in binary, which is 0 in decimal)
print(x & 1) # Output - 1 (0101 & 0001 = 0001)