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
        self.state = "game"
        self.old_count = self.game.count
        self.waiting_for_click = False
        self.remenu = False
        
        
    def init_text(self):
        text_ypos = self.start_pos[1] - 25
        text_start = self.font.render("Start", True, "red")
        text_start_pos = (self.start_pos[0], text_ypos)
        self.screen.blit(text_start, text_start_pos)
        
        text_finish = self.font.render("Finish", True, "Blue")
        text_finish_pos = (900, text_ypos)
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
        text_4surface = self.font.render("Turn Count: " + str(self.game.turn_count), True, "black")
        self.screen.blit(text_4surface, (self.x - self.radius - 100, 20))
    
    def is_within_circle(self, pos):
        dx = pos[0] - self.circle_center[0]
        dy = pos[1] - self.circle_center[1]
        return dx*dx + dy*dy <= self.radius**2
    
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.is_within_circle(event.pos):
                    self.game.turn_count += 1
                    roll_num = random.randrange(0, 20)
                    i = 0
                    while i < roll_num:
                        #print(self.game.count) #debug
                        #print(f"Before Update: {self.game.count}")
                        self.game.count = self.game.count + 1 
                        #print(f"After Update: {self.game.count}")
                        self.old_count = self.game.count
                        self.waiting_for_click = False
                        #print(self.game.count)
                        if self.old_count == 50:
                            if not self.waiting_for_click:
                                #print("Reached 50, waiting for user click to continue...")
                                self.state = "special_ui"
                                self.game.update_screen(1)
                                self.waiting_for_click = True
                                break  # Break out of the while loop to wait for a click
                        elif self.old_count == 150:
                            if not self.waiting_for_click:
                                #print("Reached 150, waiting for user click to continue...")
                                self.state = "special_ui"
                                self.game.update_screen(2)
                                self.waiting_for_click = True
                                break  # Break out of the while loop to wait for a click
                        elif self.old_count == 300:
                            if not self.waiting_for_click:
                                #print("Reached 500, waiting for user click to continue...")
                                self.state = "special_ui"
                                self.game.update_screen(3)
                                self.waiting_for_click = True
                                break  # Break out of the while loop to wait for a click
                        elif self.old_count == 450:
                            if not self.waiting_for_click:
                                #print("Reached 500, waiting for user click to continue...")
                                self.state = "special_ui"
                                self.game.update_screen(4)
                                self.waiting_for_click = True
                                break  # Break out of the while loop to wait for a click
                        elif self.old_count == 600:
                            if not self.waiting_for_click:
                                #print("Reached 500, waiting for user click to continue...")
                                self.state = "special_ui"
                                self.game.update_screen(5)
                                self.waiting_for_click = True
                                break  # Break out of the while loop to wait for a click
                        elif self.old_count == 750:
                            if not self.waiting_for_click:
                                #print("Reached 500, waiting for user click to continue...")
                                self.state = "special_ui"
                                self.game.update_screen(6)
                                self.waiting_for_click = True
                                break  # Break out of the while loop to wait for a click
                        elif self.old_count == 900:
                            self.state = "remenu"
                            #print("reached remenu")
                        i += 1
    
    def update(self, events):
        #print("Updating screen...") debug statement
        if self.state == "game":
            self.screen.fill("white")
            self.context.display_text()
           
            if self.context.handle_events(events):
                #print(self.game.count)
                if self.game.count == 0:  
                    self.state = "special_ui"
                    self.game.update_screen(0)
                elif self.game.count == 50:
                    self.state = "special_ui"
                    self.game.update_screen(1)
                    self.game.index = 1
                elif self.game.count == 150:
                    self.state = "special_ui"
                    self.game.update_screen(2)
                    self.game.index = 2
                elif self.game.count == 300:
                    self.state = "special_ui"
                    self.game.update_screen(3)
                    self.game.index = 3
                elif self.game.count == 450:
                    self.state = "special_ui"
                    self.game.update_screen(4)
                    self.game.index = 4
                elif self.game.count == 600:
                    self.state = "special_ui"
                    self.game.update_screen(5)
                    self.game.index = 5
                elif self.game.count == 750:
                    self.state = "special_ui"
                    self.game.update_screen(6)
                    self.game.index = 6
                else:
                    self.screen.fill("white")
                    self.player.move_right(self.game.count) 
                    self.player.draw(self.screen)
                    self.draw_wheel()
                    self.init_text()
                    self.draw_scoreboard()
                self.old_count = self.game.count
        elif self.state == "special_ui":
            self.game.special_handle_events(events)
        elif self.state == "remenu":
            #print("this executes")
            pass
        pygame.display.flip()
    
