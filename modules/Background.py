from modules.Animator import Animator
from modules.Collisions import Collisions
from modules.GameObject import GameObject


class Background(GameObject):
    def __init__(self, transform: tuple, sprite, moving: bool = False, animator: Animator = 0, collisions: Collisions = 0, use_gravity: bool = False, name="GameObject"):
        super().__init__(transform, sprite, animator, collisions, use_gravity, name)

        self.moving = moving

    def after_render(self, screen):
        if (not self.moving):
            return

        self.move((0, 1), 0.2)
        if(self.transform[1] + self.sprite.get_height() > screen.get_height()):
            self.move((0, -1), self.sprite.get_height())
