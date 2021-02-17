import pygame


class Board:
    def __inti__(self, size_x, size_y, cell_size):
        self.size_x = size_x    # number of cells in width
        self.size_y = size_y    # number of cells in height
        self.cell_size = cell_size

        self.left = 10
        self.top = 10

    # changes padding and cell size
    def set_view(self, left, top, cell_size=-1):
        self.left = left
        self.top = top
        if cell_size != -1:
            self.cell_size = cell_size

    def draw(self, screen):
        pass
