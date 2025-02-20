import os
import random

def generate_encryption_script():
    script_content = '''import random

def encrypt(data, password):
    # Convert password to integer
    seed = int(password)
    # Initialize random generator
    random.seed(seed)
    
    # Encrypt each byte
    encrypted = bytearray()
    for byte in data:
        key_byte = random.randint(0, 255)
        encrypted_byte = byte ^ key_byte
        encrypted.append(encrypted_byte)
    
    return encrypted

def decrypt(data, password):
    # Decryption is the same as encryption for XOR
    return encrypt(data, password)

if __name__ == "__main__":
    # Example usage
    password = "1234"  # 4-digit password
    message = b"Hello, World!"
    
    # Encrypt
    encrypted = encrypt(message, password)
    # Decrypt
    decrypted = decrypt(encrypted, password)
    
    print(f"Original: {message}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
'''
    
    # Ensure the files directory exists
    os.makedirs('files', exist_ok=True)
    
    # Write the encryption script
    with open('files/encryption_script.py', 'w') as f:
        f.write(script_content)

def create_encrypted_file():
    # The flag and password
    flag = b"flag{brut3_f0rc3_m4st3r_2024}"
    password = "5437"  # Random 4-digit password
    
    # Convert password to integer and set seed
    seed = int(password)
    random.seed(seed)
    
    # Encrypt the flag
    encrypted = bytearray()
    for byte in flag:
        key_byte = random.randint(0, 255)
        encrypted_byte = byte ^ key_byte
        encrypted.append(encrypted_byte)
    
    # Write the encrypted data to a file
    with open('files/encrypted.bin', 'wb') as f:
        f.write(encrypted)

if __name__ == "__main__":
    # Generate both challenge files
    generate_encryption_script()
    create_encrypted_file()
    print("Challenge files created in the files/ directory:")
    print("1. encryption_script.py")
    print("2. encrypted.bin") 