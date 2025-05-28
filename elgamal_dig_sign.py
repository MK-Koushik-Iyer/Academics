q = int(input("Enter q large prime: "))


def gcd(a, b):
    while(b):
        a, b = b , a%b

    return a

def validate_prime(no):
    if no < 2:
        return False
    
    for i in range(2, no//2 + 1):
        if no % i == 0:
            return False
        
    return True

if validate_prime(q):
    q = q
else:
    while(1):
        q = int(input("Enter q large prime: "))
        if validate_prime(q):
            break

def inv_mod(d, n):
    for i in range(1, n):
        if (d * i)% n == 1:
            return i
        
    raise ValueError("Error")


alpha = int(input("Enter primitive root alpha: "))

xa = int(input("Enter priv key xa: "))
ya = (alpha ** xa) % q

print(f"ya is {ya}")

hashed_m= int(input("Enter Hashed m: "))

def gen_k(q):
    for i in range(2, q - 1):
        if gcd(i, q - 1) == 1:
            return i
        
    raise ValueError("Error")

k = gen_k(q)
print(f"k is {k}")


S1 = (alpha ** k)%q
print(f"S1 is {S1}")


S2 = ((inv_mod(k, q - 1) * (hashed_m - (xa * S1)))) % (q - 1)
print(f"S2 is {S2}")

V1 = (alpha ** hashed_m)% q
print(f"V1 is {V1}")

V2 = ((ya ** S1) * (S1 ** S2))% q
print(f"V2 is {V2}")

if V1 == V2:
    print("Valid Signature ")
else:
    print("Invalid Signature")




