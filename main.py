import pygame
from constants import *
from player import Player

def main():
    pygame.init()

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updateable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2)
    
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        screen.fill((0,0,0))

        for player in drawable:
            player.draw(screen)

        updateable.update(dt)

        # hier wordt het scherm geupdate
        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()