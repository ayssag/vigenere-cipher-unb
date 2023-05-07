from modules.vigenere_decipher import vigenere_decipher
import os

english_freq = {'A': 0.08167, 'B': 0.01492, 'C': 0.02782, 'D': 0.04253, 'E': 0.12702, 'F': 0.02228, 'G': 0.02015,
                'H': 0.06094, 'I': 0.06966, 'J': 0.00153, 'K': 0.00772, 'L': 0.04025, 'M': 0.02406, 'N': 0.06749,
                'O': 0.07507, 'P': 0.01929, 'Q': 0.00095, 'R': 0.05987, 'S': 0.06327, 'T': 0.09056, 'U': 0.02758,
                'V': 0.00978, 'W': 0.02360, 'X': 0.00150, 'Y': 0.01974, 'Z': 0.00074}

english_freq_list = list(english_freq.values())

pt_freq = {
    'A': 0.14634, 'B': 0.01043, 'C': 0.03882, 'D': 0.04992, 'E': 0.12570, 'F': 0.01023, 'G': 0.01303,
    'H': 0.00781, 'I': 0.06186, 'J': 0.00397, 'K': 0.00015, 'L': 0.02779, 'M': 0.04738, 'N': 0.04446,
    'O': 0.09735, 'P': 0.02523, 'Q': 0.01204, 'R': 0.06530, 'S': 0.06805, 'T': 0.04336, 'U': 0.03639,
    'V': 0.01575, 'W': 0.00037, 'X': 0.00253, 'Y': 0.00006, 'Z': 0.00470
}

pt_freq_list = list(pt_freq.values())

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def calculate_ic(text):
    text = str(text)
    text = text.upper()
    text_length = len(text)
    if text_length <= 1:
        return 0
    letter_frequencies = {letter: 0 for letter in alphabet}
    for letter in text:
        letter_frequencies[letter] += 1
    ic = sum(letter_frequencies[c] * (letter_frequencies[c] - 1) for c in alphabet) / (text_length * (text_length - 1))
    return ic

def sort_key(item):
    return item[1]

def find_key_lengths(ciphertext, min_key_length, max_key_length, top_n):
    ic_scores = []

    for key_length in range(min_key_length, max_key_length + 1):
        ic_sum = 0
        for i in range(key_length):
            substring = ciphertext[i::key_length]
            ic = calculate_ic(substring)
            ic_sum += ic
        ic_avg = ic_sum / key_length
        ic_scores.append((key_length, ic_avg))

    ic_scores.sort(key=sort_key, reverse=True)
    return [x[0] for x in ic_scores[:top_n]]

def split_nth_letter(text, n):
    split_strings = []
    for offset in range(n):
        current_string = ""
        for i in range(offset, len(text), n):
            current_string += text[i]

        split_strings.append(current_string)

    return split_strings


def chi_square(observed, expected):
    chi_square_value = sum(((o - e) ** 2) / e for o, e in zip(observed, expected) if not e == 0)
    return chi_square_value

def letter_frequencies(text, language):
    if language == 'english':
        new_freq = english_freq.copy()
        for letter in english_freq:
            new_freq[letter] = text.count(letter)/26
    elif language == 'portuguese':
        new_freq = pt_freq.copy()
        for letter in pt_freq:
            new_freq[letter] = text.count(letter)/26
    
    return new_freq

def find_nth_letter(text, language):
    chi_values = {}
    if language == 'english':
        for letter in english_freq:
            decryption = vigenere_decipher(text, letter, display=False)
            decryption_freq = list(letter_frequencies(decryption, language).values())
            chi = chi_square(english_freq_list, decryption_freq)
            chi_values[letter] = chi
    elif language == 'portuguese':
        for letter in pt_freq:
            decryption = vigenere_decipher(text, letter, display=False)
            decryption_freq = list(letter_frequencies(decryption, language).values())
            chi = chi_square(pt_freq_list, decryption_freq)
            chi_values[letter] = chi
    
    chi_values_sorted = {key: value for key, value in sorted(chi_values.items(), key=sort_key)}
    return list(chi_values_sorted)[0]

def find_key(language, ciphertext):
    new_ciphertext = []
    
    for character in ciphertext:
        if character.isalpha():
            new_ciphertext.append(character)

    min_key_length = 1
    max_key_length = 10
    top_n = 3

    possible_key_lengths = find_key_lengths(new_ciphertext, min_key_length, max_key_length, top_n)
    os.system('clear')
    print("3 possible key lenghts:", possible_key_lengths)
    possible_keys = []
    for lenght in possible_key_lengths:
        key = []
        split_text = split_nth_letter(new_ciphertext, lenght)
        for split in split_text:
            letter = find_nth_letter(split, language)
            key.append(letter)
        key = ''.join(key)
        possible_keys.append(key)
    print('We have a guess!')
    
    return possible_keys

def check_key(text, possible_keys):
    while True:
        os.system('clear')
        print(possible_keys)
        choosen_key = input('Choose one key to decipher the text: \n')
        decryption = vigenere_decipher(text, choosen_key, display=True)
        print('Plaintext: \n', decryption)
        key = input('Does the plaintext make sense? y/n\n')
        if key == 'y':
            break
    
    return 'CRACKED!'




