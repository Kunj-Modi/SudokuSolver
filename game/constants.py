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
ROWS_FILLED = [[], [], [], [], [], [], [], [], []]
COLUMNS_FILLED = [[], [], [], [], [], [], [], [], []]
SQUARES_FILLED = [[], [], [], [], [], [], [], [], []]
ROWS_QUES = [[], [], [], [], [], [], [], [], []]
COLUMNS_QUES = [[], [], [], [], [], [], [], [], []]
SQUARES_QUES = [[], [], [], [], [], [], [], [], []]
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
QUESTION_COLOR = "#c0e8ec"
SELECTED_QUES_COLOR = "#fff4c0"
SEL_QUES_RCS_COLOR = "#f6cfff"
SC_BUTTON_COLLOR = "#ffc0c6"
DOUN_BUTTON_COLOR = "#ffc0c6"
TEXT_COLOR = "#4200ff"
QUES_FONT_COLOR = "black"
WRONG_FONT_COLOR = "#ff3300"
NUM_FONT = pygame.font.Font(None, 60)
TEXT_FONT = pygame.font.Font(None, 50)
