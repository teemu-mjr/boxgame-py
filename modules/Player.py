from modules.Animator import Animator
from modules.Collitions import Collitions
from modules.GameObject import GameObject
from modules.Platform import Platform


class Player(GameObject):
    def __init__(self, transform: tuple, sprite, animator: Animator = 0, collitions: Collitions = 0, name="GameObject"):
        super().__init__(transform, sprite, animator, collitions, name)

        self.speed = 10
        self.jump_count = 0
        self.fall_time = 0

        self.append_to_list("player")

    def append_to_list(self, key: str):
        return super().append_to_list(key)

    def after_render(self, screen):
        if(self.transform[0] <= 0):
            new_transform = (screen.get_width() - 10, self.transform[1])
            self.transform = new_transform

        if(self.transform[0] >= screen.get_width()):
            new_transform = (10, self.transform[1])
            self.transform = new_transform
        # Jumping
        if(self.jump_count > 0):
            self.fall_time = 0
            self.jump()

        # Falling
        else:
            self.fall()

    def fall(self):
        # Check for Platforms
        if(len(self.collitions.collition_list) > 0 and self.fall_time > 5):
            for obj in self.collitions.collition_list:
                if type(obj) == Platform:
                    self.jump_count = obj.power
                    # obj.delete()

        # Gravity like falling
        self.move((0, 1), ((self.fall_time) * 0.01)*9.81)
        self.fall_time += 1

    def jump(self):
        self.move((0, -1), self.jump_count + 10)
        self.jump_count -= 1
