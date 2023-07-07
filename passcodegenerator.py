import random
gene = input("Do you want to generate a passcode?: (y/n)")
if gene == "y":
    generator = True
    while generator == True:
        passc = input("Please select passcode's digit: (4 -> 8)")
        passc = int(passc)
        if passc == 4:
            num1 = (random.randint(0, 9))
            num2 = (random.randint(0, 9))
            num3 = (random.randint(0, 9))
            num4 = (random.randint(0, 9))
            print(f"Your passcode: {num1}{num2}{num3}{num4}")
            cc = input("Create another passcode?: (y/n)")
            if cc == "y":
                continue
            elif cc == "n":
                print("Ok.")
                break
            else:
                print("Invalid Command")
                break
        if passc == 5:
            num1 = (random.randint(0, 9))
            num2 = (random.randint(0, 9))
            num3 = (random.randint(0, 9))
            num4 = (random.randint(0, 9))
            num5 = (random.randint(0, 9))
            print(f"Your passcode: {num1}{num2}{num3}{num4}{num5}")
            cc = input("Create another passcode?: (y/n)")
            if cc == "y":
                continue
            elif cc == "n":
                print("Ok.")
                break
            else:
                print("Invalid Command")
                break
        if passc == 6:
            num1 = (random.randint(0, 9))
            num2 = (random.randint(0, 9))
            num3 = (random.randint(0, 9))
            num4 = (random.randint(0, 9))
            num5 = (random.randint(0, 9))
            num6 = (random.randint(0, 9))
            print(f"Your passcode: {num1}{num2}{num3}{num4}{num5}{num6}")
            cc = input("Create another passcode?: (y/n)")
            if cc == "y":
                continue
            elif cc == "n":
                print("Ok.")
                break
            else:
                print("Invalid Command")
                break
        if passc == 7:
            num1 = (random.randint(0, 9))
            num2 = (random.randint(0, 9))
            num3 = (random.randint(0, 9))
            num4 = (random.randint(0, 9))
            num5 = (random.randint(0, 9))
            num6 = (random.randint(0, 9))
            num7 = (random.randint(0, 9))
            print(f"Your passcode: {num1}{num2}{num3}{num4}{num5}{num6}{num7}")
            cc = input("Create another passcode?: (y/n)")
            if cc == "y":
                continue
            elif cc == "n":
                print("Ok.")
                break
            else:
                print("Invalid Command")
                break
        if passc == 8:
            num1 = (random.randint(0, 9))
            num2 = (random.randint(0, 9))
            num3 = (random.randint(0, 9))
            num4 = (random.randint(0, 9))
            num5 = (random.randint(0, 9))
            num6 = (random.randint(0, 9))
            num7 = (random.randint(0, 9))
            num8 = (random.randint(0, 9))
            print(f"Your passcode: {num1}{num2}{num3}{num4}{num5}{num6}{num7}{num8}")
            cc = input("Create another passcode?: (y/n)")
            if cc == "y":
                continue
            elif cc == "n":
                print("Ok.")
                break
            else:
                print("Invalid Command")
                break
    else:
        print("Invalid Command")
elif gene == "n":
    print("Ok.")
else:
    print("Invalid Command")