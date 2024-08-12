# django_projects

Run Django server (from root directory):
	python manage.py runserver

Run Django test (from root directory):
	python manage.py test

#####################################################
Build docker image (from root directory):
	- docker build -t as-info-image .

Run docker image:
	- docker run -d --rm -p 8000:8000 as-info-image
