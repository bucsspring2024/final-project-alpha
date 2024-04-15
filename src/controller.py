import pygame
import pygame_menu

class Controller:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode()
        self.screen.fill("white")
        screen_dim = pygame.display.get_surface()
        self.x = screen_dim.get_width()
        self.y = screen_dim.get_height()
        self.running = True
        #setup pygame data
        self.menu = pygame_menu.Menu('Welcome', self.x/2, self.y/2, theme=pygame_menu.themes.THEME_BLUE)
        self.menu.add.button('Play', )#function to start the game
        self.menu.add.button('Quit', pygame_menu.events.EXIT)
        self.state = "menu"
        
    def mainloop(self):
      while True:
            if self.state == "menu":
                self.menuloop()
                #print(self.state)
            elif self.state == "game":
                self.gameloop()  
    #select state loop
    
    def menuloop(self):
        while self.state == "menu":
            #event loop
            if self.menu.is_enabled():
                #saved list of events from the event loop above
                #update data
                self.menu.update(pygame.event.get())
                self.menu.draw(self.screen)
                if(False): self.state = "game"
            #redraw
            pygame.display.update()    
      
    def gameloop(self):
        while self.state == "game":  # one time through the loop is one frame (picture)
            # check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.state = "menu"
      #event loop

      #update data

      #redraw
    
#   def gameoverloop(self):
#       #event loop

#       #update data

#       #redraw
