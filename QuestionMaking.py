import random


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
    if (i in r_board[c]) or (i in c_board[r]) or (i in s_board[s]):
        return False
    else:
        return True


def select_cells(level):
    pp = 0
    while pp < level:
        x = random.randint(0, 8)
        y = random.randint(0, 8)
        if (x, y) not in selected_cells:
            selected_cells.append((x, y))
            pp += 1


def fill_cells():
    while len(selected_cells) > 0:
        pos = selected_cells[0]
        val = random.randint(1, 9)
        if fits(val, pos):
            board[pos[0]][pos[1]] = val
            selected_cells.pop(0)
            r_board[pos[1]].append(val)
            c_board[pos[0]].append(val)
            s_board[square(pos)].append(val)


board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0]]
r_board = [[], [], [], [], [], [], [], [], []]
c_board = [[], [], [], [], [], [], [], [], []]
s_board = [[], [], [], [], [], [], [], [], []]
selected_cells = []

level = int(input("Enter number of cells you want to be already filled: "))
select_cells(level)
fill_cells()
for i in board:
    print(i)
print()
