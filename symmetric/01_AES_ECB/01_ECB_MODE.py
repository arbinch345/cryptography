import base64 
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def encrypt(plain_txt, key):
    cipher_Obj = AES.new(key, AES.MODE_ECB)
    cipher_txt = cipher_Obj.encrypt(pad(plain_txt.encode(), AES.block_size))

    encrypted_txt = base64.b64encode(cipher_txt).decode()

    return encrypted_txt

def decrypt(encrypted_txt, key):
    decrypted_b64 = base64.b64decode(encrypted_txt.encode())

    cipher_obj = AES.new(key, AES.MODE_ECB)
    decrypted_txt = cipher_obj.decrypt(decrypted_b64)

    return unpad(decrypted_txt, AES.block_size).decode()

# Main Menu
def main():
    key = get_random_bytes(16)
    print("key: ",base64.b85encode(key).decode())

    while True:
        print("\n ===== AES ECB MODE ===== ")
        print("\n1. Encryption")
        print("2. Decryption")
        print("3. Exit")

        while True:
            try:
                choice = int(input("Enter your choice: "))
                break
            except ValueError:
                print("Can't be empty! Enter your choice!")
        # choice = int(input("Enter your choice: "))

        if choice == 1:
            message = input("Enter msg to be encrypted: ")

            encypted = encrypt(message, key)
            print("Cipher_txt: ", encypted)

        elif choice == 2:
            try:
                cipher_txt = input("Enter cipher_txt to be encrypted: ")

                decryted = decrypt(cipher_txt, key)
                print("Msg Decrypted: ", decryted)

            except Exception as e:
                print("Error: ", e)

        elif choice == 3:
            print("Exiting...")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()