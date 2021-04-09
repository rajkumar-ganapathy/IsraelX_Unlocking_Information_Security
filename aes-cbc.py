from Crypto.Cipher import AES
from Crypto import Random
import os

def aes_encrypt(plaintext, k):
    print("key length is " + str(len(k)))
    init_vector = Random.new().read(len(k))
    print(init_vector)
    cipher = AES.new(k.encode(), AES.MODE_CBC, init_vector)
    # init vector should be appended to the encrypted text
    enc_text = init_vector + cipher.encrypt(plaintext.encode())
    return enc_text

def aes_decrypt(ciphertext, k):
    init_vector = ciphertext[:len(k)]
    cipher = AES.new(k, AES.MODE_CBC, init_vector)
    return cipher.decrypt(ciphertext[len(k):]).decode('utf-8')


str_enc = aes_encrypt("0123450123456789ABCDEF0123456789ABCDEF6789ABCDEF", "0123456789ABCDEF")
print("encrypted string is " + str(str_enc))