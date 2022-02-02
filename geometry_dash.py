from math import fabs
import pygame
import sys
# Importing used modules from Modules folder
from modules.Collisions import Collisions
from modules.GameEvent import GameEvents
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
                    player_sprite, 0, Collisions(player_sprite), True, "Player")

# Platforms

main_platform_sprite = [
    pygame.image.load("sprites/platform.png").convert_alpha()
]
main_platform_sprite[0] = pygame.transform.scale(
    main_platform_sprite[0], (screen_width * 2, 150))

main_platform = Platform((screen_width, screen_height - 75),
                         main_platform_sprite, 0, Collisions(main_platform_sprite))

platform_sprite = [
    pygame.image.load("sprites/platform.png").convert_alpha()
]
platform_sprite[0] = pygame.transform.scale(platform_sprite[0], (50, 50))

spike_sprite = [
    pygame.image.load("sprites/platform.png").convert_alpha()
]
spike_sprite[0] = pygame.transform.scale(spike_sprite[0], (50, 50))


def spawn_obstacle(index):
    ground_level = screen_height - 175

    positions = [
        {
            "Platform": [
                (screen_width, ground_level + 25),
            ],
            "Spike":[(screen_width + 50, ground_level + 25), ],
        }
    ]

    for index in positions:
        for dic in index:
            for pos in index[dic]:
                Platform(pos, spike_sprite, 0, Collisions(
                    spike_sprite), name=dic)

    # for dic in positions:
    #     for arr in positions[dic]:
    #         for pos in arr:
    #             Platform(pos, spike_sprite, 0, Collisions(
    #                 spike_sprite), name=list)


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

        if event.type == GameEvents.player_died:
            running = False

    # Player inputs
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and jump_timer.do_action(pygame.time.get_ticks()):
        player.velocity = (0, -15)
        spawn_obstacle(0)

    if keys[pygame.K_RIGHT]:
        player.velocity = (5, player.velocity[1])

    if keys[pygame.K_LEFT]:
        player.velocity = (-5, player.velocity[1])

    # Rendering all gameobjects from GameObject modules list game_obj
    for list in game_obj:
        for obj in game_obj[list]:
            obj.render(screen)

    # Moving all platforms
    for platform in game_obj["platform"]:
        platform.move((-1, 0), 4)

    # Adding possibly new platforms to player collide list
    player.collisions.add_to_collide_with_list(game_obj["platform"])
    player.collisions.add_to_collide_with_list(game_obj["death"])

    # DEBUG/DEVELOP MODE
    render_hitboxes(screen)
    display_fps(screen, clock)

    # Updating whole display
    pygame.display.update()

    # Capping FPS
    clock.tick(90)
