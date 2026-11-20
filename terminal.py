# Small amount of utility functions to control the terminal interface with ANSI escape sequences


def clear_screen():
    print("\x1b[2J")


def go_to_home_position():
    print("\x1b[H")


def get_error_text(text: str) -> str:
    # color the given text in red and then reset to default
    return f"\x1b[31m{text}\x1b[39m"


def print_title():
    title = """
    ███████████
   ░░███░░░░░███
    ░███    ░███  ██████  ████████  ████████  █████ ████
    ░██████████  ███░░███░░███░░███░░███░░███░░███ ░███
    ░███░░░░░░  ░███████  ░███ ░░░  ░███ ░░░  ░███ ░███
    ░███        ░███░░░   ░███      ░███      ░███ ░███
    █████       ░░██████  █████     █████     ░░███████
   ░░░░░         ░░░░░░  ░░░░░     ░░░░░       ░░░░░███
                                               ███ ░███
                                              ░░██████
                                               ░░░░░░
    """
    print(title)
