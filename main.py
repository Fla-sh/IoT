import threading
import os
import time
from blueToothRadar import radar
from jointConsole import colors


def setup():
    radar.Radar().start()


def loop():
    while True:
        relay.switch_after_scan()
        time.sleep(5)


if __name__ == "__main__":
    setup()
    loop()



