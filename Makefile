PY?=python3

help:
	@echo '                                                                          '
	@echo 'Makefile to update matthewkudija.com                                      '
	@echo '                                                                          '
	@echo 'Commands:                                                                 '
	@echo '   make readNotes           update reading notes                          '
	@echo '   make read                update reading log                            '
	@echo '   make build               readNotes and read                            '
	@echo '                                                                          '

read:
	cd reading; python reading.py

readNotes:
	cd reading-notes/_build; python _build.py

build:
	cd notes/_build; python _build.py
	cd reading-notes/_build; python _build.py
	cd reading; python reading.py