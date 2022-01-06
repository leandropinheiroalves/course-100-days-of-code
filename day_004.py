# 100DaysOfCode Day 4 - Rock Paper Scissors

import random

WIN = '''
██    ██  ██████  ██    ██     ██     ██ ██ ███    ██ ██ 
 ██  ██  ██    ██ ██    ██     ██     ██ ██ ████   ██ ██ 
  ████   ██    ██ ██    ██     ██  █  ██ ██ ██ ██  ██ ██ 
   ██    ██    ██ ██    ██     ██ ███ ██ ██ ██  ██ ██    
   ██     ██████   ██████       ███ ███  ██ ██   ████ ██ 
'''

LOSE = '''
██    ██  ██████  ██    ██     ██       ██████  ███████ ███████ ██ 
 ██  ██  ██    ██ ██    ██     ██      ██    ██ ██      ██      ██ 
  ████   ██    ██ ██    ██     ██      ██    ██ ███████ █████   ██ 
   ██    ██    ██ ██    ██     ██      ██    ██      ██ ██         
   ██     ██████   ██████      ███████  ██████  ███████ ███████ ██ 
'''

DRAW = '''
██████  ██████   █████  ██     ██ ██ 
██   ██ ██   ██ ██   ██ ██     ██ ██ 
██   ██ ██████  ███████ ██  █  ██ ██ 
██   ██ ██   ██ ██   ██ ██ ███ ██    
██████  ██   ██ ██   ██  ███ ███  ██  
'''

choices = ['Rock', 'Paper', 'Scissors']
choice = int(input('What do you choose? [0 - Rock, 1 - Paper, 2 - Scissors] '))

if choice >= 3 or choice < 0:
    print(LOSE, '\nYou typed an invalid number.')

else:
    user_choice = choices[choice]
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        print(DRAW, f'\nYou choose {user_choice} and computer also choose {computer_choice}.')

    else:
        if user_choice == 'Rock':
            if computer_choice == 'Paper':
                print(LOSE, f'\nYou choose {user_choice} and computer choose {computer_choice}.')
            elif computer_choice == 'Scissors':
                print(WIN, f'\nYou choose {user_choice} and computer choose {computer_choice}.')

        elif user_choice == 'Paper':
            if computer_choice == 'Rock':
                print(WIN, f'You choose {user_choice} and computer choose {computer_choice}.')
            elif computer_choice == 'Scissors':
                print(LOSE, f'\nYou choose {user_choice} and computer choose {computer_choice}.')

        elif user_choice == 'Scissors':
            if computer_choice == 'Rock':
                print(LOSE, f'\nYou choose {user_choice} and computer choose {computer_choice}.')
            elif computer_choice == 'Paper':
                print(WIN, f'\nYou choose {user_choice} and computer choose {computer_choice}.')
