data = []

while True:
    action = input("Add data, Show data, or Remove data?: ")
    
    if action.lower() == "add data":
        namedata = input("Enter candidate name: ")
        gradedata = input("Enter candidate grade (1 -> 100): ")
        
        if gradedata.isdigit():
            gradedata = int(gradedata)
            
            if gradedata >= 101:
                print("Invalid Grade.")
            elif gradedata <= 0:
                print("Invalid Grade")
            else:
                if gradedata >= 50:
                    passgrade = "Passed"
                else:
                    passgrade = "Failed"
                    
                data.append([namedata, gradedata, passgrade])
        else:
            print("Invalid Character(s)")
            
    elif action.lower() == "show data":
        for i, candidate in enumerate(data):
            print(f"Candidate {i+1}: {candidate[0]}, {candidate[1]}, {candidate[2]}")
            
    elif action.lower() == "remove data":
        if len(data) == 0:
            print("No data to remove.")
        else:
            removedata = input("Enter the number of the candidate you want to remove: ")
            
            if removedata.isdigit():
                removedata = int(removedata)
                
                if removedata > len(data) or removedata <= 0:
                    print("Invalid candidate number.")
                else:
                    data.pop(removedata-1)
                    print(f"Candidate {removedata} removed.")
            else:
                print("Invalid character(s).")
                
    else:
        print("Invalid command, please choose between Add data, Show data, or Remove data.")