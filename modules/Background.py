from modules.GameObject import GameObject


class Background(GameObject):
    def __init__(self, transform: tuple, sprite, moving: bool = False, has_collitions: bool = False, name="GameObject"):
        super().__init__(transform, sprite, has_collitions, name)

        self.moving = moving

        self.append_to_list("background")

    def after_render(self, screen):
        if (not self.moving):
            return

        self.move((0, 1), 0.2)
        if(self.transform[1] + self.sprite.get_height() > screen.get_height()):
            self.move((0, -1), self.sprite.get_height())
