import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def encryption(plain_txt, key):
    cipher_Obj = AES.new(key, AES.MODE_CTR)
    cipher_txt = cipher_Obj.encrypt(plain_txt.encode())
    nonce = cipher_Obj.nonce

    encrypted_txt = base64.b64encode(cipher_txt).decode()
    nonce_b64 = base64.b64encode(nonce).decode()

    return encrypted_txt, nonce_b64

def decryption(encrypted_txt, key, nonce):
    cipher_bytes = base64.b64decode(encrypted_txt.encode())
    nonce_bytes = base64.b64decode(nonce.encode())
    cipher_Obj = AES.new(key, AES.MODE_CTR, nonce=nonce_bytes)

    decrypted_txt =  cipher_Obj.decrypt(cipher_bytes)

    return decrypted_txt.decode()    

def main():
    key = get_random_bytes(16)
    print("key: ",base64.b64encode(key).decode())
    while True:
        print("=" * 30)
        print("AES CTR MODE")
        print("=" * 30)

        print("\n1. Encryption")
        print("2. Decryption")
        print("3. Exit")

        while True:
            try:
                choice = int(input("Enter your choice: "))
                break

            except ValueError:
                print("Can't be empty! Enter your choice!")

        if choice == 1:
            message = input("Enter message: ")

            encrypted, nonce = encryption(message, key)
            print("Cipher_txt        :", encrypted)
            print("Nonce             :", nonce)

        elif choice == 2:
            try:
                cipher_txt = input("Enter cipher_txt: ")
                nonce_b = input("Enter nonce: ")

                decrypted = decryption(cipher_txt, key, nonce_b)
                print("Msg Decrypted: ", decrypted)

            except Exception as e:
                print("Error: ", e)

        elif choice == 3:
            print("Exitin...")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()