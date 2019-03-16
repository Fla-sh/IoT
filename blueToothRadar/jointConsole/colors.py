import enum


class Colors(enum.Enum):
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    YELLOW = "\033[0;33m"
    CYAN = "\033[0;36m"
    BOLD = "\033[1;30m"
    BLUE = "\033[0;34m"
    PINK = "\033[0;35m"
    RESET = "\033[0m"
