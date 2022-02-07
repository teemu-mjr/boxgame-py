from modules.IntervalTimer import IntervalTimer


class Animator:
    def __init__(self, animate: bool, animation_len: int, animation_speed: float):
        self.animate = animate
        self.animation_len = animation_len
        self.animation_speed = animation_speed
        self.animation_timer = IntervalTimer(animation_speed)
        self.animation_index = 0
        self.clock = 0

    def run(self):
        if(self.animate == False):
            return self.animation_index

        if (self.animation_timer.do_action()):
            if (self.animation_index < self.animation_len):
                self.animation_index += 1
            else:
                self.animation_index = 0

        return self.animation_index
