print("List of car: \nToyota Corolla - $22645 (1) \nHonda Civic - $24845 (2)")
corolla = 22645
civic = 24845
corolla = int(corolla)
civic = int(civic)
car = input("Please Select: ")
car = int(car)
if car == 1:
    trans = input("Automatic - $0 (1) \nManual - $0 (2) \nPlease Select: ")
    trans = int(trans)
    if trans == 1:
        transoption = str("Automatic Transmission")
    elif trans == 2:
        transoption = str("Manual Transmission")
    else:
        print("Invalid command")
    seat = input("Leather Seat - $200 (1) \nFabric Seat - $0 (2) \nPlease Select: ")
    seat = int(seat)
    if seat == 1:
        seatoption = str("Leather Seat")
        seatprice = 200
    elif seat == 2:
        seatoption = str("Fabric Seat")
        seatprice = 0
    else:
        print("Invalid command")
    engine = input("1.8L Engine - $0 (1) \n2.0L Engine - $1090 (2) \nPlease Select: ")
    engine = int(engine)
    if engine == 1:
        engineoption = str("1.8L Engine")
        engineprice = 0
    elif engine == 2:
        engineoption = str("2.0L Engine")
        engineprice = 1090
    else:
        print("Invalid command")
    price = civic + seatprice + engineprice
    price = str(price)
    print("You have ordered a Toyota Corolla with the following options: " + transoption + "; " + seatoption + "; " + engineoption + "!")
    print("Total Price: $" + price)
elif car == 2:
    trans = input("Automatic - $0 (1) \nManual - $0 (2) \nPlease Select: ")
    trans = int(trans)
    if trans == 1:
        transoption = str("Automatic Transmission")
    elif trans == 2:
        transoption = str("Manual Transmission")
    else:
        print("Invalid command")
    seat = input("Leather Seat - $400 (1) \nFabric Seat - $0 (2) \nPlease Select: ")
    seat = int(seat)
    if seat == 1:
        seatoption = str("Leather Seats")
        seatprice = 400
    elif seat == 2:
        seatoption = str("Fabric Seats")
        seatprice = 0
    else:
        print("Invalid command")
    engine = input("2.0L Engine $0 (1) \n1.5L Turbocharged Engine - $1975 (2) \nPlease Select: ")
    engine = int(engine)
    if engine == 1:
        engineoption = str("2.0L Engine")
        engineprice = 0
    elif engine == 2:
        engineoption = str("1.5L Turbocharged Engine")
        engineprice = 1975
    else:
        print("Invalid command")
    price = civic + seatprice + engineprice
    price = str(price)
    print("You have ordered a Honda Civic with the following options: " + transoption + "; " + seatoption + "; " + engineoption + "!")
    print("Total Price: $" + price)
    
else:
    print("Invalid command")
