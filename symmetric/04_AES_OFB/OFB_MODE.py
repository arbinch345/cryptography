import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def encryption(plain_txt:bytes, key:bytes):
    iv = get_random_bytes(16)

    cipher_Obj = AES.new(key, AES.MODE_OFB, iv=iv)
    cipher_txt = cipher_Obj.encrypt(plain_txt.encode())

    iv_b64 = base64.b64encode(iv).decode()
    encrypted_txt = base64.b64encode(cipher_txt).decode()

    return encrypted_txt, iv_b64


def decryption(encrypted_txt, key, iv):
    encrypted_txt = base64.b64decode(encrypted_txt.encode())
    iv_bytes = base64.b64decode(iv.encode())

    cipher_Obj = AES.new(key, AES.MODE_OFB, iv=iv_bytes)
    decrypted_txt = cipher_Obj.decrypt(encrypted_txt)

    return decrypted_txt.decode()

# Main Menu
def main():
    key = get_random_bytes(16)
    print("key: ", base64.b64encode(key).decode())

    while True:
        print("\n===== AES OFB MODE =====")
        print("\n1. Encryption")
        print("2. Decrytion")
        print("3. Exit")

        while True:
            try:
                choice = int(input("\nEnter your choice: ").strip())
                break
            
            except ValueError:
                print("can't be empty! Enter valid choice!")

        if choice == 1:
            print("\n ***** Encryption *****")
            message = input("\nEnter the msg to be encrypted: ")

            print("\n ***** Encryption *****")
            encrypted, iv = encryption(message, key)
            print("Cipher_txt     :", encrypted)
            print("IV             :", iv)

        elif choice == 2:
            print("\n ***** Decryption *****")
            cipher_txt = input("\nEnter ciphertxt here: ")
            iv = input("Enter nonce here: ")

            print("\n ***** Decryption *****")
            decrypted = decryption(cipher_txt, key, iv)
            print("\nMessage Decrypted: ", decrypted)

        elif choice == 3:
            print("Exiting...")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()