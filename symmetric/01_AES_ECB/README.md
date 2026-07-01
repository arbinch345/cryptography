# AES ECB Mode Encryption and Decryption

## Overview

This project demonstrates **AES (Advanced Encryption Standard)** encryption and decryption using **ECB (Electronic Codebook) mode** in Python with two different approaches:

1. **Using built-in padding functions** from the `pycryptodome` library.
2. **Using manual padding and unpadding** implementation.

The project helps understand how AES encryption works internally and how plaintext is converted into encrypted ciphertext and later restored back to its original form.

---

# What is AES?

AES (Advanced Encryption Standard) is a symmetric encryption algorithm widely used for securing data.

* It uses the **same key** for both encryption and decryption.
* AES supports key sizes of:

  * 128-bit
  * 192-bit
  * 256-bit

In this project:

* AES-128 is used in the first implementation (`16-byte random key`)
* AES-256 is used in the second implementation (`SHA-256 derived key`)

---

# What is ECB Mode?

ECB (Electronic Codebook) is one of the simplest AES modes.

### How ECB Works

* Plaintext is divided into fixed-size blocks (16 bytes for AES).
* Each block is encrypted independently using the same key.

### Diagram

```text
Plaintext Blocks:
Block1 | Block2 | Block3

        AES Encryption
             ↓
Cipher1 | Cipher2 | Cipher3
```

### Drawback of ECB

ECB is **not recommended for real-world security** because identical plaintext blocks produce identical ciphertext blocks.

Example:

```text
HELLOHELLOHELLO
HELLOHELLOHELLO
```

Both blocks generate the same encrypted output pattern.


# Requirements

Install the required package:

```bash
pip install pycryptodome
```

## Encryption Flow

```text
Plaintext
   ↓
UTF-8 Encoding
   ↓
Padding
   ↓
AES ECB Encryption
   ↓
Base64 Encoding
   ↓
Ciphertext
```

---

## Decryption Flow

```text
Ciphertext
   ↓
Base64 Decoding
   ↓
AES ECB Decryption
   ↓
Unpadding
   ↓
Original Plaintext
```

## ECB Mode Limitation

ECB mode is insecure for sensitive or repeated data because:

* Identical plaintext blocks create identical ciphertext blocks.
* Patterns in data may still be visible.


# Learning Objectives

This project helps understand:

* AES encryption and decryption
* ECB mode working mechanism
* Padding and unpadding
* Base64 encoding
* Key generation
* Difference between built-in and manual implementations


# Conclusion

This project demonstrates AES encryption in ECB mode using two approaches:

1. Library-provided padding utilities
2. Custom manual padding implementation

It is useful for learning cryptography fundamentals and understanding how block cipher encryption operates internally.

---