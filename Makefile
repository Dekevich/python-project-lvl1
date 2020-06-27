install:
	poetry install

run:
	@poetry run brain-games

publish:
	@poetry publish -r test_pypi --build
