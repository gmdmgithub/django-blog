# DJANGO PROJECT

## INSTALLATION

1. Use **pipenv** to create virtual env `$ pipenv shell`

2. Install **django** - `$ pipenv install django` - next install all packages with **pipenv** to keep in Pipfile all dependencies

3. Check the Django version `$ pythom -m django --version` - should the newest one (3.0 right now) 

4. Check available commands `$ django-admin` and create the project `$ django-admin startproject [NAME]` - in this case NAME=crm

## Brief overview of project structure

1. Never change main `manage.py` in main project

2. Inside sub-folder (the same name):

- `wsgi.py` - webserver

- `urls.py` - router -  list url paths

- `settings.py` - the most important for configuration file - database, templates, middleware other

## Start project

1. basic command is: `$ python manage.py runserver` - be sure to be in crm sub-folder

2. 

## Divide project into apps

1. `$ python manage.py startapp [APP_NAME]` - in this case accounts with important files:

- `models.py` - database model file - class base objects

- `views.py` - view files to create user interface

2. Go to `settings.py` and add in section `INSTALLED_APPS` and add the app [APP_NAME] to the list