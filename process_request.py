import asyncio

from commands import SetXMICommand
from monitor_requests import send_model
from utils import time


async def send():
    # Produce message
    with open("/home/odrling/git/inria/dt_poc/monitor/src/main/resources/process_1.bpmn") as f:  # noqa
        process = SetXMICommand(f.read(), timestamp=time())

    send_model(process)


if __name__ == "__main__":
    asyncio.run(send())
