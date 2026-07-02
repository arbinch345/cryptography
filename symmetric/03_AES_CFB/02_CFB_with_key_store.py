import os
import base64
import json
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2


# CONFIG
KEY_FILE = "secret.key"
SALT_SIZE = 16
KEY_SIZE = 32  # AES-256
ITERATIONS = 100_000


# KEY MANAGEMENT
def derive_key(password: str, salt: bytes) -> bytes:
    """Derive a secure AES key using PBKDF2."""
    return PBKDF2(password, salt, dkLen=KEY_SIZE, count=ITERATIONS)


def save_key(password: str):
    """Generate and save a persistent key."""
    salt = get_random_bytes(SALT_SIZE)
    key = derive_key(password, salt)

    with open(KEY_FILE, "wb") as f:
        f.write(salt + key)

    print("[+] Key generated and saved securely.")


def load_key(password: str) -> bytes:
    """Load and reconstruct key from stored file."""
    if not os.path.exists(KEY_FILE):
        raise FileNotFoundError("Key file not found. Generate key first.")

    with open(KEY_FILE, "rb") as f:
        data = f.read()

    salt = data[:SALT_SIZE]
    stored_key = data[SALT_SIZE:]

    key = derive_key(password, salt)

    if key != stored_key:
        raise ValueError("Invalid password!")

    return key


# ENCRYPTION
def encrypt(plaintext: str, key: bytes):
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CFB, iv=iv)

    ciphertext = cipher.encrypt(plaintext.encode())

    return {
        "iv": base64.b64encode(iv).decode(),
        "ciphertext": base64.b64encode(ciphertext).decode()
    }


# DECRYPTION
def decrypt(ciphertext_b64: str, iv_b64: str, key: bytes) -> str:
    iv = base64.b64decode(iv_b64)
    ciphertext = base64.b64decode(ciphertext_b64)

    cipher = AES.new(key, AES.MODE_CFB, iv=iv)
    plaintext = cipher.decrypt(ciphertext)

    return plaintext.decode()


# Main Menu
def main():
    print("\n🔐 AES-256 CFB Secure CLI Tool")

    while True:
        print("\n==============================")
        print("1. Generate Key")
        print("2. Encrypt Text")
        print("3. Decrypt Text")
        print("4. Exit")
        print("==============================")

        choice = input("Enter choice: ").strip()

        # KEY GENERATION
        if choice == "1":
            password = input("Create password for key: ")
            save_key(password)

        # ENCRYPTION
        elif choice == "2":
            try:
                password = input("Enter key password: ")
                key = load_key(password)

                text = input("Enter plaintext: ")
                result = encrypt(text, key)

                print("\n--- ENCRYPTED OUTPUT ---")
                print("Ciphertext:", result["ciphertext"])
                print("IV        :", result["iv"])

            except Exception as e:
                print("Error:", e)

        # DECRYPTION
        elif choice == "3":
            try:
                password = input("Enter key password: ")
                key = load_key(password)

                ciphertext = input("Enter ciphertext: ")
                iv = input("Enter IV: ")

                plaintext = decrypt(ciphertext, iv, key)

                print("\n--- DECRYPTED OUTPUT ---")
                print("Plaintext:", plaintext)

            except Exception as e:
                print("Error:", e)

        # EXIT
        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()