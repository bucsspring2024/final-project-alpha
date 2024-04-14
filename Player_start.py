import pygame
from initialize import Initialize

class Player:
    
    def screen_start(self):
        self.screen = pygame.display.set_mode()
        screen_dim = pygame.display.get_surface()
        self.x = screen_dim.get_width()
        self.y = screen_dim.get_height()
        
    def __init__(self):
        self.object = pygame.circle(self.screen, self.y, 15)
    
    # def start_up():
    #     pygame.init()
    #     screen = pygame.display.set_mode()
    #     screen.fill("white")
