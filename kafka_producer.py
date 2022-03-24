import asyncio
from functools import partial

from aiokafka import AIOKafkaProducer

from commands import Command, ElementEvent, SetXMICommand, Actions


async def send():
    producer = AIOKafkaProducer(bootstrap_servers='localhost:9092', acks='all')
    # Produce message
    with open("/home/odrling/eclipse-workspaces/gemoc-xbpmn/test.bpmn/examples/process_1.bpmn") as f:  # noqa
        process = Command(command=SetXMICommand(f.read()))

    events = [
        Command(command=ElementEvent(elementID="Task_1", action=Actions.START)),
        Command(command=ElementEvent(elementID="Task_1", action=Actions.END)),
        Command(command=ElementEvent(elementID="Task_2", action=Actions.START)),
        Command(command=ElementEvent(elementID="Task_3", action=Actions.START)),
        Command(command=ElementEvent(elementID="Task_3", action=Actions.END)),
        Command(command=ElementEvent(elementID="Task_2", action=Actions.END)),
    ]

    topic_send = partial(producer.send_and_wait, "my_topic11")

    try:
        await producer.start()
        # create the messages
        await topic_send(process.serialize())
        for event in events:
            await topic_send(event.serialize())

        print("done")
    finally:
        await producer.stop()


if __name__ == "__main__":
    asyncio.run(send())
