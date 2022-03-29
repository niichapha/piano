DOWN = 144
class Event:
    def __init__(self, state, key, velocity, deltatime):
        self.state = state
        self.key = key
        self.velocity = velocity
        self.time_delta = deltatime

    def is_down(self):
        return self.state == DOWN 

    def get_key(self):
        return self.key

    def get_velocity(self):
        return self.velocity

    def get_time_delta(self):
        return self.time_delta
