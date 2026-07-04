import hashlib
from Crypto.Cipher import AES
import base64
import os

password = b'Apple'
# key = hashlib.sha256(password).digest()

salt = os.urandom(16)    # generate cryptographically secure random bytes
key = hashlib.pbkdf2_hmac(
        'sha256',
        password,
        salt,
        100000  # iterations (important security factor)
    )
print("key: ",base64.b64encode(key).decode())

def encrypt(plain_txt, key):
    cipherObj = AES.new(key, AES.MODE_CTR)
    cipher_txt = cipherObj.encrypt(plain_txt.encode())
    nonce = cipherObj.nonce
    encoded = base64.b64encode(cipher_txt).decode()
    return encoded, nonce

def decrypt(encrypted_txt, key, nonce):
    byte_txt = base64.b64decode(encrypted_txt.encode())
    cipherObj = AES.new(key, AES.MODE_CTR, nonce=nonce)
    decrypted_txt = cipherObj.decrypt(byte_txt)
    return decrypted_txt.decode()


# Main Menu

def main():
    while True:
        print("***** AES_CTR_Cipher *****")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")

        choice = input("Enter the choice here: ")

        if choice == "1":
            txt = input("Enter txt to encrypt: ")
            encrypted, nonce = encrypt(txt, key)
            print("Encrypted:", encrypted)
            print("Nonce:", base64.b64encode(nonce).decode())

        elif choice == "2":
            cipher_txt = input("Enter cipher text here: ")
            nonce_b64 = input("Enter nonce here: ")
            try:
                nonce = base64.b64decode(nonce_b64.encode())
            except Exception:
                print("Invalid nonce.")
                continue
            try:
                decrypted = decrypt(cipher_txt, key, nonce)
                print("Decrypted:", decrypted)
            except Exception as exc:
                print("Decryption failed:", exc)

        elif choice == "3":
            break

        else:
            print("Invalid choice. Choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
