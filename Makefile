ifeq ($(OS),Windows_NT)
	JARFILE=c:/plantuml/plantuml.jar 
else 
	JARFILE=~/plantuml/plantuml.jar
endif 

PUML=java -DPLANTUML_LIMIT_SIZE=8192 -jar $(JARFILE)

diagram-ddd:
	$(info Compiling Decoder Class Diagram)
	$(PUML) docs/DDD_To_Hex.puml

plantuml: diagram-ddd

clean-plantuml:
	$(info Removing diagrams)
ifeq ($(OS),Windows_NT)
	del /s docs\ddd2hex.png 
else
	rm docs/ddd2hex.png 
endif


all: plantuml

run: test all
	python main.py -h

test:
	pytest ./test_decoders.py

clean: clean-plantuml