from modules.GameObject import GameObject


class Platform(GameObject):
    def __init__(self, transform: tuple, sprite, power: float, animator, has_collitions: bool = False, name="GameObject"):
        super().__init__(transform, sprite, animator, has_collitions, name)
        self.power = power

        self.append_to_list("platform")
