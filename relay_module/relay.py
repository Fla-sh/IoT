from relay_module import relay_controller
from relay_module import command
from blueToothRadar import scanner_reader


def switch_after_scan():
    states = scanner_reader.read()
    for switch in states:
        print(switch, states[switch])
        c = command.Command("set", switch, states[switch])
        relay_controller.Relay(c).parse()
