import subprocess
import tempfile
import datetime
import devices
import os
import threading
from jointConsole import joint_console as console
from jointConsole import colors

detection_threshold = -80


def avg(list):
    sum = 0
    for e in list:
        sum += int(e)
    return sum / len(list)


def scanner():
    """
    scan for new devices
    if device was found function evaluate avarange of its rssi
    :return:
    """
    # it's file in which scanner holds btmgmt output
    tmp = tempfile.NamedTemporaryFile()
    with open(tmp.name, "w") as file:
        subprocess.run(["/usr/bin/btmgmt", "find"], stdout=file)
        file.close()
    # read results of command run
    with open(tmp.name, "r") as file:
        output = file.readlines()
        # print(output)
        result = dict()
        for line in output:
            words = line.split(" ")
            device_address = str()
            device_rssi = int()
            for i in range(len(words)):
                # loop through one line of output to find device name and corresponding rssi
                if words[i] == "dev_found:":
                    device_address = words[i + 1]
                elif words[i] == "rssi":
                    device_rssi = words[i + 1]
            # check if device was previously found
            if device_address in result:
                result[device_address].append(device_rssi)
            else:
                result[device_address] = [device_rssi]

        # print(result)

        # swap values in results form list of ints - rssi to it avg
        for device in result:
            result[device] = avg(result[device])

        # save results to file
        # and print to joint console
        with open("blueToothRadar/running_devices.txt", "w") as f:
            running_devices = list()
            for known_device in devices.KNOW_DEVICES:
                if known_device in result:
                    if result[known_device] > detection_threshold:
                        console.Console().write("{} Device {} {} {} with address {} {} {} detected {} its avarange RSSI is {} {} {}".format(
                            console.Tags.BLT_RAD.value,
                            colors.Colors.YELLOW.value,
                            devices.KNOW_DEVICES[known_device].get_name(),
                            colors.Colors.RESET.value,
                            colors.Colors.CYAN.value,
                            known_device,
                            colors.Colors.GREEN.value,
                            colors.Colors.RESET.value,
                            colors.Colors.BLUE.value,
                            int(result[known_device]),
                            colors.Colors.RESET.value))

                        running_devices.append(known_device + "\n")
                else:
                    console.Console().write("} Device {} {} {} with address {} {} {} not detected {}".format(
                        console.Tags.BLT_RAD.value,
                        colors.Colors.YELLOW.value,
                        devices.KNOW_DEVICES[known_device].get_name(),
                        colors.Colors.RESET.value, colors.Colors.CYAN.value,
                        known_device,
                        colors.Colors.RED.value,
                        colors.Colors.RESET.value))

            f.writelines(running_devices)
            f.close()
        # print()

        file.close()


if __name__ == "__main__":
    while True:
        scanner()
        # time.sleep(5)
