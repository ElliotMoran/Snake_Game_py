import pygame
import random
import settings


class Food:
    def __init__(self):
        self.x, self.y = random.randint(
            10, settings.width - 20), random.randint(10, settings.height - 20)
        self.color = settings.RED

        self.image = pygame.image.load('data/Apple.png').convert()
        self.image.set_colorkey(settings.BLACK)
        
        
    def get_pos(self):
        return self.x, self.y

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def make_new(self):
        self.x, self.y = random.randint(
            10, settings.width - 20), random.randint(10, settings.height - 20)
