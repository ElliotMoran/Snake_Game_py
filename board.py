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
        self.board[1][1] = 1

        self.left = 10
        self.top = 10

    # changes padding and cell size
    def set_view(self, left, top, cell_size=-1):
        self.left = left
        self.top = top
        if cell_size != -1:
            self.cell_size = cell_size

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
                                                              