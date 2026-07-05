# 🔐 RSA Cryptography Lab System

A professional implementation of the **RSA Cryptographic Algorithm** using Python and the **PyCryptodome** library.
This project demonstrates:

* RSA Key Generation
* RSA Encryption & Decryption
* Digital Signature Creation
* Signature Verification
* Secure Message Handling using OAEP Padding

# 📖 Introduction

RSA (Rivest–Shamir–Adleman) is one of the most widely used **asymmetric cryptographic algorithms** for secure data transmission.

Unlike symmetric encryption, RSA uses:

* **Public Key** → Used for Encryption
* **Private Key** → Used for Decryption

This project also implements:

* **Digital Signatures**
* **SHA-256 Hashing**
* **OAEP Secure Padding**

to ensure:

✅ Confidentiality
✅ Authentication
✅ Integrity
✅ Non-repudiation

---

# ✨ Features

* 🔑 Generates a new RSA key pair every encryption
* 🔐 Encrypts messages using RSA-OAEP
* ✍️ Creates digital signatures using SHA-256
* ✔️ Verifies digital signatures
* 📂 Saves keys and encrypted data into `.pem` files
* 🛡️ Uses secure cryptographic standards

---

# 🧠 RSA Algorithm Overview

RSA is an **asymmetric encryption algorithm** based on the mathematical difficulty of factoring large prime numbers.

## Components

| Component         | Purpose                    |
| ----------------- | -------------------------- |
| Public Key        | Encrypt message            |
| Private Key       | Decrypt message            |
| SHA-256           | Hash message               |
| Digital Signature | Verify sender authenticity |
| OAEP Padding      | Secure RSA encryption      |

# ⚙️ Working Process

## Encryption Phase

1. User enters a plaintext message.
2. System generates:

   * Public Key
   * Private Key
3. Message is encrypted using the **Public Key**.
4. SHA-256 hash is generated from the message.
5. Hash is digitally signed using the **Private Key**.
6. Ciphertext, signature, and keys are stored in files.

## Decryption & Verification Phase

1. User provides:

   * Public Key
   * Private Key
   * Ciphertext
   * Signature
2. Ciphertext is decrypted using the **Private Key**.
3. SHA-256 hash is generated from decrypted message.
4. Signature is verified using the **Public Key**.
5. If valid:

   * Message is displayed
   * Signature verified successfully

---

# 🔄 Sequence Process Diagram

```text
┌──────────┐
│   User   │
└────┬─────┘
     │
     │ Enter Message
     ▼
┌────────────────────┐
│ RSA Key Generation │
└────┬───────────────┘
     │
     ├──► Public Key
     │
     └──► Private Key
     │
     ▼
┌────────────────────┐
│ Encrypt Message    │
│ using Public Key   │
└────┬───────────────┘
     │
     ▼
┌────────────────────┐
│ Generate SHA-256   │
│ Hash               │
└────┬───────────────┘
     │
     ▼
┌────────────────────┐
│ Sign Hash using    │
│ Private Key        │
└────┬───────────────┘
     │
     ▼
┌────────────────────┐
│ Save Ciphertext,   │
│ Signature & Keys   │
└────────────────────┘
```

---

# 📊 RSA Flowchart

```text
                    ┌─────────────────┐
                    │      START      │
                    └────────┬────────┘
                             │
                             ▼
                 ┌─────────────────────┐
                 │ Select Operation    │
                 │ 1. Encrypt          │
                 │ 2. Decrypt          │
                 └────────┬────────────┘
                          │
          ┌───────────────┴────────────────┐
          │                                │
          ▼                                ▼

 ┌───────────────────┐         ┌────────────────────┐
 │ Enter Plaintext   │         │ Input PEM Keys     │
 └────────┬──────────┘         └─────────┬──────────┘
          │                                │
          ▼                                ▼
 ┌───────────────────┐         ┌────────────────────┐
 │ Generate RSA Keys │         │ Load Ciphertext    │
 └────────┬──────────┘         └─────────┬──────────┘
          │                                │
          ▼                                ▼
 ┌───────────────────┐         ┌────────────────────┐
 │ Encrypt Message   │         │ Decrypt Ciphertext │
 └────────┬──────────┘         └─────────┬──────────┘
          │                                │
          ▼                                ▼
 ┌───────────────────┐         ┌────────────────────┐
 │ Generate SHA-256  │         │ Generate SHA-256   │
 └────────┬──────────┘         └─────────┬──────────┘
          │                                │
          ▼                                ▼
 ┌───────────────────┐         ┌────────────────────┐
 │ Create Signature  │         │ Verify Signature   │
 └────────┬──────────┘         └─────────┬──────────┘
          │                                │
          ▼                                ▼
 ┌───────────────────┐         ┌────────────────────┐
 │ Save Files        │         │ Show Result        │
 └────────┬──────────┘         └─────────┬──────────┘
          │                                │
          └──────────────┬─────────────────┘
                         ▼
                 ┌──────────────┐
                 │    END       │
                 └──────────────┘
```

---

# 📁 Project Structure

```text
RSA-Lab-System/
│
├── main.py
├── private.pem
├── public.pem
├── ciphertext.pem
├── signature.pem
└── README.md
```

# 🔍 Code Explanation

## Key Generation

```python
key = RSA.generate(2048)
```

Generates a secure 2048-bit RSA key pair.

---

## Encryption

```python
cipher_Obj = PKCS1_OAEP.new(public_key)
ciphertext = cipher_Obj.encrypt(message)
```

Encrypts plaintext using RSA-OAEP.

---

## Digital Signature

```python
h = SHA256.new(message)
signature = signer.sign(h)
```

Creates a SHA-256 hash and signs it using the private key.

---

## Signature Verification

```python
verifier.verify(h, signature)
```

Verifies message authenticity using the public key.

---

# 🔐 Security Concepts Used

| Concept           | Description              |
| ----------------- | ------------------------ |
| RSA               | Asymmetric encryption    |
| OAEP              | Secure RSA padding       |
| SHA-256           | Cryptographic hashing    |
| Digital Signature | Authentication mechanism |
| PEM Files         | Secure key storage       |

---

# 📌 Sample Output

## Encryption

```text
✔ NEW KEYPAIR GENERATED
✔ Files created:
  - private.pem
  - public.pem
  - ciphertext.pem
  - signature.pem
```

---

## Verification

```text
✔ Signature Verified!
✔ Message: Hello World
```

# 🔄 Mermaid.js Diagrams

## RSA Encryption & Verification Workflow

```mermaid
flowchart TD

    A[Start] --> B[User Enters Message]

    B --> C[Generate RSA Key Pair]
    C --> D[Public Key]
    C --> E[Private Key]

    D --> F[Encrypt Message using Public Key]
    B --> G[Generate SHA-256 Hash]

    E --> H[Sign Hash using Private Key]

    F --> I[Generate Ciphertext]
    H --> J[Generate Digital Signature]

    I --> K[Save Ciphertext.pem]
    J --> L[Save Signature.pem]

    E --> M[Save Private.pem]
    D --> N[Save Public.pem]

    K --> O[User Starts Decryption]
    L --> O
    M --> O
    N --> O

    O --> P[Load PEM Keys]
    P --> Q[Decrypt Ciphertext using Private Key]

    Q --> R[Recover Original Message]
    R --> S[Generate SHA-256 Hash]

    S --> T[Verify Signature using Public Key]

    T --> U{Signature Valid?}

    U -->|Yes| V[Display Verified Message]
    U -->|No| W[Verification Failed]

    V --> X[End]
    W --> X
```

---

# 🔐 RSA Sequence Diagram

```mermaid
sequenceDiagram

    participant User
    participant RSA_System
    participant KeyGen
    participant Encryptor
    participant Signer
    participant Verifier

    User->>RSA_System: Enter Plaintext Message

    RSA_System->>KeyGen: Generate RSA Key Pair
    KeyGen-->>RSA_System: Public Key + Private Key

    RSA_System->>Encryptor: Encrypt using Public Key
    Encryptor-->>RSA_System: Ciphertext

    RSA_System->>Signer: Generate SHA-256 Hash
    RSA_System->>Signer: Sign Hash using Private Key
    Signer-->>RSA_System: Digital Signature

    RSA_System-->>User: Save PEM Files

    User->>RSA_System: Provide Ciphertext + Keys

    RSA_System->>Encryptor: Decrypt using Private Key
    Encryptor-->>RSA_System: Original Message

    RSA_System->>Verifier: Verify Signature
    Verifier-->>RSA_System: Verification Result

    RSA_System-->>User: Display Verified Message
```

---

# 🧠 RSA Internal Working Diagram

```mermaid
graph LR

    A[Plaintext Message]
    --> B[SHA-256 Hash]

    A --> C[Encrypt using Public Key]

    B --> D[Sign using Private Key]

    C --> E[Ciphertext]
    D --> F[Digital Signature]

    E --> G[Decrypt using Private Key]

    G --> H[Recovered Message]

    H --> I[Generate New Hash]

    F --> J[Verify using Public Key]

    I --> J

    J --> K[Authentication Successful]
```

---

# 📂 File Generation Process

```mermaid
flowchart LR

    A[Encryption Process]
    --> B[Generate Keys]

    B --> C[private.pem]
    B --> D[public.pem]

    A --> E[Generate Ciphertext]
    E --> F[ciphertext.pem]

    A --> G[Generate Signature]
    G --> H[signature.pem]
```
