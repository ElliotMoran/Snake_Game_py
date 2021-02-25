import pygame
import random
import settings


class Food:
    def __init__(self):
        self.x, self.y = None, None
        self.color = settings.RED

        self.image = pygame.image.load('data/Apple.png').convert()
        self.image.set_colorkey(settings.BLACK)

        self.make_new([[90, 500], [75, 500], [60, 500]])  # first snake pos

    def get_pos(self) -> tuple:
        return self.x, self.y

    def draw(self, screen) -> None:
        screen.blit(self.image, (self.x, self.y))

    def make_new(self, snake_pos: list) -> None:
        # apple cannot appear on a snake
        self.x, self.y = random.randrange(
            0, settings.width, 15), random.randrange(0, settings.height, 15)

        while True:
            flag = True
            for pos in snake_pos:
                if self.x <= pos[0] + 15 and self.x >= pos[0] - 15:
                    if self.y <= pos[1] + 15 and self.y >= pos[1] - 15:
                        flag = False
            if flag:
                break
            self.x, self.y = random.randrange(
                0, settings.width, 15), random.randrange(0, settings.height, 15)
