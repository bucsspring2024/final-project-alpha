import pygame

class Player:
    
    def __init__(self, x, y):
        self.image = pygame.image.load("load image")
        self.x_cor = x
        self.y_cor = y
        self.shape = pygame.draw.circle("add circle")
        
        
    def update(self):
        self.x_cor += die_roll * value_for_one_box
        self.y_cor += die_roll * value_for_one_box
        