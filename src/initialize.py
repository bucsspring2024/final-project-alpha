import pygame

class Initialize():
    
    def __init__(self, screen):
        pygame.init()
        self.screen = screen
        self.x = self.screen.get_width()
        self.y = self.screen.get_height()
        self.player = pygame.draw.rect(self.screen, "black", (self.x/2, self.y/2, 75, 35))
        
    def update(self):
        self.dice_roll()
        self.screen.fill("white")  # Clear screen with white
        pygame.draw.rect(self.screen, (0, 0, 255), self.player)  # Draw the player
        pygame.display.flip()
    
    def dice_roll(self):
        pass
    