from game_constants import *
from evt_obj import EvtObj
import pygame as pg
import time as t
from chess_board import ChessBoard

class Game(EvtObj):
    def __init__(self, window, clock):
        EvtObj.__init__(self)
        self.win = window
        self.clock = clock
        self.keep_running = True
        self.last_cycle = t.time()
    def handle_events(self):
        # Keyboard Events are already filtered out
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.keep_running = False
            if event.type == pg.MOUSEWHEEL:
                self.MOUSEWHEEL(event.y)
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pg.mouse.get_pos()
                self.MOUSEBUTTONDOWN(mouse_x, mouse_y)
            if event.type == pg.MOUSEBUTTONUP:
                mouse_x, mouse_y = pg.mouse.get_pos()
                self.MOUSEBUTTONUP(mouse_x, mouse_y)
            if event.type == pg.MOUSEMOTION:
                mouse_x, mouse_y = pg.mouse.get_pos()
                self.MOUSEMOTION(mouse_x, mouse_y)

    def update_data(self):
        # whatever needs to changed (used for animation or special effects)
        pass

    def draw(self):
        # whatever needs to drawn happens here
        pass

    # execute_cycle is typically called from the main loop
    # execute_cycle can be called from 'background' routine like an AI-learning cycle
    # we can then play the game while the AI learns in the background
    def execute_cycle(self):
        self.last_cycle = t.time()
        self.handle_events()
        self.update_data()
        self.draw()
        return self.keep_running

    def execute(self):
        while self.execute_cycle():
            pg.display.update()
            self.clock.tick(FRAME_RATE)

    def execute_from_background(self):
        elapsed_time = t.time() - self.last_cycle
        if elapsed_time * FRAME_RATE > 1:
            self.execute_cycle()


class GameArea(EvtObj):
    def __init__(self, game, r):
        EvtObj.__init__(self)
        self.game, self.rect = game, r
    def draw(self): pass
class chess_game_area(GameArea):
    def __init__(self, game, r):
        GameArea.__init__(self, game, r)
    def draw(self): pass

class chess_history_area(GameArea):
    def __init__(self, game, r):
        GameArea.__init__(self, game, r)
    def draw(self): pass

class chess_player_area(GameArea):
    def __init__(self, game, r):
        GameArea.__init__(self, game, r)
    def draw(self): pass

class chess_control_area(GameArea):
    def __init__(self, game, r):
        GameArea.__init__(self, game, r)
    def draw(self): pass
class ChessGame(Game):
    def __init__(self, window, clock):
        Game.__init__(self, window, clock)
        self.game_area = chess_game_area(self,GAME_RECT)
        self.history_area = chess_history_area(self,HIST_RECT)
        self.player_area = chess_player_area(self,PLAYER_RECT)
        self.control_area = chess_control_area(self,CONTROL_RECT)
        self.chess_board = ChessBoard()

    def update_data(self):
        # whatever needs to change (animation,...)
        pass

    def clear_window(self):
        self.win.set_clip((0, 0, WINDOW_WIDTH, WINDOW_HEIGHT))
        self.win.fill(GAME_BG_COLOR)

    def draw(self):
        self.clear_window()
        self.game_area.draw()
        self.history_area.draw()
        self.player_area.draw()
        self.control_area.draw()



