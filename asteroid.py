import pygame
from circleshape import *
import random
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)


    def update(self, dt):
        self.position += self.velocity * dt


    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)
        first_velocity = self.velocity.rotate(random_angle) * 1.2
        second_velocity = self.velocity.rotate(-random_angle) * 1.2
        radius = self.radius - ASTEROID_MIN_RADIUS
        first_asteroid = Asteroid(self.position, self.position, radius)
        second_asteroid = Asteroid(self.position, self.position, radius)
        first_asteroid.velocity = first_velocity
        second_asteroid.velocity = second_velocity


