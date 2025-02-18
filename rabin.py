import random
from sympy import isprime
from sympy.ntheory.modular import solve_congruence

# Step 1: Key generation (using user-provided p and q)
def is_prime_input(p):
    if not isprime(p):
        raise ValueError(f"{p} is not a prime number.")
    return p

# Step 2: Encryption
def encrypt(m, n):
    return (m * m) % n

# Step 3: Decryption using Chinese Remainder Theorem
def chinese_remainder_theorem(a1, a2, p1, p2):
    # Solve the system of congruences:
    # x ≡ a1 (mod p1)
    # x ≡ a2 (mod p2)
    solution, _ = solve_congruence((a1, p1), (a2, p2))
    return solution

# Decrypt function
def decrypt(c, p, q):
    # Step 1: Compute square roots mod p and mod q
    m_p = pow(c, (p + 1) // 4, p)
    m_q = pow(c, (q + 1) // 4, q)
    
    # Step 2: Use Chinese Remainder Theorem to find all solutions
    # We have four possible solutions: (m_p, m_q), (m_p, -m_q), (-m_p, m_q), (-m_p, -m_q)
    solutions = []
    for sign_p in [1, -1]:
        for sign_q in [1, -1]:
            a1 = (sign_p * m_p) % p
            a2 = (sign_q * m_q) % q
            m = chinese_remainder_theorem(a1, a2, p, q)
            solutions.append((m, (sign_p * m_p, sign_q * m_q)))
    
    return solutions

# Example usage

# Taking user input for p and q
try:
    p = int(input("Enter a prime number p: "))
    q = int(input("Enter a prime number q: "))

    # Ensure that both p and q are prime
    p = is_prime_input(p)
    q = is_prime_input(q)

    # Compute n
    n = p * q

    # Print the public key
    print(f"Public Key (n): {n}")
    print(f"Private Key (p, q): ({p}, {q})")

    # Encrypt a message (let's pick a small number for simplicity)
    message = int(input("Enter a message (integer): "))
    ciphertext = encrypt(message, n)

    # Decrypt the ciphertext
    decrypted_messages = decrypt(ciphertext, p, q)

    # Output the results
    print(f"Original Message: {message}")
    print(f"Ciphertext: {ciphertext}")
    
    # Displaying decrypted messages along with the pairs of (m_p, m_q)
    print("Possible plaintexts and their corresponding pairs of (m_p, m_q):")
    for m, pair in decrypted_messages:
        print(f"Plaintext: {m}, Pair (m_p, m_q): {pair}")
    
except ValueError as ve:
    print(f"Error: {ve}")
