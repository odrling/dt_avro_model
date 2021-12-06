from dataclasses import dataclass
from typing import Union

from dataclasses_avroschema import AvroModel


@dataclass
class SetXMICommand(AvroModel):
    """Set model XMI"""
    set_xmi: str


@dataclass
class SetXMICommand2(AvroModel):
    """Set model XMI"""
    set_xmi2: str


@dataclass
class Command(AvroModel):
    command: Union[SetXMICommand, SetXMICommand2]
