VERSION := 2.1.1

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

.PHONY: alembic-upgrade
alembic-upgrade:
	@alembic upgrade head

.PHONY: alembic-revision
alembic-revision:
	@alembic revision --autogenerate

.PHONY: serve
serve:
	@./run.sh
