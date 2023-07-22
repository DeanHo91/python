import time
import random

# initialize the prices
gold = 200.5
silver = 24.6
apple = 191.65
boeing = 211.2
daimlerag = 71.65
generalelectric = 110.2
shell = 2416.81
unitedairlines = 57.61
nike = 109.06

while True:
    # generate random numbers between -1000 and 1000 for each price
    gold_change = random.uniform(-10, 10)
    silver_change = random.uniform(-10, 10)
    apple_change = random.uniform(-10, 10)
    boeing_change = random.uniform(-10, 10)
    daimlerag_change = random.uniform(-10, 10)
    generalelectric_change = random.uniform(-10, 10)
    shell_change = random.uniform(-10, 10)
    unitedairlines_change = random.uniform(-10, 10)
    nike_change = random.uniform(-10, 10)

    # update the prices
    gold += gold_change
    silver += silver_change
    apple += apple_change
    boeing += boeing_change
    daimlerag += daimlerag_change
    generalelectric += generalelectric_change
    shell += shell_change
    unitedairlines += unitedairlines_change
    nike += nike_change

    # make sure the prices are never below 0
    gold = max(gold, 0)
    silver = max(silver, 0)
    apple = max(apple, 0)
    boeing = max(boeing, 0)
    daimlerag = max(daimlerag, 0)
    generalelectric = max(generalelectric, 0)
    shell = max(shell, 0)
    unitedairlines = max(unitedairlines, 0)
    nike = max(nike, 0)

    # print the prices
    print(f"Gold: {gold:.2f}\nSilver: {silver:.2f}\nApple: {apple:.2f}\nBoeing: {boeing:.2f}\nDaimler AG: {daimlerag:.2f}\nGeneral Electric: {generalelectric:.2f}\nShell: {shell:.2f}\nUnited Airlines: {unitedairlines:.2f}\nNike: {nike:.2f}\n")

    # wait for 10 seconds
    time.sleep(10)