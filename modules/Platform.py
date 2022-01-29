from modules.Animator import Animator
from modules.Collitions import Collitions
from modules.GameObject import GameObject


class Platform(GameObject):
    def __init__(self, transform: tuple, sprite, power: float, animator: Animator = 0, collitions: Collitions = 0, name="GameObject"):
        super().__init__(transform, sprite, animator, collitions, name)
        self.power = power

        self.append_to_list("platform")
