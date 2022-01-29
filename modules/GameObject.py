from pygame import Rect

from modules.Animator import Animator

# GameObjects
game_obj = {
    "background": [],
    "platform": [],
    "score": [],
    "game_objects": [],
    "player": [],
}


class GameObject:
    def __init__(self, transform: tuple, sprite, animator: Animator = 0, has_collitions: bool = False, name="GameObject"):
        self.transform = transform
        self.has_collitions = has_collitions
        self.sprite = sprite
        self.sprite_index = 0
        self.animator = animator
        self.hitbox = Rect(0, 0, self.sprite[0].get_width(),
                           self.sprite[0].get_height())
        self.hitbox_color = (0, 255, 0)
        self.collition_list = []
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
        # Move hitbox to objects position
        self.hitbox.left = sprite_transform[0]
        self.hitbox.top = sprite_transform[1]

        # Rendering the image
        screen.blit(self.sprite[self.sprite_index], sprite_transform)

        if self.has_collitions:
            self.check_collitions()

        # Idle animations
        if type(self.animator) == Animator:
            self.sprite_index = self.animator.run()

        self.after_render(screen)

    def move(self, input: tuple, speed: float = 1):
        self.transform = (
            self.transform[0] + (input[0] * speed),
            self.transform[1] + (input[1] * speed),
        )

    def check_collitions(self):
        for obj in self.collition_list:
            if not self.hitbox.colliderect(obj.hitbox):
                self.collition_list.remove(obj)

    def at_collition(self, collided_obj):
        for obj in self.collition_list:
            if obj == collided_obj:
                return

        if (self.hitbox.colliderect(collided_obj.hitbox)):
            self.collition_list.append(collided_obj)

    def after_render(self, screen):
        pass

    def delete(self):
        for list in game_obj:
            if(self in game_obj[list]):
                game_obj[list].remove(self)
                return
