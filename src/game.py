import pygame
import settings
from snake import Snake
from food import Food
from menu import Menu


class Game:
    def __init__(self):
        self.snake = None
        self.food = None
        self.clock = None
        self.screen = None
        self.menu = None

        self.background_image = None
        self.background_sound = None
        self.paused = False
        self.fps = settings.fps
        self.font = None
        self.menu = None

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
            'data/background/background.png').convert()
        self.font = pygame.font.SysFont('Arial', 36, True)
        self.menu = Menu()

    # draw sprites and bg
    def draw_game_objects(self) -> None:
        self.screen.blit(self.background_image, (0, 0))
        self.snake.draw(self.screen)
        self.food.draw(self.screen)

    # game loop
    def main_loop(self) -> None:
        in_menu = True
        running = True
        render = self.font.render("PAUSE", 1, settings.RED)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if not in_menu:
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_ESCAPE:
                            self.paused = not self.paused
            if not in_menu:
                if not self.paused:
                    self.snake.movement(self.food)

                    self.draw_game_objects()

                    if not self.snake.check_collision():
                        self.game_over()
                        self.reset()
                else:
                    render_score = self.font.render(
                        f"Your score: {self.snake.score}!", 1, settings.RED)
                    self.screen.blit(render_score, (10, 10))
                    self.screen.blit(render, (435, 250))
            else:
                if self.menu.update(self.screen):
                    in_menu = not in_menu

            pygame.display.flip()
            self.clock.tick(self.fps)

    # game over func
    def game_over(self):
        print(f"Your score: {self.snake.score}!")

    # reset for new game
    def reset(self):
        self.snake = Snake()
        self.food = Food()
