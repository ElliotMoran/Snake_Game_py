import pygame
import settings


class Snake:
    def __init__(self):
        self.snake_head_pos = [100, 500]
        self.snake_pos = [self.snake_head_pos,  # first position is head
                          [98, 500], [96, 500], [94, 500], [92, 500], [90, 500], [88, 500], [86, 500], [84, 500], [82, 500], [80, 500]]

        self.color = settings.GREEN
        self.direction = "RIGHT"
        self.change_to = self.direction

    def change_direction(self):
        # checking whether it is possible to change the direction of the snake
        if any((self.change_to == "RIGHT" and not self.direction == "LEFT",
                self.change_to == "LEFT" and not self.direction == "RIGHT",
                self.change_to == "UP" and not self.direction == "DOWN",
                self.change_to == "DOWN" and not self.direction == "UP")):
            # change direction
            self.direction = self.change_to

    # collision and off-screen check
    def check_collision(self) -> bool:
        # off-sceen check
        if self.snake_head_pos[0] < 1 or self.snake_head_pos[0] > settings.width - 10:
            # off-screen
            return False
        if self.snake_head_pos[1] < 1 or self.snake_head_pos[1] > settings.height - 10:
            # off-screen
            return False

        return True

    def move(self):
        # check button pressed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.change_to = "UP"
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.change_to = "DOWN"
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.change_to = "RIGHT"
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.change_to = "LEFT"

    def movement(self):
        self.move()
        self.change_direction()

        if self.direction == "UP":
            self.snake_head_pos[1] -= 2
        elif self.direction == "DOWN":
            self.snake_head_pos[1] += 2
        elif self.direction == "RIGHT":
            self.snake_head_pos[0] += 2
        elif self.direction == "LEFT":
            self.snake_head_pos[0] -= 2

        self.snake_pos.insert(0, list(self.snake_head_pos))
        self.snake_pos.pop()

    def draw(self, screen):
        for pos in self.snake_pos:
            pygame.draw.rect(screen, self.color, (pos[0], pos[1], 10, 10))
