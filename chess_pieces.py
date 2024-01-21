from colors import *
import pygame as pg

CP_WHITE = 1
CP_BLACK = 2
class ChessPiece:
    def __init__(self,pos, black_or_white):
        self.pos = pos
        self.possible_moves = []
        self.extra_moves = []
        self.capture_moves = []
        self.extra_capture_moves = []
        self.repeat_moves = False
        self.BW = black_or_white

    def draw(self,win,square_width,x,y):
        pg.draw.rect(win, RED, (x, y, square_width, square_width), 0, 4)
        # pg.draw.rect(win, RED, (420, 155, 60, 60), 4, 0)
        print("pg.draw.rect",win,GREEN,(x,y,square_width,square_width),2,4)

class ChessPieceKing(ChessPiece):
    def __init__(self,pos, black_or_white):
        ChessPiece.__init__(self, pos, black_or_white)
        self.repeat_moves = False
        self.possible_moves=[(1,0),(1,1),(0,1),(-1,-1),(-1,0),(-1,-1),(0,-1),(1,-1)]

class ChessPieceQueen(ChessPiece):
    def __init__(self, pos, black_or_white):
        ChessPiece.__init__(self, pos, black_or_white)
        self.repeat_moves = True
        self.possible_moves = [(1, 0), (1, 1), (0, 1), (-1, -1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

class ChessPieceKnight(ChessPiece):
    def __init__(self, pos, black_or_white):
        ChessPiece.__init__(self, pos, black_or_white)
        self.repeat_moves = False
        self.possible_moves=[(2, 1),(1,2),(-1, 2),(1,-2),(-2,-1),(-1,-2),(1,-2),(2,-1)]

class ChessPieceBishop(ChessPiece):
    def __init__(self, pos, black_or_white):
        ChessPiece.__init__(self, pos, black_or_white)
        self.repeat_moves = True
        self.possible_moves = [(1, 1), (-1, 1), (-1, -1), (1, -1)]

class ChessPieceTower(ChessPiece):
    def __init__(self, pos, black_or_white):
        ChessPiece.__init__(self, pos, black_or_white)
        self.repeat_moves = True
        self.possible_moves=[(0,-1),(1,0),(0,1),(-1,0)]

class ChessPiecePawn(ChessPiece):
    def __init__(self, pos, black_or_white):
        ChessPiece.__init__(self, pos, black_or_white)
        self.repeat_moves = True
        self.possible_moves = [(1, 0)]
        self.extra_moves = [(2, 0)]
        self.capture_moves = [(1, 1),(1, -1)]
        self.extra_capture_moves = [(1, 1),(1, -1)]
