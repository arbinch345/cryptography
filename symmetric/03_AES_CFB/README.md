# AES CFB Mode Cryptography Projects

This repository contains two Python projects that demonstrate the implementation of **AES (Advanced Encryption Standard)** using **CFB (Cipher Feedback) mode**.

The projects are:

1. **Project 1 — Basic AES-CFB Encryption Tool**
2. **Project 2 — AES-256 CFB Secure CLI Tool with Key Storage**

# What is CFB (Cipher Feedback) Mode?

CFB (Cipher Feedback) is a block cipher mode that allows block ciphers like AES to behave like a stream cipher.

Instead of encrypting fixed-size blocks independently, CFB encrypts data continuously by feeding encrypted output back into the encryption process.

---

# Key Features of CFB Mode

* Converts block cipher into stream cipher behavior
* No padding required
* Supports encryption of variable-length plaintext
* Uses Initialization Vector (IV) for randomness
* Secure for real-time communication systems

---

# Working of AES-CFB Mode

## Encryption Process

1. Generate a random Initialization Vector (IV)
2. Encrypt the IV using AES key
3. XOR encrypted IV with plaintext
4. Produce ciphertext
5. Feed ciphertext back into the encryption process

## Decryption Process

1. Encrypt the same IV using AES key
2. XOR encrypted IV with ciphertext
3. Recover original plaintext

---

# AES-CFB Encryption Flow Diagram

```text
                ENCRYPTION PROCESS

        +----------------------+
        |   Plaintext Input    |
        +----------------------+
                    |
                    v
        +----------------------+
        | Generate Random IV   |
        +----------------------+
                    |
                    v
        +----------------------+
        | AES Encrypt IV using |
        | Secret Key           |
        +----------------------+
                    |
                    v
        +----------------------+
        | XOR with Plaintext   |
        +----------------------+
                    |
                    v
        +----------------------+
        | Produce Ciphertext   |
        +----------------------+
                    |
                    v
        +----------------------+
        | Send Ciphertext + IV |
        +----------------------+
```

---

# AES-CFB Decryption Flow Diagram

```text
                DECRYPTION PROCESS

        +----------------------+
        | Ciphertext + IV      |
        +----------------------+
                    |
                    v
        +----------------------+
        | AES Encrypt IV using |
        | Secret Key           |
        +----------------------+
                    |
                    v
        +----------------------+
        | XOR with Ciphertext  |
        +----------------------+
                    |
                    v
        +----------------------+
        | Recover Plaintext    |
        +----------------------+
```

---

# Project 1 — Basic AES-CFB Encryption Tool

## Description

This project is a simple command-line application that demonstrates AES encryption and decryption using CFB mode.

The program:

* Generates a random AES key
* Encrypts plaintext
* Decrypts ciphertext
* Uses Base64 encoding for safe text representation


## Project Structure

```text
project1/
│
├── main.py
└── README.md
```


## Program Flowchart

```text
                    START
                      |
                      v
          +----------------------+
          | Generate AES Key     |
          +----------------------+
                      |
                      v
          +----------------------+
          | Display Main Menu    |
          +----------------------+
                      |
         +------------+------------+
         |                         |
         v                         v
+------------------+     +------------------+
| Encrypt Message  |     | Decrypt Message  |
+------------------+     +------------------+
         |                         |
         v                         v
+------------------+     +------------------+
| Input Plaintext  |     | Input Ciphertext |
+------------------+     +------------------+
         |                         |
         v                         v
+------------------+     +------------------+
| Generate IV      |     | Decode Base64    |
+------------------+     +------------------+
         |                         |
         v                         v
+------------------+     +------------------+
| AES-CFB Encrypt  |     | AES-CFB Decrypt  |
+------------------+     +------------------+
         |                         |
         v                         v
+------------------+     +------------------+
| Display Output   |     | Display Plaintext|
+------------------+     +------------------+
                      |
                      v
                    EXIT
```

---

## Sample Output

### Encryption

```text
===== AES.CFB Encryption Tool =====

1. Encryption
2. Decryption
3. Exit

Enter your choice: 1

Encrypt the message: Hello World

----- Encryption -----

Ciphertext : jskd8923jK...
IV         : Sjdi8923...
```

---

### Decryption

```text
===== AES.CFB Encryption Tool =====

Enter your choice: 2

Enter ciphertext here: jskd8923jK...
Enter IV here: Sjdi8923...

----- Decryption -----

Plaintext: Hello World
```

---

## Advantages

* Simple implementation
* Easy to understand
* Random IV increases security
* No padding required

---

## Limitations

* Key is generated every runtime
* No persistent key storage
* If key is lost, decryption is impossible

---

# Project 2 — AES-256 CFB Secure CLI Tool with Key Storage

## Description

This project extends the basic AES-CFB implementation by adding:

* Persistent key storage
* Password-based key derivation
* AES-256 encryption
* PBKDF2 secure key generation

This makes the project significantly more secure and practical.

---

## Security Features

### AES-256 Encryption

Uses 256-bit encryption key for stronger security.

### PBKDF2 Key Derivation

The key is generated from a password using PBKDF2 with:

* Random salt
* 100,000 iterations

### Secure Key Storage

The generated key and salt are stored securely inside:

```text
secret.key
```

---

## Technologies Used

* Python 3
* PyCryptodome
* AES-256
* PBKDF2
* Base64 Encoding
* JSON

---

## Project Structure

```text
project2/
│
├── main.py
├── secret.key
└── README.md
```

## Workflow

### Key Generation

1. User creates password
2. Random salt generated
3. PBKDF2 derives AES-256 key
4. Key saved securely

### Encryption

1. Load stored key
2. Generate random IV
3. Encrypt plaintext using AES-CFB
4. Encode output in Base64

### Decryption

1. Load stored key
2. Decode Base64 ciphertext
3. AES-CFB decrypt
4. Recover plaintext

## Advantages

* Stronger AES-256 security
* Persistent key management
* Password-protected keys
* Secure PBKDF2 derivation

## Limitations

* Password must be remembered
* Losing `secret.key` file prevents decryption


# Comparison Between Project 1 and Project 2

| Feature             | Project 1 | Project 2 |
| ------------------- | --------- | --------- |
| AES Mode            | AES-CFB   | AES-CFB   |
| Key Size            | 128-bit   | 256-bit   |
| Key Storage         | No        | Yes       |
| Password Protection | No        | Yes       |
| PBKDF2              | No        | Yes       |
| Security Level      | Basic     | Advanced  |


# Conclusion

These projects demonstrate how AES encryption works using CFB mode in Python.

* **Project 1** focuses on understanding the basics of AES-CFB encryption.
* **Project 2** introduces real-world security practices such as password-based key derivation and secure key management.
