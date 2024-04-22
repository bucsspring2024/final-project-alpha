import pygame

class Initialize():
    
    def __init__(self, screen):
        pygame.init()
        self.screen = screen
        self.x = self.screen.get_width()
        x_pos = 5
        self.y = self.screen.get_height()
        y_pos = self.y/2
        self.player = pygame.Rect(x_pos, y_pos, 25, 25)
        self.font = pygame.font.Font(None, 36)
     
    def update(self):
        self.wheel_roll()
        self.screen.fill("white")  # Clear screen 
        pygame.draw.rect(self.screen, "blue", self.player)  # Draw the player
        self.wheel()  # Draw the wheel
        pygame.display.flip()
    
    def wheel(self):
        radius = 85
        circle_center = (self.x - radius + 10, radius + 10)
        pygame.draw.circle(self.screen, "black", circle_center, radius, width = 2)
        text_surface = self.font.render("Click here", True, "black")
        self.screen.blit(text_surface, (self.x-(3*radius/2),radius + 10))
        
    def wheel_roll(self):
        pass
    