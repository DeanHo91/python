import math
print("List of available units"
      "\nKilometer to Miles (PRESS 1) "
      "\nMeter to Feet (PRESS 2)"
      "\nCentimeter to Inch (PRESS 3)"
      "\nKilogram to Pound (PRESS 4)")
select = input("Please select: ")
select = int(select)
if (select == 1):
    km = input("Enter kilometer(s) here: " )
    km = float(km)
    mile = 0.62137119
    result1 = km * mile
    result1 = float(result1)
    print (str(result1) + " Mile(s)")
elif (select == 2):
    m = input("Enter Meter(s) here: ")
    m = float(m)
    ft = 3.2808399
    result2 = m * ft
    result2 = float(result2)
    print(str(result2) + " Feet(s)")
elif (select == 3):
    cm = input("Enter Centimeter(s) here: ")
    cm = float(cm)
    inch = 0.393700787
    result3 = cm * inch
    result3 = float(result3)
    print(str(result3) + " Inch(es)")
elif (select == 4):
    kg = input("Enter Kilogram(s) here: ")
    kg = float(kg)
    lb = 2.20462262
    result4 = kg * lb
    result4 = float(result4)
    print(str(result4) + " Pound(s)")
else:
    print("Invalid command")
    

