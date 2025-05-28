from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Function to perform DES encryption
def encrypt_data(key, data):
    cipher = DES.new(key, DES.MODE_CBC)
    # Pad the data to be multiple of 8 bytes
    ct_bytes = cipher.encrypt(pad(data.encode(), DES.block_size))
    return cipher.iv + ct_bytes  # Prepend IV to ciphertext for decryption

# Function to perform DES decryption
def decrypt_data(key, ciphertext):
    iv = ciphertext[:DES.block_size]  # Extract the IV
    ct = ciphertext[DES.block_size:]  # Extract the ciphertext
    cipher = DES.new(key, DES.MODE_CBC, iv)
    # Unpad the data and return the decrypted plaintext
    return unpad(cipher.decrypt(ct), DES.block_size).decode()

# Example usage
if __name__ == "__main__":
    key = get_random_bytes(8)  # DES key must be 8 bytes
    print(f"Key: {key.hex()}")

    data = "This is a secret message"
    print(f"Original Data: {data}")

    encrypted_data = encrypt_data(key, data)
    print(f"Encrypted Data (hex): {encrypted_data.hex()}")

    decrypted_data = decrypt_data(key, encrypted_data)
    print(f"Decrypted Data: {decrypted_data}")
