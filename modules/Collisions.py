from pygame import Rect
import pygame


class Collisions:
    def __init__(self, sprite, draw_hitbox: bool = False, hitbox_color: type = (0, 255, 0)):
        self.sprite = sprite
        self.draw_hitbox = draw_hitbox
        self.hitbox = Rect(0, 0, self.sprite[0].get_width(),
                           self.sprite[0].get_height())
        self.hitbox_color = hitbox_color
        self.collide_with = []

    def move(self, transform: tuple):
        # Move hitbox to given position
        self.hitbox.left = transform[0]
        self.hitbox.top = transform[1]

    def draw(self, screen):
        if (screen != 0 and self.draw_hitbox):
            pygame.draw.rect(screen, self.hitbox_color, self.hitbox, 4)

    def check_collitions(self, object_checking_for_collitions):
        for obj in self.collide_with:
            if (self.hitbox.bottom >= obj.collitions.hitbox.top and self.hitbox.left <= obj.collitions.hitbox.right and self.hitbox.right >= obj.collitions.hitbox.left and self.hitbox.top <= obj.collitions.hitbox.bottom):
                self.move_out_of_object(obj, object_checking_for_collitions)
                return obj

        return False

    def move_out_of_object(self, obj, object_checking_for_collitions):
        if (self.hitbox.bottom > obj.collitions.hitbox.top):
            object_checking_for_collitions.transform_self(
                (0, obj.collitions.hitbox.top - self.hitbox.bottom))
