from modules.Animator import Animator
from modules.Collisions import Collisions
from modules.Platform import Platform
from modules.Player import Player
from modules.ScoreText import ScoreText


class PlayerCube(Player):
    def __init__(self, transform: tuple, sprite, animator: Animator = 0, collisions: Collisions = 0, use_gravity: bool = False, name="PlayerCube"):
        super().__init__(transform, sprite, animator, collisions, use_gravity, name)
        self.is_grounded = False

    def after_render(self, screen):
        if(self.transform[0] < 0 and self.is_alive):
            self.die()

        collision_list = self.collisions.check_collisions()
        self.jump()

        # No collisions
        if len(collision_list) <= 0:
            self.is_grounded = False

        # Collision
        for coll in collision_list:
            # Check if colliding from bottom
            if((0, 1) in coll.directions):
                self.is_grounded = True
            else:
                self.is_grounded = False

            if (coll.obj.name == "Spike"):
                self.die()

            if (self.is_grounded):
                self.velocity = (self.velocity[0], 0)

            # # If player is alive check if player is inside of the object
            if(self.is_alive):
                self.collisions.register(coll, self)
