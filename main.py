import pygame

from constants import *
from player import Player


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    # Define groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    dt = 0
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Add every Player instance to both groups via a static field
    Player.containers = (updatable, drawable)

    # Initialize player object
    Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        # Enable the window's close button to work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000

        screen.fill("black")

        # Update every updatable object
        for obj in updatable:
            obj.update(dt)

        # Draw every drawable object
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
