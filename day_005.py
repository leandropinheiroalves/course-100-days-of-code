# 100DaysOfCode Day 5 - Password Generator

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
           'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('Welcome to the Password Generator!')
number_letters = int(input('How many letters would you like in your password? '))
number_symbols = int(input('How many symbols would you like in your password? '))
number_numbers = int(input('How many numbers would you like in your password? '))

password = ''
for i in range(number_letters):
    password += random.choice(letters)

for i in range(number_symbols):
    password += random.choice(symbols)

for i in range(number_numbers):
    password += random.choice(numbers)

password = ''.join(random.sample(password, len(password)))

print(f'\nHere is your password: {password}')
print(f'Your password have {len(password)} characters.')
