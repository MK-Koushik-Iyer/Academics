import math
import random


x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))


p = int(input("Enter prime no p: "))
a = int(input("Enter a: "))

num = pow((3 * pow(x1, 2) + a), 1, p)
den = pow((2 * y1), -1,  p)

lam = pow(num * den, 1, p) 

print(f"lam: {lam}")

x3 = ((lam**2) - 2 * x1) % p
print(f"x3: {x3}")

y3 = (lam *(x1 - x3) - y1) % p
print(f"y3: {y3}")

print(f"2G is {(x3, y3)}")



# import random

# def point_double(x1, y1, a, p):
#     # Calculate numerator: 3*x1^2 + a
#     numerator = (3 * pow(x1, 2, p) + a) % p
    
#     # Calculate denominator: 2*y1
#     denominator = (2 * y1) % p
    
#     # Calculate modular inverse of denominator (Fermat's Little Theorem)
#     denominator_inv = pow(denominator, p - 2, p)  # Inverse of 2*y1 mod p
    
#     # Calculate lambda (slope) using modular arithmetic
#     lam = (numerator * denominator_inv) % p
    
#     # Calculate new x3 and y3
#     x3 = (lam ** 2 - 2 * x1) % p
#     y3 = (lam * (x1 - x3) - y1) % p

#     print(f" Point is {(x3, y3)}")
    
#     return (x3, y3)

# def recursive_point_double(x1, y1, a, p, n):
#     if n == 1:
#         return (x1, y1)  # Base case: return the point itself
    
#     # Double the point and recurse
#     x2, y2 = point_double(x1, y1, a, p)
#     return recursive_point_double(x2, y2, a, p, n - 1)

# # Main input section
# x1 = int(input("Enter x1: "))
# y1 = int(input("Enter y1: "))
# p = int(input("Enter prime number p: "))
# a = int(input("Enter a: "))
# n = int(input("Enter the number of doublings (n): "))

# # Get the result after n doublings
# x_n, y_n = recursive_point_double(x1, y1, a, p, n)

# print(f"Result after {n} doublings is: ({x_n}, {y_n})")
