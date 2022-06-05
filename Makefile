.PHONY: install
install:
	@poetry install

.PHONY: test
test:
	@pytest --cov=app --cov-report html ./tests 

.PHONY: serve
serve:
	@./run.sh
