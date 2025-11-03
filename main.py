from constants import (SCREEN_WIDTH, 
                       SCREEN_HEIGHT, 
                       ASTEROID_MIN_RADIUS,
                       ASTEROID_KINDS,
                       ASTEROID_SPAWN_RATE,
                       ASTEROID_MAX_RADIUS)
from player import Player
import pygame


def main():
    pygame.init()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)
        screen.fill("black")
        for draws in drawable:
            draws.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60)/1000
        

if __name__ == "__main__":
    main()
