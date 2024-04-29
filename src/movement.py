import pygame

class Movement:
    def __init__(self, start_x, start_y, width, height, screen_width, color="green"):
        self.rect = pygame.Rect(start_x, start_y, width, height)
        self.color = color
        self.start_x = start_x
        self.x = screen_width
        
    def move_right(self, increment):
        new_x_position = self.start_x + increment
        if new_x_position + self.rect.width > self.x - 10:
            new_x_position = self.x - self.rect.width
        self.rect.x = new_x_position
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        
        
        