from config.utils import menu, get_cipher_input, display_results, get_language
from modules.vigenere_cipher import vigenere_cipher
from modules.vigenere_decipher import vigenere_decipher
from modules.attack import find_key, check_key
from config.utils import get_path_input, get_ciphertext
import getch

while True:
    menu()
    key = getch.getch()
    if key == 'q':
        break
    elif key == 'c':
        user_input = get_cipher_input()
        result = vigenere_cipher(user_input['text'], user_input['key'])
        display_results(result, mode='decrypt')
    elif key == 'd':
        user_input = get_cipher_input()
        result = vigenere_decipher(user_input['text'], user_input['key'], display=True)
        display_results(result, mode='decrypt')
    elif key == 'a':
        language = get_language()
        path = get_path_input()
        ciphertext = get_ciphertext(path)
        possible_keys = find_key(language, ciphertext)
        result = check_key(ciphertext, possible_keys)
        display_results(result, mode='attack')
        

