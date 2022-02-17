class MockApi:
    def __init__(self, num_lights):
        self.lights = list();
        self.num_lights = num_lights
        self.set_all((0,0,0))
        print("created",num_lights,"lights")

    def set_light(self, light_index, color):
        self.lights[light_index] = color
        print("Set light",light_index,"to",color)

    def set_all(self, color):
        for i in range(0,self.num_lights):
           if (i >= len(self.lights)):
               self.lights.append(color)
           else:
               self.lights[i] = color

    def get_num_lights(self):
        return self.num_lights
