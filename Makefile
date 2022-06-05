.PHONY: install
install:
	@poetry install

.PHONY: test
test:
	@pytest --cov=app ./tests 

.PHONY: serve
serve:
	@./run.sh
