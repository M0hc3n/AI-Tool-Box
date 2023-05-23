import pygame
import random
import sys
import time
import math
from pygame.locals import *
import ai
import reversi
import os
from settings import *

pygame.init()


def quit():
    pygame.quit()
    sys.exit()


class Game():
    def __init__(self):
        self.resources = {}

        self.game = reversi.Reversi()
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Sans Serif", 48)
        self.surface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

        self.resources['board'] = pygame.image.load('media/board.png')
        self.resources['black'] = pygame.image.load('media/black.png')
        self.resources['white'] = pygame.image.load('media/white.png')

        pygame.display.set_caption('Reversi')
        self.draw_board()

    def drawText(self, text, font, surface, x, y):
        textobj = font.render(text, 1, (0, 0, 0))
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)

    def display_status(self):
        if self.game.victory == -1:
            self.drawText("Stalemate", self.font, self.surface, 95, 10)
        if self.game.victory == 1:
            self.drawText("Victory to White", self.font, self.surface, 38, 10)
        if self.game.victory == 2:
            self.drawText("Victory to Black", self.font, self.surface, 39, 10)

    def draw_board(self):
        the_board = pygame.Rect(0, 0, WINDOWWIDTH, WINDOWHEIGHT)
        self.surface.blit(self.resources['board'], the_board)

        for x in range(0, 8):
            for y in range(0, 8):
                player = self.game.board[x][y]
                counter = pygame.Rect(x * TILE_SIZE + COUNTER_PADDING, y *
                                      TILE_SIZE + COUNTER_PADDING, COUNTER_SIZE, COUNTER_SIZE)

                if player == 1:
                    self.surface.blit(self.resources['white'], counter)
                elif player == 2:
                    self.surface.blit(self.resources['black'], counter)

        self.display_status()

        pygame.display.update()

    def handle_mouseup(self, event):
        x, y = event.pos
        tx = int(math.floor(x/TILE_SIZE))
        ty = int(math.floor(y/TILE_SIZE))

        try:
            self.game.player_move(tx, ty)
        except reversi.Illegal_move as e:
            print("Illegal move")
        except Exception as e:
            print(e)

    def new_game(self):
        self.game.__init__()

    def start(self):

        while True:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONUP:
                    self.handle_mouseup(event)
                if event.type == pygame.QUIT:
                    quit()

            if self.game.has_changed:
                self.draw_board()
                self.game.has_changed = False

            if self.game.ai_is_ready:
                self.game.ai_move()

            self.clock.tick(FPS)

        quit()
