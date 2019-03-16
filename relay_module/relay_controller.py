import RPi.GPIO as GPIO
from jointConsole import joint_console as console

"""
def change(pin):
    GPIO.output(pin, not GPIO.input(pin))
    print("Changed pin no. {}".format(pin))
    print("New state is: {}".format(str(GPIO.input(pin))))


def setup():
    print(GPIO.VERSION)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(list(range(1, 28)), GPIO.OUT)
    GPIO.output(list(range(1, 28)), GPIO.HIGH)


setup()
# while True:
#    chanel = int(input("Chanel number"))
#    change(chanel)
"""


class Relay:

    def __init__(self, command):
        self.command = command
        self.relay_number_to_GPIO = {
            1 : 4,
            2 : 14,
            3 : 17,
            4 : 15,
            5 : 27,
            6 : 18,
            7 : 22,
            8 : 23,
            9 : 24,
            10 : 10,
            11 : 9,
            12 : 25,
            13 : 11,
            14 : 8,
            15 : 5,
            16 : 7
        }
        self.logical_state_to_relay_state = {
            0: "on",
            1: "off"
        }
        self.relay_state_to_logical_state = {
            "on": 0,
            "off": 1
        }
        self.setup_switch()

    def parse(self):
        pin_number = self.relay_number_to_GPIO[int(self.command.relay_number)]
        if self.command.mode == "set":
            state = self.relay_state_to_logical_state[self.command.state]
            self.switch(pin_number, state)
            console.Console().write("{} Switched relay no. {} on pin no. {} to state {} and is now in sate {}".format(console.Tags.REL_MOD.value, self.command.relay_number, pin_number, state, self.command.state))
        elif self.command.mode == "state":
            #console.Console().write(self.logical_state_to_relay_state[self.state(pin_number)])
            console.Console().write("{} Not implemented".format(console.Tags.REL_MOD.value, ))

    def switch(self, pin_number, state=None):
        self.set_pin_to_out(pin_number)
        if state is None:
            GPIO.output(pin_number, not GPIO.input(pin_number))
            console.Console().write("{} Switched pin {} to {}".format(console.Tags.REL_MOD.value, pin_number, GPIO.input(pin_number)))
        else:
            if state == 1:
                GPIO.output(pin_number, state)
                console.Console().write("{} Switched pin {} to {}".format(console.Tags.REL_MOD.value, pin_number, GPIO.input(pin_number)))
            elif state == 0:
                GPIO.output(pin_number, state)
                console.Console().write("{} Switched pin {} to {}".format(console.Tags.REL_MOD.value, pin_number, GPIO.input(pin_number)))

            else:
                console.Console().write("{} State {} is wrong".format(console.Tags.REL_MOD.value, state))

    #def set_state(self, pin_number, state):

    def setup_switch(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

    def set_pin_to_in(self, pin_number):
        GPIO.setup(pin_number, GPIO.IN)

    def set_pin_to_out(self, pin_number):
        GPIO.setup(pin_number, GPIO.OUT)
