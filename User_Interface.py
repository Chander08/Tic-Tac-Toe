from lib2to3.pgen2 import pgen
import pygame as pg
import numpy as np
window = pg.display.set_mode((500,500))
pg.display.set_caption("Tic Tac Toe") #changes window name

pg.font.init()
font = pg.font.SysFont('Times New Roman', 75) #font and size
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
            square_size = 150
            list_of_positions = []
            for y in range(0,3):
                for x in range(0,3):
                    x_pos = x*square_size + 25
                    y_pos = y*square_size + 25
                    pg.draw.rect(window, white, (x_pos, y_pos, square_size, square_size), 2)
                    rectangle_positions = [x_pos, x_pos + square_size, y_pos, y_pos+square_size] #storing all positions for clicking 
                    list_of_positions.append(rectangle_positions)
            rectangle_index = 0
            for i in self.initial_values:
                for value in i:
                    display_text = font.render(str(value), True, white)
                    x_pos_left, x_pos_right, y_pos_bottom, y_pos_top = list_of_positions[rectangle_index]
                    x_middle = (x_pos_left + x_pos_right )/2
                    y_middle = (y_pos_bottom + y_pos_top) /2
                    window.blit(display_text, (x_middle, y_middle))
                    rectangle_index += 1
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
        (x, y) = pg.mouse.get_pos()
        for square in list_of_positions:
            
    #have to add user input stuff here
    pg.display.update()

pg.quit() 

