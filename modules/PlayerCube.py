from modules.Animator import Animator
from modules.Collisions import Collisions
from modules.Platform import Platform
from modules.Player import Player


class PlayerCube(Player):
    def __init__(self, transform: tuple, sprite, animator: Animator = 0, collisions: Collisions = 0, use_gravity: bool = False, name="PlayerCube"):
        super().__init__(transform, sprite, animator, collisions, use_gravity, name)
        self.is_grounded = False

    def after_render(self, screen):
        collition_list = self.collisions.check_collisions()
        self.jump()

        if(self.is_grounded and len(collition_list) <= 0):
            self.is_grounded = False

        elif(self.is_grounded == False and len(collition_list) > 0):
            self.is_grounded = True

        for obj in collition_list:
            if (obj.name == "Spike"):
                self.die()

            if (type(obj) == Platform and obj.name != "roof"):
                self.velocity = (self.velocity[0], 0)

        if(self.is_alive):
            # Check if player is inside of the object
            self.collisions.move_out_of_object(collition_list, self)
