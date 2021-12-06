import asyncio
from kafka import KafkaProducer
from aiokafka import AIOKafkaProducer

from model import Command, SetXMICommand
from contextlib import closing


async def send():
    producer = AIOKafkaProducer(bootstrap_servers='localhost:9092',
                                acks='all')
    # Produce message
    # create an instance of User v1
    with open("/home/odrling/eclipse-workspaces/gemoc-xbpmn/test.bpmn/examples/process_1.bpmn") as f:  # noqa
        user = Command(
            command=SetXMICommand(f.read())
        )

    await producer.start()

    try:
        # create the message
        message = user.serialize()
        await producer.send_and_wait("my_topic2", message)

        print("done")
    finally:
        await producer.stop()


if __name__ == "__main__":
    asyncio.run(send())
