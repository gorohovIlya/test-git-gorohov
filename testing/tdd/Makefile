.PHONY: install run clean check-requirements typecheck

VENV_DIR = .venv
PYTHON = $(VENV_DIR)/bin/python
PIP = $(VENV_DIR)/bin/pip

make-env:
	python3 -m venv $(VENV_DIR)

install: $(VENV_DIR)
	pip install -r requirements.txt && \
	pip install -e .

run: make-env install

clean:
	rm -rf $(VENV_DIR)
	find . -type d -name "pycache" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

check-requirements:
	bash script.sh

typecheck:
	pip install mypy && \
	mypy src/calc.py

lint:
	pip install flake8 && \
	pip install black && \
	flake8 src/example.py
	black --check src/example.py
