from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15
import base64

def read_pem_block(prompt):
    print(prompt)

    lines = []

    while True:
        line = input()

        if not line:
            break

        lines.append(line)

        if line.startswith("-----END "):
            break

    return "\n".join(lines)

# ENCRYPT (NEW KEYS EVERY TIME)
def encrypt_message():
    message = input("Enter message: ").encode()

    # NEW KEYPAIR EVERY ENCRYPTION
    key = RSA.generate(2048)
    private_key = key
    public_key = key.public_key()

    # Encrypt
    cipher_Obj = PKCS1_OAEP.new(public_key)
    ciphertext = cipher_Obj.encrypt(message)
    ciphertext_b64 = base64.b64encode(ciphertext).decode()

    # sign
    h = SHA256.new(message)
    signer = pkcs1_15.new(private_key)
    signature = signer.sign(h)
    signature_b64 = base64.b64encode(signature).decode()

    # Export PEM
    private_pem = private_key.export_key().decode()
    public_pem = public_key.export_key().decode()

    # Save everything to files
    with open("private.pem", "w") as f:
        f.write(private_pem)

    with open("public.pem", "w") as f:
        f.write(public_pem)

    with open("ciphertext.pem", "w") as f:
        f.write(ciphertext_b64)

    with open("signature.pem", "w") as f:
        f.write(signature_b64)

    print("\n✔ NEW KEYPAIR GENERATED")
    print("✔ Files created:")
    print("  - private.pem")
    print("  - public.pem")
    print("  - ciphertext.pem")
    print("  - signature.pem")
    
# DECRYPT
def decrypt_message():
    public_pem = read_pem_block("Enter public key (---- PEM FILE -----)\n")

    private_pem = read_pem_block("\nEnter private key (---- PEM FILE -----)\n")

    print("\nPaste CIPHERTEXT: \n")
    ciphertext_b64 = input()

    print("\nPaste SIGNATURE: \n")
    signature_b64 = input()

    # Decode base64
    ciphertext = base64.b64decode(ciphertext_b64)
    signature = base64.b64decode(signature_b64)

    # Import keys
    public_key = RSA.import_key(public_pem)
    private_key = RSA.import_key(private_pem)

    # Decrypt
    cipher_Obj = PKCS1_OAEP.new(private_key)
    message = cipher_Obj.decrypt(ciphertext)

    # Verify signature
    h = SHA256.new(message)
    verifier = pkcs1_15.new(public_key)

    try:
        verifier.verify(h, signature)
        print("\n✔ Signature Verified!")
        print("✔ Message:", message.decode())

    except (ValueError, TypeError):
        print("\n❌ Signature Verification Failed!")

# Main Menu
def main():
    while True:
        print("\n===== RSA LAB SYSTEM =====")
        print("1. Encrypt (NEW keys every time)")
        print("2. Decrypt + Verify")
        print("3. Exit")

        choice = input("\nEnter choice: ")

        if choice == "1":
            encrypt_message()

        elif choice == "2":
            decrypt_message()

        elif choice == "3":
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()