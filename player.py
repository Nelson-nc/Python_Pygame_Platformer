import pygame

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TILE_SIZE = 32

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill((0, 128, 255)) # Blue color
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.change_x = 0
        self.change_y = 0
        self.on_ground = False

    def update(self, platforms):
        # Gravity
        self.calc_grav()

        # Move left/right
        self.rect.x += self.change_x

        # Check for horizontal collisions with platforms
        platform_hit_list = pygame.sprite.spritecollide(self, platforms, False)
        for platform in platform_hit_list:
            if self.change_x > 0: # Moving right
                self.rect.right = platform.rect.left
            elif self.change_x < 0: # Moving left
                self.rect.left = platform.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Assume not on ground initially for each update
        self.on_ground = False
        
        # Check for vertical collisions with platforms
        platform_hit_list = pygame.sprite.spritecollide(self, platforms, False)
        for platform in platform_hit_list:
            if self.change_y > 0: # Falling down
                self.rect.bottom = platform.rect.top
                self.on_ground = True
            elif self.change_y < 0: # Jumping up
                self.rect.top = platform.rect.bottom
            self.change_y = 0 # Stop vertical movement on collision

        # Boundary check for screen bottom (fallback if no platforms)
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.on_ground = True
            self.change_y = 0

    def calc_grav(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35

    def jump(self):
        # Only allow jump if on ground
        if self.on_ground:
            self.change_y = -10

    def go_left(self):
        self.change_x = -5

    def go_right(self):
        self.change_x = 5

    def stop(self):
        self.change_x = 0
