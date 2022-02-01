from modules.Animator import Animator
from modules.Collisions import Collisions
from modules.GameObject import GameObject
from modules.Platform import Platform


class Player(GameObject):
    def __init__(self, transform: tuple, sprite, animator: Animator = 0, collitions: Collisions = 0, name="GameObject"):
        super().__init__(transform, sprite, animator, collitions, name)
        self.velocity = (0, 0)
        self.jump_count = 0

        self.append_to_list("player")

    def after_render(self, screen):
        pass

    def jump(self):
        if(self.jump_count <= 0):
            return

        self.move((0, -1), self.jump_count + 10)
        self.jump_count -= 1

    def gravity(self, direction: object, acceleration: tuple):
        self.velocity = (
            (self.velocity[0] + acceleration[0]),
            (self.velocity[1] + acceleration[1])
        )
        self.move(self.velocity)
