import RPi.GPIO as GPIO


class Relay:
    def __init__(self):
        self.relay_number_to_GPIO = {
            1 : 4,
            2 : 14,
            3 : 18,
            4 : 15,
            5 : 27,
            6 : 17,
            7 : 22,
            8 : 23,
            9 : 10,
            10 : 24,
            11 : 25,
            12 : 9,
            13 : 8,
            14 : 11,
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

    def on(self, relay_number):
        state = "on"
        pin_number = self.relay_number_to_GPIO[relay_number]
        state = self.relay_state_to_logical_state[state]
        self.set_pin_to_out(pin_number)
        GPIO.output(pin_number, state)
        print("Switched pin {} to {}".format(pin_number, GPIO.input(pin_number)))

    def off(self, relay_number):
        state = "off"
        pin_number = self.relay_number_to_GPIO[relay_number]
        state = self.relay_state_to_logical_state[state]
        self.set_pin_to_out(pin_number)
        GPIO.output(pin_number, state)
        print("Switched pin {} to {}".format(pin_number, GPIO.input(pin_number)))

    #def set_state(self, pin_number, state):

    def setup_switch(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

    def set_pin_to_in(self, pin_number):
        GPIO.setup(pin_number, GPIO.IN)

    def set_pin_to_out(self, pin_number):
        GPIO.setup(pin_number, GPIO.OUT)
