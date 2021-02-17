#! pypy3
import pygame
import settings


def main_loop():
    pygame.init()
    pygame.display.set_caption(settings.caption)

    screen = pygame.display.set_mode(
        (settings.width, settings.height), pygame.FULLSCREEN)
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    exit()

        pygame.display.flip()
        clock.tick(settings.fps)


if __name__ == '__main__':
    main_loop()
