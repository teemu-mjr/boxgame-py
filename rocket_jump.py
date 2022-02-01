import pygame
import sys
from random import randint

# Importing all used modules from Modules folder
from modules.Animator import Animator
from modules.Background import Background
from modules.Collisions import Collisions
from modules.GameObject import game_obj
from modules.Player import Player
from modules.Platform import Platform
from modules.PlayerRocket import PlayerRocket
from modules.Score import ScoreText
from modules.Text import text_obj

# Initializing pygame
pygame.init()

# Screen setup
screen_width = 500
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jumper")


# Creating the player
player_sprite = [
    pygame.image.load("sprites/player.png").convert_alpha(),
]
player_sprite[0] = pygame.transform.scale(player_sprite[0], (50, 80))

player = PlayerRocket((screen_width / 2, screen_height / 2),
                      player_sprite, Animator(True, len(player_sprite), 1, 100), Collisions(player_sprite, False), "Player")

# Platforms
platform_interval = 10
platform_timer = platform_interval

platform_speed = 10
platform_speed_multiplyer = 1

platform_sprite = [
    pygame.image.load("sprites/platform.png").convert(),
]

platform_sprite = [
    pygame.transform.scale(platform_sprite[0], (100, 20)),
]


def spawn_platform(posX: int = 0):
    Platform((randint(0, screen_width), posX), platform_sprite,
             10, False, Collisions(platform_sprite, False))


def spawn_starting_platforms():
    for i in range(15):
        spawn_platform((i * 100) - 500)


spawn_starting_platforms()

# Score
score_font = pygame.font.SysFont('chalkduster.ttf', 72)
score = ScoreText((screen_width/2, 50), score_font, "", (255, 255, 255))

background_bottom_sprite = [
    pygame.image.load(
        "sprites/background_bottom.png").convert(),
]

background_bottom = Background(
    (screen_width/2, screen_height - background_bottom_sprite[0].get_height() / 2), background_bottom_sprite)

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

    if keys[pygame.K_RIGHT]:
        player.move((1, 0), 5)
    if keys[pygame.K_LEFT]:
        player.move((-1, 0), 5)

    # Rendering all gameobjects
    for list in game_obj:
        for obj in game_obj[list]:
            obj.render(screen)

    # Registering player collitions
    for obj in game_obj["platform"]:
        player.collitions.at_collition(obj)

    # Rendering all textobject
    for obj in text_obj:
        obj.render(screen)

    # If player is going up, move platforms and change score
    if(player.fall_time <= 0):
        platform_timer += 1
        for obj in game_obj["platform"]:
            obj.move((0, 1), platform_speed * platform_speed_multiplyer)

        score.add_score(1)

    if platform_timer >= platform_interval:
        spawn_platform(-500)
        platform_timer = 0

    # Keep player on screen
    if (player.transform[1] <= 150):
        player.transform = (player.transform[0], 150)
        platform_speed_multiplyer = 2

    elif(platform_speed_multiplyer != 1):
        platform_speed_multiplyer = 1

    # Updating whole display
    pygame.display.update()

    # Capping FPS
    pygame.time.Clock().tick(90)
