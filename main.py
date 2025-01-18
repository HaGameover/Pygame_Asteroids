import pygame, asteroidfield
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatables, drawables)
    Asteroid.containers = (updatables, drawables, asteroids)
    AsteroidField.containers = (updatables)
    Shot.containers = (updatables, drawables, shots)

    player = Player(x=(SCREEN_WIDTH / 2),y=(SCREEN_HEIGHT / 2))
    asteroidField = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))

        for updatable in updatables:
            updatable.update(dt)
        for drawable in drawables:
            drawable.draw(screen)
        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game over!")
                exit()
            for shot in shots:
                if asteroid.check_collision(shot):
                    asteroid.split() 
                    shot.kill()

        dt = clock.tick(60) / 1000
        pygame.display.flip()

if __name__ == "__main__":
    main()