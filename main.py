import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2)
    asteroidsfield = AsteroidField()
    
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        screen.fill((0,0,0))

        for object in drawable:
            object.draw(screen)

        updateable.update(dt)

        # hier wordt het scherm geupdate
        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()