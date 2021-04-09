from Crypto.Cipher import ARC4
from Crypto.Random import get_random_bytes
from Crypto.Hash import SHA

def rc4(plaintext, key):
    nonce = get_random_bytes(16)
    tempkey = SHA.new(key+nonce).digest()
    cipher = ARC4.new(tempkey)
    return (nonce + cipher.encrypt(plaintext))

def simple_rc4(plaintext, key):
    cipher = ARC4.new(key)
    return cipher.encrypt(plaintext)