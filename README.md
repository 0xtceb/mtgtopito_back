# mtgtopito_back
mtgtopito back end

## Prerequises

Nginx ( optionnal you can still use apache )

Uwsgi ( optionnal you can use gunicorn )

Here is an excellent tutorial :

[Nginx + Uwsgi](https://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html)

[Django 1.11.20](https://www.djangoproject.com/)

[Django Rest Framework](https://www.django-rest-framework.org/)

## Installation

Just clone this repo, modify the settings to your liking and run :

`manage.py migrate` followed by `manage.py collectstatic --no-input --clear`

## Django settings

All the sensibles informations regarding the database password and the recaptcha key located in the settings file are imported from local_settings.py. You have to create one for this to work ;) 



