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
        self.font = pygame.font.Font(None, 36) 
            
    def choice_one(self):
        pygame.draw.rect(self.screen, "blue", self.box_one)
        pygame.draw.rect(self.screen, "red", self.box_two)
        #Box 1 Text
        text_surface_one = self.font.render("Career", True, "white")
        text_x_one = self.box_one.x + (self.box_one.width - text_surface_one.get_width()) // 2
        text_y_one = self.box_one.y + (self.box_one.height - text_surface_one.get_height()) // 2
        self.screen.blit(text_surface_one, (text_x_one, text_y_one))
        #Box 2 Text
        text_surface_two = self.font.render("College", True, "white")
        text_x_two = self.box_two.x + (self.box_two.width - text_surface_two.get_width()) // 2
        text_y_two = self.box_two.y + (self.box_two.height - text_surface_two.get_height()) // 2
        self.screen.blit(text_surface_two, (text_x_two, text_y_two))
        
    def update(self, events):
        self.screen.fill("green")  
        self.choice_one()
        self.handle_events(events)
        pygame.display.flip()

    def perform_action_one(self):
        self.count += 5
        # Implement the action for clicking Box One

    def perform_action_two(self):
        self.count += 1
        # Implement the action for clicking Box Two
        
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:  
                if self.box_one.collidepoint(event.pos): 
                    self.perform_action_one()
                elif self.box_two.collidepoint(event.pos): 
                    self.perform_action_two()