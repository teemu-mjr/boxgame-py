from modules.Animator import Animator
from modules.Collisions import Collisions
from modules.GameObject import GameObject
from modules.Platform import Platform


class PlatformJump(Platform):
    def __init__(self, transform: tuple, sprite, power: float, animator: Animator = 0, collitions: Collisions = 0, name="GameObject"):
        super().__init__(transform, sprite, animator, collitions, name)
        self.power = power
