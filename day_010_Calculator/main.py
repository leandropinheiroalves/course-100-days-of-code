# 100DaysOfCode Day 10 - Calculator
from art import logo, operations

print(logo)

first_number = float(input('Type the first number: '))
for i in operations:
    print(i)

while True:
    operation = input('Pick an operation: ')
    next_number = float(input('Type the next number: '))
    function = operations[operation]
    result = function(first_number, next_number)
    print(f'{first_number} {operation} {next_number} = {result}')

    should_continue = input(f'Type "y" to continue calculating with {result}, or type "n" to exit: ')
    if should_continue == 'n':
        print('Good Bye.')
        break
    first_number = result
