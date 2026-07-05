# 🔐 AES GCM Mode Cryptography

A professional Python implementation of **AES (Advanced Encryption Standard)** using **GCM (Galois/Counter Mode)** for secure encryption and authenticated decryption.

This project demonstrates how AES-GCM provides:

* ✅ Confidentiality (Encryption)
* ✅ Integrity (Tamper Detection)
* ✅ Authentication (Verification)

# 📌 Overview

AES-GCM is one of the most secure and modern encryption modes used today.

Unlike traditional AES modes, GCM provides:

* Encryption
* Authentication
* Integrity Verification

all together in a single operation.

This implementation includes:

* AES-GCM Encryption
* AES-GCM Decryption
* Authentication Tag Verification
* Nonce Generation
* Base64 Encoding
* Interactive Command-Line Interface

# 📖 What is GCM Mode?

## GCM (Galois/Counter Mode)

GCM is an authenticated encryption mode built on top of AES.

It combines:

* **CTR Mode Encryption**
* **Galois Field Authentication**

to provide both:

| Security Property | Description                |
| ----------------- | -------------------------- |
| Confidentiality   | Keeps data secret          |
| Integrity         | Detects data modification  |
| Authentication    | Verifies data authenticity |

# ⚙️ Working of AES-GCM

AES-GCM works in two major phases:

## 1️⃣ Encryption Phase

* Generate random nonce
* Encrypt plaintext using AES-CTR
* Generate authentication tag
* Return ciphertext + nonce + tag

---

## 2️⃣ Decryption Phase

* Decode ciphertext and nonce
* Verify authentication tag
* If verification succeeds:

  * decrypt ciphertext
* Else:

  * raise authentication error


# 📊 AES-GCM Encryption Workflow

```text id="k92wde"
┌─────────────────────┐
│     Plaintext       │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│ Generate Nonce/IV   │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│ AES-GCM Encryption  │
│  using Secret Key   │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│ Generate Auth Tag   │
└─────────┬───────────┘
          │
          ▼
┌────────────────────────────────┐
│ Ciphertext + Nonce + Auth Tag  │
└────────────────────────────────┘
```

# 📊 AES-GCM Decryption Workflow

```text id="m84xpa"
┌────────────────────────────────┐
│ Ciphertext + Nonce + Auth Tag  │
└─────────┬──────────────────────┘
          │
          ▼
┌─────────────────────┐
│ Verify Auth Tag     │
└─────────┬───────────┘
          │
    ┌─────┴─────┐
    │ Valid ?   │
    └─────┬─────┘
          │ Yes
          ▼
┌─────────────────────┐
│ AES-GCM Decryption  │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│ Original Plaintext  │
└─────────────────────┘
```

# 🔄 Sequence Diagram

## Encryption Process

```text id="e9vx4p"
User -> Program: Enter plaintext
Program -> Program: Generate Random Nonce
Program -> AES-GCM: Encrypt Plaintext
AES-GCM -> Program: Ciphertext + Auth Tag
Program -> User: Base64(Ciphertext + Nonce + Tag)
```

## Decryption Process

```text id="t2lq9n"
User -> Program: Provide Ciphertext + Nonce + Tag
Program -> AES-GCM: Verify Authentication Tag
AES-GCM -> Program: Tag Verification Success
Program -> AES-GCM: Decrypt Ciphertext
AES-GCM -> User: Original Plaintext
```

# 🧠 Authentication Tag Explained

The **Authentication Tag** is a cryptographic checksum generated during encryption.

It ensures:

* data was not modified
* ciphertext is authentic
* message integrity is preserved

If the ciphertext or nonce changes even slightly:

```text id="h0aw5v"
decrypt_and_verify()
```

will throw an authentication error.


# 🔐 AES-GCM Architecture Diagram

```text id="j73pkd"
                ┌────────────────────┐
                │     Plaintext      │
                └─────────┬──────────┘
                          │
                          ▼
              ┌─────────────────────────┐
              │ Generate Random Nonce   │
              └─────────┬───────────────┘
                        │
                        ▼
              ┌─────────────────────────┐
              │ AES-GCM Encryption      │
              │ using Secret Key        │
              └─────────┬───────────────┘
                        │
          ┌─────────────┴─────────────┐
          ▼                           ▼
┌──────────────────┐       ┌──────────────────┐
│   Ciphertext     │       │ Authentication   │
│                  │       │ Tag              │
└──────────────────┘       └──────────────────┘
          │                           │
          └─────────────┬─────────────┘
                        ▼
             ┌───────────────────────┐
             │ Send/Store Together   │
             └───────────────────────┘
```

# 📂 Project Structure

```text id="p3fw7n"
project/
│
├── aes_gcm.py
└── README.md
```

# 🔑 Encryption Example

```text id="u8mk1q"
Enter message: Hello World

Cipher_txt : q0P3iM5...
Nonce      : HJd82kL...
Tag        : A2bD8m...
```

---

# 🔓 Decryption Example

```text id="f3nv7a"
Enter cipher_txt: q0P3iM5...
Enter nonce: HJd82kL...
Enter tag: A2bD8m...

Decrypted msg: Hello World
```

# 📜 Code Explanation

## Encryption Function

```python id="z1pk7s"
def encryption(plain_txt, key):
```

### Steps

1. Create AES-GCM cipher object
2. Encrypt plaintext
3. Generate authentication tag
4. Generate nonce
5. Encode values using Base64
6. Return ciphertext, nonce, and tag

---

## Decryption Function

```python id="v7wx3n"
def decryption(encrypted_txt, nonce, key, tag):
```

### Steps

1. Decode Base64 values
2. Create AES-GCM cipher object
3. Verify authentication tag
4. Decrypt ciphertext
5. Return original plaintext

---

# 🔒 Security Advantages of GCM Mode

| Feature              | Benefit                     |
| -------------------- | --------------------------- |
| Authentication       | Detects tampering           |
| Integrity Protection | Ensures original data       |
| Fast Performance     | Hardware accelerated        |
| Parallel Processing  | High-speed encryption       |
| No Padding Required  | Works with variable lengths |

---

# ⚠️ Important Security Notes

## Never Reuse Nonce

Using the same:

```text id="c1qx9m"
Key + Nonce
```

combination multiple times can completely break AES-GCM security.

## Store These Values Safely

You must preserve:

* Ciphertext
* Nonce
* Authentication Tag

for successful decryption.

# 📈 Advantages of AES-GCM

✅ Authenticated Encryption
✅ High Performance
✅ Tamper Detection
✅ Parallel Processing
✅ No Padding Required
✅ Modern Industry Standard

# ⚠️ Limitations

❌ Nonce reuse is dangerous
❌ Slightly more complex than CBC/CTR
❌ Authentication tag must be preserved

# 📚 Real-World Applications

AES-GCM is widely used in:

* HTTPS/TLS
* VPNs
* Secure Messaging
* Cloud Security
* Disk Encryption
* API Security