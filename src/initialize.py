import pygame

class Initialize():
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode()
        screen_dim = pygame.display.get_surface()
        self.x = screen_dim.get_width()
        self.y = screen_dim.get_height()
        
    def menu(self):
        self.screen.fill("white")
        pygame.draw.rect(self.screen, "black", (self.x, self.y, 75, 35))
    
    