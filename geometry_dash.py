import pygame
import sys

# Importing used modules from Modules folder
from modules.GameObject import game_obj
from modules.Platform import Platform
from modules.PlayerCube import PlayerCube
from modules.Text import text_obj
from modules.Collisions import Collisions

# Initializing pygame
pygame.init()


# Screen setup
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game Name")

# Player as a cube
player_sprite = [
    pygame.image.load("sprites/platform.png").convert_alpha()
]
player_sprite[0] = pygame.transform.scale(player_sprite[0], (30, 30))

player = PlayerCube((screen_width / 2, screen_height / 2),
                    player_sprite, 0, Collisions(player_sprite, True), "Player")

# Platforms to jump over
platform = pygame.rect.Rect(0, 0, 300, 50)
Platform((400, 400), player_sprite, 0, 0, Collisions(player_sprite, True))

# Main loop
running = True
while running:
    # Setting games bg color
    screen.fill((0, 0, 0))

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Player inputs
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        player.jump_count = 2

    # Registering player collitions
    for obj in game_obj["platform"]:
        player.collitions.at_collition(obj)

    # Rendering all gameobjects from GameObject modules list game_obj
    for list in game_obj:
        for obj in game_obj[list]:
            obj.render(screen)

    # Rendering all textobject from Text modules list text_obj
    for obj in text_obj:
        obj.render(screen)

    # Updating whole display
    pygame.display.update()

    # Capping FPS
    pygame.time.Clock().tick(60)
