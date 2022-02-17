class MockApi:
   def __init__(self, num_lights):
      self.num_lights = num_lights
      print("created",num_lights,"lights")

   def set_light(self, light_index, color):
      print("Set light",light_index,"to",color)
