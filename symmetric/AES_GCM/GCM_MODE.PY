import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Encryption
def encryption(plain_txt, key):
    cipher_Obj = AES.new(key, AES.MODE_GCM)

    cipher_txt, tag = cipher_Obj.encrypt_and_digest(plain_txt.encode())   # digest = Verify data wasn't changed.
    nonce = cipher_Obj.nonce

    encrypted_txt = base64.b64encode(cipher_txt).decode()
    nonce_b64 = base64.b64encode(nonce).decode()
    auth_tag = base64.b64encode(tag).decode()

    return encrypted_txt, nonce_b64, auth_tag

# Decryption
def decryption(encrypted_txt, nonce, key, tag):
    cipher_bytes = base64.b64decode(encrypted_txt)
    nonce_bytes = base64.b64decode(nonce)
    auth_tag = base64.b64decode(tag)

    cipher_Obj = AES.new(key, AES.MODE_GCM, nonce=nonce_bytes)

    decrypted_txt = cipher_Obj.decrypt_and_verify(cipher_bytes, auth_tag)

    return decrypted_txt.decode()

# Main Menu
def main():
    key = get_random_bytes(32)
    print("key: ",base64.b64encode(key).decode())
    while True:
        print("=" * 30)
        print(" AES GCM MODE ")
        print("=" * 30)

        print("\n1. Encryption")
        print("2. Decryption")
        print("3. Exit")

        while True:
            try:
                choice = int(input("\nEnter your choice: "))
                break
                
            except ValueError:
                print("Can't be empty! Enter your choice!")

        if choice == 1:
            message = input("Enter message: ")

            encrypted, nonce, tag = encryption(message, key)
            print("\nCipher_txt    : ", encrypted)
            print("Nonce           : ", nonce)
            print("Tag             :", tag)

        elif choice == 2:
            try:
                cipher_txt = input("Enter cipher_txt: ")
                Nonce = input("Enter nonce: ")
                auth_tag = input("Enter tag: ")

                decrypted = decryption(cipher_txt, nonce, key, auth_tag)
                print("Decrypted msg: ", decrypted)

            except Exception as e:
                print("Error: ", e)

        elif choice == 3:
            print("Exiti...")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()