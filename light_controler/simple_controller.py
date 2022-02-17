from .light_controller import LightController
class SimpleController(LightController):
    DOWN = 144

    def process_event(self, event):
        message, deltatime = event
        state = message[0]
        print(message, deltatime)
        self.update_colors(state)
