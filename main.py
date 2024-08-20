import sys
import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    # Define groups
    asteroids = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()

    dt = 0
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Add classes to their respective groups
    Asteroid.containers = (asteroids, drawable, updatable)
    AsteroidField.containers = updatable
    Player.containers = (drawable, updatable)

    # Initialize objects
    asteroid_field = AsteroidField()
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

        # Check for collisions and end game if one occurs
        for obj in asteroids:
            if obj.is_colliding(player):
                print("Game over!")
                sys.exit()

        pygame.display.flip()


if __name__ == "__main__":
    main()
