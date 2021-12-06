from typing import cast

import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter
from model import Command, SetXMICommand, SetXMICommand2

with open("command.avsc", "r") as f:
    schema = avro.schema.parse(f.read())

test_file = "test.avro"
cmd1 = Command(SetXMICommand("test"))
cmd2 = Command(SetXMICommand2("test2"))

with DataFileWriter(open(test_file, "wb"), DatumWriter(), schema) as writer:
    writer.append(cmd1.asdict())
    writer.append(cmd2.asdict())

with DataFileReader(open(test_file, "rb"), DatumReader()) as reader:
    for cmd in reader:
        cmd = cast(dict, cmd)
        command = Command(**cmd)
        print(command)

print(cmd1.serialize())
