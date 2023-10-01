from tkinter import *
import random

game_width = 700
game_height = 700
speed = 50
space_size = 50
snake_color = "#00FF00"
food_color = "#FF0000"
background_color = "#000000"

class snake:
    pass

class food:
    pass

def next_turn():
    pass

def change_direction(new_direction):
    pass
 
def game_over():
    pass

def game_over():
    pass

window = Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg=background_color, height=game_height, width=game_width)
canvas.pack()
window.mainloop()