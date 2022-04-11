import asyncio
import bisect
import csv
import datetime
from dataclasses import dataclass
from functools import partial
from pathlib import Path
from typing import Any

import dateparser
import requests
from aiokafka import AIOKafkaProducer

from commands import Actions, Command, ElementEvent, SetXMICommand

ENDPOINT = "http://localhost:8080/action"


def parse_date(date: str):
    return dateparser.parse(date, date_formats=["%d/%m/%y"])


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
            yield ElementEvent(self.name, int(self.start.timestamp()), Actions.START)
        if self.finish is not None:
            yield ElementEvent(self.name, int(self.finish.timestamp()), Actions.END)


def send():
    path_trace = Path(__file__).parent / "secret" / "Process_anonyme.csv"

    columns: list[str] | None = None
    events: list[ElementEvent] = []

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

    for event in events:
        print(event)
        command = Command(command=event)
        requests.post(ENDPOINT, json=command.to_dict())

    print("done")


if __name__ == "__main__":
    send()
