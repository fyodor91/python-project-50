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
