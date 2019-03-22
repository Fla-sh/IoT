from blueToothRadar import scanner_reader as scanner
from devices import KNOW_DEVICES
from relay_module import relay_controller
from jointConsole import joint_console as console
import datetime


class Controller:
    def __init__(self):
        self.console = console.Console()
        self.relay_states = dict()
        self.relay = relay_controller.Relay()

        self.console.write("{} Initialized".format(
            console.Tags.LIGHTS.value
        ))

    def update(self):
        self.new_devices_in_range()
        self.is_night()
        self.update_relay_states()

    def new_devices_in_range(self):
        self.console.write("{} checking for new devices".format(
            console.Tags.LIGHTS.value
        ))
        devices_in_range = scanner.read()
        for known_device in KNOW_DEVICES:
            switch_number = KNOW_DEVICES[known_device].get_switch_number()
            if known_device in devices_in_range:
                self.relay_states[switch_number] = "on"
            else:
                self.relay_states[switch_number] = "off"

    def is_night(self):
        self.console.write("{} checking if is is night".format(
            console.Tags.LIGHTS.value
        ))
        now = datetime.datetime.now()
        if now.hour >= 23 and now.hour < 7:
            return True
        else:
            return False

    def update_relay_states(self):
        self.console.write("{} updating switches".format(
            console.Tags.LIGHTS.value
        ))
        for switch_number in self.relay_states:
            if self.relay_states[switch_number] == "on":
                self.relay.on(switch_number)
            else:
                self.relay.off(switch_number)
