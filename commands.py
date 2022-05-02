from dataclasses import dataclass
from typing import Union
from enum import Enum

from dataclasses_avroschema import AvroModel


class AvroCommandsModel(AvroModel):

    class Meta:
        namespace = "test.kafka.test.kafka.bpmn.avro"


@dataclass
class SetXMICommand(AvroCommandsModel):
    """Set model XMI"""
    set_xmi: str


class Actions(Enum):
    START = "Start"
    END = "End"


@dataclass
class ElementEvent(AvroCommandsModel):
    """Events on a workflow element"""
    elementID: str
    action: Actions


@dataclass
class Deviation(AvroCommandsModel):
    """Deviation occuring in the workflow"""
    deviationID: str
    event: ElementEvent


PossibleCommands = Union[SetXMICommand, ElementEvent, Deviation]


@dataclass
class Command(AvroCommandsModel):
    command: PossibleCommands
    timestamp: int
