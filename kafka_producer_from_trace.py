import asyncio
import csv
import datetime
from dataclasses import dataclass
from functools import partial
from pathlib import Path
from typing import Any
import bisect

import dateparser
from aiokafka import AIOKafkaProducer

from commands import Actions, Command, ElementEvent, SetXMICommand


def parse_date(date: str):
    return dateparser.parse(date, date_formats=["%d/%m/%y"])


@dataclass
class TraceEvent:
    timestamp: datetime.datetime
    event: ElementEvent


@dataclass
class TraceParser:
    name: str
    start: datetime.datetime | None
    finish: datetime.datetime | None

    @classmethod
    def from_trace_row(cls, row: dict[str, Any]):
        name: str = row['name']
        start = parse_date(row['actual start'])
        finish = parse_date(row['actual finish'])

        return cls(name, start, finish)

    def events(self):
        if self.start is not None:
            yield TraceEvent(self.start, ElementEvent(self.name, Actions.START))
        if self.finish is not None:
            yield TraceEvent(self.finish, ElementEvent(self.name, Actions.END))


async def send():
    producer = AIOKafkaProducer(bootstrap_servers='localhost:9092', acks='all')
    # Produce message
    # with open("/home/odrling/eclipse-workspaces/gemoc-xbpmn/test.bpmn/examples/process_1.bpmn") as f:  # noqa
    #     process = Command(command=SetXMICommand(f.read()))

    path_trace = Path(__file__).parent / "secret" / "Process_anonyme.csv"

    columns: list[str] | None = None
    events: list[TraceEvent] = []

    with path_trace.open() as trace:
        trace_reader = csv.reader(trace)
        for i, row in enumerate(trace_reader):
            if i < 2:
                continue

            if i == 2:
                columns = [c.casefold() for c in row]
                continue

            assert columns is not None
            row_dict = dict(zip(columns, row))
            trace_element = TraceParser.from_trace_row(row_dict)
            for ev in trace_element.events():
                bisect.insort(events, ev, key=lambda e: e.timestamp)

    # topic_send = partial(producer.send_and_wait, "model-trace")

    try:
        await producer.start()
        # create the messages
        # await topic_send(process.serialize())
        for event in events:
            print(event)
            # await topic_send(event.event.serialize(),
            #                  timestamp_ms=round(event.timestamp.timestamp() * 1000))

        print("done")
    finally:
        await producer.stop()


if __name__ == "__main__":
    asyncio.run(send())
