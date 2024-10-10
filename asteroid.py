import pygame
from circleshape import *
from constants import *


class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (self.x, self.y), self.radius, 2)

    def update(self, dt):
        forward = pygame.Vector2(0, 1)
        self.position += forward * PLAYER_SPEED * dt