# general imports
import pygame
import chess
# import our own files
from constants import *
import chessboard
import chessclock

# set up pygame
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Hector Chess - Sint-Pieterscollege, Jette")
clock = pygame.time.Clock()
running = True

# set up our own chessboard
board = chessboard.ChessBoard(top=100,left=100,width=400)
chessclock = chessclock.ChessClock()

# game loop
while running:
    # ... get events for player interaction
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_position = pygame.mouse.get_pos()


    # ... logic comes here


    # ... rendering the screen
    # clear the screen before rendering
    window.fill("white")

    # draw relevant areas
    chess_area = pygame.Rect(GAME_AREA)
    pygame.draw.rect(window,"red",chess_area,border_radius=2)
    clock_area = pygame.Rect(720,60,500,200)
    pygame.draw.rect(window,"red",clock_area)
    info_area = pygame.Rect(720,320,500,340)
    pygame.draw.rect(window,"red",info_area,border_radius=2)
    # clock_area = pygame.Rect()

    # draw chessboard
    board.draw_background(window)
    board.draw_pieces(window,position=chess.STARTING_FEN)

    # draw clock


    pygame.display.flip() # update the screen

    clock.tick(60) # wait until the next frame (60FPS)

