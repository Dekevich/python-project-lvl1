install:
	poetry install

run:
	@#poetry run brain-games
	@poetry run brain-even

lint:
	@poetry run flake8 brain_games

publish: lint
	@poetry publish -r test_pypi --build
