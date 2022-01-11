# 100DaysOfCode Day 9 - Blind Auction

from blind_auction_functions import auction, clear
from blind_auction_art import logo

print(logo)
print('Welcome to the secret auction program.')

should_continue = 'yes'
while should_continue == 'yes':
    name = input('What is your name?: ')
    bid = int(input('What is your bid?: $'))
    winner = auction(name, bid)
    should_continue = input('Have more bidders?: ')
    clear()
    if should_continue == 'no':
        print(f'The winner is {winner[0]} with a bid of ${winner[1]}.')
