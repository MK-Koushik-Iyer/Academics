p = int(input("Enter the prime p value: "))
q = int(input("Enter the prime q value: "))


def is_prime(no):
    if no < 2:
        return False
    
    for i in range(2, no //2 + 1):
        if no % i == 0:
            return False
        
    return True


if is_prime(p):
    p = p

else:
    while(1):
        p = int(input("Enter the prime p value: "))
        if is_prime(p):
            p = p
            break


if is_prime(q):
   q = q

else:
    while(1):
        q = int(input("Enter the prime q value: "))
        if is_prime(p):
            q = q
            break


n = p * q
print(f"n is {n}")



phi_n = (p - 1) * (q - 1)
print(f"phi is {phi_n}")

e = int(input("Enter public key e: "))
d = int(input("Enter pvt key d: "))


H_m = int(input("Enter Hashed M: "))

#Signing

S = (H_m ** d) % n
print(f"Signed Value is {S}")

H_M = (S ** e)% n
print(f"H_M is {H_M}")

if H_m == H_M:
    print("Valid")

else:
    print("Invalid")

