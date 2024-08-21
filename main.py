import sys
import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    # Define groups
    asteroids = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()

    dt = 0
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Add classes to their respective groups
    Asteroid.containers = (asteroids, drawable, updatable)
    AsteroidField.containers = updatable
    Player.containers = (drawable, updatable)
    Shot.containers = (shots, drawable, updatable)

    # Initialize objects
    AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Start the game loop
    while True:
        # Enable the window's close button to work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Get the current delta
        dt = clock.tick(60) / 1000

        # Set the background color
        screen.fill("black")

        # Update every updatable object
        for obj in updatable:
            obj.update(dt)

        # Draw every drawable object
        for obj in drawable:
            obj.draw(screen)

        for asteroid in asteroids:
            # End game if an asteroid collides with the player
            if asteroid.is_colliding(player):
                print("Game over!")
                sys.exit()

            # Destroy an asteroid if it collides with a shot
            for shot in shots:
                if asteroid.is_colliding(shot):
                    asteroid.kill()

        pygame.display.flip()


if __name__ == "__main__":
    main()
