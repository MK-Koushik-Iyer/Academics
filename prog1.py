import math
from Crypto import DES
import base64

def division_algorithm():
    print("\n=== Division Algorithm ===")
    dividend = int(input("Enter dividend: "))
    divisor = int(input("Enter divisor: "))
    if divisor == 0:
        print("Divisor cannot be zero.")
        return
    quotient = dividend // divisor
    remainder = dividend % divisor
    print(f"Quotient: {quotient}, Remainder: {remainder}")

def gcd_algorithm():
    print("\n=== GCD Algorithm ===")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    gcd = math.gcd(a, b)
    print(f"GCD of {a} and {b} is {gcd}")

def fermats_little_theorem():
    print("\n=== Fermat's Little Theorem ===")
    a = int(input("Enter base (a): "))
    p = int(input("Enter prime number (p): "))
    if p <= 1 or not all(p % i != 0 for i in range(2, int(math.sqrt(p)) + 1)):
        print(f"{p} is not a prime number.")
        return
    result = pow(a, p - 1, p)
    print(f"{a}^(p-1) mod {p} = {result}")

def caesar_cipher_encryption():
    print("\n=== Caesar Cipher Encryption ===")
    text = input("Enter plaintext: ")
    shift = int(input("Enter shift value: "))
    ciphertext = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            ciphertext += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            ciphertext += char
    print(f"Encrypted text: {ciphertext}")

def des_one_iteration():
    print("\n=== DES Encryption (One Iteration) ===")
    key = input("Enter 8-byte key: ").ljust(8)[:8].encode('utf-8')
    plaintext = input("Enter plaintext (8 bytes): ").ljust(8)[:8].encode('utf-8')
    cipher = DES.new(key, DES.MODE_ECB)
    encrypted_text = cipher.encrypt(plaintext)
    encrypted_base64 = base64.b64encode(encrypted_text).decode('utf-8')
    print(f"Encrypted text (Base64): {encrypted_base64}")

def main():
    while True:
        print("\n=== Menu ===")
        print("1. Division Algorithm")
        print("2. GCD Algorithm")
        print("3. Fermat's Little Theorem")
        print("4. Caesar Cipher Encryption")
        print("5. DES with One Iteration")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            division_algorithm()
        elif choice == "2":
            gcd_algorithm()
        elif choice == "3":
            fermats_little_theorem()
        elif choice == "4":
            caesar_cipher_encryption()
        elif choice == "5":
            des_one_iteration()
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()