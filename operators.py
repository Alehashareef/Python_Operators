# 1. Arithmetic Operators
# Used for mathematical operations.

a = 10  
b = 3  

print(a + b)   # 13 (Addition)
print(a - b)   # 7  (Subtraction)
print(a * b)   # 30 (Multiplication)
print(a / b)   # 3.33 (Division)
print(a // b)  # 3  (Floor Division - removes decimal)
print(a % b)   # 1  (Modulus - remainder)
print(a ** b)  # 1000 (Exponentiation - 10^3)


# 2. Assignment Operators
# Used to assign values to variables.

x = 5  
x += 3  # Same as x = x + 3
print(x)  # 8

x -= 2  # x = x - 2
print(x)  # 6

x *= 4  # x = x * 4
print(x)  # 24

x /= 6  # x = x / 6
print(x)  # 4.0


# 3. Comparison Operators
# Used to compare values (True/False).


a = 10  
b = 20  

print(a == b)  # False (Equal to)
print(a != b)  # True  (Not equal to)
print(a > b)   # False (Greater than)
print(a < b)   # True  (Less than)
print(a >= b)  # False (Greater than or equal to)
print(a <= b)  # True  (Less than or equal to)


# 4. Logical Operators
# Used for combining conditions.

x = 5  
y = 10  

print(x > 3 and y < 20)  # True (Both conditions are True)
print(x > 3 or y > 20)   # True (At least one condition is True)
print(not(x > 3))        # False (Reverses the result)


# 5. Bitwise Operators
# Works at the binary level (0s and 1s).

a = 5   # 0101 in binary  
b = 3   # 0011 in binary  

print(a & b)  # 1  (Bitwise AND -> 0001)
print(a | b)  # 7  (Bitwise OR -> 0111)
print(a ^ b)  # 6  (Bitwise XOR -> 0110)
print(~a)     # -6 (Bitwise NOT -> Inverts all bits)
print(a << 1) # 10 (Left shift -> 1010)
print(a >> 1) # 2  (Right shift -> 0010)


# 6. Identity Operators
# Checks if two variables refer to the same object.

a = [1, 2, 3]  
b = a  
c = [1, 2, 3]  

print(a is b)      # True  (Same object)
print(a is c)      # False (Different objects, same values)
print(a is not c)  # True  (Not the same object)


# 7. Membership Operators
# Checks if a value exists in a sequence (list, string, etc.).

my_list = [10, 20, 30, 40]  

print(20 in my_list)   # True (20 is in the list)
print(50 not in my_list)  # True (50 is NOT in the list)
