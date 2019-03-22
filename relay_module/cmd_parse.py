import argparse
import sys
import relay_controller

class CMDParse:
    def __init__(self, argv):
        self.parser = argparse.ArgumentParser()
        self.argv = argv
        self.settings = dict()

    def parse(self):
        parser = self.setup_argparse()
        namespace = parser.parse_args(self.argv)
        relay_number = int(namespace.relay_number)
        state = namespace.state

        if state == "on":
            relay_controller.Relay().on(relay_number)
        else:
            relay_controller.Relay().off(relay_number)

    def setup_argparse(self) -> argparse.ArgumentParser:
        description = "Set of commands to control the relay"
        epilog = "An epilog"
        prog = "relay"
        relay_numbers = [str(x) for x in range(0, 28)]

        parser = argparse.ArgumentParser(description=description, epilog=epilog, prog=prog)

        parser.add_argument("relay_number", choices=relay_numbers, help="Relay number to which action refers")

        parser.add_argument("-s", "--state", choices=["on", "off"], help="State to which relay should be set", default="None")
        return parser
