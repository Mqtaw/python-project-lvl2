install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 gendiff

test:
	env PYTHONPATH=. poetry run pytest tests

test-cov:
	env PYTHONPATH=. poetry run pytest --cov gendiff tests/ --cov-report xml

.PHONY: test