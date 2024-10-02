import pygame

class Character(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Put image here").convert_alpha()
        self.rect = self.image.get_rect()
        self.x_velocity = 0
        self.y_velocity = 0
        self.is_jumping = True
        self.gravity = 1
        self.window_height = 1080
        self.alive = True

