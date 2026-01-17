import pygame

# --- Constants ---
TILE_SIZE = 32

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color) # Green color
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
