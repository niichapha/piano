DOWN = 144
class Event:
   def __init__(self, state, key, velocity, deltatime):
      self.state = state
      self.key = key
      self.velocity = velocity
      self.time_delta = deltatime

   def isDown(self):
      return self.state == DOWN 

   def getKey(self):
      return self.key

   def getVelocity(self):
      return self.velocity

   def getTimeDelta(self):
      return self.time_delta
