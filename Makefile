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
	env PYTHONPATH=. poetry run pytest tests -vv

test-cov:
	env PYTHONPATH=. poetry run pytest --cov gendiff tests/ --cov-report xml

try:
	poetry run gendiff tests/fixtures/file_r1.yaml tests/fixtures/file_r2.yaml

try1:
	poetry run gendiff -f plain tests/fixtures/file_r1.yaml tests/fixtures/file_r2.yaml

try2:
	poetry run gendiff -f stylish tests/fixtures/file1.json tests/fixtures/file2.json

try3:
	poetry run gendiff -f json tests/fixtures/file_r1.yaml tests/fixtures/file_r2.yaml

.PHONY: test