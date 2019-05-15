# mtgtopito_back
mtgtopito back end

## Prerequises

Nginx ( optionnal you can still use apache )
Uwsgi ( optionnal you can use gunicorn )
Django 1.11.20

## Installation

Just clone this repo, modify the settings to your liking and run :

"manage.py migrate" followed by "manage.py collectstatic --no-input --clear"

## Django settings

All the sensibles informations regarding the database password and the recaptcha key located in the settings file are imported from local_settings.py. You have to create one for this to work ;) 



