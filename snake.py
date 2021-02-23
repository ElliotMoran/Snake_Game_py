import pygame
import settings
from food import Food


class Snake:
    def __init__(self):
        self.snake_head_pos = [100, 500]
        self.snake_pos = [[100, 500],  # first position is head
                          [85, 500], [70, 500]]

        self.color = settings.GREEN
        self.direction = "RIGHT"
        self.change_to = self.direction

        self.speed = 15

        self.image_snake_head_up = pygame.image.load(
            'data/Snake_head.png').convert()
        self.image_snake_head_up.set_colorkey(settings.BLACK)
        self.image_snake_head_down = pygame.transform.rotate(
            self.image_snake_head_up, 180)
        self.image_snake_head_right = pygame.transform.rotate(
            self.image_snake_head_up, 270)
        self.image_snake_head_left = pygame.transform.rotate(
            self.image_snake_head_up, 90)

        self.image_snake_body_up = pygame.image.load(
            'data/Snake_body.png').convert()
        self.image_snake_body_up.set_colorkey(settings.BLACK)
        self.image_snake_body_right = pygame.transform.rotate(
            self.image_snake_body_up, 270)
        self.image_snake_body_left = pygame.transform.rotate(
            self.image_snake_body_up, 90)
        self.image_snake_body_down = pygame.transform.rotate(
            self.image_snake_body_up, 180)

        self.image_snake_tail_up = pygame.image.load(
            'data/Snake_tail.png').convert()
        self.image_snake_tail_up.set_colorkey(settings.BLACK)
        self.image_snake_tail_right = pygame.transform.rotate(
            self.image_snake_tail_up, 270)
        self.image_snake_tail_left = pygame.transform.rotate(
            self.image_snake_tail_up, 90)
        self.image_snake_tail_down = pygame.transform.rotate(
            self.image_snake_tail_up, 180)
        self.tail_direction = "RIGHT"

    def change_direction(self) -> None:
        # checking whether it is possible to change the direction of the snake
        if any((self.change_to == "RIGHT" and not self.direction == "LEFT",
                self.change_to == "LEFT" and not self.direction == "RIGHT",
                self.change_to == "UP" and not self.direction == "DOWN",
                self.change_to == "DOWN" and not self.direction == "UP")):
            # change direction
            self.direction = self.change_to

    def change_tail_direction(self) -> None:
        pos_tail = self.snake_pos[-1]
        pos_pre_tail = self.snake_pos[-2]

        if pos_tail[0] < pos_pre_tail[0]:
            self.tail_direction = "RIGHT"
        if pos_tail[0] > pos_pre_tail[0]:
            self.tail_direction = "LEFT"
        if pos_tail[1] < pos_pre_tail[1]:
            self.tail_direction = "DOWN"
        if pos_tail[1] > pos_pre_tail[1]:
            self.tail_direction = "UP"

    # collision and off-screen check
    def check_collision(self) -> bool:
        # off-sceen check
        if self.snake_head_pos[0] <= 1 or self.snake_head_pos[0] > settings.width - 15:
            # off-screen
            return False
        if self.snake_head_pos[1] <= 1 or self.snake_head_pos[1] > settings.height - 15:
            # off-screen
            return False

        for pos in self.snake_pos[1:]:
            if self.snake_head_pos[0] == pos[0] and self.snake_head_pos[1] == pos[1]:
                return False

        return True

    def move(self) -> None:
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

    def movement(self, food: Food) -> None:
        self.move()
        self.snake_pos.insert(0, list(self.snake_head_pos))

        # eat apple
        food_was_eaten = False
        for x in range(15):
            if self.snake_head_pos[0] + x <= food.get_pos()[0] + 20 and self.snake_head_pos[0] + x >= food.get_pos()[0]:
                for y in range(15):
                    if self.snake_head_pos[1] + y <= food.get_pos()[1] + 20 and self.snake_head_pos[1] + y >= food.get_pos()[1]:
                        food.make_new(self.snake_pos)
                        food_was_eaten = True
                        break

        if not food_was_eaten:
            self.snake_pos.pop()

    def draw(self, screen: pygame.display) -> None:
        self.change_tail_direction()
        for i in range(len(self.snake_pos)):
            pos = self.snake_pos[i]
            # draw snake head
            if i == 0:
                # change head rotation
                if self.direction == "UP":
                    image_snake_head = self.image_snake_head_up
                elif self.direction == "DOWN":
                    image_snake_head = self.image_snake_head_down
                elif self.direction == "RIGHT":
                    image_snake_head = self.image_snake_head_right
                elif self.direction == "LEFT":
                    image_snake_head = self.image_snake_head_left

                screen.blit(image_snake_head, (pos[0], pos[1]))

            elif i == len(self.snake_pos) - 1:
                # draw snake tail
                if self.tail_direction == "UP":
                    image_snake_tail = self.image_snake_tail_up
                elif self.tail_direction == "DOWN":
                    image_snake_tail = self.image_snake_tail_down
                elif self.tail_direction == "RIGHT":
                    image_snake_tail = self.image_snake_tail_right
                elif self.tail_direction == "LEFT":
                    image_snake_tail = self.image_snake_tail_left

                screen.blit(image_snake_tail, (pos[0], pos[1]))

            else:
                # draw snake body
                pos = self.snake_pos[i]
                pos_pre = self.snake_pos[i - 1]
                if pos[0] < pos_pre[0]:
                    direction = "RIGHT"
                if pos[0] > pos_pre[0]:
                    direction = "LEFT"
                if pos[1] < pos_pre[1]:
                    direction = "DOWN"
                if pos[1] > pos_pre[1]:
                    direction = "UP"

                if direction == "UP":
                    image_snake_body = self.image_snake_body_up
                elif direction == "DOWN":
                    image_snake_body = self.image_snake_body_down
                elif direction == "RIGHT":
                    image_snake_body = self.image_snake_body_right
                elif direction == "LEFT":
                    image_snake_body = self.image_snake_body_left

                screen.blit(image_snake_body, (pos[0], pos[1]))
