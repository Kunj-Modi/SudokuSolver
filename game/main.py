import pygame
import random
import time

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
BACKGROUND_COLOR = (64, 64, 64)
CELL_COLOR = "#c0e8ec"
TEXT_COLOR = (64, 64, 64)
NUM_FONT = pygame.font.Font(None, 60)
TEXT_FONT = pygame.font.Font(None, 50)
CLEAR = False
SOLVE = False


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
        return self.r, self.c, self.s

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

        def select_cells(lev):
            pp = 0
            while pp < lev:
                x = random.randint(0, 8)
                y = random.randint(0, 8)
                if (x, y) not in self.selected_cells:
                    self.selected_cells.append((x, y))
                    pp += 1

        def fill_cells():
            s = time.time()
            while len(self.selected_cells) > 0:
                e = time.time()
                if e - s > 0.1:
                    start(level)
                    break
                pos = self.selected_cells[0]
                val = random.randint(1, 9)
                if fits(val, pos):
                    self.board[pos[0]][pos[1]] = val
                    self.selected_cells.pop(0)
                    self.r_board[pos[1]].append(val)
                    self.c_board[pos[0]].append(val)
                    self.s_board[square(pos)].append(val)

        def start(lev):
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
            select_cells(lev)
            fill_cells()

        start(level)
        return self.board


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
        self.ln = 157
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


screen = pygame.display.set_mode((599, 665))
screen.fill(BACKGROUND_COLOR)
pygame.display.set_caption("Sudoku")

clock = pygame.time.Clock()

q_board = Question().question(35)
board = Board(q_board)
clear = Clear()
solve = Solve()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    clear.update()
    solve.update()
    board.update()

    pygame.display.update()
    clock.tick(60)
