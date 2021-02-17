import pygame

# delta move notation:
#       1 - up
#       2 - down
#       3 - left
#       4 - right


class Player:
    def __init__(self, board_x, board_y):
        # snake part coords
        self.snake_part_coords = [[board_x, board_y]]

        self.delta_move = 1

    def get_head_pos(self):
        return self.snake_part_coords[0][0], self.snake_part_coords[0][1]

    def move(self):
        for j in range(len(self.snake_part_coords)):
            # up
            if self.delta_move == 1:
                self.snake_part_coords[j][1] -= 1

            # down
            elif self.delta_move == 2:
                self.snake_part_coords[j][1] += 1

            # left
            elif self.delta_move == 3:
                self.snake_part_coords[j][0] -= 1

            # right
            elif self.delta_move == 4:
                self.snake_part_coords[j][0] += 1

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.delta_move = 1
        elif keys[pygame.K_DOWN]:
            self.delta_move = 2
        elif keys[pygame.K_LEFT]:
            self.delta_move = 3
        elif keys[pygame.K_RIGHT]:
            self.delta_move = 4

        self.move()
        


    def eat_apple(self):
        pass


    
