# Cryptography

A collection of cryptographic algorithms and symmetric encryption modes implemented for learning, experimentation, and educational purposes.

## 📌 Overview

This repository is divided into two major categories of cryptography:

### 🔐 Asymmetric Cryptography (Public-Key Cryptography)

Asymmetric cryptography uses two different but mathematically related keys:

Public Key – Shared openly and used for encryption or signature verification.
Private Key – Kept secret and used for decryption or digital signing.

Because the encryption and decryption keys are different, asymmetric cryptography enables secure communication without requiring both parties to share a secret key beforehand.

### 🔒 Symmetric Cryptography (Secret-Key Cryptography)

Symmetric cryptography uses a single shared secret key for both encryption and decryption. The sender and receiver must possess the same key before communication begins.

It is significantly faster than asymmetric cryptography, making it the preferred choice for encrypting large amounts of data.

The goal of this project is to demonstrate the implementation and working principles of different cryptographic techniques and modes of operation.

---

# 📂 Repository Structure

```bash
cryptography/
│
├── Asymmetric/
│   └── RSA/
│
└── Symmetric/
    ├── ECB/
    ├── CBC/
    ├── CFB/
    ├── OFB/
    ├── CTR/
    └── GCM/
```

---

# 🔐 Asymmetric Cryptography

## RSA Algorithm

RSA is one of the most widely used public-key cryptographic algorithms. It is used for:

* Secure data transmission
* Encryption and decryption
* Digital signatures
* Key exchange

### Features

* Public and private key generation
* Encryption using public key
* Decryption using private key

---

## 🔒 Symmetric Cryptography Modes

This repository also contains implementations of different block cipher modes used in symmetric encryption.

## 1. ECB (Electronic Codebook)

* Simplest encryption mode
* Encrypts each block independently
* Fast but less secure for repeated patterns

### Characteristics

* Easy to implement
* Parallel encryption possible
* Not recommended for sensitive data

---

## 2. CBC (Cipher Block Chaining)

* Each plaintext block is XORed with the previous ciphertext block
* Uses an Initialization Vector (IV)

### Characteristics

* More secure than ECB
* Prevents identical plaintext blocks from producing identical ciphertext

---

## 3. CFB (Cipher Feedback)

* Converts block cipher into stream cipher
* Encrypts small units of data

### Characteristics

* Suitable for real-time applications
* Self-synchronizing

---

## 4. OFB (Output Feedback)

* Generates keystream independent of plaintext and ciphertext

### Characteristics

* Error in one bit does not propagate
* Suitable for noisy communication channels

---

## 5. CTR (Counter Mode)

* Uses a counter value for encryption
* Converts block cipher into stream cipher

### Characteristics

* High performance
* Supports parallel processing
* Widely used in modern systems

---

## 6. GCM (Galois/Counter Mode)

* Advanced encryption mode providing:

  * Confidentiality
  * Authentication
  * Integrity

### Characteristics

* Fast and secure
* Used in TLS, HTTPS, and modern security protocols

---

# 🚀 Getting Started

## Clone the Repository

```bash
git clone https://github.com/arbinch345/cryptography.git
```

---

# 📚 Learning Objectives

This repository helps in understanding:

* Basic cryptographic principles
* Public-key cryptography
* Symmetric encryption modes
* Encryption and decryption processes
* Security advantages and limitations of different modes

---

# ⚠️ Disclaimer

This repository is intended for **educational and learning purposes only**.
Do not use these implementations directly in production systems without proper security review.

---

# 🤝 Contributing

Contributions are welcome.

Feel free to:

* Fork the repository
* Create a new branch
* Improve implementations
* Add new cryptographic algorithms or modes
* Submit a pull request
