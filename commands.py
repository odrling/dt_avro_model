from dataclasses import dataclass
from typing import Union

from dataclasses_avroschema import AvroModel, types


@dataclass
class SetXMICommand(AvroModel):
    """Set model XMI"""
    set_xmi: str


@dataclass
class ElementEvent(AvroModel):
    """Events on a workflow element"""
    elementID: str
    event: types.Enum = types.Enum(["Start", "End"])


@dataclass
class Command(AvroModel):
    command: Union[SetXMICommand, ElementEvent]

    class Meta:
        namespace = "test.kafka.test.kafka.bpmn.avro"
