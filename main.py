import pygame
import sys
from character import Character
from physics import Physics
import background
from pygame.sprite import LayeredUpdates

pygame.init()
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
screen = pygame.display.set_mode(
    (SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF
)
clock = pygame.time.Clock()
running = True

mc = Character(1000, 500)
physics = Physics(gravity=3000)


all_sprites = LayeredUpdates()


background_elements = background.load_background(SCREEN_WIDTH, SCREEN_HEIGHT)
all_sprites.add(background_elements['sky_sprite'])
all_sprites.add(background_elements['ground_sprite'])
all_sprites.add(background_elements['sun_sprite'])
all_sprites.add(background_elements['cloud_sprites'])


mc._layer = 2
all_sprites.add(mc)

while running:
    delta_time = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if mc.alive:
                    mc.jump()

    all_sprites.update(delta_time, physics)
    all_sprites.draw(screen)

    pygame.display.flip()

    if not mc.alive:
        pygame.quit()
        sys.exit(0)

pygame.quit()
