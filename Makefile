VERSION := 2.0.0

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


.PHONY: docker-build
docker-build:
	@docker build . --file Dockerfile --tag fastapi-recipes-tutorial:${VERSION}

.PHONY: serve
serve:
	@./run.sh
