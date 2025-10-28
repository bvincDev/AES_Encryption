# AES Encryption Program

A simple  implementation of **AES-128 encryption** in pure Python.
This project demonstrates the internal steps of the AES algorithm — including SubBytes, ShiftRows, MixColumns, AddRoundKey, and KeyExpansion — without using any external cryptographic libraries.

---

## ⚙️ Features

* Full AES-128 block encryption (16 bytes per block)
* Implements:

  * SubBytes transformation using the AES S-box
  * ShiftRows permutation
  * MixColumns polynomial transformation
  * AddRoundKey XOR operation
  * Key expansion for all 10 rounds
* Clean and modular Python design
* No external dependencies

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/bvincDev/AES_Encryption.git
cd AES_Encryption
```

### 2. Run the Program

Make sure you have **Python 3.8+** installed.

```bash
python main.py
```

### 3. Input Text

You will be prompted to enter a **16-character plaintext block** (AES requires exactly 16 bytes):

```
Enter 16-character plaintext: mysecretmessage1
Enter 16-character key: myencryptionkey
```

### 4. Output

The program will display the encrypted ciphertext in hexadecimal format, for example:

```
Encrypted (hex): 8a2b1f4e9cd67320f5e61e9bb9a7b3c1
```

---

## 🧠 How It Works

### AES Steps Implemented

| Step          | Function          | Description                                |
| ------------- | ----------------- | ------------------------------------------ |
| SubBytes      | `sub_bytes()`     | Replaces bytes using the AES S-Box         |
| ShiftRows     | `shift_rows()`    | Cyclically shifts rows in the state        |
| MixColumns    | `mix_columns()`   | Mixes data columns using Galois Field math |
| AddRoundKey   | `add_round_key()` | XORs state with the round key              |
| Key Expansion | `key_expansion()` | Generates round keys for all AES rounds    |

Each 16-byte plaintext block undergoes **10 rounds** of transformations to produce the final ciphertext.

---

## 🧩 Example Code Snippet

```python
from encrypt import encrypt_block

key = b'myencryptionkey'     # 16 bytes
plaintext = b'mysecretmessage1'  # 16 bytes

ciphertext = encrypt_block(plaintext, key)
print(ciphertext.hex())
```

---

## 🧱 Educational Purpose

⚠️ This project is for **educational and demonstration purposes only**.
It is **not optimized** for performance or security in production environments.
For real-world cryptography, use vetted libraries like `cryptography` or `PyCryptodome`.

---

**Billy Vincini**
[My Website](https://bvincdev.github.io/Portfolio/)
[GitHub Profile](https://github.com/yourusername)

---

## 📝 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.
