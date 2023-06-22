from time import sleep


def run(n: int) -> int:
    print(f"This is test number {n}")
    sleep(1)
    return n + 1


if __name__ == "__main__":
    run(10)
