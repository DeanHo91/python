account = 1000

while True:
    print(f"Your Account: ${account}")
    action = input("Deposit/Withdraw/Exit: ")
    
    if action.lower() == "deposit":
        damount = input("How much do you want to deposit? (Limit: $3000): ")
        if damount.isdigit():
            damount = int(damount)
            if damount > 3000:
                print("Deposit exceeds the limit.")
            elif damount <= 0:
                print("You cannot deposit a negative amount of money. Please use withdraw.")
            else:
                account += damount
        else:
            print("Invalid characters. Please enter a valid amount.")
    
    elif action.lower() == "withdraw":
        wamount = input(f"How much do you want to withdraw? (Current balance: ${account}): ")
        if wamount.isdigit():
            wamount = int(wamount)
            if wamount > account:
                print("Withdrawal failed. Withdrawal exceeds the amount of money you currently have.")
            elif wamount <= 0:
                print("You cannot withdraw a negative amount of money. Please use deposit.")
            else:
                account -= wamount
        else:
            print("Invalid characters. Please enter a valid amount.")
    
    elif action.lower() == "exit":
        print("Ok.")
        break
    
    else:
        print("Invalid action. Please enter a valid action (Deposit/Withdraw/Exit).")