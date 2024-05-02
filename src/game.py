import pygame
import random

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.count = 0
        self.setup_choices()
        # self.x = self.screen.get_width()
        # self.y = self.screen.get_height()
        # self.rectangles = []
        # self.box_1_1 = pygame.Rect(self.x/10, self.y/4, self.x/3, self.x/3)
        # self.box_1_2 = pygame.Rect(6*self.x/10, self.y/4, self.x/3, self.x/3)
        # self.box_2_1 = pygame.Rect(self.x/10, self.y/4, self.x/3, self.x/3)
        # self.box_2_2 = pygame.Rect(6*self.x/10, self.y/4, self.x/3, self.x/3)
        # self.box_3_1 = pygame.Rect(self.x/10, self.y/4, self.x/3, self.x/3)
        # self.box_3_2 = pygame.Rect(6*self.x/10, self.y/4, self.x/3, self.x/3)
        # self.box_4_1 = pygame.Rect(self.x/10, self.y/4, self.x/3, self.x/3)
        # self.box_4_2 = pygame.Rect(6*self.x/10, self.y/4, self.x/3, self.x/3)
        # self.box_5_1 = pygame.Rect(self.x/10, self.y/4, self.x/3, self.x/3)
        # self.box_5_2 = pygame.Rect(6*self.x/10, self.y/4, self.x/3, self.x/3)
        self.font = pygame.font.Font(None, 36) 
        self.turn_count = 0
        self.multiplier = 1
        self.additioner = 0
        self.click_check = False
        
    def setup_choices(self):
        self.x = self.screen.get_width()
        self.y = self.screen.get_height()
        self.choices = [
            {"text": ("Start Driving", "Refuel"), "color": ("blue", "red")},
            {"text": ("Spare Tire", "Food"), "color": ("blue", "red")},
            {"text": ("Rest at the rest area", "Keep going"), "color": ("blue", "red")},
            {"text": ("Find a detour", "Risk driving through the storm"), "color": ("blue", "red")},
            {"text": ("Retrace your steps", "Follow your gut"), "color": ("blue", "red")}
        ]
        self.rects = [
            (pygame.Rect(self.x/10, self.y/4, self.x/3, self.x/3), pygame.Rect(6*self.x/10, self.y/4, self.x/3, self.x/3))
            for _ in self.choices
        ]
    
    def draw_choice(self, index):
        choice = self.choices[index]
        rects = self.rects[index]
        for i, rect in enumerate(rects):
            pygame.draw.rect(self.screen, choice["color"][i], rect)
            text = self.font.render(choice["text"][i], True, "white")
            text_x = rect.x + (rect.width - text.get_width()) // 2
            text_y = rect.y + (rect.height - text.get_height()) // 2
            self.screen.blit(text, (text_x, text_y))
            
    def update_screen(self, index):
        self.screen.fill("green")
        self.draw_choice(index)
        
    def perform_action(self, index, subindex):
        if index == 0:
            if subindex == 0:
                self.count += 15
            else:
                self.count += 1
            self.turn_count += 1
        elif index == 1:
            self.count += 10
            self.turn_count += 2 if subindex == 0 else 1
        elif index == 2:
            if subindex == 0:
                self.turn_count += 5
                self.multiplier = 1.5
            else:
                self.count += 75
                self.turn_count += 1
        elif index == 3:
            if subindex == 1:
                roll = random.randrange(1, 10)
                if roll > 5:
                    self.count += 50
                    self.multiplier += 0.5
                    self.turn_count += 1
                    self.risk_result("Success")
                else:
                    self.turn_count += 7
                    self.risk_result("Failure")
            else:
                self.count -= 25
                self.turn_count += 1
        elif index == 4:
            if subindex == 0:
                self.turn_count += 5
                self.multiplier = 1.5
            else:
                self.count += 75
                self.turn_count += 1

    def risk_result(self, choice_result):
        self.screen.fill("aqua")
        text_choice_result = self.font.render(f"Risk: {choice_result}", True, "black" if choice_result == "Success" else "red")
        self.screen.blit(text_choice_result, (self.x/2, self.y/2))

    # def choice_one(self):
    #     pygame.draw.rect(self.screen, "blue", self.box_1_1)
    #     pygame.draw.rect(self.screen, "red", self.box_1_2)
    #     #Box 1 Text
    #     self.text_surface_one = self.font.render("Start Driving", True, "white")
    #     self.text_x_one = self.box_1_1.x + (self.box_1_1.width - self.text_surface_one.get_width()) // 2
    #     self.text_y_one = self.box_1_1.y + (self.box_1_1.height - self.text_surface_one.get_height()) // 2
    #     self.screen.blit(self.text_surface_one, (self.text_x_one, self.text_y_one))
    #     #Box 2 Text
    #     self.text_surface_two = self.font.render("Refuel", True, "white")
    #     self.text_x_two = self.box_1_2.x + (self.box_1_2.width - self.text_surface_two.get_width()) // 2
    #     self.text_y_two = self.box_1_2.y + (self.box_1_2.height - self.text_surface_two.get_height()) // 2
    #     self.screen.blit(self.text_surface_two, (self.text_x_two, self.text_y_two))
    #     #Instructions
    #     text_instruct = self.font.render("Choose One", True, "white")
    #     self.screen.blit(text_instruct, ((self.text_x_one+self.text_x_two)/2, self.y/6))
        
    # def choice_two(self): 
    #     pygame.draw.rect(self.screen, "blue", self.box_2_1)
    #     pygame.draw.rect(self.screen, "red", self.box_2_2)
    #     #Box 1 Text
    #     self.text_surface_one = self.font.render("Spare Tire", True, "white")
    #     self.screen.blit(self.text_surface_one, (self.text_x_one, self.text_y_one))
    #     #Box 2 Text
    #     self.text_surface_two = self.font.render("Food", True, "white")
    #     self.screen.blit(self.text_surface_two, (self.text_x_two, self.text_y_two))
    #     #Instructions
    #     text_context = self.font.render("You stop at a gas station", True, "white")
    #     self.screen.blit(text_context, ((self.text_x_one+self.text_x_two)/2, self.y/10))
    #     text_instruct = self.font.render("Choose one to buy", True, "white")
    #     self.screen.blit(text_instruct, ((self.text_x_one+self.text_x_two)/2, self.y/6))
        
    # def choice_three(self): 
    #     pygame.draw.rect(self.screen, "blue", self.box_3_1)
    #     pygame.draw.rect(self.screen, "red", self.box_3_2)
    #     #Box 1 Text
    #     self.text_surface_one = self.font.render("Rest at the rest area", True, "white")
    #     self.screen.blit(self.text_surface_one, (self.text_x_one, self.text_y_one))
    #     #Box 2 Text
    #     self.text_surface_two = self.font.render("Keep going", True, "white")
    #     self.screen.blit(self.text_surface_two, (self.text_x_two, self.text_y_two))
    #     #Instructions
    #     text_context = self.font.render("There is a rest area coming up", True, "white")
    #     self.screen.blit(text_context, ((self.text_x_one+self.text_x_two)/2, self.y/10))
    #     text_instruct = self.font.render("Choose one", True, "white")
    #     self.screen.blit(text_instruct, ((self.text_x_one+self.text_x_two)/2, self.y/6))
        
    # def choice_four(self): 
    #     pygame.draw.rect(self.screen, "blue", self.box_4_1)
    #     pygame.draw.rect(self.screen, "red", self.box_4_2)
    #     #Box 1 Text
    #     self.text_surface_one = self.font.render("Find a detour", True, "white")
    #     self.screen.blit(self.text_surface_one, (self.text_x_one, self.text_y_one))
    #     #Box 2 Text
    #     self.text_surface_two = self.font.render("Risk driving through the storm", True, "white")
    #     self.screen.blit(self.text_surface_two, (self.text_x_two - 45, self.text_y_two))
    #     #Instructions
    #     text_context = self.font.render("There is a storm coming up", True, "white")
    #     self.screen.blit(text_context, ((self.text_x_one+self.text_x_two)/2, self.y/10))
    #     text_instruct = self.font.render("Choose one", True, "white")
    #     self.screen.blit(text_instruct, ((self.text_x_one+self.text_x_two)/2, self.y/6))
    
    # def choice_five(self): 
    #     pygame.draw.rect(self.screen, "blue", self.box_4_1)
    #     pygame.draw.rect(self.screen, "red", self.box_4_2)
    #     #Box 1 Text
    #     self.text_surface_one = self.font.render("Retrace your steps", True, "white")
    #     self.screen.blit(self.text_surface_one, (self.text_x_one, self.text_y_one))
    #     #Box 2 Text
    #     self.text_surface_two = self.font.render("Follow your gut", True, "white")
    #     self.screen.blit(self.text_surface_two, (self.text_x_two - 45, self.text_y_two))
    #     #Instructions
    #     text_context = self.font.render("You are lost", True, "white")
    #     self.screen.blit(text_context, ((self.text_x_one+self.text_x_two)/2, self.y/10))
    #     text_instruct = self.font.render("Choose one", True, "white")
    #     self.screen.blit(text_instruct, ((self.text_x_one+self.text_x_two)/2, self.y/6))
        
    # def first_update(self):
    #     #print(f"Running first_update with count: {self.count}")  # Debug
    #     self.screen.fill("green")
    #     self.choice_one()
    #     #self.special_handle_events(events)
    #     #pygame.display.flip()
    
    # def second_update(self):
    #     #print(f"Running second_update with count: {self.count}")  # Debug
    #     self.screen.fill("green")
    #     self.choice_two()
        
    # def third_update(self):
    #     self.screen.fill("green")
    #     self.choice_three()
    
    # def fourth_update(self):
    #     self.screen.fill("green")
    #     self.choice_four()
    
    # def fifth_update(self):
    #     self.screen.fill("green")
    #     self.choice_five()
        
    # def perform_action_1_1(self):
    #     self.count += 15
    #     self.turn_count += 1
    #     # Clicking Start Driving

    # def perform_action_1_2(self):
    #     self.count += 1
    #     self.turn_count += 1
    #     # Clicking Refuel
        
    # def perform_action_2_1(self):
    #     self.count += 10
    #     self.turn_count += 2
    #     #self.click_check = True
    #     #print (self.count)
    #     #print(self.turn_count)
    #     #print(self.click_check)
    #     # Clicking Spare Tire

    # def perform_action_2_2(self):
    #     self.count += 10
    #     self.turn_count += 1
    #     #self.click_check = True
    #     # Clicking Food
        
    # def perform_action_3_1(self):
    #     self.count += 0
    #     self.turn_count += 5
    #     self.multiplier = 1.5
    #     # Clicking Rest Area

    # def perform_action_3_2(self):
    #     self.count += 75
    #     self.turn_count += 1
    #     # Clicking Keep Going
        
    # def perform_action_4_1(self):
    #     self.count -= 25
    #     self.turn_count += 1
    #     # Clicking Detour
            
    # def perform_action_4_2(self):
    #     roll = random.randrange(1,10)
    #     if roll > 5:
    #         self.count += 50
    #         self.turn_count += 1
    #         self.multiplier += 0.5
    #         choice_result = "Success"
    #     else: 
    #         self.turn_count += 7
    #         choice_result = "Failure"
    #     self.risk_result(choice_result)
    #     # Clicking Drive through storm
        
    # def perform_action_5_1(self):
    #     self.count += 0
    #     self.turn_count += 5
    #     self.multiplier = 1.5
    #     # Clicking Retrace steps

    # def perform_action_5_2(self):
    #     self.count += 75
    #     self.turn_count += 1
    #     # Clicking Follow your guts
        
    # def risk_result(self, choice_result):
    #     if choice_result == "Success":
    #         self.screen.fill("aqua")
    #         text_choice_result = self.font.render("Risk: " + str(self.choice_result), True, "black")
    #     else:
    #         self.screen.fill("aqua")
    #         text_choice_result = self.font.render("Risk: " + str(self.choice_result), True, "red")
    #     self.screen.blit(text_choice_result, (self.x/2, self.y/2))
    
    # def special_handle_events(self, events):
    #     for event in events:
    #         #print(f"Event detected: {event}")
    #         if event.type == pygame.MOUSEBUTTONDOWN:  
    #             #print(f"Mouse button down at {event.pos}")  # Debug statement
    #             if self.box_1_1.collidepoint(event.pos):
    #                 #print("Box One Clicked") #Debug
    #                 self.perform_action_1_1()
    #             elif self.box_1_2.collidepoint(event.pos): 
    #                 #print("Box Two Clicked") #Debug
    #                 self.perform_action_1_2()
    #             elif self.box_2_1.collidepoint(event.pos):
    #                 #print("Box One Clicked") #Debug
    #                 self.perform_action_2_1()
    #             elif self.box_2_2.collidepoint(event.pos): 
    #                 #print("Box Two Clicked") #Debug
    #                 self.perform_action_2_2()
    #             elif self.box_3_1.collidepoint(event.pos):
    #                 #print("Box One Clicked") #Debug
    #                 self.perform_action_3_1()
    #             elif self.box_3_2.collidepoint(event.pos): 
    #                 #print("Box Two Clicked") #Debug
    #                 self.perform_action_3_2()
    #             elif self.box_4_1.collidepoint(event.pos):
    #                 #print("Box One Clicked") #Debug
    #                 self.perform_action_4_1()
    #             elif self.box_4_2.collidepoint(event.pos): 
    #                 #print("Box Two Clicked") #Debug
    #                 self.perform_action_4_2()
                
    def special_handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                for index, (rect1, rect2) in enumerate(self.rects):
                    if rect1.collidepoint(event.pos):
                        self.perform_action(index, 0)
                        break
                    elif rect2.collidepoint(event.pos):
                        self.perform_action(index, 1)
                        break
                    