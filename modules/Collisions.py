import pygame


class Collision:
    def __init__(self, obj, directions: list):
        self.obj = obj
        self.directions = directions


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

    def is_colliding_bottom(self, obj):
        if (self.hitbox.top < obj.collisions.hitbox.top and
            self.hitbox.top < obj.collisions.hitbox.bottom and
            self.hitbox.bottom < obj.collisions.hitbox.bottom and
            (self.hitbox.right > obj.collisions.hitbox.left or
                self.hitbox.left < obj.collisions.hitbox.right)):
            return True
        else:
            return False

    def is_colliding_right(self, obj):
        if(self.hitbox.left < obj.collisions.hitbox.left and
           self.hitbox.left < obj.collisions.hitbox.right and
           self.hitbox.right < obj.collisions.hitbox.right and
           (self.hitbox.top < obj.collisions.hitbox.bottom or
                self.hitbox.bottom > obj.collisions.hitbox.top)):
            return True
        else:
            return False

    def is_colliding_left(self, obj):
        if(self.hitbox.right > obj.collisions.hitbox.right and
           self.hitbox.right > obj.collisions.hitbox.left and
           self.hitbox.left > obj.collisions.hitbox.left and
           (self.hitbox.top < obj.collisions.hitbox.bottom or
                self.hitbox.bottom > obj.collisions.hitbox.top)):
            return True
        else:
            return False

    def is_colliding_top(self, obj):
        if(self.hitbox.bottom > obj.collisions.hitbox.bottom and
           self.hitbox.bottom > obj.collisions.hitbox.top and
           self.hitbox.top > obj.collisions.hitbox.top and
           (self.hitbox.left < obj.collisions.hitbox.right or
                self.hitbox.right > obj.collisions.hitbox.left)):
            return True
        else:
            return False

    def check_collisions(self):
        collision_list = []
        for obj in self.collide_with:
            if (self.hitbox.bottom >= obj.collisions.hitbox.top and self.hitbox.left <= obj.collisions.hitbox.right and self.hitbox.right >= obj.collisions.hitbox.left and self.hitbox.top <= obj.collisions.hitbox.bottom):
                directions = []

                # Collition from BOTTOM
                if self.is_colliding_bottom(obj):
                    directions.append((0, 1))

                # Collition from RIGHT
                if self.is_colliding_right(obj):
                    directions.append((1, 0))

                # Collition from LEFT
                if self.is_colliding_left(obj):
                    directions.append((-1, 0))

                # Collition from TOP
                if self.is_colliding_top(obj):
                    directions.append((0, -1))

                # Append the object to collision list
                collision_list.append(Collision(obj, directions))

        # Return the list of all collitions
        return collision_list

    def register(self, coll: Collision, object_checking):
        """"NOT READY!"""

        if ((0, 1) in coll.directions and self.hitbox.bottom > coll.obj.collisions.hitbox.top and self.hitbox.bottom < coll.obj.collisions.hitbox.top + 25):
            # Move UP
            object_checking.transform_self((0, coll.obj.collisions.hitbox.top -
                                           self.hitbox.bottom))

        if ((1, 0) in coll.directions and self.hitbox.right > coll.obj.collisions.hitbox.left and self.hitbox.bottom > coll.obj.collisions.hitbox.top + 25):
            object_checking.transform_self((coll.obj.collisions.hitbox.left -
                                           self.hitbox.right, 0))

        if ((-1, 0) in coll.directions and self.hitbox.left < coll.obj.collisions.hitbox.right and self.hitbox.bottom > coll.obj.collisions.hitbox.top + 25):
            object_checking.transform_self((coll.obj.collisions.hitbox.right -
                                           self.hitbox.left, 0))
