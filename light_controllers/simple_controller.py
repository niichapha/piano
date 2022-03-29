from .light_controller import LightController
class SimpleController(LightController):

    def process_event(self, event):
        self.update_colors(event.isDown())
