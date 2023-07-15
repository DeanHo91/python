orders = []
total_price = 0

while True:
    order = input("Fluffy Burgers menu: \n1. Cheese Burger (Size M: $2 / Size L: $3) \n2. Beef Burger (Size M: $3 / Size L: $4 / Double Decker: $7 / Triple Decker: $12) \n3. Chicken Burger (Size M: $3 / Size L: $4 / Double Decker Extra Crispy: $8) \n4. BBQ Fries (Size S: $1 / Size M: $2 / Size L: $3 / Bucket Size: $6) \n5. Onion Rolls (Size S: $1) \n6. Coke (Size L: $1 or get one free if your order is above $10)\n")
    
    if order.lower() == "cheese burger":
        size1 = input("Size (M/L)?")
        if size1.lower() == "m":
            item = "Cheese Burger (Size M)"
            price = 2
            total_price += price
            orders.append(item)
        elif size1.lower() == "l":
            item = "Cheese Burger (Size L)"
            price = 3
            total_price += price
            orders.append(item)
        else:
            print("Invalid Size.")
    elif order.lower() == "beef burger":
        size2 = input("Size (M/L/Double Decker/Triple Decker)?")
        if size2.lower() == "m":
            item = "Beef Burger (Size M)"
            price = 3
            total_price += price
            orders.append(item)
        elif size2.lower() == "l":
            item = "Beef Burger (Size L)"
            price = 4
            total_price += price
            orders.append(item)
        elif size2.lower() == "double decker":
            item = "Beef Burger (Double Decker)"
            price = 7
            total_price += price
            orders.append(item)
        elif size2.lower() == "triple decker":
            item = "Beef Burger (Triple Decker)"
            price = 12
            total_price += price
            orders.append(item)
        else:
            print("Invalid Size")
    elif order.lower() == "chicken burger":
        size3 = input("Size (M/L/Double Decker Extra Crispy)?")
        if size3.lower() == "m":
            item = "Chicken Burger (Size M)"
            price = 3
            total_price += price
            orders.append(item)
        elif size3.lower() == "l":
            item = "Chicken Burger (Size L)"
            price = 4
            total_price += price
            orders.append(item)
        elif size3.lower() == "double decker":
            item = "Chicken Burger (Double Decker Extra Crispy)"
            price = 8
            total_price += price
            orders.append(item)
        else:
            print("Invalid Size")
    elif order.lower() == "bbq fries":
        size4 = input("Size (S/M/L/Bucket Size)?")
        if size4.lower() == "s":
            item = "BBQ Fries (Size S)"
            price = 1
            total_price += price
            orders.append(item)
        elif size4.lower() == "m":
            item = "BBQ Fries (Size M)"
            price = 2
            total_price += price
            orders.append(item)
        elif size4.lower() == "l":
            item = "BBQ Fries (Size L)"
            price = 3
            total_price += price
            orders.append(item)
        elif size4.lower() == "bucket size":
            item = "BBQ Fries (Size L)"
            price = 6
            total_price += price
            orders.append(item)
        else:
            print("Invalid Size")
    elif order.lower() == "onion rolls":
        item = "Onion Rolls"
        price = 1
        total_price += price
        orders.append(item)
    elif order.lower() == "coke":
        item = "Coke"
        price = 1
        total_price += price
        orders.append(item)
    else:
        print("Invalid order, please choose items on the menu.")
    if total_price >= 10:
        print("Congratulations! You get a free Coke with your order.")
        item = "Coke"
        orders.append(item)
    print(f"Your order consists of {len(orders)} items: {', '.join(orders)}. Total price: ${total_price}")
    
    more_orders = input("Would you like to order more? (Y/N) ")
    if more_orders.lower() == "n":
        print("Thank you for ordering!")
        location = input("Please select your location: \n1.Neville \n2.Havenport \n3.Avalen")
    if location.lower() == "neville":
        house_num = input("Please enter your house number:")
        if house_num.isdigit():
            print(f"Your order will arrive at {house_num} Neville in 21 minutes!")
            break
        else:
            print("Invalid house number")
    elif location.lower() == "havenport":
        house_num = input("Please enter your house number:")
        if house_num.isdigit():
            print(f"Your order will arrive at {house_num} Havenport in 32 minutes!")
            break
        else:
            print("Invalid house number")
    elif location.lower() == "avalen":
        house_num = input("Please enter your house number:")
        if house_num.isdigit():
            print(f"Your order will arrive at {house_num} Avalen in 15 minutes!")
            break
        else:
            print("Invalid house number")
    
