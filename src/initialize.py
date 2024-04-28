import pygame
import pygame_menu
import random
from src.game import Game
from src.context import Context

class Initialize():
    
    def __init__(self, screen):
        pygame.init()
        self.screen = screen
        self.x = self.screen.get_width()
        self.y = self.screen.get_height()
        self.start_pos = (5, 5*self.y/8)
        self.player = pygame.Rect((self.start_pos), (25, 25))
        self.font = pygame.font.Font(None, 36)
        self.radius = 85
        self.circle_center = (self.x/2, 3*self.y/8)
        self.game = Game(self.screen)
        self.context = Context(self.screen)
    
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
        self.screen.blit(text_surface, (self.x - self.radius - 30, 0))
    
    def is_within_circle(self, pos):
        dx = pos[0] - self.circle_center[0]
        dy = pos[1] - self.circle_center[1]
        return dx*dx + dy*dy <= self.radius**2
    
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.is_within_circle(event.pos):
                    roll_num = random.randrange(0, 10)
                    for i in range(roll_num):
                        self.game.count += 1
                        if self.game.count >= self.x-10:
                            return "game_over"
                        return "continue"

    def display_menu(self):
        self.menu = pygame_menu.Menu('Game Over', 400, 100, theme=pygame_menu.themes.THEME_BLUE)
        self.menu.add.label(f"Score: {self.game.count}", max_char=-1, font_size=24)
        self.menu.add.button('Restart', self.restart_game)
        self.menu.add.button('Quit', pygame_menu.events.EXIT)
        self.menu.mainloop(self.screen)
        
    def restart_game(self):
        self.game.count = 0  
        self.state = "game"  
        self.gameloop()
    
    def update(self, events):
        #print("Updating screen...") debug statement
        self.screen.fill("white")
        self.context.display_text()
        if self.context.handle_events(events):
            if self.game.count == 0:  
                self.game.first_update(events) 
            elif self.game.count == 15:
                self.game.second_update(events)
            else:
                self.screen.fill("white")
                pygame.draw.rect(self.screen, "green", self.player)  # Draws the player
                self.draw_wheel()
                self.init_text()
                self.draw_scoreboard()
        pygame.display.flip()
    
