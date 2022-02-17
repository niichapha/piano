# libraries for controlling lights
import board
import neopixel

class Ws281x:
   def __init__(self, num_lights):
       self.num_lights = num_lights

       # initialize the lights array, turn all lights off
       self.pixels = neopixel.NeoPixel(board.D18,
                                       self.num_lights,
                                       brightness=1,
                                       pixel_order=neopixel.RGB)
       self.pixels.fill((0,0,0))

   def set_light(self, light_index, color):
       self.pixels[light_index] = color

   def set_all(self, color):
       self.pixels.fill(color)

   def get_num_lights(self):
       return self.num_lights
