import pygame


class Character(pygame.sprite.Sprite):
    def __init__(self, positionx, positiony):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Put image here").convert_alpha()
        self.rect = self.image.get_rect()
        self.V_x = 10
        self.V_y = 0
        self.position = [positionx, positiony]
        self.is_jumping = True
        self.window_height = 1080
        self.alive = True

    def get_position(self):
        return self.position

    def get_velocity(self):
        return [self.V_x, self.V_y]

    def is_alive(self):
        return self.alive
