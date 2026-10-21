"""Local authenticated-encryption demonstration, not a network chat server."""
import argparse
from cryptography.fernet import Fernet

def encrypt_message(key, message):
    return Fernet(key).encrypt(message.encode())

def decrypt_message(key, token):
    return Fernet(key).decrypt(token).decode()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("message")
    args = parser.parse_args()
    key = Fernet.generate_key()
    ciphertext = encrypt_message(key, args.message)
    print("Ciphertext:", ciphertext.decode())
    print("Decrypted:", decrypt_message(key, ciphertext))
    print("Demo-only ephemeral key; never commit real secrets.")

if __name__ == "__main__":
    main()
