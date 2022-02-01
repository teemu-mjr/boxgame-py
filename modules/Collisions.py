import pygame


class Collisions:
    def __init__(self, sprite, hitbox_add_size: tuple = (0, 0, 0, 0), hitbox_color: tuple = (0, 255, 0)):
        self.sprite = sprite
        self.hitbox_add_size = hitbox_add_size
        self.hitbox = pygame.rect.Rect(hitbox_add_size[0], hitbox_add_size[1], self.sprite[0].get_width() + hitbox_add_size[2],
                                       self.sprite[0].get_height() + hitbox_add_size[3])

        self.hitbox_color = hitbox_color
        self.collide_with = []

    def add_to_collide_with_list(self, items_to_add):
        for obj in items_to_add:
            if(obj.collisions != 0):
                self.collide_with.append(obj)

    def move(self, transform: tuple):
        # Move hitbox to given position
        self.hitbox.left = transform[0] + self.hitbox_add_size[0]
        self.hitbox.top = transform[1] + self.hitbox_add_size[1]

    def draw(self, screen):
        if (screen != 0):
            pygame.draw.rect(screen, self.hitbox_color, self.hitbox, 4)

    def check_collisions(self, object_checking):
        for obj in self.collide_with:
            if (self.hitbox.bottom >= obj.collisions.hitbox.top and self.hitbox.left <= obj.collisions.hitbox.right and self.hitbox.right >= obj.collisions.hitbox.left and self.hitbox.top <= obj.collisions.hitbox.bottom):
                self.move_out_of_object(obj, object_checking)
                return obj

        return False

    def move_out_of_object(self, obj, object_checking):
        # FROM TOP OR BOTTOM
        if(abs(obj.collisions.hitbox.top - self.hitbox.bottom) < abs(obj.collisions.hitbox.bottom - self.hitbox.top)):
            # TOP
            object_checking.transform_self(
                (0, obj.collisions.hitbox.top - self.hitbox.bottom))
        else:
            # BOTTOM
            object_checking.transform_self(
                (0, obj.collisions.hitbox.bottom - self.hitbox.top))

        # FROM LEFT OR RIGHT
        if(abs(obj.collisions.hitbox.left - self.hitbox.right) < abs(obj.collisions.hitbox.right - self.hitbox.left)):
            # LEFT
            print("left")
#            object_checking.transform_self(
#                (obj.collisions.hitbox.left - self.hitbox.right, 0))

        else:
            # RIGHT
            print("right")
#            object_checking.transform_self(
#                (obj.collisions.hitbox.right - self.hitbox.left, 0))
