from .light_controller import LightController
class SimpleController(LightController):
    DOWN = 144
    def __init__(self, num_lights, color_on, color_off):
        self.__init__(num_lights, color_on, color_off)

    def process_event(self, event):
        message, deltatime = event
        state = message[0]
        print(message, deltatime)
        self.update_colors(state)
