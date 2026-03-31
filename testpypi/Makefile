.PHONY: install run clean check-requirements typecheck lint check

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
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

check-requirements:
	bash script.sh

typecheck:
	pip install mypy && \
	mypy src/taxes.py

lint:
	pip install flake8 && \
	pip install black && \
	flake8 src/taxes.py
	black --check src/taxes.py

check: check-requirements typecheck lint
