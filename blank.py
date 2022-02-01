import pygame
import sys

# Importing used modules from Modules folder
from modules.GameObject import game_obj
from modules.Text import text_obj

# Initializing pygame
pygame.init()

# Screen setup
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game Name")

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
