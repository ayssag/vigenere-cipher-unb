def vigenere_decipher(text, key, display):
    cyphertext = ""
    key_length = len(key)
    key_as_int = [ord(i.upper()) - 65 for i in key]
    index = 0

    for letter in text:
        if letter.isalpha():
            offset = 65 if letter.isupper() else 97
            cyphertext += chr((ord(letter) - offset - key_as_int[index % key_length]) % 26 + offset)
            index += 1
        elif display:
            cyphertext += letter

    return cyphertext