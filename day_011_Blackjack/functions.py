# 100DaysOfCode Day 11 - Blackjack
from random import choice
import os
from art import logo


def clear():
    """Clear the screen"""
    return os.system('clear')


def deal_card():
    """Returns a random card from the deck"""
    cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
    card = choice(cards)
    return card


def new_hand():
    """Return a list with 2 cards"""
    hand = []
    for _ in range(2):
        hand.append(deal_card())
    return hand


def calculate_score(hand):
    """Take a list of cards and return the score calculated from the cards"""
    score = 0
    for card in hand:
        if card == 'A':
            score += 11
        elif card in ('J', 'Q', 'K'):
            score += 10
        else:
            score += card
    if score > 21 and 'A' in hand:
        score -= 10
    if len(hand) == 2 and score == 21:
        score = 0
    return score


def compare(user_score, computer_score):
    """Compare user and computer's score and return the result"""
    if user_score == computer_score:
        result = 'DRAW! 🙃'
    elif computer_score == 0:
        result = 'Lose, opponent has Blackjack. 😱'
    elif user_score == 0:
        result = 'Win with a Blackjack! 😎'
    elif user_score > 21:
        result = 'You went over. You lose. 😭'
    elif computer_score > 21:
        result = 'Opponent went over. You win! 😁'
    elif user_score > computer_score:
        result = 'You win! 😃'
    else:
        result = 'You lose. 😤'
    return result


def play_game():
    """Run the Blackjack game"""
    user_cards = new_hand()
    computer_cards = new_hand()
    clear()
    print(logo)

    while True:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f'Your cards: {user_cards}, current score: {user_score}')
        print(f'Computer\'s first card: {computer_cards[0]}')

        if user_score == 0 or computer_score == 0 or user_score > 21:
            break

        else:
            new_card = input('\tDo you need another card? ["y" or "n"]: ')
            if new_card == 'y':
                user_cards.append(deal_card())
            else:
                break

    while computer_score < 17 and computer_score != 0:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(compare(user_score, computer_score))
    print(f'\tYour final hand: {user_cards}, final score: {user_score}')
    print(f'\tComputer\'s final hand: {computer_cards}, final score: {computer_score}')
