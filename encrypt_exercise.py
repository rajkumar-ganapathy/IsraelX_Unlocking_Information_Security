def encrypt(plaintext, k) :
    encrypted_text = ""
    for index in range(len(plaintext)) :
        encrypted_text = encrypted_text + chr(ord(plaintext[index]) ^ ord(k[index]))
    return encrypted_text