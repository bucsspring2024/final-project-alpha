import pygame
from src.context import Context

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
        self.text_surface_one = self.font.render("Start Driving", True, "white")
        self.text_x_one = self.box_one.x + (self.box_one.width - self.text_surface_one.get_width()) // 2
        self.text_y_one = self.box_one.y + (self.box_one.height - self.text_surface_one.get_height()) // 2
        self.screen.blit(self.text_surface_one, (self.text_x_one, self.text_y_one))
        #Box 2 Text
        self.text_surface_two = self.font.render("Refuel", True, "white")
        self.text_x_two = self.box_two.x + (self.box_two.width - self.text_surface_two.get_width()) // 2
        self.text_y_two = self.box_two.y + (self.box_two.height - self.text_surface_two.get_height()) // 2
        self.screen.blit(self.text_surface_two, (self.text_x_two, self.text_y_two))
        #Instructions
        text_instruct = self.font.render("Choose One", True, "white")
        self.screen.blit(text_instruct, ((self.text_x_one+self.text_x_two)/2, self.y/6))
        
    def choice_two(self): 
        pygame.draw.rect(self.screen, "blue", self.box_one)
        pygame.draw.rect(self.screen, "red", self.box_two)
        #Box 1 Text
        self.text_surface_one = self.font.render("Spare Tire", True, "white")
        self.screen.blit(self.text_surface_one, (self.text_x_one, self.text_y_one))
        #Box 2 Text
        self.text_surface_two = self.font.render("Food", True, "white")
        self.screen.blit(self.text_surface_two, (self.text_x_two, self.text_y_two))
        #Instructions
        text_context = self.font.render("You stop at a gas station", True, "white")
        self.screen.blit(text_context, ((self.text_x_one+self.text_x_two)/2, self.y/10))
        text_instruct = self.font.render("Choose one to buy", True, "white")
        self.screen.blit(text_instruct, ((self.text_x_one+self.text_x_two)/2, self.y/6))
        
        
    def first_update(self, events):
        self.screen.fill("green")
        self.choice_one()
        self.handle_events(events)
        pygame.display.flip()
    
    def second_update(self, events):
        self.screen.fill("green")
        self.choice_two()
        self.handle_events(events)
        pygame.display.flip()
        
    def perform_action_one(self):
        self.count += 5
        # Implement the action for clicking Start Driving

    def perform_action_two(self):
        self.count += 1
        # Implement the action for clicking Refuel
        
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:  
                if self.box_one.collidepoint(event.pos):
                    print("Box One Clicked") #Debug
                    self.perform_action_one()
                elif self.box_two.collidepoint(event.pos): 
                    print("Box Two Clicked") #Debug
                    self.perform_action_two()
                    