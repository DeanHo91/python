import random

#Special
go = 0
CommunityChest = [2, 17, 33]
Chance = [7, 22, 36]
Jail_JustVisiting = 10
FreeParking = 20
GoToJail = 30

#Property
MediterraneanAvenue = 1
BalticAvenue = 3
OrientalAvenue = 6
VermontAvenue = 8
ConnecticutAvenue = 9
StCharlesPlace = 11
StatesAvenue = 13
VirginiaAvenue = 14
StJamesPlace = 16
TennesseeAvenue = 18
NewYorkAvenue = 19
KentuckyAvenue = 21
IndianaAvenue = 23
IllinoisAvenue = 24
AtlanticAvenue = 26
VentnorAvenue = 27
MarvinGardens = 29
PacificAvenue = 31
NorthCarolinaAvenue = 32
PennsylvaniaAvenue = 34
ParkPlace = 37
BoardWalk = 39

#Railroad/Ultilities
ReadingRailroad = 5
ElectricCompany = 12
PennsylvaniaRailroad = 15
BORailroad = 25
WaterWorks = 28
ShortLine = 35

#Tax
IncomeTax = 4
LuxuryTax = 38

#Property color
brown = [MediterraneanAvenue, BalticAvenue]
light_blue = [OrientalAvenue, VermontAvenue, ConnecticutAvenue]
pink = [StCharlesPlace, StatesAvenue, VirginiaAvenue]
orange = [StJamesPlace, TennesseeAvenue, NewYorkAvenue]
red = [KentuckyAvenue, IndianaAvenue, IllinoisAvenue]
yellow = [AtlanticAvenue, VentnorAvenue, MarvinGardens]
green = [PacificAvenue, NorthCarolinaAvenue, PennsylvaniaAvenue]
dark_blue = [ParkPlace, BoardWalk]

#Mechanics
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
move = 0
ai1dice1 = random.randint(1, 6)
ai1dice2 = random.randint(1, 6)
ai1move = 0
ai2dice1 = random.randint(1, 6)
ai2dice2 = random.randint(1, 6)
ai2move = 0

#Summary
