def get_prg(plaintext_size, k):
    i = j = idx = 0
    key_len = len(k)
    k_list = list(k)
    key_stream = ""

    while idx < plaintext_size :
        i = (i + 1) % key_len
        j = (j + ord(k_list[i])) % key_len
        enc_idx = (ord(k_list[i]) + ord(k_list[j])) % key_len
        k_list[i], k_list[j] = k_list[j], k_list[i]
        key_stream = key_stream + k_list[enc_idx]
        idx = idx + 1

    return key_stream

def fake_rc4(plaintext, keystream):
    text_length = len(plaintext)
    enc_text = ""
    for idx in range(text_length) :
        enc_text = enc_text + chr(ord(plaintext[idx]) ^ ord(keystream[idx]))
    return enc_text