import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Encryption
def encrypt(plain_txt: bytes, key:bytes):
    iv = get_random_bytes(16)

    cipher_Obj = AES.new(key, AES.MODE_CBC, iv)
    ct_bytes = cipher_Obj.encrypt(pad(plain_txt, AES.block_size))

    iv_64 = base64.b64encode(iv).decode()
    ct_b64 = base64.b64encode(ct_bytes).decode()

    return iv_64, ct_b64

# Decryption
def decrypt(iv_64: str, ct_b64: str, key):
    try:
        iv = base64.b64decode(iv_64)
        ct = base64.b64decode(ct_b64)

        cipher_Obj = AES.new(key, AES.MODE_CBC, iv)
        pt = unpad(cipher_Obj.decrypt(ct), AES.block_size)

        return pt.decode()
    
    except Exception as e:
        return "Incorrect Decryption", e
    
# Main Menu:
def main():
    # IMPORTANT: for demo only (key should be saved in real apps)
    key = get_random_bytes(16)
    print("key: ",base64.b64encode(key).decode())
    
    while True:

        print("\n===== AES.CBC Encryption Tool =====")

        print("\n1. Encryption")
        print("2. Decryption")
        print("3. Exit")

        while True:
            raw_choice = input("\nEnter your choice: ").strip()

            if not raw_choice:
                print("Can't be empty! Enter your choice!")
                continue

            try:
                choice = int(raw_choice)
            except ValueError:
                print("Enter valid choice!")
                continue

            if choice not in (1, 2, 3):
                print("Enter valid choice!")
                continue

            break

        # Encrypt the message
        if choice == 1:
            message = input("Enter message to encrypt: ").encode()
            iv, ciphertext = encrypt(message, key)

            print("\n------ Encryption Output -----")
            print("\nIV             :", iv)
            print("Ciphertext     :", ciphertext)

        # Decrypt the message
        elif choice == 2:
            iv = input("Enter IV here: ")
            ciphertext = input("Enter ciphertext here: ")

            print("\n------ Decryption Output -----")
            decrypted = decrypt(iv, ciphertext, key)
            print("\nDecrypted: ", decrypted)

        elif choice == 3:
            print("Exiting...")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()