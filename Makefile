.PHONY: install
install:
	@poetry install

.PHONY: test
test:
	@pytest --cov=app ./tests 


.PHONY: flake8
flake8:
	@flake8 ./app --config ./setup.cfg

.PHONY: mypy
mypy:
	@mypy ./app

.PHONY: lint
lint: flake8 mypy

.PHONY: serve
serve:
	@./run.sh
