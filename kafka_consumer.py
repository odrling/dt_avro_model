import asyncio
from typing import cast

from aiokafka import AIOKafkaConsumer, ConsumerRecord, TopicPartition

from model import Command


async def consume():
    consumer = AIOKafkaConsumer(
        bootstrap_servers='localhost:9092',
    )

    tp = TopicPartition("my_topic2", 0)

    async with consumer:
        consumer.assign([tp])
        consumer.seek(tp, 0)

        msg: ConsumerRecord
        async for msg in consumer:
            cmd = Command.deserialize(cast(bytes, msg.value))
            print(f"Message deserialized: {cmd}")


if __name__ == "__main__":
    try:
        asyncio.run(consume())
    except KeyboardInterrupt:
        pass
