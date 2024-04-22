import pygame
import random

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
        self.radius = 85
        self.circle_center = (self.x - self.radius + 10, self.radius + 10)
     
    def update(self):
        self.wheel_roll()
        self.screen.fill("white")  # Clear screen 
        pygame.draw.rect(self.screen, "blue", self.player)  # Draw the player
        self.wheel()  # Draw the wheel
        pygame.display.flip()
    
    def wheel(self):
        pygame.draw.circle(self.screen, "black", self.circle_center, self.radius, width = 2)
        text_surface = self.font.render("Click here", True, "black")
        text_pos = (self.circle_center[0] - text_surface.get_width() / 2,
                    self.circle_center[1] - text_surface.get_height() / 2)
        self.screen.blit(text_surface, text_pos)
        
    def wheel_roll(self):
        pass
    
    def is_within_circle(self, pos):
        dx = pos[0] - self.circle_center[0]
        dy = pos[1] - self.circle_center[1]
        return dx*dx + dy*dy <= self.radius**2
    
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.is_within_circle(event.pos):
                    roll_num = random.randrange(0, 10)
                    print(roll_num)
    
    
