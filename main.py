
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for mem in updatable:
            mem.update(dt)
        for mem in asteroids:
            if player.is_colliding(mem):
                print("GAME OVER!")
                return

        screen.fill(BLACK)
        for mem in drawable:
            mem.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000





if __name__=="__main__":
    main()