class Command:
    def __init__(self, mode, relay_number, state):
        self.mode = mode #set or state
        self.relay_number = relay_number #as stated
        self.state = state #on or off
