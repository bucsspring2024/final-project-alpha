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
        self.menu = pygame_menu.Menu('Welcome', 400, 300, theme=pygame_menu.themes.THEME_BLUE)
        self.menu.add.button('Play', )#function to start the game
        self.menu.add.button('Quit', pygame_menu.events.EXIT)
  def mainloop(self):
    #select state loop
    
  
  ### below are some sample loop states ###

  def menuloop(self):
    
      #event loop

      #update data

      #redraw
      
  def gameloop(self):
      #event loop

      #update data

      #redraw
    
  def gameoverloop(self):
      #event loop

      #update data

      #redraw
