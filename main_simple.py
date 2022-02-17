import light_controller.simple_controller as simple_controller
import lights_api.mock_api as mock_api
from piano_lights import LightsFromPiano

api = mock_api.MockApi(100)
lights_controller = simple_controller.SimpleController(api, (244,0,0), (0,0,255))
piano_input = LightsFromPiano()
piano_input.run(lights_controller)
