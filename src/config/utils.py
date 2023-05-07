import os
import getch

def get_cipher_input():
    user_input = {}
    os.system('clear')
    text = input('Enter the text: ')
    key = input('Enter the key: ')

    user_input['text'] = text
    user_input['key'] = key

    return user_input 

def get_path_input():
    path = './texts/'+input('\nWrite the name for the ciphertext file: ')
    return path

def get_ciphertext(path):
    cipherfile = open(path,'r')
    ciphertext = []
    for line in cipherfile:
        for word in line:
            ciphertext.append(word.upper())

    ciphertext = ''.join(ciphertext)

    return ciphertext

def menu():
    os.system('clear')
    screen = open('config/screens/menu_screen.txt', 'r')
    for line in screen:
        print(line)

def display_results(results, mode):
    key = None
    while True:
        os.system('clear')
        if mode == 'decrypt':
            screen = open('config/screens/result_screen.txt','r')
        elif mode == 'attack':
            screen = open('config/screens/attack_screen.txt','r')
        for line in screen:
            print(line)
        print(results)
        
        print("\n'b' <- back")
        key = getch.getch()
        if key == 'b':
            break

def get_language():
    key = None
    while True:
        os.system('clear')
        print('Choose the possible language for the ciphertext:')
        print("'e' -> english")
        print("'p' -> português")
        
        key = getch.getch()
        if key == 'e':
            return 'english'
        elif key == 'p':
            return 'portuguese'




        
    
