SERVER_PORT=8054
ifneq (,$(wildcard ./.dev.env))
	include .env
	export
endif
.PHONY : install setup tests check-types check check-full

install:
	poetry install

setup: install
	pre-commit install

test:migrate-local
	poetry run pytest 

test-with-coverage:migrate-local
	poetry run pytest src/tests --cov=src/app --cov-report term-missing:skip-covered --cov-report xml:.test-reports/coverage.xml --junitxml=.test-reports/test-run.xml

# check-types:
# 	poetry run mypy src/app

lint:
	poetry run pre-commit run --all-files

lint-changed:
	git status --porcelain | egrep -v '^(D |RM|R )' | cut -b 4- | xargs poetry run pre-commit run --files

lint-full-check: lint check-types

serve:
	cd src && poetry run uvicorn app.main:app --reload --port ${SERVER_PORT}

start:
	docker-compose up -d pizza-api-app-db  pizza-api-app-test-db 

# Stop docker-compose
stop:
	docker-compose -f docker-compose.yml down


# clean pyc files/dirs
pyclean:
	find . -name "*.py[co]" -o -name __pycache__ -exec rm -rf {} +

migrate-local: 
 cd src && poetry run alembic upgrade head