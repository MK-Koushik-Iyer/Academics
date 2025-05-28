from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Function to perform Triple DES encryption
def encrypt_data(key, data):
    cipher = DES3.new(key, DES3.MODE_CBC)  # Triple DES with CBC mode
    # Pad the data to be a multiple of DES3.block_size (8 bytes for DES)
    ct_bytes = cipher.encrypt(pad(data.encode(), DES3.block_size))
    return cipher.iv + ct_bytes  # Prepend IV to ciphertext for decryption

# Function to perform Triple DES decryption
def decrypt_data(key, ciphertext):
    iv = ciphertext[:DES3.block_size]  # Extract the IV
    ct = ciphertext[DES3.block_size:]  # Extract the ciphertext
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    # Unpad the data and return the decrypted plaintext
    return unpad(cipher.decrypt(ct), DES3.block_size).decode()

# Example usage
if __name__ == "__main__":
    key = get_random_bytes(24)  # 3DES key must be 24 bytes (192 bits)
    print(f"Key: {key.hex()}")

    data = "This is a secret message"
    print(f"Original Data: {data}")

    encrypted_data = encrypt_data(key, data)
    print(f"Encrypted Data (hex): {encrypted_data.hex()}")

    decrypted_data = decrypt_data(key, encrypted_data)
    print(f"Decrypted Data: {decrypted_data}")
