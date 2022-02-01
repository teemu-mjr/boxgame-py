import pygame
import sys
# Importing used modules from Modules folder
from modules.Collisions import Collisions
from modules.Text import text_obj
from modules.PlayerCube import PlayerCube
from modules.Platform import Platform
from modules.IntervalTimer import IntervalTimer
from modules.GameObject import game_obj

# DEVELOPING/TESTING
from fps_meter import display_fps


def render_hitboxes(screen):
    for list in game_obj:
        for obj in game_obj[list]:
            if(obj.collisions != 0):
                obj.collisions.draw(screen)


# Initializing pygame
pygame.init()
clock = pygame.time.Clock()

# Screen setup
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game Name")

# Creating the player
player_sprite = [
    pygame.image.load("sprites/platform.png").convert_alpha()
]
player_sprite[0] = pygame.transform.scale(player_sprite[0], (50, 50))

player = PlayerCube((100, screen_height - 220),
                    player_sprite, 0, Collisions(player_sprite), "Player")

# Platforms

main_platform_sprite = [
    pygame.image.load("sprites/platform.png").convert_alpha()
]
main_platform_sprite[0] = pygame.transform.scale(
    main_platform_sprite[0], (screen_width * 2, 150))

main_platform = Platform((screen_width, screen_height - 75),
                         main_platform_sprite, 0, Collisions(main_platform_sprite))
main_platform = Platform((screen_width, screen_height - 350),
                         main_platform_sprite, 0, Collisions(main_platform_sprite), "roof")

platform_sprite = [
    pygame.image.load("sprites/platform.png").convert_alpha()
]
platform_sprite[0] = pygame.transform.scale(platform_sprite[0], (50, 50))


def spawn_obstacle(index):
    ground_level = screen_height - 175

    positions = [
        [
            (screen_width, ground_level),
        ]
    ]

    for pos in positions[index]:
        Platform(pos, platform_sprite, 0, Collisions(
            platform_sprite))


spawn_obstacle(0)

# add game_obj list of platform to players collition list
player.collisions.add_to_collide_with_list(game_obj["platform"])


# Timers
jump_timer = IntervalTimer(60)

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

    if keys[pygame.K_SPACE] and jump_timer.do_action(pygame.time.get_ticks()):
        player.jump_count = 10

    # Rendering all gameobjects from GameObject modules list game_obj
    for list in game_obj:
        for obj in game_obj[list]:
            obj.render(screen)

    # Moving all platforms
    for platform in game_obj["platform"]:
        platform.move((-1, 0), 1)

    # DEBUG/DEVELOP MODE
    render_hitboxes(screen)
    display_fps(screen, clock)

    # Updating whole display
    pygame.display.update()

    # Capping FPS
    clock.tick(60)
