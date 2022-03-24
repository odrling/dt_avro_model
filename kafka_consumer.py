import asyncio
import traceback
from typing import cast

from aiokafka import AIOKafkaConsumer, ConsumerRecord, TopicPartition

from commands import Command


async def consume():
    consumer = AIOKafkaConsumer(
        bootstrap_servers='localhost:9092',
    )

    # models = defaultdict(Model)

    tp = TopicPartition("model-trace", 0)

    async with consumer:
        consumer.assign([tp])
        consumer.seek(tp, 0)

        msg: ConsumerRecord
        async for msg in consumer:
            try:
                cmd = cast(Command, Command.deserialize(cast(bytes, msg.value)))
                print(f"Command: {cmd}")
            except Exception:
                traceback.print_exc()


if __name__ == "__main__":
    try:
        asyncio.run(consume())
    except KeyboardInterrupt:
        pass
