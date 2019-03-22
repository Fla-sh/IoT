import threading
import os
import time
from blueToothRadar import radar
from jointConsole import colors
from lights import controller

def setup():
    radar.Radar().start()


def loop():
    while True:
        controller.Controller().update()
        time.sleep(5)


if __name__ == "__main__":
    setup()
    loop()



