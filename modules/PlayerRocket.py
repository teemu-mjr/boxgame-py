from modules.Animator import Animator
from modules.Collisions import Collisions
from modules.Player import Player
from modules.PlatformJump import PlatformJump


class PlayerRocket(Player):
    def __init__(self, transform: tuple, sprite, animator: Animator = 0, collisions: Collisions = 0, name="GameObject"):
        super().__init__(transform, sprite, animator, collisions, name)
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
        obj = self.collisions.check_collisions(self)
        if(type(obj) == PlatformJump and self.fall_time > 5):
            self.jump_count = obj.power
