import devices
from jointConsole import colors
from jointConsole import joint_console as console


def read():
    console.Console().write("{} Reading running_devices.txt".format(
        console.Tags.BLT_RAD.value
    ))

    found_devices = list()
    with open("blueToothRadar/running_devices.txt", "r") as file:
        data = file.readlines()
        file.close()

    for known_device_address in devices.KNOW_DEVICES:
        for line in data:
            if line.find(known_device_address) != -1:
                found_devices.append(known_device_address)
                break

    console.Console().write("{} running_devices.txt contained {} {} {}".format(
        console.Tags.BLT_RAD.value,
        colors.Colors.YELLOW.value,
        found_devices,
        colors.Colors.RESET
    ))

    return found_devices
