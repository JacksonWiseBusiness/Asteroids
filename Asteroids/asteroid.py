from circleshape import CircleShape
from constants import *
import pygame
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
        
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
        
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
        
    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")
        
        randangle = random.uniform(20, 50)
        vector1 = self.velocity.rotate(randangle)
        vector2 = self.velocity.rotate(-randangle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid1.velocity = vector1 * 1.2
        new_asteroid2.velocity = vector2 * 1.2