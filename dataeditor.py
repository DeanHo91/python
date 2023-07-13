name = input("Enter your name: ")
name = str(name)
age = input("Enter your age: ")
age = int(age)
nation = input("Enter your nationality: ")
userdic = [name,age,nation]
while True:
    print(f"Name: {name}, Age: {age}, Nationality: {nation} \nDo you want to edit any information?")
    edit = input("(y/n)")
    if edit == "y":
        editinfo = True
        while editinfo == True:
            if edit == "y":
                choice = input("What information do you want to edit?: (name/age/nationality)")
                if choice == "name":
                    editname = input("Enter your new name: ")
                    name = editname
                    editinfo = False
                elif choice == "age":
                    editage = input("Enter your new age: ")
                    age = editage
                    editinfo = False
                elif choice == "nationality":
                    editnation = input("Enter your new nationality: ")
                    nation = editnation
                    editinfo = False
            elif edit == "n":
                editinfo = False
            else:
                print("Invalid Command")
    elif edit == "n":
        break
    else:
        print("Invalid Command")