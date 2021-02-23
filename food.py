import pygame
import random
import settings


class Food:
    def __init__(self):
        self.x, self.y = random.randint(
            200, settings.width - 20), random.randint(10, settings.height - 20)
        self.color = settings.RED

        self.image = pygame.image.load('data/Apple.png').convert()
        self.image.set_colorkey(settings.BLACK)

    def get_pos(self) -> tuple:
        return self.x, self.y

    def draw(self, screen) -> None:
        screen.blit(self.image, (self.x, self.y))

    def make_new(self, snake_pos: list) -> None:
        # apple cannot appear on a snake
        self.x, self.y = random.randint(
            10, settings.width - 20), random.randint(10, settings.height - 20)

        while True:
            flag = True
            for pos in snake_pos:
                if self.x <= pos[0] + 15 and self.x >= pos[0] - 20:
                    if self.y <= pos[1] + 15 and self.y >= pos[1] - 20:
                        flag = False
            if flag:
                break
            self.x, self.y = random.randint(
                10, settings.width - 20), random.randint(10, settings.height - 20)
