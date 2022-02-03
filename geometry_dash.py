import pygame
import sys
from random import randint
from modules.Background import Background
# Importing used modules from Modules folder
from modules.Collisions import Collisions
from modules.GameEvent import GameEvents
from modules.GameText import GameText
from modules.PlayerCube import PlayerCube
from modules.Platform import Platform
from modules.IntervalTimer import IntervalTimer

# DEVELOPING/TESTING
from fps_meter import display_fps


# Initializing pygame
pygame.init()
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)

# Screen setup
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game Name")

# GameObjects
game_obj = {
    "background": [],
    "platform": [],
    "spike": [],
    "player": [],
}

text_obj = {
    "menu": [],
    "game": []
}


# Game sprites

player_sprite = [
    pygame.image.load("sprites/crate.png").convert_alpha()
]
player_sprite[0] = pygame.transform.scale(player_sprite[0], (50, 50))

main_platform_sprite = [
    pygame.image.load("sprites/crate2.png").convert_alpha()
]
main_platform_sprite[0] = pygame.transform.scale(
    main_platform_sprite[0], (screen_width * 2, 150))

platform_sprite = [
    pygame.image.load("sprites/crate2.png").convert_alpha()
]
platform_sprite[0] = pygame.transform.scale(platform_sprite[0], (50, 50))

spike_sprite = [
    pygame.image.load("sprites/spike.png").convert_alpha()
]
spike_sprite[0] = pygame.transform.scale(spike_sprite[0], (25, 50))

background_sprite = [
    pygame.image.load("sprites/bg.png")
]
background_sprite[0] = pygame.transform.scale(background_sprite[0], (800, 600))

black_sprite = [
    pygame.image.load("sprites/blank.png").convert_alpha()
]

text_back = [
    pygame.image.load("sprites/blank_br.png").convert_alpha()
]
text_back[0] = pygame.transform.scale(text_back[0], (300, 100))
text_back[0].set_alpha(150)


# Platforms


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

        (center_pos, ground_level),
        (center_pos + 50, ground_level),
    ],
        100
    ),


    #     S
    #   B B B
    ObstaclePreset([
        (center_pos, ground_level),
        (center_pos + 50, ground_level),
        (center_pos + 100, ground_level),
    ], [

        (center_pos + 50, ground_level - 50),
    ],
        100
    ),


    #       B   B
    #
    #   B S S S S S B
    ObstaclePreset([
        (center_pos, ground_level),
        (center_pos + 125, ground_level - 100),
        (center_pos + 275, ground_level - 100),
        (center_pos + 400, ground_level),
    ], [

        (center_pos + 50, ground_level),
        (center_pos + 100, ground_level),
        (center_pos + 150, ground_level),
        (center_pos + 200, ground_level),
        (center_pos + 250, ground_level),
        (center_pos + 300, ground_level),
        (center_pos + 350, ground_level),
    ], 200
    ),

    #     B S S B S
    #   B B B B B B
    ObstaclePreset([
        (center_pos, ground_level),
        (center_pos + 50, ground_level),
        (center_pos + 100, ground_level),
        (center_pos + 150, ground_level),
        (center_pos + 200, ground_level),
        (center_pos + 250, ground_level),
        (center_pos + 50, ground_level - 50),
        (center_pos + 200, ground_level - 50),

    ], [

        (center_pos + 100, ground_level - 50),
        (center_pos + 150, ground_level - 50),
        (center_pos + 250, ground_level - 50),
    ], 200
    ),

]


def spawn_obstacle(index):

    for platform_pos in presets[index].platforms:
        game_obj["platform"].append(
            Platform(platform_pos, platform_sprite, 0, Collisions(
                platform_sprite))
        )

    for spike_pos in presets[index].spikes:
        game_obj["platform"].append(
            Platform(spike_pos, spike_sprite, 0, Collisions(
                spike_sprite, (10, 20, -20, 5)), name="Spike")
        )

    return presets[index].interval


# Timers
obstacle_timer = IntervalTimer(0)

# Main loop booleans
running = True
in_menu = True
playing = False

# Game functions


def render_hitboxes(screen):
    for list in game_obj:
        for obj in game_obj[list]:
            if(obj.collisions != 0):
                obj.collisions.draw(screen)


def clear_screen():
    # Platforms
    if len(game_obj["platform"]) > 0:
        while len(game_obj["platform"]) > 0:
            game_obj["platform"].pop(0)
    # Spike
    if len(game_obj["spike"]) > 0:
        while len(game_obj["spike"]) > 0:
            game_obj["spike"].pop(0)
    # Player
    if len(game_obj["player"]) > 0:
        while len(game_obj["player"]) > 0:
            game_obj["player"].pop(0)


def find_object_by_name(name: str):
    for list in game_obj:
        for obj in game_obj[list]:
            if obj.name == name:
                return obj
    return False


def create_player():
    game_obj["player"].append(
        PlayerCube((100, screen_height - 220),
                   player_sprite, 0, Collisions(player_sprite, (0, 5, 0, -5)), True, name="Player")
    )


def create_main_platform():
    game_obj["platform"].append(
        Platform((screen_width, screen_height - 75),
                 main_platform_sprite, 0, Collisions(main_platform_sprite), name="Floor")
    )


def create_background():
    game_obj["background"].append(
        Background((screen_width / 2, screen_height / 2), background_sprite)
    )


def start_game():
    clear_screen()
    create_main_platform()
    create_player()
    create_background()


def stop_game():
    player.velocity = (0, -5)
    player.collisions.collide_with = []


def create_menu():
    create_background()
    text_obj["menu"].append(
        Background((screen_width / 2, 200), text_back)
    )
    text_obj["menu"].append(
        GameText((screen_width / 2, 200), font, "Press ENTER to Start!", (200, 150, 0)))


create_menu()

while running:
    # Setting games bg color
    screen.fill((0, 0, 0))

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == GameEvents.player_died:
            stop_game()
            in_menu = True
            playing = False

        # Menu events
        if in_menu:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    start_game()
                    in_menu = False
                    playing = True

    # Rendering all gameobjects from GameObject modules list game_obj
    for list in game_obj:
        for obj in game_obj[list]:
            obj.render(screen)

####################################################################################

    if playing:
        # Find player
        player = find_object_by_name("Player")

        # Player inputs
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and player.is_grounded:
            player.velocity = (0, -15)

        if keys[pygame.K_RIGHT] and player.collisions.hitbox.right < screen_width:
            player.velocity = (5, player.velocity[1])

        if keys[pygame.K_LEFT] and player.collisions.hitbox.left > 0:
            player.velocity = (-5, player.velocity[1])

        # Moving all platforms and spikes
        for platform in game_obj["platform"]:
            if(platform.name != "Floor"):
                platform.move((-1, 0), 4)

        # Spawn obstacles
        if(obstacle_timer.do_action(pygame.time.get_ticks())):
            obstacle_timer.interval = spawn_obstacle(
                randint(0, len(presets) - 1))

        # Render GameText (game)
        for txt in text_obj["game"]:
            txt.render(screen)

        # Update platforms to player collide list
        player.collisions.add_to_collide_with_list(game_obj["platform"])

        # DEBUG/DEVELOP MODE
        # render_hitboxes(screen)
        # display_fps(screen, clock)

####################################################################################

    if in_menu:

        # Render GameText (menu)
        for txt in text_obj["menu"]:
            txt.render(screen)

####################################################################################

    # Updating whole display
    pygame.display.update()

    # Capping FPS
    clock.tick(90)
