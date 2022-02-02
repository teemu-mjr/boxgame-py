from modules.Animator import Animator
from modules.Collisions import Collisions
from modules.GameObject import GameObject


class Platform(GameObject):
    def __init__(self, transform: tuple, sprite, animator: Animator = 0, collisions: Collisions = 0, use_gravity: bool = False, name="Platform"):
        super().__init__(transform, sprite, animator, collisions, use_gravity, name)

        self.append_to_list("platform")
