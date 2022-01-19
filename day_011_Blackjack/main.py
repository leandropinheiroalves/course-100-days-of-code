# 100DaysOfCode Day 11 - Blackjack

# ############## Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

from functions import play_game

while True:
    choice = input('Do you wanna play a Blackjack game? ["y" or "n"]: ')
    if choice == 'y':
        play_game()
    else:
        print('Good Bye!')
        break
