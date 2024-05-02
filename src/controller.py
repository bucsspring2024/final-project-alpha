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
        self.menu = pygame_menu.Menu("Welcome to Roadtrip", self.x/2, self.y/2, theme=pygame_menu.themes.THEME_BLUE)
        self.start_button = self.menu.add.button("Play", self.start_game)
        self.quit_button = self.menu.add.button("Quit", self.quit_game)
        
    
    def start_game(self):
        self.state = "game" 
        self.game = Initialize(self.screen) 
        
    def quit_game(self):
        self.running = False  
        
    def update_button_text(self, new_label, new_action):
        self.start_button.set_title(new_label)
        self.start_button.update_callback(new_action)
        
    def mainloop(self):
      while self.running:
            #print(self.state)
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
            if self.game.state == "game":
                #print("update")
                self.game.update(events)
                self.game.handle_events(events)
                #print(self.game.remenu)
                # if self.game.remenu == True:
                #     #print("works")
                #     self.state = "menu"
                #     self.setup_game_over_menu()
                    #print("Setup game over menu executed")
            if self.game.state == "special_ui":  
                self.game.game.special_handle_events(events)
                self.game.state = "game"
            if self.game.state == "remenu":
                self.state = "menu"
                game_running = False
                #print("state changed to menu")
                self.game.update(events)
                self.setup_game_over_menu()
            

        #redraw
        pygame.display.flip() 
            
    def setup_game_over_menu(self):
        #print("Setting up game over menu"
        #self.game.state = "menu"
        self.menu = pygame_menu.Menu('Game Over', self.x/2, self.y/2, theme=pygame_menu.themes.THEME_BLUE)
        self.menu.add.label(f"Score: {self.game.game.turn_count}", max_char=-1, font_size=24)
        self.start_button = self.menu.add.button("Play", self.start_game)
        self.quit_button = self.menu.add.button("Quit", self.quit_game)
        self.update_button_text("Play Again", self.start_game)
        #self.menu.draw(self.screen)
        #print(f"Current state: {self.state}")

        
#   def gameoverloop(self):
#       #event loop

#       #update data

#       #redraw
