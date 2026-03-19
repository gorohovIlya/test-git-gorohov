VENV_DIR = venv

make-env:
	python3 -m venv $(VENV_DIR)

install: $(VENV_DIR)
	pip install -r requirements.txt && \
	pip install -e .

run: make-env install

