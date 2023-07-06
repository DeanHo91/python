import random
l1 = input("Enter number 1 (From 1 to 99): ")
l2 = input("Enter number 2 (From 1 to 99): ")
l3 = input("Enter number 3 (From 1 to 99): ")
l4 = input("Enter number 4 (From 1 to 99): ")
l5 = input("Enter number 5 (From 1 to 99): ")
ll1 = (random.randint(1, 99))
ll2 = (random.randint(1, 99))
ll3 = (random.randint(1, 99))
ll4 = (random.randint(1, 99))
ll5 = (random.randint(1, 99))
print("The lottery numbers are " + str(ll1) + "; " + str(ll2) + "; " + str(ll3) + "; " + str(ll4) + "; " + str(ll5) + ".")
win = 0
l1 = int(l1)
l2 = int(l2)
l3 = int(l3)
l4 = int(l4)
l5 = int(l5)
ll1 = int(ll1)
ll2 = int(ll2)
ll3 = int(ll3)
ll4 = int(ll4)
ll5 = int(ll5)
win = int(win)
if l1 == ll1:
    wwin1 = 1
elif l1 == ll2:
    wwin1 = 1
elif l1 == ll3:
    wwin1 = 1
elif l1 == ll4:
    wwin1 = 1
elif l1 == ll5:
    wwin1 = 1
else:
    wwin1 = 0
if l2 == ll1:
    wwin2 = 1
elif l2 == ll2:
    wwin2 = 1
elif l2 == ll3:
    wwin2 = 1
elif l2 == ll4:
    wwin2 = 1
elif l2 == ll5:
    wwin2 = 1
else:
    wwin2 = 0
if l3 == ll1:
    wwin3 = 1
elif l3 == ll2:
    wwin3 = 1
elif l3 == ll3:
    wwin3 = 1
elif l3 == ll4:
    wwin3 = 1
elif l3 == ll5:
    wwin3 = 1
else:
    wwin3 = 0
if l4 == ll1:
    wwin4 = 1
elif l4 == ll2:
    wwin4 = 1
elif l4 == ll3:
    wwin4 = 1
elif l4 == ll4:
    wwin4 = 1
elif l4 == ll5:
    wwin4 = 1
else:
    wwin4 = 0
if l5 == ll1:
    wwin5 = 1
elif l5 == ll2:
    wwin5 = 1
elif l5 == ll3:
    wwin5 = 1
elif l5 == ll4:
    wwin5 = 1
elif l5 == ll5:
    wwin5 = 1
else:
    wwin5 = 0
totalwin = win + wwin1 + wwin2 + wwin3 + wwin4 + wwin5
print("You have " + str(totalwin) + " matching number(s)!")