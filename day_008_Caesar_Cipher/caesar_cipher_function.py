# 100DaysOfCode Day 8 - Caesar Cipher
from string import ascii_lowercase
alphabet = ascii_lowercase * 2


def caesar(text, shift, direction):
    result = ''
    shift = shift % len(ascii_lowercase)
    if direction == 'decode':
        shift *= -1
    for letter in text:
        if letter.isalpha():
            position = alphabet.index(letter) + shift
            letter = alphabet[position]
            result += letter
        else:
            result += letter
    return print(f'The {direction}d text is {result}')
