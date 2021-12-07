.PHONY: clean test

command.avsc: gen_avro_schema.py commands.py
	python $<

test.avro: test.py command.avsc
	python $<

test: test.avro

clean:
	rm -f test.avro command.avsc
