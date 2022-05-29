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
BG_COLOUR = (28, 170, 156)
BLACK = (0,0,0)
LINE_COLOUR = (23, 145, 135)
LINE_WIDTH = 10
BOARD_ROWS = 3
BOARD_COLS = 3
RED = (255, 0 , 0)
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CIRCLE_COLOUR = (239, 231, 200)
CROSS_WIDTH = 10
SPACE = 55

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

game_over = False

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pg.draw.circle( screen, CIRCLE_COLOUR, (int( col * 200 + 100 ), int( row * 200 + 100)), CIRCLE_RADIUS, CIRCLE_WIDTH) 
            elif board[row][col] == 2:
                pg.draw.line( screen, BLACK, (col * 200 + SPACE, row * 200 + 200 - SPACE), (col * 200 + 200 - SPACE, row * 200 + SPACE), 30 )
                pg.draw.line( screen, BLACK, (col * 200 + SPACE, row * 200 + SPACE), (col * 200 + 200 - SPACE, row * 200 + 200 - SPACE), 30)
player = 1

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

def check_win(player):
    #vertical win check
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col, player)
            return True
    #horizontal win check
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row, player)
            return True
    #ascending diagonal win check
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_ascending_diagonal(player)
        return True
    #descending diagonal win check
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_descending_diagonal
        return True

    return False

def draw_vertical_winning_line(col,player):
    #200 is squares size
    posX = col * 200 + 100 

    if player == 1:
        colour = CIRCLE_COLOUR
    elif player == 2:
        colour = BLACK

    pg.draw.line( screen, colour, (posX, 15), (posX, HEIGHT - 15), 15)


def draw_horizontal_winning_line(row,player):
    posY = row * 200 + 100 
    if player == 1:
        colour = CIRCLE_COLOUR
    elif player == 2:
        colour = BLACK
    pg.draw.line(screen, colour, (15, posY), (WIDTH -15 , posY), 15)

def draw_ascending_diagonal(player):
    if player == 1:
        colour = CIRCLE_COLOUR
    elif player == 2:
        colour = BLACK
    pg.draw.line(screen,colour, (15, HEIGHT - 15), (WIDTH - 15, 15), 15)

def draw_descending_diagonal(player):
    if player == 1:
        colour = CIRCLE_COLOUR
    elif player == 2:
        colour = BLACK
    pg.draw.line(screen, colour, (15,15), (WIDTH-15,HEIGHT-15), 15)

def restart():
    screen.fill(BG_COLOUR)
    draw_line()
    player = 1
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0
            
    

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        
        if event.type == pg.MOUSEBUTTONDOWN and not game_over:

            mouseX = event.pos[0] #x
            mouseY = event.pos[1] #y

            clicked_row = int(mouseY // 200)
            clicked_col = int(mouseX // 200)

            if available_square ( clicked_row, clicked_col):
                if player == 1:
                    mark_square( clicked_row, clicked_col, 1)
                    if check_win(player):
                        game_over = True

                    player = 2

                elif player == 2:
                    mark_square(clicked_row, clicked_col, 2)
                    if check_win(player):
                        game_over = True
                    player = 1

                draw_figures()

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_r:
                restart()
                game_over = False
 
    pg.display.update()