import pygame
import settings

# board notation:
#  -1 - snake
#   0 - nothing
#   1 - apple


class Board:
    def __init__(self, size_x, size_y, cell_size):
        self.size_x = size_x    # number of cells in width
        self.size_y = size_y    # number of cells in height
        self.cell_size = cell_size

        self.board = [[0] * self.size_x for _ in range(self.size_y)]
        self.snake = None

        self.left = 10
        self.top = 10

    # changes padding and cell size
    def set_view(self, left, top, cell_size=-1):
        self.left = left
        self.top = top
        if cell_size != -1:
            self.cell_size = cell_size

    def add_snake(self, player):
        self.snake = player

    def update(self):
        for col in range(self.size_y):
            for row in range(self.size_x):
                # change board where snake
                for snake_coords in self.snake.snake_part_coords:
                    if col == snake_coords[1] and row == snake_coords[0]:
                        self.board[col][row] = -1
                    else:
                        self.board[col][row] = 0

    def draw(self, screen):
        for col in range(self.size_y):
            for row in range(self.size_x):
                # draw contour
                pygame.draw.rect(screen, settings.WHITE, (self.left + row * self.cell_size,
                                                          self.top + col * self.cell_size, self.cell_size, self.cell_size), 1)

                color = settings.BLACK
                if self.board[col][row] == 0:
                    # draw nothing
                    pygame.draw.rect(screen, settings.BLACK, (self.left + row * self.cell_size + 1,
                                                              self.top + col * self.cell_size + 1, self.cell_size - 2, self.cell_size - 2))

                elif self.board[col][row] == 1:
                    # draw apple
                    pygame.draw.circle(screen, settings.RED, (self.left + row * self.cell_size + self.cell_size // 2, 
                                                              self.top + col * self.cell_size + self.cell_size // 2), self.cell_size // 2 - 2)

                elif self.board[col][row] == -1:
                    snake_head_x, snake_head_y = self.snake.get_head_pos()
                    if col == snake_head_y and row == snake_head_x:
                        # draw snake head
                        pygame.draw.circle(screen, settings.GREEN, (self.left + row * self.cell_size + self.cell_size // 2, 
                                                              self.top + col * self.cell_size + self.cell_size // 2), self.cell_size // 2 - 2, 1)
                    else:
                        # draw snake bode
                        pygame.draw.circle(screen, settings.GREEN, (self.left + row * self.cell_size + self.cell_size // 2, 
                                                              self.top + col * self.cell_size + self.cell_size // 2), self.cell_size // 2 - 2)
                                                              