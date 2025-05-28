from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Function to perform AES encryption
def encrypt_data(key, data):
    cipher = AES.new(key, AES.MODE_CBC)  # AES with CBC mode
    # Pad the data to be a multiple of AES.block_size
    ct_bytes = cipher.encrypt(pad(data.encode(), AES.block_size))
    return cipher.iv + ct_bytes  # Prepend IV to ciphertext for decryption

# Function to perform AES decryption
def decrypt_data(key, ciphertext):
    iv = ciphertext[:AES.block_size]  # Extract the IV
    ct = ciphertext[AES.block_size:]  # Extract the ciphertext
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # Unpad the data and return the decrypted plaintext
    return unpad(cipher.decrypt(ct), AES.block_size).decode()

# Example usage
if __name__ == "__main__":
    key = get_random_bytes(16)  # AES key must be either 16, 24, or 32 bytes (128, 192, or 256 bits)
    print(f"Key: {key.hex()}")

    data = "This is a secret message"
    print(f"Original Data: {data}")

    encrypted_data = encrypt_data(key, data)
    print(f"Encrypted Data (hex): {encrypted_data.hex()}")

    decrypted_data = decrypt_data(key, encrypted_data)
    print(f"Decrypted Data: {decrypted_data}")
