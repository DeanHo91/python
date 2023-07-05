import random
play = input("Do you want to play?: (YES / 1) (NO / 2)")
play = int(play)
if play == 1:
    game = True
    while game == True:
         rps1 = input("Rock (1); Paper (2); Scissor (3); Cancel (ANY KEY): ")
         rps2 = (random.randint(1, 3))
         rps1 = int(rps1)
         rps2 = int(rps2)
         if rps1 == 1 and rps2 == 1:
              print("Rock - Rock (DRAW)")
         elif rps1 == 1 and rps2 == 2:
              print("Rock - Paper (YOU LOSE)")
         elif rps1 == 1 and rps2 == 3:
              print("Rock - Scissor (YOU WIN)")
         elif rps1 == 2 and rps2 == 1:
              print("Paper - Rock (YOU WIN)")
         elif rps1 == 2 and rps2 == 2:
              print("Paper - Paper (DRAW)")
         elif rps1 == 2 and rps2 ==3:
              print("Paper - Scissor (YOU LOSE)")
         elif rps1 == 3 and rps2 == 1:
              print("Scissor - Rock (YOU LOSE)")
         elif rps1 == 3 and rps2 == 2:
              print("Scissor - Paper (YOU WIN)")
         elif rps1 == 3 and rps2 == 3:
              print("Scissor - Scissor (DRAW)")
         else:
              print("Game is over!")
              game = False
