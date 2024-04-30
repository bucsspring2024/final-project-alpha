import pygame
import time

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.count = 0
        self.x = self.screen.get_width()
        self.y = self.screen.get_height()
        self.box_1_1 = pygame.Rect(self.x/10, self.y/4, self.x/3, self.x/3)
        self.box_1_2 = pygame.Rect(6*self.x/10, self.y/4, self.x/3, self.x/3)
        self.box_2_1 = pygame.Rect(self.x/10, self.y/4, self.x/3, self.x/3)
        self.box_2_2 = pygame.Rect(6*self.x/10, self.y/4, self.x/3, self.x/3)
        self.box_3_1 = pygame.Rect(self.x/10, self.y/4, self.x/3, self.x/3)
        self.box_3_2 = pygame.Rect(6*self.x/10, self.y/4, self.x/3, self.x/3)
        self.font = pygame.font.Font(None, 36) 
        self.turn_count = 0
        
            
    def choice_one(self):
        pygame.draw.rect(self.screen, "blue", self.box_1_1)
        pygame.draw.rect(self.screen, "red", self.box_1_2)
        #Box 1 Text
        self.text_surface_one = self.font.render("Start Driving", True, "white")
        self.text_x_one = self.box_1_1.x + (self.box_1_1.width - self.text_surface_one.get_width()) // 2
        self.text_y_one = self.box_1_1.y + (self.box_1_1.height - self.text_surface_one.get_height()) // 2
        self.screen.blit(self.text_surface_one, (self.text_x_one, self.text_y_one))
        #Box 2 Text
        self.text_surface_two = self.font.render("Refuel", True, "white")
        self.text_x_two = self.box_1_2.x + (self.box_1_2.width - self.text_surface_two.get_width()) // 2
        self.text_y_two = self.box_1_2.y + (self.box_1_2.height - self.text_surface_two.get_height()) // 2
        self.screen.blit(self.text_surface_two, (self.text_x_two, self.text_y_two))
        #Instructions
        text_instruct = self.font.render("Choose One", True, "white")
        self.screen.blit(text_instruct, ((self.text_x_one+self.text_x_two)/2, self.y/6))
        
    def choice_two(self): 
        pygame.draw.rect(self.screen, "blue", self.box_2_1)
        pygame.draw.rect(self.screen, "red", self.box_2_2)
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
        
    def choice_three(self): 
        pygame.draw.rect(self.screen, "blue", self.box_3_1)
        pygame.draw.rect(self.screen, "red", self.box_3_2)
        #Box 1 Text
        self.text_surface_one = self.font.render("Rest at the rest area", True, "white")
        self.screen.blit(self.text_surface_one, (self.text_x_one, self.text_y_one))
        #Box 2 Text
        self.text_surface_two = self.font.render("Keep going", True, "white")
        self.screen.blit(self.text_surface_two, (self.text_x_two, self.text_y_two))
        #Instructions
        text_context = self.font.render("There is a rest area coming up", True, "white")
        self.screen.blit(text_context, ((self.text_x_one+self.text_x_two)/2, self.y/10))
        text_instruct = self.font.render("Choose one", True, "white")
        self.screen.blit(text_instruct, ((self.text_x_one+self.text_x_two)/2, self.y/6))
        
    def first_update(self, events):
        self.screen.fill("green")
        self.choice_one()
        self.handle_events(events)
        pygame.display.flip()
    
    def second_update(self, events):
        self.screen.fill("green")
        self.choice_two()
        pygame.display.flip()
        time.sleep(0.5)
        self.handle_events(events)
    
    def third_update(self, events):
        self.screen.fill("green")
        self.choice_three()
        pygame.display.flip()
        time.sleep(0.5)
        self.handle_events(events)
        
    def perform_action_1_1(self):
        self.count += 5
        self.turn_count += 0
        # Clicking Start Driving

    def perform_action_1_2(self):
        self.count += 1
        self.turn_count += 1
        # Clicking Refuel
        
    def perform_action_2_1(self):
        self.count += 5
        self.turn_count += 2
        # Clicking Spare Tire

    def perform_action_2_2(self):
        self.count += 1
        self.turn_count += 1
        # Clicking Food
        
    def perform_action_3_1(self):
        self.count += 0
        self.turn_count += 4
        # Clicking Rest Area

    def perform_action_3_2(self):
        self.count += 50
        self.turn_count += 1
        # Clicking Keep Going
            
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:  
                if self.box_1_1.collidepoint(event.pos):
                    #print("Box One Clicked") #Debug
                    self.perform_action_1_1()
                elif self.box_1_2.collidepoint(event.pos): 
                    #print("Box Two Clicked") #Debug
                    self.perform_action_1_2()
                elif self.box_2_1.collidepoint(event.pos):
                    #print("Box One Clicked") #Debug
                    self.perform_action_2_1()
                elif self.box_2_2.collidepoint(event.pos): 
                    #print("Box Two Clicked") #Debug
                    self.perform_action_2_2()
                elif self.box_3_1.collidepoint(event.pos):
                    #print("Box One Clicked") #Debug
                    self.perform_action_3_1()
                elif self.box_3_2.collidepoint(event.pos): 
                    #print("Box Two Clicked") #Debug
                    self.perform_action_3_2()
                    