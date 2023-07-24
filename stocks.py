#WILL FIX
import time
import random

prices = {
    "gold": 200.5,
    "silver": 24.6,
    "apple": 191.65,
    "boeing": 211.2,
    "daimlerag": 71.65,
    "generalelectric": 110.2,
    "shell": 2416.81,
    "unitedairlines": 57.61,
    "nike": 109.06
}

balance = 1000
holdings = {}

def calculate_net_worth():
    net_worth = balance
    for stock, price in prices.items():
        net_worth += price * holdings.get(stock, 0)
    return net_worth

while True:
    for stock in prices:
        prices[stock] += random.uniform(-10, 10)
        prices[stock] = max(prices[stock], 0)
    
    print(f"Current Prices:\nGold: {prices['gold']:.2f}\nSilver: {prices['silver']:.2f}\nApple: {prices['apple']:.2f}\nBoeing: {prices['boeing']:.2f}\nDaimler AG: {prices['daimlerag']:.2f}\nGeneral Electric: {prices['generalelectric']:.2f}\nShell: {prices['shell']:.2f}\nUnited Airlines: {prices['unitedairlines']:.2f}\nNike: {prices['nike']:.2f}\n")
    
    net_worth = calculate_net_worth()
    print(f"Your Balance: {balance:.2f}\nYour Holdings: {holdings}\nYour Net Worth: {net_worth:.2f}\n")
    
    print("Prices refresh every 5 seconds.")
    
    action = input("Do you want to buy or sell a stock? ")
    
    if action.lower() == "buy":
        stock = input("Which stock do you want to buy? ")
        if stock in prices:
            price = prices[stock]
            max_shares = int(balance / price)
            shares = int(input(f"How many shares do you want to buy? (max {max_shares}) "))
            shares = min(shares, max_shares)
            cost = shares * price
            balance -= cost
            holdings[stock] = holdings.get(stock, 0) + shares
            print(f"Bought {shares} shares of {stock} for {cost:.2f}.")
        else:
            print("Invalid stock.")
    elif action.lower() == "sell":
        stock = input("Which stock do you want to sell? ")
        if stock in holdings:
            price = prices[stock]
            shares = int(input(f"How many shares do you want to sell? (max {holdings[stock]}) "))
            shares = min(shares, holdings[stock])
            earnings = shares * price
            balance += earnings
            holdings[stock] -= shares
            if holdings[stock] == 0:
                del holdings[stock]
            print(f"Sold {shares} shares of {stock} for {earnings:.2f}.")
        else:
            print("You don't own any shares of that stock.")
    else:
        print("Invalid action.")
    
    time.sleep(5)
