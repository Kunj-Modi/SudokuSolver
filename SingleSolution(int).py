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


def fits(i, cell):
    (r, c, s) = cell
    if (i in r_board[c]) or (i in c_board[r]) or (i in s_board[s]):
        return False
    else:
        return True


def possible_values(cell):
    l = []
    for i in range(1, 10):
        if fits(i, cell):
            l.append(i)
    return l


def posb_in_pos(i, cell):
    (r, c, s) = cell
    if i not in r_new[c] and i not in c_new[r] and i not in s_new[s]:
        return True
    else:
        return False


def fill_cell(i, cell):
    (r, c, s) = cell
    r_new[c].append(i)
    c_new[r].append(i)
    s_new[s].append(i)


def unfill_cell(cell):
    (r, c, s) = cell
    r_new[c].pop()
    c_new[r].pop()
    s_new[s].pop()


def initialize():
    for r in range(len(board)):
        for c in range(len(board[r])):
            s = square(r, c)
            if board[r][c] == 0:
                empty_cells.append((r, c, s))
            else:
                r_board[c].append(board[r][c])
                c_board[r].append(board[r][c])
                s_board[s].append(board[r][c])

    for cell in empty_cells:
        posb_for_empty[cell] = possible_values(cell)


def start(n):
    if n == len(empty_cells):
        return True
    cell = empty_cells[n]
    for i in posb_for_empty[cell]:
        if posb_in_pos(i, cell):
            fill_cell(i, cell)
            if not start(n + 1):
                unfill_cell(cell)
            else:
                return True
    else:
        return False


def fill_board():
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == 0:
                board[r][c] = c_new[r][0]
                c_new[r].pop(0)


board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
         [6, 0, 0, 1, 9, 5, 0, 0, 0],
         [0, 9, 8, 0, 0, 0, 0, 6, 0],
         [8, 0, 0, 0, 6, 0, 0, 0, 3],
         [4, 0, 0, 8, 0, 3, 0, 0, 1],
         [7, 0, 0, 0, 2, 0, 0, 0, 6],
         [0, 6, 0, 0, 0, 0, 2, 8, 0],
         [0, 0, 0, 4, 1, 9, 0, 0, 5],
         [0, 0, 0, 0, 8, 0, 0, 7, 9]]

r_board = [[], [], [], [], [], [], [], [], []]
c_board = [[], [], [], [], [], [], [], [], []]
s_board = [[], [], [], [], [], [], [], [], []]
empty_cells = []
posb_for_empty = {}
r_new = [[], [], [], [], [], [], [], [], []]
c_new = [[], [], [], [], [], [], [], [], []]
s_new = [[], [], [], [], [], [], [], [], []]

initialize()
start(0)
fill_board()
for i in board:
    print(i)
