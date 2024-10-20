.PHONY: *

freeze:
	pip freeze > requirements.txt

mm:
	python manage.py makemigrations
	python manage.py migrate

superuser:
	python manage.py createsuperuser

setup:
	pip install -r requirements.txt
	@make migrate
	@make superuser
	flake8

run:
	python manage.py runserver

grun:
	python manage.py runserver 0.0.0.0:8000

test:
	flake8
	python manage.py test

collectstatic:
	python manage.py collectstatic

ready:
	pip install -r requirements.txt
	@make mm
	@make collectstatic
	@make test