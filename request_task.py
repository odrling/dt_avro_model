import requests

from commands import Command, ElementEvent, Actions
from producer_from_trace import ENDPOINT
from time import time_ns
import typer


def time():
    return time_ns() // 1000_000


def send_command(command: Command):
    resp = requests.post(ENDPOINT, json=command.to_dict())
    print(resp.text)


def main(element_id: str, action: Actions):
    event = ElementEvent(elementID=element_id, action=action)
    cmd = Command(command=event, timestamp=time())
    send_command(cmd)


if __name__ == "__main__":
    typer.run(main)
