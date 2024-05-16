import pygame

class Movement:
    def __init__(self, start_x, start_y, width, height, screen_width, color="green"):
        self.rect = pygame.Rect(start_x, start_y, width, height)
        self.color = color
        self.start_x = start_x
        self.x = screen_width
        
    def move_right(self, increment):
        '''
        Arg: self, increment(int)
        Stores the x coordinate of self.stat_x into new_x_position.
        Also checks that if new_x_position is greater than self.x - 10, new_x_position will
        change to be less than self.x - 10. Then new_x_position is stored back into self.x
        Return: None
        '''
        new_x_position = self.start_x + increment
        if new_x_position + self.rect.width > self.x - 10:
            new_x_position = self.x - self.rect.width
        self.rect.x = new_x_position
    
    def draw(self, screen):
        '''
        Arg: self, screen
        Draws a rectangle on the screen with the defined color and shape/size.
        Return: None
        '''
        pygame.draw.rect(screen, self.color, self.rect)
        
        
        