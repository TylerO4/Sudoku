import pygame
from constants import *
class Cell:
    def __init__(self, value, row, col, width, height, sketched = None):
        self.value = value
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False
        self.sketched = sketched
    def set(self, val):
        self.value = val
    def set_sketched_value(self, value):
        self.sketched = value

    def draw(self, screen):
        chip_font = pygame.font.Font(None, 60)
        #chip_o_surf = chip_font.render(self.value, 0, CIRCLE_COLOR)
        #print("Drawing:", self.sketched, self.value)
        if self.sketched != None and self.value == 0:
            chip_surf = chip_font.render(str(self.sketched), 0, CROSS_COLOR)
            chip_rect = chip_surf.get_rect(
                center=(self.width // 3 + self.width * self.col, self.height // 2.5 + self.height * self.row))
            screen.blit(chip_surf, chip_rect)

        if self.value != 0:

            chip_surf = chip_font.render(str(self.value), 0, CROSS_COLOR)
            chip_rect = chip_surf.get_rect(center=(self.width//2+self.width*self.col, self.height//2+self.height*self.row))
            screen.blit(chip_surf, chip_rect)
