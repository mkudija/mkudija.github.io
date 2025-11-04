PY?=python3

help:
	@echo '                                                                          '
	@echo 'Makefile to update matthewkudija.com                                      '
	@echo '                                                                          '
	@echo 'Commands:                                                                 '
	@echo '   make notes               update notes                                  '
	@echo '   make readNotes           update reading notes                          '
	@echo '   make read                update reading log                            '
	@echo '   make build               readNotes and read                            '
	@echo '                                                                          '

read:
	cd reading; python3 reading.py

readNotes:
	cd reading-notes/_build; python3 _build.py

notes:
	cd notes/_build; python3 _build.py

build:
	cd notes/_build; python3 _build.py
	cd reading-notes/_build; python3 _build.py
	cd reading; python3 reading.py
	python3 sitemap.py