from modules.Animator import Animator
from modules.Collisions import Collisions
from modules.GameObject import GameObject


class Platform(GameObject):
    def __init__(self, transform: tuple, sprite, animator: Animator = 0, collisions: Collisions = 0, name="GameObject"):
        super().__init__(transform, sprite, animator, collisions, name)

        self.append_to_list("platform")
