install:
	poetry install

lint:
	@poetry run flake8 brain_games

publish: lint
	@poetry publish -r test_pypi --build
