import pygame

pygame.init()

BLANK_INT_BOARD = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0]]
FINAL_BOARD = []
UNDO_V = False
REDO_V = False
UNDO = []
REDO = []
CLEAR = False
SOLVE = False

BACKGROUND_COLOR = (64, 64, 64)
CELL_COLOR = "#c0e8ec"
TEXT_COLOR = (64, 64, 64)
NUM_FONT = pygame.font.Font(None, 60)
TEXT_FONT = pygame.font.Font(None, 50)
