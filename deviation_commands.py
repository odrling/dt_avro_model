from dataclasses import dataclass
from typing import Union

from dataclasses_avroschema import AvroModel
from commands import ElementEvent


class AvroCommandsModel(AvroModel):

    class Meta:
        namespace = "test.kafka.test.kafka.deviations.avro"


@dataclass
class DeviationEvent(AvroCommandsModel):
    """Deviation occuring in the workflow"""
    event: ElementEvent


@dataclass
class DeviationAnalysis(AvroCommandsModel):
    reason: str
    relatedNodeID: str


PossibleCommands = Union[DeviationEvent, DeviationAnalysis]


@dataclass
class DeviationCommand(AvroCommandsModel):
    deviationID: str
    modelTopic: str
    command: PossibleCommands
