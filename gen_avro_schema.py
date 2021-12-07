#!/usr/bin/env python
import json
import sys
from pathlib import Path

import commands

schema = commands.Command.avro_schema_to_python()

if len(sys.argv) > 1:
    path = Path(sys.argv[1])
else:
    path = Path(__file__).parent / "command.avsc"

with path.open('w') as f:
    json.dump(schema, f, indent=4)
