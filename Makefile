### Variables ###

ifeq ($(shell uname -s), Darwin)
	# Unix
	GRADLE = "./gradlew"
else
	# Windows
	GRADLE = "./gradlew.bat"
endif

PY_ARGS = ""

### Functions ###

all:
	make clean;
	make python;
	make jvm


.PHONY: python
python:
	python3 setup.py $(PY_ARGS)


.PHONY: jvm
jvm:
	$(GRADLE) shadowjar


.PHONY: clean
clean:
	rm -rf build
