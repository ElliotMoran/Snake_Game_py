import pygame
import settings
from food import Food


class Snake:
    def __init__(self):
        self.snake_head_pos = [100, 500]
        self.snake_pos = [[100, 500],  # first position is head
                            [90, 500], [80, 500]]

        self.color = settings.GREEN
        self.direction = "RIGHT"
        self.change_to = self.direction

        self.speed = 15

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
        if self.snake_head_pos[0] < 1 or self.snake_head_pos[0] > settings.width - 15:
            # off-screen
            return False
        if self.snake_head_pos[1] < 1 or self.snake_head_pos[1] > settings.height - 15:
            # off-screen
            return False

        for pos in self.snake_pos[1:]:
            if self.snake_head_pos[0] == pos[0] and self.snake_head_pos[1] == pos[1]:
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

        self.change_direction()

        if self.direction == "UP":
            self.snake_head_pos[1] -= self.speed
        elif self.direction == "DOWN":
            self.snake_head_pos[1] += self.speed
        elif self.direction == "RIGHT":
            self.snake_head_pos[0] += self.speed
        elif self.direction == "LEFT":
            self.snake_head_pos[0] -= self.speed

    def movement(self, food: Food):
        self.move()
        self.snake_pos.insert(0, list(self.snake_head_pos))


        # eat apple
        food_was_eaten = False
        for x in range(15):
            if self.snake_head_pos[0] + x <= food.get_pos()[0] + 20 and self.snake_head_pos[0] + x >= food.get_pos()[0]:
                for y in range(15):
                    if self.snake_head_pos[1] + y <= food.get_pos()[1] + 20 and self.snake_head_pos[1] + y >= food.get_pos()[1]:
                        food.make_new()
                        food_was_eaten = True
                        break
        if not food_was_eaten:
            self.snake_pos.pop()
        # else:
        #     self.snake_pos.insert(0, list(self.snake_head_pos))

    def draw(self, screen):
        for pos in self.snake_pos:
            pygame.draw.rect(screen, self.color, (pos[0], pos[1], 15, 15))
