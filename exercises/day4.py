'''
File created by:  Chris  Cozort

This series of files will include a step by step process for creating a basic pygame-based game in python

Scavenger hunt: Comment on the following items as you see them below:
- Variables
- Data Types
- Numbers
- Strings
- Booleans
- Operators
- Tuples
- While loops
- For loops
- If Else Conditional statements
- Functions
'''

import pygame as pg

from pygame.sprite import Sprite

from random import *

from math import *

import os

vec = pg.math.Vector2

"""
From https://www.geeksforgeeks.org/__file__-a-special-variable-in-python/ 
A double underscore variable in Python is usually referred to as a dunder. A dunder variable is a 
variable that Python has defined so that it can use it in a “Special way”. 
This Special way depends on the variable that is being used.
The variable below __file__ is a variable that contains the path to the module that is currently being imported.
"""

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')

print("here's the current game folder", game_folder)
print("here's the current game folder", img_folder)
# tells the size of the cube that will move
WIDTH = 800
HEIGHT = 600
FPS = 30
# tuple that creates an RBG value
BLACK = (0,0,0)
WHITE = (255,255,255)
TILESIZE = 32
x = 0
y = 0

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("My First Pygame...")
clock = pg.time.Clock()


running = True
# boolean value that determines if the game is running
while running:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    ##### UPDATE #####
    x += 1 * FPS/1000
    y += 1 * FPS/1000

    rect = pg.Rect(x * TILESIZE, y * TILESIZE, TILESIZE, TILESIZE)

    #####  DRAW  #####
    screen.fill(BLACK)
    pg.draw.rect(screen, WHITE, rect)

    pg.display.flip()

pg.quit()