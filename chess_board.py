from colors import *
import chess_pieces as cp
import pygame as pg
class ChessBoard:
    def __init__(self):
        self.pieces = []
        self.reset()

    def reset(self):
        self.pieces = []
        self.pieces.append(cp.ChessPieceTower((8, 1), cp.CP_BLACK))
        self.pieces.append(cp.ChessPieceKnight((8, 2), cp.CP_BLACK))
        self.pieces.append(cp.ChessPieceBishop((8, 3), cp.CP_BLACK))
        self.pieces.append(cp.ChessPieceKing((8, 4), cp.CP_BLACK))
        self.pieces.append(cp.ChessPieceQueen((8, 5), cp.CP_BLACK))
        self.pieces.append(cp.ChessPieceBishop((8, 6), cp.CP_BLACK))
        self.pieces.append(cp.ChessPieceKnight((8, 7), cp.CP_BLACK))
        self.pieces.append(cp.ChessPieceTower((8, 8), cp.CP_BLACK))
        for i in range(1, 8):
            self.pieces.append(cp.ChessPiecePawn((7, i), cp.CP_BLACK))
        self.pieces.append(cp.ChessPieceTower((1, 1), cp.CP_BLACK))
        self.pieces.append(cp.ChessPieceKnight((1, 2), cp.CP_BLACK))
        self.pieces.append(cp.ChessPieceBishop((1, 3), cp.CP_BLACK))
        self.pieces.append(cp.ChessPieceKing((1, 4), cp.CP_BLACK))
        self.pieces.append(cp.ChessPieceQueen((1, 5), cp.CP_BLACK))
        self.pieces.append(cp.ChessPieceBishop((1, 6), cp.CP_BLACK))
        self.pieces.append(cp.ChessPieceKnight((1, 7), cp.CP_BLACK))
        self.pieces.append(cp.ChessPieceTower((1, 8), cp.CP_BLACK))
        for i in range(1, 8):
            self.pieces.append(cp.ChessPiecePawn((2, i), cp.CP_BLACK))


    def draw(self,win,r):
        """
        :param win: hierop tekenen we
        :param r: is de rechthoek waarbinnen we tekenen
        """

        """
            Teken bord: 2 opties, 
                een image die juist geplaatst is (eventueel herschalen)
                lijnen zelf tekenen en vierkanten opvullen met pg.draw.rect(win, color, rect
        """
