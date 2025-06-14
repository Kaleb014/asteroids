import pygame
import sys
from constants import *
from player import *

def main():
    pygame.init()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))

        # Check for player inputs
        player.update(dt)
        # Update the game world
        
        #Draw the game to the screen
        player.draw(screen)




        pygame.display.flip()
        dt = clock.tick(60) / 1000







if __name__ == "__main__":
    main()
