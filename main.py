import pygame
from player import Player
from game_platform import Platform
from door import Door
from enemy import Enemy

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
TILE_SIZE = 32

# --- Colors ---
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# --- Level Data (Room 1) ---
LEVEL_1 = [
    "                            ",
    "                            ",
    "                            ",
    "                            ",
    "                            ",
    "                            ",
    "                            ",
    "           P                ",
    "        XXXXXX              ",
    "                     D      ",
    "      XXXXXXXXXXXXX         ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXX"
]

# --- Level Data (Room 2) ---
LEVEL_2 = [
    "                            ",
    "                            ",
    "                            ",
    "                            ",
    "                            ",
    "                            ",
    "                            ",
    "                            ",
    "  X                 E       ",
    " XXXXXX    XXXXXXXXXXXXX    ",
    "XXXXXXXX   XXXXX            ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXX"
]

# --- Game Class ---
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Platformer")
        self.clock = pygame.time.Clock()
        self.running = True
        self.current_room = 1 # Start in room 1
        
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.doors = pygame.sprite.Group() # New sprite group for doors
        self.enemies = pygame.sprite.Group() # New sprite group for enemies
        self.player = Player(50, SCREEN_HEIGHT - TILE_SIZE * 2) # Adjusted player starting position
        self.all_sprites.add(self.player)
        
        self.setup_level(LEVEL_1)

    def setup_level(self, level_data):
        self.all_sprites.empty()
        self.platforms.empty()
        self.doors.empty() # Clear existing doors
        self.enemies.empty() # Clear existing enemies
        self.all_sprites.add(self.player) # Re-add player
        # self.player.platforms = self.platforms # Pass platforms to player

        for row_index, row in enumerate(level_data):
            for col_index, char in enumerate(row):
                if char == "X":
                    platform = Platform(col_index * TILE_SIZE, row_index * TILE_SIZE, TILE_SIZE, TILE_SIZE, GREEN)
                    self.platforms.add(platform)
                    self.all_sprites.add(platform)
                elif char == "P":
                    self.player.rect.x = col_index * TILE_SIZE
                    self.player.rect.y = row_index * TILE_SIZE
                elif char == "D":
                    door = Door(col_index * TILE_SIZE, row_index * TILE_SIZE, TILE_SIZE, TILE_SIZE * 2) # Door is 2 tiles high
                    self.doors.add(door)
                    self.all_sprites.add(door)
                elif char == "E":
                    enemy = Enemy(col_index * TILE_SIZE, row_index * TILE_SIZE, col_index * TILE_SIZE - TILE_SIZE*2, col_index * TILE_SIZE + TILE_SIZE*2, RED)
                    self.enemies.add(enemy)
                    self.all_sprites.add(enemy)

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.handle_events()
            self.update()
            self.draw()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.player.go_left()
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.player.go_right()
                if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                    self.player.jump()
            elif event.type == pygame.KEYUP:
                if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and self.player.change_x < 0:
                    self.player.stop()
                if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and self.player.change_x > 0:
                    self.player.stop()

    def update(self):
        self.player.update(self.platforms)
        self.platforms.update()
        self.doors.update()
        self.enemies.update()
        # self.all_sprites.update() # Pass platforms to player update
        
        # Check for player-door collision
        door_hit_list = pygame.sprite.spritecollide(self.player, self.doors, False)
        for door in door_hit_list:
            if self.current_room == 1:
                self.current_room = 2
                self.setup_level(LEVEL_2)
                self.player.rect.x = 100 # Reset player position for new room
                self.player.rect.y = SCREEN_HEIGHT - TILE_SIZE * 10
            elif self.current_room == 2:
                # Handle transition from room 2 (e.g., win condition or next level)
                pass

        # Check for player-enemy collision
        enemy_hit_list = pygame.sprite.spritecollide(self.player, self.enemies, False)
        if enemy_hit_list:
            self.running = False # Game Over

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

# --- Main ---
if __name__ == '__main__':
    game = Game()
    game.run()
    pygame.quit()
