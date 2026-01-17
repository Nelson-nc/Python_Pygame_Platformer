# Platformer Clones

This repository contains two implementations of a basic platformer game, one in C++ with SDL2 and another in Python with Pygame.

## C++ with SDL2

This section documents the process of creating the platformer clone in C++ with SDL2.

### Setup

1.  **Install MinGW-w64:** If you don't have `g++`, you'll need to install a C++ compiler like MinGW-w64. You can find installers and instructions online.
2.  **Download SDL2 Development Libraries:** Go to the [SDL website](https://www.libsdl.org/download-2.0.php) and download the "Development Libraries" for MinGW (usually a `.zip` file).
3.  **Extract SDL2:** Extract the contents of the `.zip` file to a convenient location.
4.  **Copy SDL2 files:** Copy the `include` and `lib` folders from the extracted SDL2 directory into the `PlatformerClones/platformer_sdl2_cpp/src` directory. You will also need to copy `SDL2.dll` and `SDL2_ttf.dll` from the `bin` folder of the extracted SDL2 directory into the `PlatformerClones/platformer_sdl2_cpp` directory (where the executable will be).
5.  **Compile:** Navigate to the `PlatformerClones/platformer_sdl2_cpp` directory in your terminal and compile the game using the following command:
    ```bash
    g++ -std=c++11 main.cpp Player.cpp Door.cpp Enemy.cpp -o main -Isrc/include -Lsrc/lib -lmingw32 -lSDL2main -lSDL2 -lSDL2_ttf
    ```
6.  **Run:** Execute the compiled program:
    ```bash
    ./main.exe
    ```

### Code Structure

The code is organized into several files:

-   `main.cpp`: This is the main entry point of the game. It contains the `Game` class which manages the game loop, event handling, level setup, and rendering.
-   `Player.h`/`Player.cpp`: These files contain the `Player` class, which represents the player character. It handles player movement, jumping, gravity, and collision with platforms.
-   `Door.h`/`Door.cpp`: These files contain the `Door` class, which allows the player to transition between levels/rooms.
-   `Enemy.h`/`Enemy.cpp`: These files contain the `Enemy` class, representing a basic enemy that patrols platforms.
-   `constants.h`: This header file defines various constants used throughout the game, such as screen dimensions, tile size, and colors.

### Implementation Details

-   **Game Loop:** The main game loop is in the `run` method of the `Game` class. It handles events, updates the game state, and draws game objects.
-   **Player:** The `Player` class represents the player character. It's a blue rectangle with movement (left/right), jumping, and gravity. Collision detection with platforms is handled internally.
-   **Platforms:** Platforms are static `SDL_Rect` objects that the player can stand on. They are rendered as green rectangles.
-   **Door:** The `Door` class represents a brown rectangular door. When the player collides with the door, the game transitions to the next room/level.
-   **Enemy:** The `Enemy` class represents a red rectangular enemy. Enemies patrol platforms by moving back and forth. When the player collides with an enemy, the game ends.
-   **Levels/Rooms:** The game has two predefined levels (`LEVEL_1_DATA` and `LEVEL_2_DATA`) represented by vectors of strings. The `setupLevel` method in the `Game` class parses these strings to create platforms, doors, and enemies.
-   **Collision Detection:** SDL's `SDL_HasIntersection` function is used for collision detection between the player and platforms, doors, and enemies.
-   **Text Rendering:** Text is rendered using the `SDL_ttf` library to display game information (e.g., score, lives, game over messages, though not fully implemented in this basic version).

### Understanding C++ Pointers and `->`

In C++, `->` is called the "arrow operator" and is used to access members of a class, struct, or union through a pointer.

-   **Pointers:** A pointer is a variable that stores the memory address of another variable. For example, `Player* player;` declares a pointer named `player` that can hold the memory address of a `Player` object.
-   **`->` Operator:** When you have a pointer to an object (e.g., `player`), you use the `->` operator to call a method or access a member variable of that object. So, `player->update()` means "call the `update()` method on the object that `player` points to." This is equivalent to `(*player).update()`, where `*player` dereferences the pointer to get the object itself, and then `.` is used to access its members.

### Adding Assets (Images, Sprites, and Animations)

This game uses primitive shapes for rendering. To add more visually appealing assets like images, sprites, and animations, you would typically use an additional SDL2 library called `SDL_image` for loading various image formats (PNG, JPG, etc.).

**Steps to add images/sprites:**

1.  **Include SDL_image:** You would need to include `#include <SDL_image.h>` in your relevant `.cpp` files.
2.  **Initialize SDL_image:** Call `IMG_Init(IMG_INIT_PNG);` (or other formats you need) at the start of your program and `IMG_Quit();` at the end.
3.  **Load Image:** Use `IMG_LoadTexture(renderer, "path/to/your/image.png");` to load an image into an `SDL_Texture*`.
4.  **Render Image:** Use `SDL_RenderCopy(renderer, texture, &sourceRect, &destinationRect);` to draw a portion of the texture (sprite) to a specific area on the screen.
    -   `sourceRect`: Defines the part of the image you want to draw (for sprite sheets).
    -   `destinationRect`: Defines where on the screen and what size you want to draw it.

**For Sprite Animation:**

-   A sprite animation typically involves a sequence of images (frames) from a sprite sheet.
-   You would keep track of the current frame, the total number of frames, and the time each frame should be displayed.
-   In your `update` method, you'd advance the current frame based on elapsed time.
-   In your `render` method, you'd calculate the `sourceRect` to display the correct frame from your sprite sheet.

## Python with Pygame

This section documents the process of creating the platformer clone in Python with Pygame.

### Setup

1.  **Install Python:** Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
2.  **Install Pygame:** Open a terminal or command prompt and run the following command to install Pygame:
    ```
    pip install pygame
    ```

### Code Structure

The code is organized into several files:

-   `main.py`: This is the main entry point of the game. It contains the `Game` class which manages the game loop, event handling, level setup, and rendering.
-   `player.py`: This file contains the `Player` class, which represents the player character. It handles player movement, jumping, gravity, and collision with platforms.
-   `platform.py`: This file contains the `Platform` class, representing static platforms in the game.
-   `door.py`: This file contains the `Door` class, which allows the player to transition between levels/rooms.
-   `enemy.py`: This file contains the `Enemy` class, representing a basic enemy that patrols platforms.

### Implementation Details

-   **Game Loop:** The main game loop is in the `run` method of the `Game` class. It handles events, updates the game state, and draws game objects.
-   **Player:** The `Player` class is a Pygame `Sprite`. It's a blue rectangle with movement (left/right), jumping, and gravity. Collision detection with platforms is handled internally.
-   **Platforms:** The `Platform` class is a Pygame `Sprite`, represented by green rectangles. They are static obstacles the player can stand on.
-   **Door:** The `Door` class is a Pygame `Sprite`, represented by a brown rectangle. When the player collides with the door, the game transitions to the next room/level.
-   **Enemy:** The `Enemy` class is a Pygame `Sprite`, represented by a red rectangle. Enemies patrol platforms and cause a game over when the player collides with them.
-   **Levels/Rooms:** The game has two predefined levels (`LEVEL_1` and `LEVEL_2`) represented by lists of strings. The `setup_level` method in the `Game` class parses these strings to create platforms, doors, and enemies.
-   **Collision Detection:** Pygame's `pygame.sprite.spritecollide` is used for collision detection between the player and platforms, doors, and enemies.

### Adding Assets (Images, Sprites, and Animations)

Pygame makes it relatively straightforward to incorporate images and handle sprite animations.

**Steps to add images/sprites:**

1.  **Load Image:** Use `pygame.image.load("path/to/your/image.png").convert_alpha()` to load an image. `.convert_alpha()` optimizes the image for Pygame and handles transparency.
2.  **Create Sprite:** In your `Sprite` subclass (like `Player`, `Enemy`, etc.), you would set `self.image` to the loaded image surface and `self.rect` to its `get_rect()`.
3.  **Draw Sprite:** In your `Game` class, after creating a `pygame.sprite.Group()` or individual sprites, you can draw them using `self.all_sprites.draw(self.screen)` (for groups) or `screen.blit(sprite.image, sprite.rect)` (for individual sprites) in your `draw` method.

**For Sprite Animation:**

-   **Sprite Sheet:** You typically have a single image file (sprite sheet) containing all frames of an animation.
-   **Extract Frames:** Load the sprite sheet and then use `image.subsurface(rect)` to extract individual frames from it. Store these frames in a list.
-   **Animate:** In your sprite's `update` method, cycle through the list of frames based on a timer. For example:
    ```python
    self.current_frame = (self.current_frame + 1) % len(self.animation_frames)
    self.image = self.animation_frames[self.current_frame]
    ```
    You would usually control the speed of animation by only updating the frame every few game ticks.

