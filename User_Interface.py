from lib2to3.pgen2 import pgen
import pygame as pg
import numpy as np
window = pg.display.set_mode((700,700))
pg.display.set_caption("Tic Tac Toe") #changes window name

pg.font.init()
font = pg.font.SysFont('Times New Roman', 50) #font and size
white = (255,255,255) #colors defined in RGB format
black = (0,0,0)
red = (255,0,0)
grey = (107,107,107)

class Board:
    def __init__(self, initial_values):
            '''
            Initializes the board with the given initial values.
            '''
            self.initial_values = initial_values

    def create_board(self):
            '''
            creates the 3x3 board to play on based on the initial values of the initialized board
            '''
            square_size = 100
            for y in range(1,4):
                for x in range(1,4):
                    x_pos = x*square_size
                    y_pos = y*square_size
                    pg.draw.rect(window, white, (x_pos, y_pos, square_size, square_size), 2)
            pg.display.update()

empty_board = [[0,0,0],
                [0,0,0],
                [0,0,0]]
board1 = Board(empty_board)
board1.create_board()


run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    #have to add user input stuff here
    pg.display.update()

pg.quit() 

