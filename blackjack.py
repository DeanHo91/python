import random
playerin = True
dealerin = True

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10,
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
    for card in turn:
        if card in turn:
            if card in range(1, 11):
                total += card
            elif card in face:
                total += 10
            else:
                if total > 11:
                    total += 1
                else:
                    total += 11
    return total

def revealdealerhand():
    if len(dealerhand) == 2:
        return dealerhand[0]
    elif len(dealerhand) > 2:
        return dealerhand[0], dealerhand[1]
    
for _ in range(2):
    dealcard(dealerhand)
    dealcard(playerhand)

while playerin or dealerin:
    print(f"Dealer hand {revealdealerhand()} and X")
    print(f"You have {playerhand}, total: {total(playerhand)}")
    if playerin:
        stayorhit = input("1. Stay \n2. Hit\n")
    if total(dealerhand) > 16:
        dealerin = False
    else:
        dealcard(dealerhand)
    if stayorhit == '1':
        playerin = False
    else:
        dealcard(playerhand)
    if total(playerhand) >= 21:
        break
    elif total(dealerhand) >= 21:
        break

if total(playerhand) == 21:
    print(f"You have {playerhand} for a total of {total(playerhand)} and the dealer has {dealerhand} for a total of {total(dealerhand)}")
    print("Blackjack, you win!")
elif total(dealerhand) == 21:
    print(f"You have {playerhand} for a total of {total(playerhand)} and the dealer has {dealerhand} for a total of {total(dealerhand)}")
    print("Blackjack, dealer wins!")
elif total(playerhand) > 21:
    print(f"You have {playerhand} for a total of {total(playerhand)} and the dealer has {dealerhand} for a total of {total(dealerhand)}")
    print("You bust, dealer wins!")
elif total(dealerhand) > 21:
    print(f"You have {playerhand} for a total of {total(playerhand)} and the dealer has {dealerhand} for a total of {total(dealerhand)}")
    print("Dealer bust, you win!")
elif 21 - total(dealerhand) < 21 - total(playerhand):
    print(f"You have {playerhand} for a total of {total(playerhand)} and the dealer has {dealerhand} for a total of {total(dealerhand)}")
    print("Dealer wins!")
elif 21 - total(dealerhand) > 21 - total(playerhand):
    print(f"You have {playerhand} for a total of {total(playerhand)} and the dealer has {dealerhand} for a total of {total(dealerhand)}")
    print("You win!")
