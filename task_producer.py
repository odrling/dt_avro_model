import requests

from commands import Command, ElementEvent, Actions
from producer_from_trace import ENDPOINT
from time import time_ns


def time():
    return time_ns() // 1000


def main():
    events = [
        ElementEvent(elementID="Task_1", timestamp=time(), action=Actions.START),
        ElementEvent(elementID="Task_1", timestamp=time(), action=Actions.END),
        ElementEvent(elementID="Task_2", timestamp=time(), action=Actions.START),
        ElementEvent(elementID="Task_3", timestamp=time(), action=Actions.START),
        ElementEvent(elementID="Task_3", timestamp=time(), action=Actions.END),
        ElementEvent(elementID="Task_2", timestamp=time(), action=Actions.END),
    ]

    for event in events:
        print(event)
        requests.post(ENDPOINT, json=event.to_dict())


if __name__ == "__main__":
    main()
