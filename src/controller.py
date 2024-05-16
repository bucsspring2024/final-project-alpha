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
        '''
        Arg: self
        Changes game state to "game" and calls the Initialize class
        Return: None
        '''
        self.state = "game" 
        self.game = Initialize(self.screen) 
        
    def quit_game(self):
        '''
        Arg: self
        Sets self.running to False
        Return: None
        '''
        self.running = False  
        
    def update_button_text(self, new_label, new_action):
        '''
        Arg: self, new_label (str), new_action (function)
        Replaces the button with the new_label that performs the function of new_action
        Return: None
        '''
        self.start_button.set_title(new_label)
        self.start_button.update_callback(new_action)
        
    def mainloop(self):
        '''
        Arg: self
        Calls on loop functions based on what the game state is
        Return: None
        '''
        while self.running:
            if self.state == "menu":
                self.menuloop()
            elif self.state == "game":
                self.gameloop()  
    
    def menuloop(self):
        '''
        Arg: self
        Initiates the menu when game state is in menu and either quits the program or draws the menu
        Return: None
        '''
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False  # Exit the entire program
            #event loop
        if self.menu.is_enabled():
            self.menu.update(events)
            self.menu.draw(self.screen)
        #redraw
        pygame.display.update()    
      
    def gameloop(self):
        '''
        Arg: self
        Controls the various sub game states and intiates events based on the states.
        The gameloop can quit the game, update events, trigger different handle events, or
        changes the game state back to menu.
        Return: None
        '''
        game_running = True
        while self.running and game_running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
            #update data
            if self.game.state == "game":
                self.game.update(events)
                self.game.handle_events(events)
            if self.game.state == "special_ui":  
                self.game.game.special_handle_events(events)
                self.game.state = "game"
            if self.game.state == "remenu":
                self.state = "menu"
                game_running = False
                self.game.update(events)
                self.setup_game_over_menu()
        #redraw
        pygame.display.flip() 
            
    def setup_game_over_menu(self):
        '''
        Arg: self
        Redraws the menu and replaces the button to play again and adds the label of turns taken
        Return: None
        '''
        self.menu = pygame_menu.Menu('Game Over', self.x/2, self.y/2, theme=pygame_menu.themes.THEME_BLUE)
        self.menu.add.label(f"Turns Taken: {self.game.game.turn_count}", max_char=-1, font_size=24)
        self.start_button = self.menu.add.button("Play", self.start_game)
        self.quit_button = self.menu.add.button("Quit", self.quit_game)
        self.update_button_text("Play Again", self.start_game)


