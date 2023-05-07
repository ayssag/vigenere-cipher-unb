def vigenere_cipher(text, key):
    cyphertext = ""
    key_length = len(key)
    key_as_int = [ord(i.upper()) - ord('A') for i in key]
    index = 0

    for letter in text:
        if letter.isalpha():
            offset = ord('A') if letter.isupper() else ord('a')
            cyphertext += chr((ord(letter) - offset + key_as_int[index % key_length]) % 26 + offset)
            index += 1
        else:
            cyphertext += letter

    return cyphertext
