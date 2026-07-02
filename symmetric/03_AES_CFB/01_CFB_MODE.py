import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def encrypt(plain_txt, key):
    iv = get_random_bytes(16)

    cipher_Obj = AES.new(key, AES.MODE_CFB, iv=iv)
    cipher_txt = cipher_Obj.encrypt(plain_txt.encode())

    iv_b64 = base64.b64encode(iv).decode()
    encrypted_txt = base64.b64encode(cipher_txt).decode()

    return encrypted_txt, iv_b64

def decrypt(encrypted_txt, key, iv):
    encrypted_b64 = base64.b64decode(encrypted_txt.encode())
    iv_bytes = base64.b64decode(iv.encode())

    cipher_Obj = AES.new(key, AES.MODE_CFB, iv=iv_bytes)

    decrypted_txt = cipher_Obj.decrypt(encrypted_b64)

    return decrypted_txt.decode()

# Main Menu
def main():
    key = get_random_bytes(16)
    print("Key: ", base64.b64encode(key).decode())

    while True:
        print("===== AES.CFB Encryption Tool =====")
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
            print("\n***** Encryption *****")
            message = input("\nEncrypt the message: ")

            print(" \n----- Encryption ----- ")
            encrypted, iv = encrypt(message, key)
            print("Ciphertext         : ", encrypted)
            print("IV                 :", iv)

        elif choice == 2:
            print("\n***** Decryption *****")
            cipher_txt = input("\nEnter ciphertext here: ")
            iv = input("Enter IV here: ")

            print(" \n----- Decryption ----- ")
            decrypted = decrypt(cipher_txt, key, iv)
            print("Plaintext: ", decrypted)

        elif choice == 3:
            print("Exiting ...")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()