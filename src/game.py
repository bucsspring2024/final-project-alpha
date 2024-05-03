import pygame
import random

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.count = 0
        self.setup_choices()
        self.font = pygame.font.Font(None, 36) 
        self.turn_count = 0
        self.click_check = False
        self.index = 0
        self.Tire = False
        
    def setup_choices(self):
        '''
        Arg: self
        Defines the lists and variables to be used in other functions.
        Return: None
        '''
        self.x = self.screen.get_width()
        self.y = self.screen.get_height()
        self.choices = [
            {"text": ("Start Driving", "Refuel"), "color": ("blue", "red")},
            {"text": ("Spare Tire", "Food"), "color": ("blue", "red")},
            {"text": ("Rest at the rest area", "Keep going"), "color": ("blue", "red")},
            {"text": ("Risk driving through the storm", "Find a detour"), "color": ("blue", "red")},
            {"text": ("Retrace your steps", "Risk following your gut feeling"), "color": ("blue", "red")},
            {"text": ("Replace the tire", "Wait for a mechanic"), "color": ("blue", "red")},
            {"text": ("Take a gamble and wait in traffic", "Take another road"), "color": ("blue", "red")}
        ]
        self.rects = [
            (pygame.Rect(self.x/10, self.y/4, self.x/3, self.x/3), pygame.Rect(6*self.x/10, self.y/4, self.x/3, self.x/3))
            for _ in self.choices
        ]
        self.choice_context = [
            {"context": "Choose your start"},
            {"context": "You reach a nearby store"},
            {"context": "There is a rest area coming up"},
            {"context": "There is a big storm ahead"},
            {"context": "You are lost"},
            {"context": "You have a flat tire"},
            {"context": "There is an accident on the freeway"}
        ]
    
    def draw_choice(self, index):
        '''
        Arg: self, index
        Chooses the text and context bits from the lists created in setup_choices based on index. This function
        displays the context string in the middle of the screen and draws rectangles on each side of the
        screen with the corresponding text from the list. If index is equal to 5, inventory_tire function is called.
        Return: None
        '''
        choice_context = self.choice_context[index]
        choice = self.choices[index]
        rects = self.rects[index]
        
        context_text = self.font.render(choice_context["context"], True, "black")
        context_text_x = (self.screen.get_width() - context_text.get_width()) // 2
        context_text_y = self.y / 10  
        self.screen.blit(context_text, (context_text_x, context_text_y))
        
        for i, rect in enumerate(rects):
            pygame.draw.rect(self.screen, choice["color"][i], rect)
            text = self.font.render(choice["text"][i], True, "white")
            text_x = rect.x + (rect.width - text.get_width()) // 2
            text_y = rect.y + (rect.height - text.get_height()) // 2
            self.screen.blit(text, (text_x, text_y))
        
        if index == 5:
            self.inventory_tire()
            
            
    def update_screen(self, index):
        '''
        Arg: self, index (int)
        Defines index to be the value of self.index and draws a green screen which then calls 
        on the function, self.draw_choice with parameter index.
        Return: None
        '''
        index = self.index
        self.screen.fill("green")
        self.draw_choice(index)
        
    def perform_action(self, index, subindex):
        '''
        Arg: self, index (int), subindex (int)
        This function checks for entries of index and subindex. Corresponding
        index and subindex integers will perform different results depending on which 
        combination of integers is used.
        Return: None
        '''
        if index == 0:
            if subindex == 0:
                self.count += 15
                #Picks Start Driving
            else:
                self.count += 1
                #Picks Refuel
            self.turn_count += 1
        if index == 1:
            if subindex == 0:
                self.count += 10
                self.turn_count += 2
                self.Tire = True
                #Picks Spare Tire  
            else:
                self.count += 20
                self.turn_count += 1
            #Picks Food
        if index == 2:
            if subindex == 0:
                self.count += 1
                self.turn_count += 25
                #Picks Rest at Rest Area
            else:
                self.count += 55
                self.turn_count += 1
                #Picks Keep Going
        if index == 3:
            if subindex == 0:
                roll = random.randrange(1, 10)
                if roll > 5:
                    self.count += 75
                    self.turn_count += 1
                    self.risk_result("Success")
                else:
                    self.count += 1
                    self.turn_count += 7
                    self.risk_result("Failure")
                #Picks Drive Through Storm
            else:
                self.count += 1
                self.turn_count += 7
                #Picks Detour
        if index == 4:
            if subindex == 0:
                self.count += 1
                self.turn_count += 5
                #Picks retrace steps
            else:
                roll = random.randrange(1, 10)
                if roll > 5:
                    self.count += 75
                    self.turn_count += 1
                    self.risk_result("Success")
                else:
                    self.count += 1
                    self.turn_count += 7
                    self.risk_result("Failure")
                #Picks Follow your gut
        if index == 5:
            #Flattire
            if subindex == 0:
                if self.Tire == True:
                    self.turn_count += 1
                    self.count += 1
                else:
                    self.no_tire()
            else:
                self.turn_count += 5
                self.count += 1
        if index == 6:
            if subindex == 0:
                roll = random.randrange(1, 10)
                if roll > 5:
                    self.count += 75
                    self.turn_count += 1
                    self.risk_result("Success")
                else:
                    self.count += 1
                    self.turn_count += 7
                    self.risk_result("Failure")
                #Wait in traffic
            else:
                self.count += 1
                self.turn_count += 4
                #Take another road
                
    def risk_result(self, choice_result):
        '''
        Arg: self, choice_result(str)
        Fills the screen color with aqua and displays text depending on the argument, choice_result, given.
        If "Success" was given, the screen will dislay Score + 75, but if "Failure" was given,
        Turn Count + 7 will be displayed. 
        Return: None
        '''
        self.screen.fill("aqua")
        text_choice_result = self.font.render(f"Risk: {choice_result}", True, "black" if choice_result == "Success" else "red")
        self.screen.blit(text_choice_result, (self.x/2, self.y/2))
        if choice_result == "Success":
            text_choice_result_effects = self.font.render("Score + 75", True, "black")
            self.screen.blit(text_choice_result_effects, (self.x/2, self.y/2 + 40))
        else:
            text_choice_result_effects = self.font.render("Turn Count + 7", True, "black")
            self.screen.blit(text_choice_result_effects, (self.x/2, self.y/2 + 40))
        pygame.display.flip()
        pygame.time.wait(1000)
        
    def inventory_tire(self):
        '''
        Arg: self
        Displays the text, tire in inventory (False or True) at the x and y coordinates defined in the function
        Return: None
        '''
        tire_text = self.font.render(f"Tire in inventory: {self.Tire}", True, "black")
        tire_text_x = (self.screen.get_width() - tire_text.get_width()) // 2
        tire_text_y = self.y / 10 - 30
        self.screen.blit(tire_text, (tire_text_x,tire_text_y))
    
    def no_tire(self):
        '''
        Arg: self
        Sets the screen color to aqua and displays text in the center of the screen and flips the screen
        Return: None
        '''
        self.screen.fill("aqua")
        text_tire = self.font.render(f"You do not have a spare tire", True, "black")
        self.screen.blit(text_tire, (self.x/2, self.y/2))
        pygame.display.flip()
        pygame.time.wait(1000)
    
    def special_handle_events(self, events):
        '''
        Arg: self, events
        Detects a user click on the screen. If the user clicks on the rectangle on the left, perform_action will execute
        with parameters, self.index and 0. A click on the right rectangle will execute perform_action with self.index and 1.
        Return: None
        '''
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, (rect1, rect2) in enumerate(self.rects):
                    if rect1.collidepoint(event.pos):
                        self.perform_action(self.index, 0)
                        break
                    elif rect2.collidepoint(event.pos):
                        self.perform_action(self.index, 1)
                        break
                    