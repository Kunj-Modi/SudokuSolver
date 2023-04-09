from objects import *

pygame.init()
mouse_down = False

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

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_down = True
        else:
            mouse_down = False

    clear.update(mouse_down)
    solve.update(mouse_down)
    undo.update(mouse_down)
    redo.update(mouse_down)
    board.update(mouse_down)

    pygame.display.update()
    clock.tick(60)
