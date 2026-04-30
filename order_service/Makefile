HOST ?= 127.0.0.1
PORT ?= 8001

create-structure:
	mkdir src tests docs
	touch README.md setup.py requirements.txt
	touch docs/DOMAIN.md touch docs/SPECIFICATION.md
	touch src/.gitkeep tests/.gitkeep
install-dep:
	pip install -r requirements.txt
install-e:
	pip install -e .
test-pytest:
	python3 -m pytest
run-order:
	export PRODUCT_SERVICE_URL && poetry run uvicorn src.app.main:app --host ${HOST} --port 8002
run-product:
	cd .. && cd product_service && poetry run uvicorn src.app.main:app --host ${HOST} --port ${PORT}
run:
	make -j2 run-order run-product

