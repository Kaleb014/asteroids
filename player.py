from circleshape import *
from constants import *
import math

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
        
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255,255,255), self.triangle(), 2)

    
    def rotate_right(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt


    def rotate_left(self, dt):
        self.rotation -= PLAYER_TURN_SPEED * dt


    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate_left(dt)
        if keys[pygame.K_d]:
            self.rotate_right(dt)
        if keys[pygame.K_w]:
            self.move_forward(dt)
        if keys[pygame.K_s]:
            self.move_backward(dt)


    def move_forward(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def move_backward(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position -= forward * PLAYER_SPEED * dt

       
