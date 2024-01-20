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
game_clock = pygame.time.Clock()
running = True

# set up our own chessboard
board = chessboard.ChessBoard(top=100,left=100,width=400)
chess_clock = chessclock.ChessClock()

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

    # draw "target" areas
    chess_area = pygame.Rect(GAME_AREA)
    pygame.draw.rect(window,"pink",chess_area)
    clock_area = pygame.Rect(CLOCK_AREA)
    pygame.draw.rect(window,"pink",clock_area)
    info_area = pygame.Rect(INFO_AREA)
    pygame.draw.rect(window,"pink",info_area)

    # draw chessboard
    board.draw_background(window)
    board.draw_pieces(window,position=chess.STARTING_FEN)

    # draw clock
    chess_clock.update()

    pygame.display.flip() # update the screen

    game_clock.tick(60) # wait until the next frame (60FPS)

