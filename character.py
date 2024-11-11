# character.py

import pygame

class Character(pygame.sprite.Sprite):
    def __init__(self, positionx, positiony, physics, jump_sound):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = (positionx, positiony)
        self.V_x = 0
        self.V_y = 0
        self.positionx = positionx
        self.positiony = positiony
        self.is_jumping = False
        self.window_height = 1080
        self.alive = True
        self.physics = physics  # Stores the physics object
        self.jump_sound = jump_sound  # Stores the jump sound

    def update(self, delta_time, *args):
        self.physics.apply_gravity(delta_time, self)
        self.rect.x = self.positionx
        self.rect.y = self.positiony

    def jump(self):
        self.is_jumping = True
        self.V_y = -800
        self.jump_sound.play()  # Plays the jump sound effect
