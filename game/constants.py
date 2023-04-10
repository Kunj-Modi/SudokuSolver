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
SELECTED_CELL = (0, 0)
UNDO_V = False
REDO_V = False
UNDO = []
REDO = []
CLEAR = False
SOLVE = False

MOUSE_DOWN = False
MOUSE_POS = (0, 0)
KEY_PRESSED = 0

BACKGROUND_COLOR = "black"
CELL_COLOR = "#c0e8ec"
SELECTED_CELL_COLOR = "white"
SEL_CELL_RCS_COLOR = "#f6cfff"
QUESTION_COLOR = "pink"
SELECTED_QUES_COLOR = "#fff4c0"
SEL_QUES_RCS_COLOR = "#f6cfff"
SC_BUTTON_COLLOR = "#fff4c0"
DOUN_BUTTON_COLOR = "#fff8c0"
TEXT_COLOR = (64, 64, 64)
QUES_FONT_COLOR = "black"
NUM_FONT = pygame.font.Font(None, 60)
TEXT_FONT = pygame.font.Font(None, 50)
