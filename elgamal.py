import random
import math

def gen_key(q):
    key = random.randint(2, q - 1)
    if math.gcd(q, key ) != 1:
        key = random.randint(2, q - 1)
    
    return key

def encrypt(msg, q, h, g):
    en_msg = []
    k = gen_key(q)
    s = pow(h, k, q)
    p = pow(g, k, q)

    for i in range(len(msg)):
        en_msg.append(msg[i])

    print("g^k used: ", p)
    print("g^ak used: ", s)

    for i in range(len(en_msg)):
        en_msg[i] = s * ord(en_msg[i])

    return en_msg, p

def decrypt(en_msg, p, key, q):
    dr_msg = []
    h = pow(p, key, q)
    for i in range(len(en_msg)):
        dr_msg.append(chr(int(en_msg[i]/h)))
    return dr_msg

def main():
    q = int(input("Enter a large number of prime number q:"))
    g = int (input("Enter a generator g: "))

    key = int(input("Enter a priv key: "))

    while math.gcd(q, key) != 1:
        key = int(input("Invalid"))

    h = pow(g, key, q)
    print("Public key h: ", h)
    msg = input("Enter message to encrypt: ")
    en_msg, p = encrypt(msg, q, h, g)
    print("Encrypted message: ", en_msg)
    dr_msg = decrypt(en_msg, p, key, q)
    print("Decrypted message: ", ''.join(dr_msg))

if __name__ == "__main__":
    main()




