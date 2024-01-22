from colors import *
import chess_pieces as cp
import pygame as pg
class ChessBoard:
    """
    Het chessboard bevat schaakstukken. We beginnen met een lege array.
    Om snel te starten resetten we het bord bij initialisatie zodat er stukken opstaan
    """
    def __init__(self):
        self.pieces = []
        self.reset()

    def reset(self):
        # We vegen alle stukken van het bord
        self.pieces = []
        # We plaatsen alle zwarte stukken bovenaan
        self.pieces.append(cp.ChessPieceTower((8, 1), cp.CP_BLACK))
        self.pieces.append(cp.ChessPieceKnight((8, 2), cp.CP_BLACK))
        self.pieces.append(cp.ChessPieceBishop((8, 3), cp.CP_BLACK))
        self.pieces.append(cp.ChessPieceKing((8, 4), cp.CP_BLACK))
        self.pieces.append(cp.ChessPieceQueen((8, 5), cp.CP_BLACK))
        self.pieces.append(cp.ChessPieceBishop((8, 6), cp.CP_BLACK))
        self.pieces.append(cp.ChessPieceKnight((8, 7), cp.CP_BLACK))
        self.pieces.append(cp.ChessPieceTower((8, 8), cp.CP_BLACK))
        # Ook een rij pionnen
        for i in range(1, 8):
            self.pieces.append(cp.ChessPiecePawn((7, i), cp.CP_BLACK))
        # We plaatsen alle witte stukken onderaan
        self.pieces.append(cp.ChessPieceTower((1, 1), cp.CP_BLACK))
        self.pieces.append(cp.ChessPieceKnight((1, 2), cp.CP_BLACK))
        self.pieces.append(cp.ChessPieceBishop((1, 3), cp.CP_BLACK))
        self.pieces.append(cp.ChessPieceKing((1, 4), cp.CP_BLACK))
        self.pieces.append(cp.ChessPieceQueen((1, 5), cp.CP_BLACK))
        self.pieces.append(cp.ChessPieceBishop((1, 6), cp.CP_BLACK))
        self.pieces.append(cp.ChessPieceKnight((1, 7), cp.CP_BLACK))
        self.pieces.append(cp.ChessPieceTower((1, 8), cp.CP_BLACK))
        # Ook een rij witte pionnen
        for i in range(1, 8):
            self.pieces.append(cp.ChessPiecePawn((2, i), cp.CP_BLACK))


    def draw(self,win,r):
        """
        :param win: hierop tekenen we
        :param r: is de rechthoek waarbinnen we tekenen

        Teken bord: 2 opties,
                optie 1: een image die juist geplaatst is (eventueel herschalen)
                          er zit al een image in assets/boards/
                optie 2: lijnen zelf tekenen en vierkanten opvullen met pg.draw.rect(win, color, rect
        """
