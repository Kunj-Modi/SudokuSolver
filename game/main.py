from objects import *

pygame.init()

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
