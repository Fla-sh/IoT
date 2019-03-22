from blueToothRadar import scanner_reader as scanner
from devices import KNOW_DEVICES
from relay_module import relay_controller
import datetime


class Controller:
    def __init__(self):
        self.relay_states = dict()
        self.relay = relay_controller.Relay()

    def update(self):
        self.new_devices_in_range()
        self.is_night()
        self.update_relay_states()

    def new_devices_in_range(self):
        devices_in_range = scanner.read()
        for known_device in KNOW_DEVICES:
            switch_number = known_device.get_switch_number()
            if known_device in devices_in_range:
                self.relay_states[switch_number] = "on"
            else:
                self.relay_states[switch_number] = "off"

    def is_night(self):
        now = datetime.datetime.now()
        if now.hour >= 23 and now.hour < 7:
            return True
        else:
            return False

    def update_relay_states(self):
        for switch_number in self.relay_states:
            if self.relay_states[switch_number] == "on":
                self.relay.on(switch_number)
            else:
                self.relay.off(switch_number)
