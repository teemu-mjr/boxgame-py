from pygame import Rect
import pygame


class Collitions:
    def __init__(self, sprite, draw_hitbox: bool = False, hitbox_color: type = (0, 255, 0)):
        self.sprite = sprite
        self.draw_hitbox = draw_hitbox
        self.hitbox = Rect(0, 0, self.sprite[0].get_width(),
                           self.sprite[0].get_height())
        self.hitbox_color = hitbox_color
        self.collition_list = []

    def move(self, transform: tuple):
        # Move hitbox to objects position
        self.hitbox.left = transform[0]
        self.hitbox.top = transform[1]

    def draw(self, screen):
        if (screen != 0 and self.draw_hitbox):
            pygame.draw.rect(screen, self.hitbox_color, self.hitbox, 4)

    def check_collitions(self):
        for obj in self.collition_list:
            if not self.hitbox.colliderect(obj.collitions.hitbox):
                self.collition_list.remove(obj)

    def at_collition(self, collided_obj):
        for obj in self.collition_list:
            if obj == collided_obj:
                return

        if (self.hitbox.colliderect(collided_obj.collitions.hitbox)):
            self.collition_list.append(collided_obj)
