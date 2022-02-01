from modules.Animator import Animator
from modules.Collisions import Collisions
from modules.Player import Player
from modules.Platform import Platform


class PlayerRocket(Player):
    def __init__(self, transform: tuple, sprite, animator: Animator = 0, collitions: Collisions = 0, name="GameObject"):
        super().__init__(transform, sprite, animator, collitions, name)
        self.speed = 15
        self.jump_count = 0
        self.fall_time = 0

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
        self.check_for_platform()

        # Gravity like falling
        self.move((0, 1), ((self.fall_time) * 0.01)*9.81)
        self.fall_time += 1

    def check_for_platform(self):
        if(len(self.collitions.collition_list) > 0 and self.fall_time > 5):
            for obj in self.collitions.collition_list:
                if type(obj) == Platform:
                    self.jump_count = obj.power
