# library for processing midi inputs
from rtmidi import midiutil
from serializers import event_serializer

class MidiInput:
    def __init__(self, queue):
        self.event_queue = queue
        # initialize midi processing
        midiin = midiutil.open_midiinput(1)[0]
        midiin.set_callback(self)

    # function that gets called when midi signal is detected
    def __call__(self, midi_event, data=None):
        event = event_serializer.from_midi_to_event(midi_event)
        self.event_queue.put(event)
