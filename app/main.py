"""The main application module
"""

from time import sleep


def run(number: int) -> int:
    """Runs the application

    Args:
        number (int): the number to test

    Returns:
        int: the test number incremented
    """
    print(f"This is test number {number}")
    sleep(1)
    return number + 1


if __name__ == "__main__":
    run(10)
