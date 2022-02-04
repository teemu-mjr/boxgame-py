import pygame
import sys
# Importing used modules from Modules folder
from modules.Collisions import Collisions
from modules.PlayerCube import PlayerCube
from modules.Platform import Platform
from modules.Background import Background

# DEVELOPING/TESTING
from fps_meter import display_fps


# Initializing pygame
pygame.init()
clock = pygame.time.Clock()

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
    "all": [],
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
    main_platform_sprite[0], (screen_width, 150))

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
test_platform = Platform((0, 0), platform_sprite, 0,
                         Collisions(platform_sprite))
game_obj["platform"].append(test_platform)

# Main loop booleans
running = True

# Game functions


def render_hitboxes(screen):
    for list in game_obj:
        for obj in game_obj[list]:
            if(obj.collisions != 0):
                obj.collisions.draw(screen)


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
        Platform((screen_width / 2, screen_height - 75),
                 main_platform_sprite, 0, Collisions(main_platform_sprite), name="Floor")
    )


def create_background():
    game_obj["background"].append(
        Background((screen_width / 2, screen_height / 2), background_sprite)
    )


def start_game():
    create_main_platform()
    create_player()
    create_background()


def follow_mouse(obj):
    obj.transform = pygame.mouse.get_pos()


# Init game and start main loop
start_game()

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

    if keys[pygame.K_SPACE] and player.is_grounded:
        player.velocity = (0, -15)

    if keys[pygame.K_RIGHT] and player.collisions.hitbox.right < screen_width:
        player.velocity = (5, player.velocity[1])

    if keys[pygame.K_LEFT] and player.collisions.hitbox.left > 0:
        player.velocity = (-5, player.velocity[1])

    # Rendering all gameobjects from GameObject modules list game_obj
    for list in game_obj:
        for obj in game_obj[list]:
            obj.render(screen)

    # DEBUG/DEVELOP MODE
    render_hitboxes(screen)
    display_fps(screen, clock)
    follow_mouse(test_platform)

    # Update platforms to player collide list
    for player in game_obj["player"]:
        player.collisions.add_to_collide_with_list(game_obj["platform"])

    # Updating whole display
    pygame.display.update()

    # Capping FPS
    clock.tick(90)
