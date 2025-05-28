import math
import random

def main():
    p = int(input("Enter p: "))
    d = int(input("Enter d: "))
    e1 = int(input("Enter e1: "))
    pt = int(input("Enter int plaintext: "))

    print("Computing e2...")

    e2 = pow(e1, d, p)
    print(f"e2: {e2}")

    r = int(input("Enter r: "))

    print("Calculating C1...")
    c1 = pow(e1, r, p)
    c2 = pow(pt*(e2**r),1,p)

    print(f"Ciphertext: c1-{c1}, c2-{c2}")

    print("Decrypting...")

    plaintext = pow(c2*pow(c1**d, -1, p), 1, p)

    print(f"Plaintext: {plaintext}")

main()