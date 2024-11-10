import pygame


class BackgroundElement(pygame.sprite.Sprite):
    def __init__(self, image, position, layer=0):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=position)
        self._layer = layer


def load_background(SCREEN_WIDTH, SCREEN_HEIGHT):
    WHITE = (255, 255, 255)
    BLUE = (135, 206, 235)
    YELLOW = (255, 255, 0)
    GREY = (169, 169, 169)
    GREEN = (0, 128, 0)

    sun_image = pygame.Surface((80, 80))
    sun_image.fill(YELLOW)

    moon_image = pygame.Surface((80, 80))
    moon_image.fill(GREY)

    cloud_image = pygame.Surface((100, 50))
    cloud_image.fill(WHITE)

    sky = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    sky.fill(BLUE)
    ground = pygame.Surface((SCREEN_WIDTH, 100))
    ground.fill(GREEN)

    clouds = [(300, 100), (700, 200), (500, 300), (100, 400)]

    sky_sprite = BackgroundElement(sky, (0, 0), layer=0)
    ground_sprite = BackgroundElement(ground, (0, SCREEN_HEIGHT - 100), layer=1)
    sun_sprite = BackgroundElement(sun_image, (SCREEN_WIDTH - 200, 100), layer=1)

    cloud_sprites = []
    for pos in clouds:
        cloud_sprite = BackgroundElement(cloud_image, pos, layer=1)
        cloud_sprites.append(cloud_sprite)

    return {
        'sky_sprite': sky_sprite,
        'ground_sprite': ground_sprite,
        'sun_sprite': sun_sprite,
        'cloud_sprites': cloud_sprites,
    }
