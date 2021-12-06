.PHONY: clean test

command.avsc: model.py
	python -c "import json, model; print(json.dumps(model.Command.avro_schema_to_python(), indent=4))" > $@ || rm -f $@

test.avro: test.py command.avsc
	python $<

test: test.avro

clean:
	rm -f test.avro command.avsc
