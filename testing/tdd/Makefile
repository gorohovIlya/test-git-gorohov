.PHONY: install run clean check-requirements

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
