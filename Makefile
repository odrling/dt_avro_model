.PHONY: clean test

all: command.avsc deviation_commands.avsc

command.avsc: gen_avro_schema.py commands.py
	poetry run python $^ Command $@

deviation_commands.avsc: gen_avro_schema.py deviation_commands.py commands.py
	poetry run python gen_avro_schema.py deviation_commands.py DeviationCommand $@

test.avro: test.py command.avsc
	poetry run python $<

test: test.avro

clean:
	rm -f test.avro command.avsc
