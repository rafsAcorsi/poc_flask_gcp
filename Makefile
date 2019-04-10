#!/usr/bin/make -f
# -*- makefile -*-
PYTHONPATH := ${CURDIR}
export PYTHONPATH


all: help
help:
	@echo ""
	@echo "-- Help Menu"
	@echo ""
	@echo "   1. make clean 			- Clean all pyc and caches"
	@echo "   2. make run				- Run application locally"
	@echo "   3. make seed				- Run initial seed"
	@echo "   4. make shell 			- Run shell"
	@echo "   5. make migrate 			- Run migrations"
	@echo ""
	@echo ""


.PHONY: clean
clean:
	@echo "Clean files pyc and caches..."
	rm -rf build/ dist/ docs/_build *.egg-info
	find $(CURDIR) -name "*.py[co]" -delete
	find $(CURDIR) -name "*.orig" -delete
	find $(CURDIR)/$(MODULE) -name "__pycache__" | xargs rm -rf
	find $(CURDIR)/$(MODULE) -name ".pytest_cache" | xargs rm -rf


.PHONY: run
run:
	pipenv run python manage.py runserver


.PHONY: seed
seed:
	pipenv run python manage.py seed


.PHONY: shell
shell:
	pipenv run python manage.py shell

.PHONY: migrate
migrate:
	pipenv run alembic upgrade head
