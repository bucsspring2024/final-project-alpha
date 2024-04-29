import pygame
import pygame_menu
from src.initialize import Initialize

class Controller:
    def __init__(self):
        pygame.init()
        self.screen_x = 1000
        self.screen_y = 800
        self.screen = pygame.display.set_mode((self.screen_x, self.screen_y))
        self.x, self.y = self.screen.get_size()
        self.running = True
        #setup pygame data
        self.state = "menu"
        self.menu = pygame_menu.Menu('Welcome', self.x/2, self.y/2, theme=pygame_menu.themes.THEME_BLUE)
        self.start_button = self.menu.add.button("Play", self.start_game)
        self.quit_button = self.menu.add.button("Quit", self.quit_game)
        
    
    def start_game(self):
        self.state = "game" 
        self.game = Initialize(self.screen) 
        
    def quit_game(self):
        self.running = False  
    
    def restart_game(self):
        self.start_game()  # Reuse start_game to reset everything
        
    def update_button_text(self, new_label, new_action):
        self.start_button.set_title(new_label)
        self.start_button.update_callback(new_action)
        
    def mainloop(self):
      while self.running:
            if self.state == "menu":
                self.menuloop()
            elif self.state == "game":
                self.gameloop()  
    
    def menuloop(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False  # Exit the entire program
            #event loop
        if self.menu.is_enabled():
            #saved list of events from the event loop above
            #update data
            self.menu.update(events)
            self.menu.draw(self.screen)
        #redraw
        pygame.display.update()    
      
    def gameloop(self):
        game_running = True
        while self.running and game_running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
            #update data
            if self.state == "game":
                self.game.update(events)
                game_result = self.game.handle_events(events)
                if game_result == "game_over":
                    self.menu = pygame_menu.Menu('Game Over', self.x/2, self.y/2, theme=pygame_menu.themes.THEME_BLUE)
                    self.menu.add.label(f"Score: {self.game.game.turn_count}", max_char=-1, font_size=24)
                    self.start_button = self.menu.add.button("Play", self.start_game)
                    self.quit_button = self.menu.add.button("Quit", self.quit_game)
                    self.update_button_text("Play Again", self.start_game)
                    self.state = "menu"
                    game_running = False
        #redraw
        pygame.display.flip() 
            
#   def gameoverloop(self):
#       #event loop

#       #update data

#       #redraw
