import pygame # type: ignore
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt: int = 0
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = (updateable)
    Shot.containers = (updateable, drawable, bullets)

    print(f"""
Starting Asteroids!
Screen width: {SCREEN_WIDTH}
Screen height: {SCREEN_HEIGHT}
        """)
    
    screen = pygame.display.set_mode(SCREEN_SIZE)
    player = Player(*PLAYER_SPAWN_POINT)
    asteroid_field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        dt = clock.tick(FPS) / 1000
            
        screen.fill(SCREEN_COLOR)
        
        updateable.update(dt)
        for item in drawable:
            item.draw(screen)
        for asteroid in asteroids:
            if asteroid.check_collisions(player):
                print("Game Over!")
                sys.exit()

        pygame.display.flip()
        

if __name__ == "__main__":
    main()
