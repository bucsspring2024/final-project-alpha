import pygame
import random

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.count = 0
        self.setup_choices()
        self.font = pygame.font.Font(None, 36) 
        self.turn_count = 0
        self.multiplier = 1
        self.additioner = 0
        self.click_check = False
        self.index = 0
        self.Tire = False
        
    def setup_choices(self):
        self.x = self.screen.get_width()
        self.y = self.screen.get_height()
        self.choices = [
            {"text": ("Start Driving", "Refuel"), "color": ("blue", "red")},
            {"text": ("Spare Tire", "Food"), "color": ("blue", "red")},
            {"text": ("Rest at the rest area", "Keep going"), "color": ("blue", "red")},
            {"text": ("Risk driving through the storm", "Find a detour"), "color": ("blue", "red")},
            {"text": ("Retrace your steps", "Follow your gut"), "color": ("blue", "red")},
            {"text": ("Replace the tire", "Wait for a mechanic"), "color": ("blue", "red")},
            {"text": ("Wait in traffic", "Take another road"), "color": ("blue", "red")}
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
        index = self.index
        #print(index)
        #print(self.index)
        self.screen.fill("green")
        self.draw_choice(index)
        
    def perform_action(self, index, subindex):
        #print(f"This is the {index}")
        if index == 0:
            if subindex == 0:
                self.count += 15
                #Picks Start Driving
            else:
                self.count += 1
                self.additioner += 5
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
                self.turn_count += 5
                self.multiplier += 0.5
                #print(self.multiplier)
                #Picks Rest at Rest Area
            else:
                self.count += 55
                self.turn_count += 1
                #Picks Keep Going
        if index == 3:
            if subindex == 0:
                roll = random.randrange(1, 10)
                #print(roll)
                if roll > 5:
                    self.count += 50
                    self.multiplier += 0.5
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
                self.multiplier += 0.5
                #Picks retrace steps
            else:
                self.count += 75
                self.turn_count += 1
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
                print(roll)
                if roll > 5:
                    self.count += 50
                    self.multiplier += 0.5
                    self.turn_count += 1
                    self.risk_result("Success")
            else:
                    self.count += 1
                    self.turn_count += 7
                    self.risk_result("Failure")
                
    def risk_result(self, choice_result):
        #print("Goes to this screen")
        self.screen.fill("aqua")
        text_choice_result = self.font.render(f"Risk: {choice_result}", True, "black" if choice_result == "Success" else "red")
        self.screen.blit(text_choice_result, (self.x/2, self.y/2))
        if choice_result == "Success":
            text_choice_result_effects = self.font.render("Multiplier + 0.5 and Score + 50", True, "black")
            self.screen.blit(text_choice_result_effects, (self.x/2, self.y/2 + 40))
        else:
            text_choice_result_effects = self.font.render("Turn Count + 7", True, "black")
            self.screen.blit(text_choice_result_effects, (self.x/2, self.y/2 + 40))
        pygame.display.flip()
        pygame.time.wait(1000)
        
    def inventory_tire(self):
        tire_text = self.font.render(f"Tire in inventory: {self.Tire}", True, "black")
        tire_text_x = (self.screen.get_width() - tire_text.get_width()) // 2
        tire_text_y = self.y / 10 - 30
        self.screen.blit(tire_text, (tire_text_x,tire_text_y))
    
    def no_tire(self):
        self.screen.fill("aqua")
        text_tire = self.font.render(f"You do not have a spare tire", True, "black")
        self.screen.blit(text_tire, (self.x/2, self.y/2))
        pygame.display.flip()
        pygame.time.wait(1000)
    
    def special_handle_events(self, events):
        #print(f"Handling events with current rects: {self.rects}")
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, (rect1, rect2) in enumerate(self.rects):
                    if rect1.collidepoint(event.pos):
                        #print(f"Mouse clicked on choice 0 of {index}")
                        self.perform_action(self.index, 0)
                        #print("funky")
                        #print("performed action 1")
                        break
                    elif rect2.collidepoint(event.pos):
                        #print(f"Mouse clicked on choice 0 of {index}")
                        self.perform_action(self.index, 1)
                        #print("pop")
                        #print("performed action 2")
                        break
                    