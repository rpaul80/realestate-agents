install:
	poetry install --no-root


lint:
	poetry run black .
	poetry run isort .


dev:
	fastapi dev