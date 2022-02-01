from modules.Animator import Animator
from modules.Collisions import Collisions
from modules.GameObject import GameObject
from modules.Platform import Platform
from modules.Player import Player


class PlayerCube(Player):
    def __init__(self, transform: tuple, sprite, animator: Animator = 0, collitions: Collisions = 0, name="GameObject"):
        super().__init__(transform, sprite, animator, collitions, name)

    def after_render(self, screen):
        self.jump()

        if(not self.collitions.is_colliding_with_type(Platform)):
            self.gravity((0, 1), (0, 2))

        else:
            self.velocity = (0, 0)
