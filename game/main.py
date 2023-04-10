from objects import *

pygame.init()
mouse_down = False
mouse_pos = (0, 0)
key = 0

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

print(pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_down = True
            mouse_pos = pygame.mouse.get_pos()

        if event.type == pygame.KEYDOWN:
            key = event.key

    updateConstants(mouse_down, mouse_pos, key)

    clear.update()
    solve.update()
    undo.update()
    redo.update()
    board.update()

    pygame.display.update()
    mouse_down = False
    mouse_pos = (0, 0)
    key = 0
    clock.tick(60)
