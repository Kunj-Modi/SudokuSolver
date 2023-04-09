from objects import *

pygame.init()

screen.fill(BACKGROUND_COLOR)
pygame.display.set_caption("Sudoku")
icon_surf = pygame.image.load("images/sudoku_icon.png")
pygame.display.set_icon(icon_surf)

clock = pygame.time.Clock()

q_board = Question().question(35)
board = Board(q_board)
clear = Clear()
solve = Solve()
undo = UndoButton()
redo = RedoButton()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    clear.update()
    solve.update()
    undo.update()
    redo.update()
    board.update()

    pygame.display.update()
    clock.tick(60)
