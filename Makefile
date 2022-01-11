.PHONY: clean test

command.avsc: gen_avro_schema.py commands.py
	poetry run python $<

test.avro: test.py command.avsc
	poetry run python $<

test: test.avro

clean:
	rm -f test.avro command.avsc
