import pygame
from character import Character
from physics import Physics
import sys

pygame.init()
screen = pygame.display.set_mode(
    (1920, 1080), pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF
)
clock = pygame.time.Clock()
running = True
playing = True

mc = Character(1000, 500)
physics = Physics(gravity=3000)
all_sprites = pygame.sprite.Group()
all_sprites.add(mc)

while running:
    delta_time = clock.tick(60) / 1000.0
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                mc.jump()

    all_sprites.update(delta_time, physics)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)
    if not mc.alive:
        pygame.quit()
        sys.exit(0)