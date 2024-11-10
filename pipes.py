import pygame
import random

GREEN = (0, 255, 0)

class TubePair:
    def __init__(self, x, screen_height, tube_width, tube_gap, tube_velocity, layer=1):
        self.screen_height = screen_height
        self.width = tube_width
        self.gap = tube_gap
        self.velocity = tube_velocity

        self.top_height = random.randint(50, self.screen_height - self.gap - 50)
        self.bottom_height = self.screen_height - self.top_height - self.gap
        self.x = x

        self.top_tube = TubeSegment(
            x,
            0,
            self.width,
            self.top_height,
            self.velocity,
            is_top=True,
            layer=layer
        )

        self.bottom_tube = TubeSegment(
            x,
            self.screen_height - self.bottom_height,
            self.width,
            self.bottom_height,
            self.velocity,
            is_top=False,
            layer=layer
        )

        self.passed = False

    def add_to_group(self, pipes_group, all_sprites):
        pipes_group.add(self.top_tube)
        pipes_group.add(self.bottom_tube)
        all_sprites.add(self.top_tube)
        all_sprites.add(self.bottom_tube)

class TubeSegment(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, velocity, is_top, layer=1):
        super().__init__()
        self._layer = layer
        self.image = pygame.Surface((width, height))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.velocity = velocity
        self.is_top = is_top

    def update(self, delta_time, *args):
        self.rect.x -= self.velocity * delta_time

        if self.rect.right < 0:
            self.kill()
