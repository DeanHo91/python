orders = []
total_price = 0

while True:
    order = input("Fluffy Burgers menu: \n1. Cheese Burger (Size M: $2 / Size L: $3) \n2. Beef Burger (Size M: $3 / Size L: $4 / Double Decker: $7 / Triple Decker: $12) \n3. Chicken Burger (Size M: $3 / Size L: $4 / Double Extra Crispy: $6) \n4. BBQ Fries (Size S: $1 / Size M: $2 / Size L: $3 / Bucket Size: $6) \n5. Onion Rolls (Size S: $1) \n6. Coke (Size L: $1 or get one free if your order is above $10)\n")
    
    if order.lower() == "cheese burger":
        size = input("Size (M/L)?")
        if size.lower() == "m":
            item = "Cheese Burger (Size M)"
            price = 2
            total_price += price
            orders.append(item)
        elif size.lower() == "l":
            item = "Cheese Burger (Size L)"
            price = 3
            total_price += price
            orders.append(item)
        else:
            print("Invalid Size.")
    elif order.lower() == "beef burger":
        if size.lower() == "m":
            item = "Beef Burger (Size M)"
            price = 3
            total_price += price
            orders.append(item)
        elif size.lower() == "l":
            item = "Beef Burger (Size L)"
            price = 4
            total_price += price
            orders.append(item)
        elif size.lower() == "double decker":
            item = "Beef Burger (Double Decker)"
            price = 7
            total_price += price
            orders.append(item)
        else:
            print("Invalid Size")
    elif order.lower() == "chicken burger":
        item = "Chicken Burger"
        price = 3
        total_price += price
        orders.append(item)
    elif order.lower() == "bbq fries":
        item = "BBQ Fries"
        price = 1
        total_price += price
        orders.append(item)
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
        break