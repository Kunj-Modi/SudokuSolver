import random
import time
from constants import *

screen = pygame.display.set_mode((599, 665))


class Cell(pygame.sprite.Sprite):
    def __init__(self, row, column, value=None, mutability=True):
        super().__init__()
        self.r = row
        self.c = column
        self.s = self.square()
        self.val = value
        self.mutable = mutability

        self.x = column * 60 + (column + 1) * 5 + ((column // 3) + 1) * (7 - 5)
        self.y = row * 60 + (row + 1) * 5 + ((row // 3) + 1) * (7 - 5)
        self.rect = pygame.rect.Rect(self.x, self.y, 60, 60)

    def square(self):
        if self.r < 3:
            if self.c < 3:
                return 0
            elif 2 < self.c < 6:
                return 1
            elif 5 < self.c < 9:
                return 2
        elif 2 < self.r < 6:
            if self.c < 3:
                return 3
            elif 2 < self.c < 6:
                return 4
            elif 5 < self.c < 9:
                return 5
        elif 5 < self.r < 9:
            if self.c < 3:
                return 6
            elif 2 < self.c < 6:
                return 7
            elif 5 < self.c < 9:
                return 8

    def get_cords(self):
        return self.r, self.c

    def update(self):
        pygame.draw.rect(screen, CELL_COLOR, self.rect, border_radius=3)
        if self.mutable:
            keys = pygame.key.get_pressed()
            mouse = pygame.mouse.get_pressed()
            mouse_pos = pygame.mouse.get_pos()
            if CLEAR or (mouse[0] and self.rect.collidepoint(mouse_pos)):
                if keys[pygame.K_0] or CLEAR:
                    self.val = None
                elif keys[pygame.K_1]:
                    self.val = 1
                elif keys[pygame.K_2]:
                    self.val = 2
                elif keys[pygame.K_3]:
                    self.val = 3
                elif keys[pygame.K_4]:
                    self.val = 4
                elif keys[pygame.K_5]:
                    self.val = 5
                elif keys[pygame.K_6]:
                    self.val = 6
                elif keys[pygame.K_7]:
                    self.val = 7
                elif keys[pygame.K_8]:
                    self.val = 8
                elif keys[pygame.K_9]:
                    self.val = 9
        if SOLVE:
            self.val = FINAL_BOARD[self.r][self.c]
        if self.val:
            val_surface = NUM_FONT.render(f"{self.val}", True, TEXT_COLOR)
            val_rect = val_surface.get_rect()
            val_rect.center = self.rect.center
            screen.blit(val_surface, val_rect)


class Board(pygame.sprite.Sprite):
    def __init__(self, int_board):
        super().__init__()
        self.board = [[], [], [], [], [], [], [], [], []]
        self.rows = [[], [], [], [], [], [], [], [], []]
        self.columns = [[], [], [], [], [], [], [], [], []]
        self.squares = [[], [], [], [], [], [], [], [], []]
        self.int_board = int_board
        self.fill_board()

    def fill_board(self):
        for r in range(9):
            for c in range(9):
                if self.int_board[r][c]:
                    cell = Cell(row=r, column=c, value=self.int_board[r][c], mutability=False)
                    self.board[r].append(cell)
                    self.rows[c].append(cell)
                    self.columns[r].append(cell)
                    self.squares[cell.s].append(cell)
                else:
                    cell = Cell(r, c)
                    self.board[r].append(cell)
                    self.rows[c].append(cell)
                    self.columns[r].append(cell)
                    self.squares[cell.s].append(cell)

    def update(self):
        global CLEAR
        for r in range(9):
            for c in range(9):
                self.board[r][c].update()
        CLEAR = False


class Question:
    def __init__(self):
        self.board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.r_board = [[], [], [], [], [], [], [], [], []]
        self.c_board = [[], [], [], [], [], [], [], [], []]
        self.s_board = [[], [], [], [], [], [], [], [], []]
        self.selected_cells = []

    def question(self, level):
        def square(pos):
            r, c = pos
            if r < 3:
                if c < 3:
                    return 0
                elif 2 < c < 6:
                    return 1
                elif 5 < c < 9:
                    return 2
            elif 2 < r < 6:
                if c < 3:
                    return 3
                elif 2 < c < 6:
                    return 4
                elif 5 < c < 9:
                    return 5
            elif 5 < r < 9:
                if c < 3:
                    return 6
                elif 2 < c < 6:
                    return 7
                elif 5 < c < 9:
                    return 8

        def fits(i, cell):
            (r, c) = cell
            s = square(cell)
            if (i in self.r_board[c]) or (i in self.c_board[r]) or (i in self.s_board[s]):
                return False
            else:
                return True

        def select_random_cells():
            pp = 0
            self.selected_cells.append((0, 0))
            while pp < 17:
                x = random.randint(0, 8)
                y = random.randint(0, 8)
                if (x, y) not in self.selected_cells:
                    self.selected_cells.append((x, y))
                    pp += 1

        def fill_random_cells():
            while len(self.selected_cells) > 0:
                pos = self.selected_cells[0]
                val = random.randint(1, 9)
                if fits(val, pos):
                    self.board[pos[0]][pos[1]] = val
                    self.selected_cells.pop(0)
                    self.r_board[pos[1]].append(val)
                    self.c_board[pos[0]].append(val)
                    self.s_board[square(pos)].append(val)
            if Solution(self.board).unique_solu() == -1:
                start()

        def zero_cell(r, c):
            self.board[r][c] = 0

        def refill_cell(r, c):
            self.board[r][c] = FINAL_BOARD[r][c]

        def start():
            self.board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0]]
            self.r_board = [[], [], [], [], [], [], [], [], []]
            self.c_board = [[], [], [], [], [], [], [], [], []]
            self.s_board = [[], [], [], [], [], [], [], [], []]
            self.selected_cells = []
            select_random_cells()
            fill_random_cells()

        def next_stage(lev):
            pp = 0
            while pp < 81 - lev:
                x = random.randint(0, 8)
                y = random.randint(0, 8)
                if (x, y) not in self.selected_cells:
                    self.selected_cells.append((x, y))
                    zero_cell(x, y)
                    if Solution(self.board).unique_solu():
                        refill_cell(x, y)
                        pp -= 1
                    pp += 1


        start()
        Solution(self.board).find_1st_solu()
        for i in self.board:
            FINAL_BOARD.append(i.copy())
        next_stage(level)

        return self.board


class Solution:
    def __init__(self, board):
        self.board = board
        self.r_board = [[], [], [], [], [], [], [], [], []]
        self.c_board = [[], [], [], [], [], [], [], [], []]
        self.s_board = [[], [], [], [], [], [], [], [], []]
        self.empty_cells = []
        self.posb_for_empty = {}
        self.r_new = [[], [], [], [], [], [], [], [], []]
        self.c_new = [[], [], [], [], [], [], [], [], []]
        self.s_new = [[], [], [], [], [], [], [], [], []]
        self.num = 0
        self.tame = time.time()
        self.initialize()

    def square(self, r, c):
        if r < 3:
            if c < 3:
                return 0
            elif 2 < c < 6:
                return 1
            elif 5 < c < 9:
                return 2
        elif 2 < r < 6:
            if c < 3:
                return 3
            elif 2 < c < 6:
                return 4
            elif 5 < c < 9:
                return 5
        elif 5 < r < 9:
            if c < 3:
                return 6
            elif 2 < c < 6:
                return 7
            elif 5 < c < 9:
                return 8

    def fits(self, i, cell):
        (r, c, s) = cell
        if (i in self.r_board[c]) or (i in self.c_board[r]) or (i in self.s_board[s]):
            return False
        else:
            return True

    def possible_values(self, cell):
        l = []
        for i in range(1, 10):
            if self.fits(i, cell):
                l.append(i)
        return l

    def posb_in_pos(self, i, cell):
        (r, c, s) = cell
        if i not in self.r_new[c] and i not in self.c_new[r] and i not in self.s_new[s]:
            return True
        else:
            return False

    def fill_cell(self, i, cell):
        (r, c, s) = cell
        self.r_new[c].append(i)
        self.c_new[r].append(i)
        self.s_new[s].append(i)

    def unfill_cell(self, cell):
        (r, c, s) = cell
        self.r_new[c].pop()
        self.c_new[r].pop()
        self.s_new[s].pop()

    def initialize(self):
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                s = self.square(r, c)
                if self.board[r][c] == 0:
                    self.empty_cells.append((r, c, s))
                else:
                    self.r_board[c].append(self.board[r][c])
                    self.c_board[r].append(self.board[r][c])
                    self.s_board[s].append(self.board[r][c])

        for cell in self.empty_cells:
            self.posb_for_empty[cell] = self.possible_values(cell)

    def print_board(self):
        t_board = [[], [], [], [], [], [], [], [], []]
        for r in range(len(self.board)):
            j = 0
            for c in range(len(self.board[r])):
                if self.board[r][c] == 0:
                    t_board[r].append(self.c_new[r][j])
                    j += 1
                else:
                    t_board[r].append(self.board[r][c])
        for i in t_board:
            print(i)
        print()

    def fill_board(self):
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                if self.board[r][c] == 0:
                    self.board[r][c] = self.c_new[r][0]
                    self.c_new[r].pop(0)

    def find_1st_solu(self):
        def start(n):
            if n == len(self.empty_cells):
                return True
            cell = self.empty_cells[n]
            for i in self.posb_for_empty[cell]:
                if self.posb_in_pos(i, cell):
                    self.fill_cell(i, cell)
                    if not start(n + 1):
                        self.unfill_cell(cell)
                    else:
                        return True
            else:
                return False

        if not start(0):
            print("No solution!")
            return False
        else:
            self.fill_board()
            return True

    def find_multiple_solu(self):
        def start(n):
            if n == len(self.empty_cells):
                self.print_board()
                return None
            cell = self.empty_cells[n]
            if time.time() - self.tame > 0.1:
                return False
            for i in self.posb_for_empty[cell]:
                if self.posb_in_pos(i, cell):
                    self.fill_cell(i, cell)
                    start(n + 1)
                    self.unfill_cell(cell)
            else:
                return False

        if not start(0):
            print("No solution")

    def unique_solu(self):
        def start(n):
            if n == len(self.empty_cells):
                self.num += 1
                return None
            cell = self.empty_cells[n]
            if self.num > 1:
                return True
            if time.time() - self.tame > 0.1:
                return False
            for i in self.posb_for_empty[cell]:
                if self.num > 1:
                    return True
                if self.posb_in_pos(i, cell):
                    self.fill_cell(i, cell)
                    start(n + 1)
                    self.unfill_cell(cell)
            else:
                return False

        if start(0): return 1
        if self.num == 0:
            return -1
        else:
            return 0


class Clear(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 137
        self.y = 598
        self.h = 60
        self.ln = 157
        self.rect = pygame.rect.Rect(self.x, self.y, self.ln, self.h)
        self.text_surf = TEXT_FONT.render("CLEAR", True, TEXT_COLOR)
        self.text_rect = self.text_surf.get_rect()
        self.text_rect.center = self.rect.center

    def update(self):
        global CLEAR
        pygame.draw.rect(screen, CELL_COLOR, self.rect, border_radius=3)
        screen.blit(self.text_surf, self.text_rect)
        mouse = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        if mouse[0] and self.rect.collidepoint(mouse_pos):
            CLEAR = True


class Solve(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 301
        self.y = 598
        self.h = 60
        self.ln = 159
        self.rect = pygame.rect.Rect(self.x, self.y, self.ln, self.h)
        self.text_surf = TEXT_FONT.render("SOLVE", True, TEXT_COLOR)
        self.text_rect = self.text_surf.get_rect()
        self.text_rect.center = self.rect.center

    def update(self):
        global SOLVE
        pygame.draw.rect(screen, CELL_COLOR, self.rect, border_radius=3)
        screen.blit(self.text_surf, self.text_rect)
        mouse = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        if mouse[0] and self.rect.collidepoint(mouse_pos):
            SOLVE = True


class UndoButton(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 7
        self.y = 598
        self.h = 60
        self.ln = 123
        self.rect = pygame.rect.Rect(self.x, self.y, self.ln, self.h)
        self.text_surf = TEXT_FONT.render("<", True, TEXT_COLOR)
        self.text_rect = self.text_surf.get_rect()
        self.text_rect.center = self.rect.center

    def update(self):
        global UNDO_V
        pygame.draw.rect(screen, CELL_COLOR, self.rect, border_radius=3)
        screen.blit(self.text_surf, self.text_rect)
        mouse = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        if mouse[0] and self.rect.collidepoint(mouse_pos):
            UNDO_V = True


class RedoButton(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 467
        self.y = 598
        self.h = 60
        self.ln = 123
        self.rect = pygame.rect.Rect(self.x, self.y, self.ln, self.h)
        self.text_surf = TEXT_FONT.render(">", True, TEXT_COLOR)
        self.text_rect = self.text_surf.get_rect()
        self.text_rect.center = self.rect.center

    def update(self):
        global REDO_V
        pygame.draw.rect(screen, CELL_COLOR, self.rect, border_radius=3)
        screen.blit(self.text_surf, self.text_rect)
        mouse = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        if mouse[0] and self.rect.collidepoint(mouse_pos):
            REDO_V = True
