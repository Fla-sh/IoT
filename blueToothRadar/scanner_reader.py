from blueToothRadar import devices
from jointConsole import colors
from jointConsole import joint_console as console
import datetime


def read():
    switches_states = dict()
    with open("blueToothRadar/running_devices.txt", "r") as file:
        data = file.readlines()
        file.close()

    for device_address in devices.KNOW_DEVICES:
        switch_number = str(devices.KNOW_DEVICES[device_address].get_switch_number())
        is_device_found = False
        for line in data:
            if line.find(device_address) != -1:
                console.Console().write("{} {} {} {} Switch no. {} {} {} set to state {} on {}".format(
                    colors.Colors.BOLD.value, datetime.datetime.now(), colors.Colors.RESET.value, console.Tags.BLT_RAD.value, colors.Colors.YELLOW.value, switch_number,
                    colors.Colors.RESET.value, colors.Colors.GREEN.value, colors.Colors.RESET.value))
                switches_states[switch_number] = "on"
                is_device_found = True
                break
        if not is_device_found:
            console.Console().write("{} {} {} {} Switch no. {} {} {} set to state {} off {}".format(
                colors.Colors.BOLD.value, datetime.datetime.now(), colors.Colors.RESET.value, console.Tags.BLT_RAD.value, colors.Colors.YELLOW.value, switch_number, colors.Colors.RESET.value, colors.Colors.RED.value, colors.Colors.RESET.value))
            switches_states[switch_number] = "off"

    return switches_states
