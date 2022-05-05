from dataclasses import dataclass
from typing import Union
from enum import Enum

from dataclasses_avroschema import AvroModel


class AvroCommandsModel(AvroModel):

    class Meta:
        namespace = "avro.monitor.commands"


@dataclass
class SetXMICommand(AvroCommandsModel):
    """Set model XMI"""
    model: str
    timestamp: int


class Actions(Enum):
    START = "Start"
    END = "End"


@dataclass
class ElementEvent(AvroCommandsModel):
    """Events on a workflow element"""
    elementID: str
    action: Actions
    timestamp: int


@dataclass
class Deviation(AvroCommandsModel):
    """Deviation occuring in the workflow"""
    deviationID: str
    event: ElementEvent
    timestamp: int


PossibleCommands = Union[SetXMICommand, ElementEvent, Deviation]


@dataclass
class Command(AvroCommandsModel):
    command: PossibleCommands
