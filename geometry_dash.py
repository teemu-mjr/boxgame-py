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
player_sprite[0] = pygame.transform.scale(player_sprite[0], (50, 50))

player = PlayerCube((screen_width / 2, screen_height / 2),
                    player_sprite, 0, Collisions(player_sprite), "Player")

# Platforms

platform_sprite = [
    pygame.image.load("sprites/platform.png").convert_alpha()
]
platform_sprite[0] = pygame.transform.scale(platform_sprite[0], (50, 50))


def spawn_obstacle(index):
    positions = [
        [
            (100, 100),
            (200, 200),
            (300, 300),
            (400, 400),
        ]
    ]

    for pos in positions[index]:
        Platform(pos, platform_sprite, 0, Collisions(platform_sprite))


spawn_obstacle(0)


# add game_obj list of platform to players collition list
player.collisions.add_to_collide_with_list(game_obj["platform"])


def render_hitboxes(screen):
    for list in game_obj:
        for obj in game_obj[list]:
            if(obj.collisions != 0):
                obj.collisions.draw(screen)


# Main loop
running = True
jump_cooldown = 0
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

    if keys[pygame.K_SPACE] and jump_cooldown <= 0:
        jump_cooldown = 40
        player.jump_count = 10

    # Rendering all gameobjects from GameObject modules list game_obj
    for list in game_obj:
        for obj in game_obj[list]:
            obj.render(screen)

    # Rendering all textobject from Text modules list text_obj
    for obj in text_obj:
        obj.render(screen)

    # Timer for now...
    if(jump_cooldown > 0):
        jump_cooldown -= 1

    # Rendering ALL hitboxes
    render_hitboxes(screen)

    # Updating whole display
    pygame.display.update()

    # Capping FPS
    pygame.time.Clock().tick(100)
