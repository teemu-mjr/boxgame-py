from modules.Animator import Animator
from modules.Collisions import Collisions
from modules.Platform import Platform
from modules.Player import Player


class PlayerCube(Player):
    def __init__(self, transform: tuple, sprite, animator: Animator = 0, collisions: Collisions = 0, use_gravity: bool = False, name="PlayerCube"):
        super().__init__(transform, sprite, animator, collisions, use_gravity, name)

    def after_render(self, screen):
        self.jump()

        collition_list = self.collisions.check_collisions(self)

        for obj in collition_list:
            if (obj.name == "Spike"):
                self.die()

            if (type(obj) == Platform and obj.name != "roof"):
                self.velocity = (self.velocity[0], 0)
