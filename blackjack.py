import random

ceck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A',]
playerhand = []
dealerhand = []

def dealcard(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)

def total(turn):
    total = 0
    face = ['A', 'J', 'K', 'Q']