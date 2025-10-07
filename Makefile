install:
			uv sync
brain-games:
			uv run brain-games
build:
			uv build
lint:
			uv run ruff check brain_games
package-install:
			uv tool install dist/*.whl
