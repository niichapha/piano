import sys
import queue

from light_controllers import simple_controller, rainbow_controller
from lights_api import mock_api
from inputs.midi_input import MidiInput
from use_cases.event_queue_runner import EventQueueRunner

api = mock_api.MockApi(100)

if len(sys.argv) > 1 and sys.argv[1]=='rainbow':
   lights_controller = rainbow_controller.RainbowController(api)
else:
   lights_controller = simple_controller.SimpleController(api, (244,0,0), (0,0,255))

event_queue = queue.Queue(1024)
midi_input = MidiInput(event_queue)
runner = EventQueueRunner(event_queue, lights_controller)
runner.run()
