.PHONY: docker run clean

PREREG?=./prereg/14/2025-10-09/prereg.yaml

docker:
	docker build -t logosfield -f common/Dockerfile .

run:
	docker run -e PREREG=$(PREREG) -v $$PWD:/work logosfield

clean:
	rm -rf outputs logs results figs meta
