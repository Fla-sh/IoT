import devices
from jointConsole import colors
from jointConsole import joint_console as console
import datetime


def read():
    found_devices = list()
    with open("blueToothRadar/running_devices.txt", "r") as file:
        data = file.readlines()
        file.close()

    for known_device_address in devices.KNOW_DEVICES:
        for line in data:
            if line.find(known_device_address) != -1:
                found_devices.append(known_device_address)
                break

    return found_devices
