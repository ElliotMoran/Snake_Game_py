#! pypy3
import pygame
import settings
from snake import Snake
from food import Food


class Game:
    def __init__(self):
        self.snake = None
        self.food = None
        self.clock = None
        self.screen = None

        self.background_image = None

    # pygame and other object inizialization
    def inizialization(self) -> None:
        # pygame inizialization
        pygame.init()
        pygame.display.set_caption(settings.caption)

        # other objects inizialization
        self.screen = pygame.display.set_mode(
            (settings.width, settings.height))
        self.snake = Snake()
        self.food = Food()
        self.clock = pygame.time.Clock()
        self.background_image = pygame.image.load(
            'data/background.png').convert()

    # draw sprites and bg
    def draw_game_objects(self) -> None:
        self.screen.blit(self.background_image, (0, 0))
        self.snake.draw(self.screen)
        self.food.draw(self.screen)

    # game loop
    def main_loop(self) -> None:
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        exit()

            self.snake.movement(self.food)

            self.draw_game_objects()

            if not self.snake.check_collision():
                running = False
                print(self.snake.score)

            pygame.display.flip()
            self.clock.tick(settings.fps)


if __name__ == '__main__':
    game = Game()
    game.inizialization()
    game.main_loop()
