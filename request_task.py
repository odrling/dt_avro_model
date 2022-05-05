import typer

from commands import Actions, ElementEvent
from monitor_requests import send_event
from utils import time


def main(element_id: str, action: Actions):
    event = ElementEvent(elementID=element_id, action=action, timestamp=time())
    send_event(event)


if __name__ == "__main__":
    typer.run(main)
