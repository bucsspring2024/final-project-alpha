import pygame
import random
from src.game import Game

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
        self.turn_count = 0
        self.game = None
    
    def draw_wheel(self):
        pygame.draw.circle(self.screen, "black", self.circle_center, self.radius, width = 2)
        text_surface = self.font.render("Click here", True, "black")
        text_pos = (self.circle_center[0] - text_surface.get_width() / 2,
                    self.circle_center[1] - text_surface.get_height() / 2)
        self.screen.blit(text_surface, text_pos)
    
    def is_within_circle(self, pos):
        dx = pos[0] - self.circle_center[0]
        dy = pos[1] - self.circle_center[1]
        return dx*dx + dy*dy <= self.radius**2
    
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.is_within_circle(event.pos):
                    roll_num = random.randrange(0, 10)
                    self.turn_count += roll_num

    def update(self):
        self.screen.fill("white")
        if self.turn_count in [0, 20, 30]:  
            if not self.game:
                self.game = Game(self.screen)
            self.game.update()  
        else:
            pygame.draw.rect(self.screen, "blue", self.player)  # Draws the player
            self.draw_wheel() 
        pygame.display.flip()
    
