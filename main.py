#! pypy3
import pygame
import settings
from snake import Snake
from food import Food


# function for the main loop
def main_loop():
    pygame.init()
    pygame.display.set_caption(settings.caption)

    screen = pygame.display.set_mode(
        (settings.width, settings.height))
    clock = pygame.time.Clock()

    snake = Snake()
    food = Food()

    # main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    exit()

        screen.fill(settings.BLACK)

        snake.movement()
        if not snake.check_collision():
            running = False
        snake.draw(screen)
        food.draw(screen)

        pygame.display.flip()
        clock.tick(settings.fps)


if __name__ == '__main__':
    main_loop()
