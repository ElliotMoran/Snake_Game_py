#! pypy3
import pygame
import settings
from board import Board
from player import Player

# function for the main loop
def main_loop():
    pygame.init()
    pygame.display.set_caption(settings.caption)

    screen = pygame.display.set_mode(
        (settings.width, settings.height), pygame.FULLSCREEN)
    clock = pygame.time.Clock()

    board = Board(9, 9, 50)

    snake = Player(4, 5)
    board.add_snake(snake)

    # main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    exit()

        snake.movement()
        board.update()
        board.draw(screen)

        pygame.display.flip()
        clock.tick(settings.fps)


if __name__ == '__main__':
    main_loop()
