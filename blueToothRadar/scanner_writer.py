import subprocess
import tempfile
import datetime
import devices
from jointConsole import joint_console as console
from jointConsole import colors

detection_threshold = -80

def avg(list):
    sum = 0
    for e in list:
        sum += int(e)
    return sum / len(list)


def scanner():
    tmp = tempfile.NamedTemporaryFile()
    with open(tmp.name, "w") as file:
        subprocess.run(["/usr/bin/btmgmt", "find"], stdout=file)
        file.close()
    with open(tmp.name, "r") as file:
        data = file.readlines()
        # print(data)
        result = dict()
        for line in data:
            words = line.split(" ")
            device_address = str()
            device_rssi = int()
            for i in range(len(words)):
                if words[i] == "dev_found:":
                    device_address = words[i + 1]
                elif words[i] == "rssi":
                    device_rssi = words[i + 1]
            if device_address in result:
                result[device_address].append(device_rssi)
            else:
                result[device_address] = [device_rssi]

        # print(result)

        for key in result:
            result[key] = avg(result[key])

        with open("blueToothRadar/running_devices.txt", "w") as f:
            running_devices = list()
            for device_address in devices.KNOW_DEVICES:
                if device_address in result:
                    if result[device_address] > detection_threshold:
                        console.Console().write("{} {} {} {} Device {} {} {} with address {} {} {} detected {} its avarange RSSI is {} {} {}".format(
                            colors.Colors.BOLD.value, datetime.datetime.now(), colors.Colors.RESET.value, console.Tags.BLT_RAD.value, colors.Colors.YELLOW.value, devices.KNOW_DEVICES[device_address].get_name(), colors.Colors.RESET.value, colors.Colors.CYAN.value, device_address, colors.Colors.GREEN.value, colors.Colors.RESET.value, colors.Colors.BLUE.value, int(result[device_address]), colors.Colors.RESET.value))
                        running_devices.append(device_address + "\n")
                else:
                    console.Console().write("{} {} {} {} Device {} {} {} with address {} {} {} not detected {}".format(
                        colors.Colors.BOLD.value, datetime.datetime.now(), colors.Colors.RESET.value, console.Tags.BLT_RAD.value, colors.Colors.YELLOW.value, devices.KNOW_DEVICES[device_address].get_name(), colors.Colors.RESET.value, colors.Colors.CYAN.value, device_address, colors.Colors.RED.value, colors.Colors.RESET.value))
            f.writelines(running_devices)
            f.close()
        # print()

        file.close()


if __name__ == "__main__":
    while True:
        scanner()
        # time.sleep(5)
