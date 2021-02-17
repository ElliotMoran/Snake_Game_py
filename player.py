import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, board_x, board_y):
        
        self.snake_part_coords = [[board_x, board_y]]

    def get_head_pos(self):
        return self.snake_part_coords[0][0], self.snake_part_coords[0][1]

    
    
