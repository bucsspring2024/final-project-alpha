import pygame
import pygame_menu
from src.initialize import Initialize

class Controller:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.x, self.y = self.screen.get_size()
        self.running = True
        #setup pygame data
        self.state = "menu"
        self.menu = pygame_menu.Menu('Welcome', self.x/2, self.y/2, theme=pygame_menu.themes.THEME_BLUE)
        self.menu.add.button('Play', self.start_game)#function to start the game
        self.menu.add.button('Quit', self.quit_game)
    
    def start_game(self):
        self.state = "game" 
        self.game = Initialize(self.screen) 
        
    def quit_game(self):
        self.running = False  
        
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
        events = pygame.event.get()   
        # check for events
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
        if self.game:
            #update data
            self.game.update()  
        #redraw
        pygame.display.flip() 
            
#   def gameoverloop(self):
#       #event loop

#       #update data

#       #redraw
