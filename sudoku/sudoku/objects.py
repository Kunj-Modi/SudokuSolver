import random
import time


def square(r, c):
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


FINAL_BOARD = []
SQUARES = {(0, 0): 0, (0, 1): 0, (0, 2): 0, (0, 3): 1, (0, 4): 1, (0, 5): 1, (0, 6): 2, (0, 7): 2, (0, 8): 2, (1, 0): 0, (1, 1): 0, (1, 2): 0, (1, 3): 1, (1, 4): 1, (1, 5): 1, (1, 6): 2, (1, 7): 2, (1, 8): 2, (2, 0): 0, (2, 1): 0, (2, 2): 0, (2, 3): 1, (2, 4): 1, (2, 5): 1, (2, 6): 2, (2, 7): 2, (2, 8): 2, (3, 0): 3, (3, 1): 3, (3, 2): 3, (3, 3): 4, (3, 4): 4, (3, 5): 4, (3, 6): 5, (3, 7): 5, (3, 8): 5, (4, 0): 3, (4, 1): 3, (4, 2): 3, (4, 3): 4, (4, 4): 4, (4, 5): 4, (4, 6): 5, (4, 7): 5, (4, 8): 5, (5, 0): 3, (5, 1): 3, (5, 2): 3, (5, 3): 4, (5, 4): 4, (5, 5): 4, (5, 6): 5, (5, 7): 5, (5, 8): 5, (6, 0): 6, (6, 1): 6, (6, 2): 6, (6, 3): 7, (6, 4): 7, (6, 5): 7, (6, 6): 8, (6, 7): 8, (6, 8): 8, (7, 0): 6, (7, 1): 6, (7, 2): 6, (7, 3): 7, (7, 4): 7, (7, 5): 7, (7, 6): 8, (7, 7): 8, (7, 8): 8, (8, 0): 6, (8, 1): 6, (8, 2): 6, (8, 3): 7, (8, 4): 7, (8, 5): 7, (8, 6): 8, (8, 7): 8, (8, 8): 8}


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
        def fits(i, cell):
            (r, c) = cell
            s = square(r, c)
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
                    r, c = pos
                    self.board[pos[0]][pos[1]] = val
                    self.selected_cells.pop(0)
                    self.r_board[pos[1]].append(val)
                    self.c_board[pos[0]].append(val)
                    self.s_board[square(r, c)].append(val)
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
                s = square(r, c)
                if self.board[r][c] == 0:
                    self.empty_cells.append((r, c, s))
                else:
                    self.r_board[c].append(self.board[r][c])
                    self.c_board[r].append(self.board[r][c])
                    self.s_board[s].append(self.board[r][c])

        for cell in self.empty_cells:
            self.posb_for_empty[cell] = self.possible_values(cell)

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
