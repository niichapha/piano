from entity.midi_event import Event

def from_midi_to_event(midi_event):
    message, deltatime = midi_event
    midi_event = Event(message[0], message[1], message[2], deltatime)
    return midi_event
