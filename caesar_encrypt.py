alphabet = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(plaintext, k) :
    crypt_text = ""
    for char_element in plaintext :
        index_of_char_element = alphabet.find(char_element)
        cipher_index = index_of_char_element - k
        if cipher_index < 0 :
            cipher_index = len(alphabet) + cipher_index
        crypt_text = crypt_text + alphabet[cipher_index]
    return crypt_text


plaintext = "attack at dawn"
crypted_pass = encrypt(plaintext, 3)
print(crypted_pass)