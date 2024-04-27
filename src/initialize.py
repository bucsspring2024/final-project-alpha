import pygame
import pygame_menu
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
        self.circle_center = (self.x/2, 3*self.y/8)
        self.game = Game(self.screen)
    
    def draw_wheel(self):
        pygame.draw.circle(self.screen, "black", self.circle_center, self.radius, width = 2)
        text_surface = self.font.render("Click here", True, "black")
        text_pos = (self.circle_center[0] - text_surface.get_width() / 2,
                    self.circle_center[1] - text_surface.get_height() / 2)
        self.screen.blit(text_surface, text_pos)
        
    def draw_scoreboard(self):
        text_surface = self.font.render("Score: " + str(self.game.count), True, "black")
        self.screen.blit(text_surface, (self.x - self.radius - 25, 0))
    
    def is_within_circle(self, pos):
        dx = pos[0] - self.circle_center[0]
        dy = pos[1] - self.circle_center[1]
        return dx*dx + dy*dy <= self.radius**2
    
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.is_within_circle(event.pos):
                    roll_num = random.randrange(0, 10)
                    self.game.count += roll_num
                    if self.game.count >= 100:
                        return 'game_over'
                    return 'continue'

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
        if self.game.count == 0:  
            self.game.update(events)  
        else:
            pygame.draw.rect(self.screen, "blue", self.player)  # Draws the player
            self.draw_wheel()
        self.draw_scoreboard()
        pygame.display.flip()
    
