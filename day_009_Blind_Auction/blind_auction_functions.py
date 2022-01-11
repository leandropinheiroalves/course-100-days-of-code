# 100DaysOfCode Day 9 - Blind Auction

bids = dict()


def auction(name, bid):
    bids[name] = bid
    winner_bid = 0
    winner = list(['', ''])
    for nm, bd in bids.items():
        if bd > winner_bid:
            winner_bid = bd
            winner[0] = nm, bd
    return winner[0]


def clear():
    import os
    os.system('clear')
