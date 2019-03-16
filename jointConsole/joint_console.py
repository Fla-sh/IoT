import enum
from jointConsole import colors


class Console:
    def __init__(self):
        self.file_name = "jointConsole/console_log.txt"
        self.file_name2 = "jointConsole/console_log_continous.txt"

    def write(self, data):
        with open(self.file_name, "w") as file:
            file.write(data)
            file.close()
        with open(self.file_name2, "a") as file:
            file.write(data)
            file.close()

    def read(self):
        with open(self.file_name, "r") as file:
            data = file.read()
            file.close()
        return data


class Tags(enum.Enum):
    REL_MOD = "{} <REL_MOD> {}".format(colors.Colors.PINK.value, colors.Colors.RESET.value)
    BLT_RAD = "{} <BLT_RAD> {}".format(colors.Colors.PINK.value, colors.Colors.RESET.value)
