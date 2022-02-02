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
            if(obj.collisions != 0 and obj not in self.collide_with):
                self.collide_with.append(obj)

    def move(self, transform: tuple):
        # Move hitbox to given position
        self.hitbox.left = transform[0] + self.hitbox_add_size[0]
        self.hitbox.top = transform[1] + self.hitbox_add_size[1]

    def draw(self, screen):
        if (screen != 0):
            pygame.draw.rect(screen, self.hitbox_color, self.hitbox, 4)

    def check_collisions(self):
        collision_list = []
        for obj in self.collide_with:
            if (self.hitbox.bottom >= obj.collisions.hitbox.top and self.hitbox.left <= obj.collisions.hitbox.right and self.hitbox.right >= obj.collisions.hitbox.left and self.hitbox.top <= obj.collisions.hitbox.bottom):
                # Append the object to collision list
                collision_list.append(obj)

        # Return the list of all collitions
        return collision_list

    def move_out_of_object(self, obj_list, object_checking):
        for obj in obj_list:
            # FROM TOP OR BOTTOM
            if(abs(obj.collisions.hitbox.top - self.hitbox.bottom) < abs(obj.collisions.hitbox.bottom - self.hitbox.top)):
                # TOP
                if (self.hitbox.bottom - 2 > obj.collisions.hitbox.top and self.hitbox.left < obj.collisions.hitbox.right and self.hitbox.right > obj.collisions.hitbox.left and self.hitbox.top < obj.collisions.hitbox.bottom):
                    # Move out of the object
                    object_checking.transform_self(
                        (0, obj.collisions.hitbox.top - self.hitbox.bottom - 5))
            # else:
            #     # BOTTOM
            #     if (self.hitbox.bottom > obj.collisions.hitbox.top and self.hitbox.left < obj.collisions.hitbox.right and self.hitbox.right > obj.collisions.hitbox.left and self.hitbox.top < obj.collisions.hitbox.bottom - 2):
            #         # Move out of the object
            #         object_checking.transform_self(
            #             (0, obj.collisions.hitbox.bottom - self.hitbox.top - 5))
