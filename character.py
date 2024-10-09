import pygame

class Character(pygame.sprite.Sprite):
    def __init__(self, positionx, positiony):
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

    def update(self, delta_time, physics):
        physics.apply_gravity(delta_time, self)
        self.rect.x = self.positionx
        self.rect.y = self.positiony

    def jump(self):
        self.is_jumping = True
        self.V_y = -400
