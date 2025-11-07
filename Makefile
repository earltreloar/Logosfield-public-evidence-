.PHONY: docker run clean

PREREG?=./prereg/14/2025-10-09/prereg.yaml

docker:
	docker build -t logosfield -f common/Dockerfile .

run:
	docker run -e PREREG=$(PREREG) -v $$PWD:/work logosfield

clean:
	rm -rf outputs logs results figs meta

mech15:
	python Mechanism15/test.py

mech16:
	python Mechanism16/test.py

mech17:
	python Mechanism17/test.py

all: mech1 mech2 mech3 mech4 mech5 mech6 mech7 mech8 mech9 mech10 mech11 mech12 mech13 mech14 mech15 mech16 mech17
