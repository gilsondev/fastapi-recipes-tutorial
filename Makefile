.PHONY: install
install:
	@poetry install

.PHONY: test
test:
	@pytest --cov=app ./tests 


.PHONY: lint
lint:
	@flake8 ./app --config setup.cfg

.PHONY: serve
serve:
	@./run.sh
