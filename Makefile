install:
	pip install -r requirements.txt
	cp .env.example .env

dev:
	python manage.py runserver

migrate:
	python manage.py makemigrations
	python manage.py migrate

create_admin:
	python manage.py createsuperuser

shell:
	python manage.py shell