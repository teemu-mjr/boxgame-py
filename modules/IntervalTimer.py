class IntervalTimer:
    def __init__(self, interval):
        self.interval = interval * 10
        self.last_action = 0

    def do_action(self, current_time):
        if(current_time - self.last_action >= self.interval):
            self.last_action = current_time
            return True

        return False
