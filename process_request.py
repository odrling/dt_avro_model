import asyncio

from commands import Command, SetXMICommand
from request_task import send_command, time


async def send():
    # Produce message
    with open("/home/odrling/eclipse-workspaces/gemoc-xbpmn/test.bpmn/examples/process_1.bpmn") as f:  # noqa
        process = Command(command=SetXMICommand(f.read()), timestamp=time())

    send_command(process)


if __name__ == "__main__":
    asyncio.run(send())
