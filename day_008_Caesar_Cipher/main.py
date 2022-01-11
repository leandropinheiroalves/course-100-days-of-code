# 100DaysOfCode Day 8 - Caesar Cipher
from caesar_cipher_function import caesar
from caesar_cipher_art import logo

print(logo)

while True:
    choice = input('Type "encode" to encrypt, type "decode" to decrypt: ')
    message = input('Type your message: ')
    shift = int(input('Type the shift number: '))
    caesar(message, shift, choice)

    run_again = input('Type "yes" to continue or type "no" to exit. ')
    if run_again == 'no':
        print('Good Bye...')
        break
