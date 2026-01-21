import pygame
from constants import *
from logger import log_state
from player import *
from asteroid import *
from asteroidfield import AsteroidField

def main():

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroids.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
        
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidField = AsteroidField()
    
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0


    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        dt = clock.tick(60) / 1000

        updatable.update(dt)


        screen.fill("black")
        for draw in drawable:
            draw.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
