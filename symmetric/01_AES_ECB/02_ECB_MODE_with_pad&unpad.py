import hashlib
import base64
from Crypto.Cipher import AES

password = b'apple'
key = hashlib.sha256(password).digest()

def pad(txt):
    txt_length = 16 - (len(txt) % 16)

    return (txt + chr(txt_length) * txt_length)

def unpad(txt):
    last_value = txt[len(txt) - 1]
    padding_len = ord(last_value)

    return txt[0: -padding_len]

def encryption(plain_txt, key):
    cipher_Obj = AES.new(key, AES.MODE_ECB)
    cipher_txt = cipher_Obj.encrypt(pad(plain_txt).encode())

    encrypted_txt = base64.b64encode(cipher_txt)

    return encrypted_txt.decode()

def decryption(encrypted_txt, key):
    cipher_bytes = base64.b64decode(encrypted_txt)
    cipher_Obj = AES.new(key, AES.MODE_ECB)
    decrypted_txt = cipher_Obj.decrypt(cipher_bytes).decode()

    return unpad(decrypted_txt)

def main():
    while True:
        print("=" * 20)
        print("AES ECB MODE")
        print("=" * 20)

        print("\n1. Encryption")
        print("2. Decryption")
        print("3. Exit")

        while True:
            try:
                choice = int(input("\nEnter your choice: "))
                break

            except:
                print("Can't be empty! Enter something!")

        if choice == 1:
            message = input("Enter message: ")
            encrypted = encryption(message, key)
            print("Cipher_txt: ", encrypted)
        
        elif choice == 2:
            try:
                cipher_txt = input("Enter cipher_txt: ")
                decrypted = decryption(cipher_txt, key)
                print("Decrytion: ", decrypted)

            except Exception as e:
                print("Error: ", e)

        elif choice == 3:
            print("Exiting...")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()

# txt = input("Enter text: ")

# try:
#     # decrypted = decryption(txt, key)
#     # print(decrypted)

# except Exception:
#     output = encryption(txt, key)
#     print(output)