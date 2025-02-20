# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
import os
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    pygame.font.init()
    #sets the size of the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #setting up the fps/delta time
    clock = pygame.time.Clock()
    dt = 0
    player_score = 0
    font = pygame.font.Font(None, 36)

    #adding groups to lessen cltter
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

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
                print(player_score)
                sys.exit("Game Over!")
            for shot in shots:
                if shot.collisionCheck(object):
                    player_score += 1
                    object.split()
                    shot.kill()


        for item in drawable:
            item.draw(screen)

        # Draw the score to the screen
        score_text = font.render(f'Score: {player_score}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        pygame.display.flip()

        #This checks to see if the close button has been pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                (print(player_score))
                return

        clock.tick(60)
        dt = clock.tick(60)/1000



if __name__ == "__main__":


    main()
