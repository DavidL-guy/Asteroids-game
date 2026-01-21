from circleshape import *
from constants import LINE_WIDTH

class Asteroids(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = (x,y)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt