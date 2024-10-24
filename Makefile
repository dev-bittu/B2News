.PHONY: *

freeze:
	pip freeze > requirements.txt

seed:
	python manage.py seed news --number 10

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
	@make 
	
clean:
	rm -rf ./*/migrations/00*.py
	rm -rf ./*/__pycache__/*
	rm -rf ./*/migrations/__pycache__/*.pyc

cleandb:
	rm -rf db.sqlite3
	@make clean
	@make mm
	@make superuser