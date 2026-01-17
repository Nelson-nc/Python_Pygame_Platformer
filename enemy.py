import pygame

# --- Constants ---
TILE_SIZE = 32

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, patrol_start, patrol_end, color):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(color) # Red color
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.change_x = 2 # Initial speed
        self.patrol_start = patrol_start
        self.patrol_end = patrol_end

    def update(self):
        self.rect.x += self.change_x
        
        if self.rect.right >= self.patrol_end or self.rect.left <= self.patrol_start:
            self.change_x *= -1 # Reverse direction
