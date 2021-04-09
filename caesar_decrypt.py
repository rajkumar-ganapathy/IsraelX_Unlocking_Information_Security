alphabet = "abcdefghijklmnopqrstuvwxyz"

def encrypt(plaintext, k):
    ciphertext = []
    for c in plaintext:
        i = alphabet.index(c)
        j = (i + k) % len(alphabet)
        ciphertext.append(alphabet[j])
    return ''.join(ciphertext)

def decrypt(ciphertext, k):
    return encrypt(ciphertext, -k)
    
def brute_force(ciphertext):
    for key in range(len(alphabet)) :
        print("Decrypted text with key " + str(key) + " is " + decrypt(ciphertext, key))
    
brute_force("kyvtrmrcipnzccrkkrtbwifdkyvefikynvjkrkeffe")