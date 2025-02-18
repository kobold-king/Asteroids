# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()

    #sets the size of the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #setting up the fps/delta time
    clock = pygame.time.Clock()
    dt = 0

    #adding groups to lessen cltter
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    #define Player
    player =  Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    print("Starting asteroids!")
    print(f"Screen width:", (SCREEN_WIDTH))
    print(f"Screen height:", (SCREEN_HEIGHT))

    while True:
        #draws the screen and updates
        pygame.Surface.fill(screen, (0, 0, 0))
        updatable.update(dt)

        for object in asteroids:
            if object.collisionCheck(player):
                sys.exit("Game Over!")


        for item in drawable:
            item.draw(screen)

        pygame.display.flip()

        #This checks to see if the close button has been pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(dt)
                return

        clock.tick(60)
        dt = clock.tick(60)/1000



if __name__ == "__main__":


    main()
