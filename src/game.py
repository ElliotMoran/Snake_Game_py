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
        self.background_sound = None
        self.paused = False
        self.fps = settings.fps

        self.font = None

    # pygame and other object inizialization
    def inizialization(self) -> None:
        # pygame inizialization
        # pygame.mixer.pre_init(44100, 16, 2, 4096)
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
        # self.background_sound = pygame.mixer.Sound(
        #     'data/background/background_music.wav')
        self.font = pygame.font.SysFont('Arial', 36, True)

    # draw sprites and bg
    def draw_game_objects(self) -> None:
        self.screen.blit(self.background_image, (0, 0))
        self.snake.draw(self.screen)
        self.food.draw(self.screen)

    # game loop
    def main_loop(self) -> None:
        running = True
        render = self.font.render("PAUSE", 0, settings.RED)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        self.paused = not self.paused

            if not self.paused:
                # self.background_sound.unpause()
                self.snake.movement(self.food)

                self.draw_game_objects()

                if not self.snake.check_collision():
                    running = False
                    self.game_over()
            else:
                self.screen.blit(render, (435, 250))
                # self.background_sound.pause()

            pygame.display.flip()
            self.clock.tick(self.fps)

    def game_over(self):
        render = self.font.render(
            f"Your score: {self.snake.score}!", 0, settings.RED)
        self.screen.blit(render, (400, 250))
        print(f"Your score: {self.snake.score}!")
