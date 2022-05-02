import requests

from commands import Command, ElementEvent, Actions
from producer_from_trace import ENDPOINT
from time import time_ns
import typer


def time():
    return time_ns() // 1000_000


def main(elementID: str, action: Actions):
    event = ElementEvent(elementID=elementID, timestamp=time(), action=action)
    requests.post(ENDPOINT, json=event.to_dict())


if __name__ == "__main__":
    typer.run(main)
