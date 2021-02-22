import pygame
import random
import settings


class Food:
    def __init__(self):
        self.x, self.y = random.randint(
            10, settings.width - 10), random.randint(10, settings.height - 10)
        self.color = settings.RED

    def get_pos(self):
        return self.x, self.y

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, 10, 10))

    def make_new(self):
        self.x, self.y = random.randint(
            10, settings.width - 10), random.randint(10, settings.height - 10)
