from random import randint
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
                    player_sprite, 0, Collisions(player_sprite, (0, 5, 0, -5)), True, "Player")

# Platforms

main_platform_sprite = [
    pygame.image.load("sprites/platform.png").convert_alpha()
]
main_platform_sprite[0] = pygame.transform.scale(
    main_platform_sprite[0], (screen_width * 2, 150))

main_platform = Platform((screen_width, screen_height - 75),
                         main_platform_sprite, 0, Collisions(main_platform_sprite), name="Floor")

platform_sprite = [
    pygame.image.load("sprites/platform.png").convert_alpha()
]
platform_sprite[0] = pygame.transform.scale(platform_sprite[0], (50, 50))

spike_sprite = [
    pygame.image.load("sprites/spike0.png").convert_alpha()
]
spike_sprite[0] = pygame.transform.scale(spike_sprite[0], (25, 50))


class ObstaclePreset:
    def __init__(self, platforms: list, spikes: list, interval: int):
        self.platforms = platforms
        self.spikes = spikes
        self.interval = interval * 10


ground_level = screen_height - 175
center_pos = screen_width
presets = [
    # S S
    ObstaclePreset([

    ], [

        (center_pos - 25, ground_level),
        (center_pos + 25, ground_level),
    ],
        100
    ),


    #     S
    #   B B B
    ObstaclePreset([
        (center_pos - 50, ground_level),
        (center_pos, ground_level),
        (center_pos + 50, ground_level),
    ], [

        (center_pos, ground_level - 50),
    ],
        100
    ),


    #       B   B
    #
    #   B S S S S S B
    ObstaclePreset([
        (center_pos - 200, ground_level),
        (center_pos - 75, ground_level - 100),
        (center_pos + 75, ground_level - 100),
        (center_pos + 200, ground_level),
    ], [

        (center_pos - 150, ground_level),
        (center_pos - 100, ground_level),
        (center_pos - 50, ground_level),
        (center_pos, ground_level),
        (center_pos + 50, ground_level),
        (center_pos + 100, ground_level),
        (center_pos + 150, ground_level),
    ], 200
    ),

]


def spawn_obstacle(index):

    for platform_pos in presets[index].platforms:
        Platform(platform_pos, platform_sprite, 0, Collisions(
            platform_sprite))

    for spike_pos in presets[index].spikes:
        Platform(spike_pos, spike_sprite, 0, Collisions(
            spike_sprite, (10, 10, -20, 10)), name="Spike")

    return presets[index].interval


# Timers
jump_timer = IntervalTimer(60)
obstacle_timer = IntervalTimer(0)

# Main loop
running = True
in_menu = True
playing = True
while running:
    # Setting games bg color
    screen.fill((0, 0, 0))

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == GameEvents.player_died:
            playing = False

    # Rendering all gameobjects from GameObject modules list game_obj
    for list in game_obj:
        for obj in game_obj[list]:
            obj.render(screen)

####################################################################################
    if playing:
        # Player inputs
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and player.is_grounded:
            player.velocity = (0, -15)

        if keys[pygame.K_RIGHT] and player.collisions.hitbox.right < screen_width:
            player.velocity = (5, player.velocity[1])

        if keys[pygame.K_LEFT] and player.collisions.hitbox.left > 0:
            player.velocity = (-5, player.velocity[1])

        # Moving all platforms
        for platform in game_obj["platform"]:
            if(platform.name != "Floor"):
                platform.move((-1, 0), 4)

        # Adding possibly new platforms to player collide list
        player.collisions.add_to_collide_with_list(game_obj["platform"])
        player.collisions.add_to_collide_with_list(game_obj["death"])

        # Spawn obstacles
        if(obstacle_timer.do_action(pygame.time.get_ticks())):
            obstacle_timer.interval = spawn_obstacle(randint(0, len(presets)))

        # DEBUG/DEVELOP MODE
        render_hitboxes(screen)
        display_fps(screen, clock)
####################################################################################

    # Updating whole display
    pygame.display.update()

    # Capping FPS
    clock.tick(90)
