import threading
import os
import time
from relay_module import relay
from jointConsole import colors

class Radar(threading.Thread):
    def run(self):
        os.system("/home/relay/IoT/venv/start")


def setup():
    Radar().start()


def loop():
    while True:
        relay.switch_after_scan()
        time.sleep(5)


if __name__ == "__main__":
    setup()
    loop()



