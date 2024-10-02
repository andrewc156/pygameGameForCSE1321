import pygame


class Character(pygame.sprite.Sprite):
    def __init__(self, positionx, positiony):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Put image here").convert_alpha()
        self.rect = self.image.get_rect()
        self.V_x = 10
        self.V_y = 0
        self.positionx = 0
        self.positiony = 0
        self.is_jumping = True
        self.window_height = 1080
        self.alive = True

    def get_position(self) -> tuple:
        return (self.positionx, self.positiony)

    def get_velocity(self) -> tuple:
        return (self.V_x, self.V_y)

    def is_alive(self) -> bool:
        return self.alive

    def jump(self):
        self.V_y = 40
