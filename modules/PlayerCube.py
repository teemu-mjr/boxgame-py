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

        collition_obj = self.collisions.check_collisions(self)

        if (type(collition_obj) == Platform and self.collisions.check_collisions(self).name != "roof"):
            self.velocity = (0, 0)

        else:
            self.gravity((0, 1), (0, 0.5))
