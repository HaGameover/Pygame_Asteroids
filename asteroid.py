import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()

        if self.radius == ASTEROID_MIN_RADIUS:
            #was a small asteroid => no spawn
            return
        
        random_angle = random.uniform(20, 50)
        new_vel1 = self.velocity.rotate(random_angle) * 1.2
        new_vel2 = self.velocity.rotate(-random_angle) * 1.2
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid1.velocity = new_vel1
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2.velocity = new_vel2
