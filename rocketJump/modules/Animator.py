class Animator:
    def __init__(self, animate: bool, animation_len: int, animation_speed: float, animation_interval: float):
        self.animate = animate
        self.animation_len = animation_len
        self.animation_speed = animation_speed
        self.animation_interval = animation_interval
        self.animation_index = 0
        self.clock = 0

    def run(self):
        if(self.animate == False):
            return self.animation_index

        self.clock += self.animation_speed

        if self.clock >= self.animation_interval:
            if self.animation_index >= self.animation_len - 1:
                self.animation_index = 0
            else:
                self.animation_index += 1

            self.clock = 0

        return self.animation_index
