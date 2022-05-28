# Tic-Tac-Toe
from turtle import bgcolor
import pygame as pg
import sys
import numpy as np
#New File

pg.init()
WIDTH = 600
HEIGHT = 600
# rbg = red green blue
BG_COLOUR = (255, 255, 255)
BLACK = (0,0,0)
LINE_COLOUR = (23, 145, 135)
LINE_WIDTH = 10
BOARD_ROWS = 3
BOARD_COLS = 3

screen = pg.display.set_mode( (WIDTH, HEIGHT))
pg.display.set_caption( 'TIC-TAC-TOE')
screen.fill( BG_COLOUR )

board = np.zeros( (BOARD_COLS, BOARD_ROWS))
print(board)
#pg.draw.line( screen, BLACK, (10,10), (300,300), 10 ) 

def draw_line():
    pg.draw.line(screen, LINE_COLOUR, (0,200), (600,200), LINE_WIDTH )

    pg.draw.line(screen, LINE_COLOUR, (0,400), (600,400), LINE_WIDTH)

    pg.draw.line(screen , LINE_COLOUR, (200,0), (200,600), LINE_WIDTH)

    pg.draw.line(screen, LINE_COLOUR, (400,0), (400,600), LINE_WIDTH)
draw_line()

def mark_square(row, col, player):
    board[row][col]= player

def available_square(row,col):
    return board[row][col]== 0

def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True




while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        
        if event.type == pg.MOUSEBUTTONDOWN:

            mouseX = event.pos[0] #x
            mouseY = event.pos[1] #y

            clicked_row = int(mouseY // 200)
            clicked_col = int(mouseX // 200)

            if available_square ( clicked_row, clicked_row):
                if player == 1:
                    mark_square( clicked_row, clicked_col, 1)

                elif player == 2:
                    mark_square(clicked_row, clicked_col, 2)

            
 
    pg.display.update()