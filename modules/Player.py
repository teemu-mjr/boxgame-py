import pygame
import modules.GameEvent as GameEvent
from modules.Animator import Animator
from modules.Collisions import Collisions
from modules.GameObject import GameObject


class Player(GameObject):
    def __init__(self, transform: tuple, sprite, animator: Animator = 0, collisions: Collisions = 0, use_gravity: bool = False, name="Player"):
        super().__init__(transform, sprite, animator, collisions, use_gravity, name)
        self.jump_count = 0
        self.is_alive = True

    def after_render(self, screen):
        pass

    def jump(self):
        if(self.jump_count <= 0):
            return

        self.velocity = (
            (self.velocity[0] - self.jump_count),
            (self.velocity[1])
        )

    def die(self):
        self.is_alive = False
        GameEvent.rase_event(GameEvent.GameEvents.player_died)
