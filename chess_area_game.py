from colors import *
from game_area import GameArea
import pygame as pg

class GameAreaChessBoard(GameArea):
    def __init__(self, game, r):
        GameArea.__init__(self, game, r)

    def draw(self):
        win = self.game.win
        GameArea.draw(self)
        self.game.chess_board.draw(win,self.rect)