import pygame

class Context:
    def __init__(self, screen):
        pygame.init()
        self.screen = screen
        self.x = self.screen.get_width()
        self.y = self.screen.get_height()
        self.intro = """
        You want to travel to San Francisco\n
        from New York City. However, all the flights to San Francisco\n
        are booked so you decide to drive across the country. Through\n
        a series of decision making, reach the west coast as fast\n
        as possible.
        """
        self.lines = self.intro.split('\n')
        self.font = pygame.font.Font(None, 36)
        self.click = False
        self.instructions = """Click to Continue"""
        self.list = []
        for line in self.lines:
            surface = self.font.render(line, True, "black")
            self.list.append(surface)
        
    def display_text(self):
        intro_y = 50
        self.screen.fill("orange")
        for surface in self.list:
            self.screen.blit(surface, (50, intro_y)) 
            intro_y += surface.get_height() + 10
        text_intro_instruct = self.font.render(self.instructions, True, "black")
        self.screen.blit(text_intro_instruct, (5, self.y-75))
        self.box = pygame.Rect(0,self.y-100, 225, 100)
        pygame.draw.rect(self.screen, "magenta", self.box, width=3)
    
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                #print("Handle)")
                if self.box.collidepoint(event.pos):
                    self.click = True  
        return self.click