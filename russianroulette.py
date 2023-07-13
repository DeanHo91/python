import random
chamber = 1

while True:
    chance = random.randint(1, 6)
    action = input("Shoot or spin the chamber?: ")
    
    if action.lower() == "shoot":
        if chamber == chance:
            print("Shot fired, You lost!")
            break
        else:
            print("You pulled the trigger but nothing happened")
            chamber += 1  
            if chamber > 6:
                chamber = 1
    elif action.lower() == "spin the chamber":
        chance = random.randint(1, 6)
        if chamber == chance:
            print("Shot fired, You lost!")
            break
        else:
            print("You spinned the chamber and pulled the trigger but nothing happened")
    else:
        print("Invalid command please choose shoot or spin the chamber")