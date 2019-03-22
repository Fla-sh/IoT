
class Device():
    def __init__(self, name, id, switch_number):
        self._name = name
        self._id = id
        self._switch_number = switch_number

    def get_name(self):
        return self._name

    def get_id(self):
        return self._id

    def get_switch_number(self):
        return self._switch_number


KNOW_DEVICES = {
    "E4:A7:C5:B5:69:51": Device("Huawei P20", 1, 2),
    "94:7B:E7:6E:FD:04": Device("Galaxy J5", 2, 10)
}
