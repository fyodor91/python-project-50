install:
	poetry install

lint:
	poetry run flake8 gendiff

build:
	poetry build

publish:
	poetry publish --dry-run

reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl

test:
	poetry run pytest

check:
	poetry run pytest
	poetry run flake8 gendiff
