from modules.Animator import Animator
from modules.Collitions import Collitions

# GameObjects
game_obj = {
    "background": [],
    "platform": [],
    "score": [],
    "game_objects": [],
    "player": [],
}


class GameObject:
    def __init__(self, transform: tuple, sprite, animator: Animator = 0, collitions: Collitions = 0, name="GameObject"):
        self.transform = transform
        self.animator = animator
        self.collitions = collitions
        self.sprite = sprite
        self.sprite_index = 0

        self.name = name

    def append_to_list(self, key: str):
        game_obj[key].append(self)

    def render(self, screen):
        # Getting the center of the image
        sprite_transform = (
            self.transform[0] -
            (self.sprite[self.sprite_index].get_width() / 2),
            self.transform[1] -
            (self.sprite[self.sprite_index].get_height() / 2)
        )

        # Rendering the image
        screen.blit(self.sprite[self.sprite_index], sprite_transform)

        if type(self.collitions) == Collitions:
            self.collitions.move(sprite_transform)
            self.collitions.check_collitions()
            self.collitions.draw(screen)

        # Idle animations
        if type(self.animator) == Animator:
            self.sprite_index = self.animator.run()

        self.after_render(screen)

    def move(self, input: tuple, speed: float = 1):
        self.transform = (
            self.transform[0] + (input[0] * speed),
            self.transform[1] + (input[1] * speed),
        )

    def after_render(self, screen):
        pass

    def delete(self):
        for list in game_obj:
            if(self in game_obj[list]):
                game_obj[list].remove(self)
                return
