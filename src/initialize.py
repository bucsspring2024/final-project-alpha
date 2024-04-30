import pygame
import pygame_menu
import random
from src.game import Game
from src.context import Context
from src.movement import Movement

class Initialize():
    
    def __init__(self, screen):
        pygame.init()
        self.screen = screen
        self.x = self.screen.get_width()
        self.y = self.screen.get_height()
        self.start_pos = (5, 5*self.y/8)
        self.player = Movement(5, 5*self.y/8, 25, 25, self.x)
        self.font = pygame.font.Font(None, 36)
        self.radius = 85
        self.circle_center = (self.x/2, 3*self.y/8)
        self.game = Game(self.screen)
        self.context = Context(self.screen)
        self.old_count = self.game.count
        self.waiting_for_click = False
        self.state = "game"
    
    def init_text(self):
        text_ypos = self.start_pos[1] - 25
        text_start = self.font.render("Start", True, "red")
        text_start_pos = (self.start_pos[0], text_ypos)
        self.screen.blit(text_start, text_start_pos)
        
        text_finish = self.font.render("Finish", True, "Blue")
        text_finish_pos = (self.x - 75, text_ypos)
        self.screen.blit(text_finish, text_finish_pos)
    
    def draw_wheel(self):
        pygame.draw.circle(self.screen, "black", self.circle_center, self.radius, width = 2)
        text_surface = self.font.render("Click here", True, "black")
        text_pos = (self.circle_center[0] - text_surface.get_width() / 2,
                    self.circle_center[1] - text_surface.get_height() / 2)
        self.screen.blit(text_surface, text_pos)
        
    def draw_scoreboard(self):
        text_surface = self.font.render("Score: " + str(self.game.count), True, "black")
        self.screen.blit(text_surface, (self.x - self.radius - 35, 0))
        text_2surface = self.font.render("Turn Count: " + str(self.game.turn_count), True, "black")
        self.screen.blit(text_2surface, (self.x - self.radius - 100, 20))
    
    def is_within_circle(self, pos):
        dx = pos[0] - self.circle_center[0]
        dy = pos[1] - self.circle_center[1]
        return dx*dx + dy*dy <= self.radius**2
    
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.waiting_for_click:
                # If waiting for click and it's a valid click, reset the flag
                    if self.is_within_circle(event.pos):
                        self.waiting_for_click = False
                        print("Click received, continuing count...")
                    continue  # Skip the normal processing when waiting for a click
                
                if self.is_within_circle(event.pos):
                    self.game.turn_count += 1
                    roll_num = random.randrange(0, 20)
                    i = 0
                    while i < roll_num:
                        self.old_count = self.game.count
                        #print(self.game.count) #debug
                        print(f"Before Update: {self.game.count}")
                        self.game.count = round((self.game.count + 1 + self.game.additioner) * self.game.multiplier)
                        print(f"After Update: {self.game.count}")
                        
                        if self.old_count <= 50 <= self.game.count:
                            if not self.waiting_for_click:
                                print("Reached 50, waiting for user click to continue...")
                                self.game.second_update(events)
                                self.state = "special_ui"
                                self.waiting_for_click = True
                                break  # Break out of the while loop to wait for a click
                        elif self.old_count <= 150 <= self.game.count:
                            self.game.third_update(events)
                        elif self.old_count <= 400 <= self.game.count:
                            self.game.fourth_update(events)
                        elif self.game.count >= self.x-10:
                            return "game_over"
                        i += 1
                    return "continue"

    def restart_game(self):
        self.game.count = 0  
        self.state = "game"  
        self.gameloop()
    
    def update(self, events):
        #print("Updating screen...") debug statement
        if self.state == "game":
            self.screen.fill("white")
            self.context.display_text()
            #print(f"Game Count: {self.game.count}, Old Count: {self.old_count}") #debug
            if self.context.handle_events(events):
                if self.game.count == 0:  
                    self.game.first_update(events)
                else:
                    self.screen.fill("white")
                    self.player.move_right(self.game.count) 
                    self.player.draw(self.screen)
                    self.draw_wheel()
                    self.init_text()
                    self.draw_scoreboard()
                self.old_count = self.game.count
        elif self.state == "special_ui":
            pass
        pygame.display.flip()
    
