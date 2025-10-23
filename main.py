# Billy Vincini
# main.py
# main script that encrypts a single block of plaintext

from encrypt import encrypt_block

if __name__ == "__main__":
    key = b"Thats my Kung Fu"      # 16 bytes
    plaintext = b"Two One Nine Two" # 16 bytes

    ciphertext = encrypt_block(plaintext, key)
    print("Ciphertext:", ciphertext.hex())
