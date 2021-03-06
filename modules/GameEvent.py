import pygame


class GameEvents:
    pause_game = pygame.USEREVENT + 0
    start_game = pygame.USEREVENT + 1
    restart_game = pygame.USEREVENT + 2
    player_died = pygame.USEREVENT + 3
    spawn_ground = pygame.USEREVENT + 4
    game_obj_deleted = pygame.USEREVENT + 5


def rase_event(event: GameEvents):
    pygame.event.post(pygame.event.Event(event))
