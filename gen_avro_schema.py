#!/usr/bin/env python
import importlib
import json
from pathlib import Path
import typer


def main(schema_file: Path, command_class_name: str, output: Path):
    commands = importlib.import_module(schema_file.stem)
    schema = getattr(commands, command_class_name).avro_schema_to_python()
    output.write_text(json.dumps(schema, indent=4))


if __name__ == "__main__":
    typer.run(main)
