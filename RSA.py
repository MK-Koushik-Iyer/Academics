import random
import math

def is_prime(number):
    if number < 2:
        return False
   
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
        
    return True

def generate_prime(min_num, max_num):
    prime = random.randint(min_num, max_num)
    while not is_prime(prime):
        prime = random.randint(min_num, max_num)

    return prime

def inv_modulo(e, phi):
    for d in range(3, phi):
        if (e * d) % phi == 1:
            return d

    raise ValueError("Error")


p = generate_prime(1200,1500)
q = generate_prime(1200,1500)

while p == q:
    q = generate_prime(1200,1500)
        

n = p * q

phi_n = (p-1) *(q-1)

e = random.randint(3, phi_n - 1)

while math.gcd(e, phi_n) != 1:
    e = random.randint(3, phi_n - 1)

d = inv_modulo(e, phi_n)

msg = "Hello Cyber"

print(p)
print(q)
print(n)
print(phi_n)
print(e)
print(d)
print(msg)


msg_enc = [ord(ch) for ch in msg]
CT = [pow(ch, e, n) for ch in msg_enc]

print(CT)

decoded = [pow(ch,d, n) for ch in CT]

PT = "".join(chr(ch) for ch in decoded)

print(PT)


            