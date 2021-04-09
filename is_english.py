from collections import Counter

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

def is_english(s):
    if is_ascii(s) == False : 
        return False
    alphabet_counter = [0] * 26

    # convert the string to lower for easy comparison
    s = s.lower()
    for c in s:
        ascii_c = ord(c)
        if ascii_c >= 97 and ascii_c <= 122 :
            alphabet_counter[ascii_c - 97] += 1
    print("The alphabet counter is ", alphabet_counter)

    # find the indexes of the top 6 alphabets
    max_occurence_idxs = sorted(range(len(alphabet_counter)), key=lambda i: alphabet_counter[i], reverse=True)[:3]

    print("max occurence index is ", max_occurence_idxs)
    english_freq_chars = ['e', 't', 'a', 'o', 'i', 'n']

    freq_char_found = False
    for idx in max_occurence_idxs :
        max_occur_char = chr(idx + 97)
        for eng_freq_char in english_freq_chars :
            if max_occur_char == eng_freq_char :
                freq_char_found = True
                continue
        
        # continue comes here
        if freq_char_found == True :
            freq_char_found = False
            continue
        else :
            # if it comes here then it means that the char in max_occurence_idx
            # did not match eng_freq_char
            return False
    return True

check_if_english = is_english("!@#$%^&*()!@#$%^&*()!@#$%^&*()!@#$%^&*()")
print("Is is English " + str(check_if_english))