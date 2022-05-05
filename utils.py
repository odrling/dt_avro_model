from time import time_ns


def time():
    return time_ns() // 1000_000

