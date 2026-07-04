# 🔐 AES CTR Mode Cryptography Projects

This repository contains two different implementations of **AES (Advanced Encryption Standard)** using **CTR (Counter) Mode** in Python.

Both projects demonstrate secure encryption and decryption using the `PyCryptodome` library, but each implementation uses a different method for key generation and handling.

---

# 📌 Repository Overview

| Project   | Description                                    |
| --------- | ---------------------------------------------- |
| Project 1 | AES CTR Mode using randomly generated AES key  |
| Project 2 | AES CTR Mode using PBKDF2 password-derived key |

---

# 📚 What is AES CTR Mode?

**CTR (Counter) Mode** is a mode of operation that converts a block cipher into a stream cipher.

Instead of encrypting plaintext blocks directly:

1. A counter value is generated
2. AES encrypts the counter
3. A keystream is produced
4. The keystream is XOR-ed with plaintext
5. Ciphertext is generated

The same process is used for decryption.

---

# ⚙️ Working of CTR Mode

## Encryption Flow

```text id="k2as0c"
Plaintext
    │
    ▼
Generate Counter + Nonce
    │
    ▼
AES Encrypt Counter
    │
    ▼
Generate Keystream
    │
    ▼
XOR with Plaintext
    │
    ▼
Ciphertext
```

---

## Decryption Flow

```text id="n9s2ax"
Ciphertext
    │
    ▼
Generate Same Counter + Nonce
    │
    ▼
AES Encrypt Counter
    │
    ▼
Generate Same Keystream
    │
    ▼
XOR with Ciphertext
    │
    ▼
Original Plaintext
```

---

# 📊 AES CTR Mode Architecture Diagram

```text id="x93d1k"
                ┌────────────────────┐
                │     Plaintext      │
                └─────────┬──────────┘
                          │
                          ▼
              ┌─────────────────────────┐
              │ Generate Nonce/Counter  │
              └─────────┬───────────────┘
                        │
                        ▼
              ┌─────────────────────────┐
              │ AES Encrypt Counter     │
              │ using Secret Key        │
              └─────────┬───────────────┘
                        │
                        ▼
              ┌─────────────────────────┐
              │     Create Keystream    │
              └─────────┬───────────────┘
                        │
                        ▼
              ┌─────────────────────────┐
              │ XOR with Plaintext      │
              └─────────┬───────────────┘
                        │
                        ▼
                 ┌───────────────┐
                 │  Ciphertext   │
                 └───────────────┘
```

---

# 🧩 Project 1 — AES CTR with Random AES Key

## 📖 Description

This implementation generates a **random 128-bit AES key** using:

```python id="h3v82q"
get_random_bytes(16)
```

The key is directly used for encryption and decryption.

---

## 🔑 Features

* AES CTR Encryption
* AES CTR Decryption
* Random secure AES key generation
* Base64 encoding support
* Nonce handling
* Interactive CLI menu

---

## 📂 Project Structure

```text id="f1c9qk"
project_1/
│
├── ctr_mode.py
└── README.md
```

---

## 🚀 How It Works

### Encryption

1. Generate random AES key
2. Create AES cipher object in CTR mode
3. Encrypt plaintext
4. Generate nonce
5. Encode ciphertext and nonce using Base64

### Decryption

1. Decode Base64 ciphertext
2. Recreate AES object using nonce
3. Decrypt ciphertext
4. Return original plaintext

## 🔐 Example Output

```text id="g7z2lm"
Enter message: Hello World

Cipher_txt : q0P3iM5...
Nonce      : HJd82kL...
```

---

# 🧩 Project 2 — AES CTR with PBKDF2 Key Derivation

## 📖 Description

This implementation derives the AES key from a password using:

* PBKDF2-HMAC
* SHA-256
* Random Salt
* 100000 iterations

This approach is more secure for password-based encryption systems.

---

# 🔒 What is PBKDF2?

PBKDF2 (Password-Based Key Derivation Function 2) strengthens passwords by repeatedly hashing them with salt.

It helps protect against:

* Brute-force attacks
* Rainbow table attacks
* Weak password vulnerabilities

---

## 🔑 Key Derivation Process

```text id="m9v1az"
Password
   │
   ▼
Generate Random Salt
   │
   ▼
PBKDF2-HMAC-SHA256
   │
   ▼
100000 Iterations
   │
   ▼
Derived AES Key
```

---

## 🔑 Features

* Password-based AES key generation
* PBKDF2-HMAC-SHA256
* Random salt generation
* AES CTR Encryption/Decryption
* Base64 encoding support
* Secure nonce handling

---

## 📂 Project Structure

```text id="d1q9sl"
project_2/
│
├── aes_ctr_pbkdf2.py
└── README.md
```

---

## 🚀 How It Works

### Key Generation

```python id="w7n2jd"
key = hashlib.pbkdf2_hmac(
    'sha256',
    password,
    salt,
    100000
)
```

### Encryption

1. Generate key using PBKDF2
2. Create AES cipher object
3. Encrypt plaintext
4. Generate nonce
5. Encode ciphertext

### Decryption

1. Decode Base64 ciphertext
2. Recreate AES object with nonce
3. Decrypt ciphertext
4. Return original message

## 🔐 Example Output

```text id="p4v2dy"
Enter txt to encrypt: Cyber Security

Encrypted: Jk92m...
Nonce: Pm21a...
```

---

# 📊 Project Comparison

| Feature                   | Project 1 | Project 2 |
| ------------------------- | --------- | --------- |
| AES CTR Mode              | ✅         | ✅         |
| Random AES Key            | ✅         | ❌         |
| PBKDF2 Key Derivation     | ❌         | ✅         |
| Password-Based Encryption | ❌         | ✅         |
| Base64 Encoding           | ✅         | ✅         |
| Random Nonce              | ✅         | ✅         |
| SHA-256 Support           | ❌         | ✅         |
| Secure Salt               | ❌         | ✅         |

# 🔒 Security Considerations

## Important Notes

* Never reuse the same nonce with the same key
* Store keys securely
* Use strong passwords
* PBKDF2 improves password security
* CTR mode does not provide authentication

---

# ⚠️ Limitations of CTR Mode

❌ No built-in integrity verification
❌ Vulnerable if nonce is reused
❌ Requires secure key management

---

# ✅ Advantages of CTR Mode

✔ High performance
✔ Parallel encryption/decryption
✔ No padding required
✔ Efficient for streaming data
✔ Random access support
