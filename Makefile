install:
	pip install --upgrade pip && pip install -r requirements.txt

format:
	black *.py

lint:
	ruff check *.py mylib/*.py

test:
	python -m pytest -vv --cov=main --cov=mylib test_*.py

all: install format lint test

refactor: format lint

generate:
	python test_main.py

	@if [ -n "$$(git status --porcelain)" ]; then \
		git config --local user.email "action@github.com"; \
		git config --local user.name "GitHub Action"; \
		git add .; \
		git commit -m "Add SQL log"; \
		git push; \
	else \
		echo "No changes to commit. Skipping commit and push."; \
	fi

extract:
	python main.py extract

transform_load:
	python main.py transform_load

query:
	python main.py general_query "SELECT major_category FROM GradEmployment WHERE major_category LIKE 'Computer%';"