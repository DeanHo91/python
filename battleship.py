#EXTREMELY BUGGY, WILL FIX!!!
#Really need support from the community
import random

board = [['-' for _ in range(20)] for _ in range(20)]
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

print('  | ' + ' | '.join(letters))
print('--+' + '--+' * 9)

for i in range(10):
    print(numbers[i] + ' | ' + ' | '.join(board[i]))

patrolboatplacement = input("Select your patrol boat's position (e.g. A1): ")
row, col = ord(patrolboatplacement[0]) - ord('A'), int(patrolboatplacement[1:]) - 1
board[row][col] = 'P'

print('  | ' + ' | '.join(letters))
print('--+' + '--+' * 9)

for i in range(10):
    print(numbers[i] + ' | ' + ' | '.join(board[i]))

frigateplacement = input("Select your frigate's position (e.g. B2): ")
row, col = ord(frigateplacement[0]) - ord('A'), int(frigateplacement[1:]) - 1

if input("Do you want to place the frigate horizontally (H) or vertically (V)? ") == 'H':
    board[row][col] = 'F'
    board[row][col+1] = 'F'
else:
    board[row][col] = 'F'
    board[row+1][col] = 'F'

print('  | ' + ' | '.join(letters))
print('--+' + '--+' * 9)

for i in range(10):
    print(numbers[i] + ' | ' + ' | '.join(board[i]))

enemy_ships = []
for i in range(3):
    row = random.randint(0, 9)
    col = random.randint(0, 9)
    while board[row][col] != '-':
        row = random.randint(0, 9)
        col = random.randint(0, 9)
    enemy_ships.append((row, col))
    board[row][col] = 'E'

for i in range(3):
    shot = input("Enter the coordinates of your shot (e.g. A1): ")
    row, col = ord(shot[0]) - ord('A'), int(shot[1:]) - 1
    if (row, col) in enemy_ships:
        print("Hit!")
        board[row][col] = 'X'
        enemy_ships.remove((row, col))
    else:
        print("Miss!")
        board[row][col] = 'O'

    for j in range(3):
        row = random.randint(0, 9)
        col = random.randint(0, 9)
        if board[row][col] == 'P' or board[row][col] == 'F':
            print("You've been hit!")
            board[row][col] = 'X'
        else:
            board[row][col] = 'O'

    print('  | ' + ' | '.join(letters))
    print('--+' + '--+' * 9)

    for i in range(10):
        print(numbers[i] + ' | ' + ' | '.join(board[i]))
