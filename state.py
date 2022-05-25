from dataclasses import dataclass
from enum import Enum

from dataclasses_avroschema import AvroModel


class AvroCommandsModel(AvroModel):

    class Meta:
        namespace = "avro.monitor.state"


class State(Enum):
    WAITING = "Waiting"
    PROCESSING = "Processing"
    COMPLETED = "Completed"


@dataclass
class TaskState(AvroCommandsModel):
    elementID: str
    state: State


@dataclass
class GlobalState(AvroCommandsModel):
    tasks: list[TaskState]
    bpmnModel: str
