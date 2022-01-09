# 100DaysOfCode Day 7 - Hangman

from random import choice
from day_007_Hangman.hangman_words import word_list
from day_007_Hangman.hangman_art import stages, logo

chosen_word = choice(word_list)
blank_cases = ['_'] * len(chosen_word)

lives = 6
end_of_game = False
print(logo)
while not end_of_game:
    letter = input('Guess a letter: ').lower()
    if letter in chosen_word:
        for i, v in enumerate(chosen_word):
            if letter == chosen_word[i]:
                blank_cases[i] = letter
    else:
        lives -= 1
        if lives == 0:
            print('You Lose!')
            end_of_game = True
    if '_' not in blank_cases:
        print('You Win!')
        end_of_game = True
    print(' '.join(blank_cases))
    print(stages[lives])
