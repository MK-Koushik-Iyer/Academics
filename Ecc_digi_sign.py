# x1 = int(input("Enter G's x1: "))
# y1 = int(input("Enter G's y1: "))

# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# p = int(input("Enter p: "))


# d = int(input("Enter pvt key d: "))

# def inv_mod(s, g):
#     for i in range(2, g):
#         if (i * s) % g == 1:
#             return i
        
#     raise ValueError("Error")


# def ptdbl(x1, y1, a, p):
#     num = (3 * (x1 ** 2) + a) % p
#     den = (2 * y1) % p

#     print(f"num is {num}")
#     print(f"den is {den}")
    

#     lam = (num * inv_mod(den, p)) % p
#     print(f"lam is {lam}")


#     x3 = ((lam ** 2) - (2 * x1)) % p
#     print(f"x3 is {x3}")

#     y3 = ((lam * (x1 - x3)) - y1)% p
#     print(f"y3 is {y3}")

#     print(f"{(x3, y3)}")

#     return x3, y3


# n = int(input("Enter n: "))

# def recursive(x1, y1, a, p, l):
#     if n == 1:
#         return (x1, y1)
    
#     else:
#         x, y = ptdbl(x1, y1, a, p)
#         return recursive(x, y, a, p, l-1)
    



# def ptadd(x1, y1, x2, y2, p):
#     nu = (y2 - y1) % p
#     de = (x2 - x1) % p
#     print(f"{nu}")
#     print(f"{de}")

#     lamd = (nu * (inv_mod(de)))*p
#     print(f"{lamd}")

#     x4 = ((lamd ** 2) - x1 - x2)%p
#     y4 = ((lamd * (x1 - x4) - y1))%p

#     print(f"{x4}")
#     print(f"{y4}")
#     print(f"{(x4, y4)}")

#     return x4, y4


# Qx,Qy = recursive(x1, y1, a, p, d)
# print(f"Q is {(Qx,Qy)}")

# k = int(input("Enter random k val: "))

# K1,K2 = recursive(x1, y1, a, p, k)
# print(f"K is {(K1, K2)}")

# r = K1

# H = int(input("Enter H value: "))

# #Signing
# S = (inv_mod(k) * (H + d * r))% n

# #Verifying

# W = (inv_mod(S)) % n


# u1x, u1y = ((H * W) % n) * recursive(x1, y1, a, p , 1)
# print(f"u1 is {(u1x, u1y)}")

# u2x, u2y = ((r * W)%n) * Q
# print(f" u2 is {(u2x, u2y)}")

# res1, res2 = ptadd(u1x, u1y, u2x, u2y, n)
# print(f"{(res1, res2)}")


# if res1 % n == r % n:
#     print("Valid")
# else:
#     print("Invalid")




# Elliptic Curve Point Doubling
def point_double(x, y, a, p):
    if y == 0:
        return None
    lam = (3 * x * x + a) * pow(2 * y, -1, p) % p
    x_r = (lam * lam - 2 * x) % p
    y_r = (lam * (x - x_r) - y) % p
    return x_r, y_r

# Point Addition (no doubling)
def point_add(x1, y1, x2, y2, p):
    if x1 == x2 and y1 == (-y2 % p):
        return None
    lam = ((y2 - y1) * pow(x2 - x1, -1, p)) % p
    x_r = (lam * lam - x1 - x2) % p
    y_r = (lam * (x1 - x_r) - y1) % p
    return x_r, y_r

# Scalar multiply via repeated doubling (simple)
def scalar_double(x, y, k, a, p):
    result = (x, y)
    for _ in range(k - 1):
        result = point_double(result[0], result[1], a, p)
    return result

# Key generation (Q = d * G, R = k * G)
def generate_keys(Gx, Gy, a, p):
    d = 7
    k = 3
    Qx, Qy = scalar_double(Gx, Gy, d, a, p)
    Rx, _ = scalar_double(Gx, Gy, k, a, p)
    return d, k, Qx, Qy, Rx

# Signing
def sign(k, n, m, d, r):
    s = pow(k, -1, n) * (m + d * r) % n
    return s

# Verification
def verify(s, n, Gx, Gy, Qx, Qy, r, m, a, p):
    w = pow(s, -1, n)
    u1 = scalar_double(Gx, Gy, m * w % n, a, p)
    u2 = scalar_double(Qx, Qy, r * w % n, a, p)
    R = point_add(u1[0], u1[1], u2[0], u2[1], p)
    if R and R[0] == r:
        print("Valid")
    else:
        print("Invalid")

# Input and Run
a = int(input("Enter curve coefficient a: "))
p = int(input("Enter prime p: "))
Gx = int(input("Enter x-coordinate of base point G: "))
Gy = int(input("Enter y-coordinate of base point G: "))
n = int(input("Enter order n: "))
m = int(input("Enter message (as integer): "))

d, k, Qx, Qy, r = generate_keys(Gx, Gy, a, p)
print(f"Private key d: {d}, Random nonce k: {k}")
print(f"Public key Q: ({Qx}, {Qy})")
print(f"r (from R=kG): {r}")

s = sign(k, n, m, d, r)
print(f"Signature s: {s}")
verify(s, n, Gx, Gy, Qx, Qy, r, m, a, p)





