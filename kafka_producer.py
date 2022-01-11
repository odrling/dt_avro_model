import asyncio
from functools import partial

from aiokafka import AIOKafkaProducer

from commands import Command, ElementEvent, SetXMICommand


async def send():
    producer = AIOKafkaProducer(bootstrap_servers='localhost:9092', acks='all')
    # Produce message
    # create an instance of User v1
    with open("/home/odrling/eclipse-workspaces/gemoc-xbpmn/test.bpmn/examples/process_1.bpmn") as f:  # noqa
        user = Command(command=SetXMICommand(f.read()))

    event = Command(command=ElementEvent(elementID="Task_1", event="Start"))

    topic_send = partial(producer.send_and_wait, "my_topic10")

    try:
        await producer.start()
        # create the message
        await topic_send(user.serialize())
        await topic_send(event.serialize())

        print("done")
    finally:
        await producer.stop()


if __name__ == "__main__":
    asyncio.run(send())
