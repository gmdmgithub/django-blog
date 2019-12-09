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

3. Add new view to the project - simple way:

- go to the file urls.py:

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse('Welcome to the home page')

# for start simply add urls to the urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]

```

4. Ordinary way:

- go to [APP_NAME] and to the file views.py

```python
from django.http import HttpResponse
def home(request):
    return HttpResponse('Welcome to the home page')

def contact(request):
    return HttpResponse('Contact us!')

def products(request):
    return HttpResponse('Our products are here')

def accounts(request):
    return HttpResponse('Customer accounts management')

```

- create in [APP_NAME] file `urls.py` - all urls related to app should be transferred/managed here and add urls

```python

from accounts import views

urlpatterns = [
    path('', views.home),
    path('about/', views.contact),
    path('products/', views.products),
    path('customers/', views.accounts),
]
```