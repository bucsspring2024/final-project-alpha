import random
import pygame

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.count = 0
        self.x = self.screen.get_width()
        self.y = self.screen.get_height()
        self.box_one = pygame.Rect(self.x/10, self.y/4, self.x/3, self.x/3)
        self.box_two = pygame.Rect(6*self.x/10, self.y/4, self.x/3, self.x/3)
            
    def option_one(self):
        pygame.draw.rect(self.screen, "blue", self.box_one)
        pygame.draw.rect(self.screen, "red", self.box_two)
        
    def update(self):
        self.screen.fill("green")  
        self.option_one()