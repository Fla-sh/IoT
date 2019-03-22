import os
import threading


class Radar(threading.Thread):
    def run(self):
        cwd = os.getcwd()
        os.system(cwd + "/start")
