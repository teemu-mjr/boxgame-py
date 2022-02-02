import pygame
from modules.Animator import Animator
from modules.Collisions import Collisions

# GameObjects
game_obj = {
    "background": [],
    "platform": [],
    "score": [],
    "game_objects": [],
    "player": [],
    "death": [],
}


class GameObject:
    def __init__(self, transform: tuple, sprite, animator: Animator = 0, collisions: Collisions = 0, use_gravity: bool = False, name="GameObject"):
        self.transform = transform
        self.animator = animator
        self.collisions = collisions
        self.sprite = sprite
        self.use_gravity = use_gravity
        self.name = name

        self.sprite_index = 0
        self.velocity = (0, 0)

    def append_to_list(self, key: str):
        game_obj[key].append(self)

    def render(self, screen):
        # Applying the objects velocity
        if(self.velocity != (0, 0)):
            self.move(self.velocity, 1)

        # Applying gravity
        if(self.use_gravity == True):
            self.gravity((0, 1), (0, 1))

        # Getting the center of the image
        sprite_transform = (
            self.transform[0] -
            (self.sprite[self.sprite_index].get_width() / 2),
            self.transform[1] -
            (self.sprite[self.sprite_index].get_height() / 2)
        )

        # Rendering the image
        screen.blit(self.sprite[self.sprite_index], sprite_transform)

        # If the object has collisions move them with the object
        if type(self.collisions) == Collisions:
            self.collisions.move(sprite_transform)

        # Run animations
        if type(self.animator) == Animator:
            self.sprite_index = self.animator.run()

        self.after_render(screen)

    def gravity(self, direction: tuple, acceleration: tuple):
        self.velocity = (
            ((self.velocity[0] + acceleration[0]) * direction[0]),
            ((self.velocity[1] + acceleration[1]) * direction[1])
        )

    def move(self, direction: tuple, speed: float = 1):
        self.transform = (
            self.transform[0] + (direction[0] * speed),
            self.transform[1] + (direction[1] * speed),
        )

    def transform_self(self, value: tuple):
        self.transform = (
            (self.transform[0] + (value[0])),
            (self.transform[1] + (value[1])),
        )

    def after_render(self, screen):
        pass

    def delete(self):
        for list in game_obj:
            if(self in game_obj[list]):
                game_obj[list].remove(self)
                return
