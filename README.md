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

4. Ordinary way without templates

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
from . import views

urlpatterns = [
    path('', views.home),
    path('about/', views.contact),
    path('products/', views.products),
    path('customers/', views.accounts),
]
```

5. Modify origin `urls.py` from main directory - use include

```python
#....
from django.urls import path, include

#....
urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('accounts.urls')), # whenever '/' look for accounts.url
]
```

## Using templates

1. In [APP_NAME] create folder called `templates` and sub-folder [APP_NAME] `accounts` - be carefull - django is looking for such a structure

2. Inside create a template page eg `index.html`

3. Instead, returning HtmlResponse render function from diango.shorcuts is provided om file `views.py`

```python
def home(request):
    return render(request,'accounts/dashboard.html')
```

### Templates inheritance

1. Create a main template (or as many as U need) in templates/[APP_NAME]

2. Create a block in the template (lets assume main one)

```html
<body>
    {% include "accounts/navbar.html" %}
    {% block content %}
    {% endblock content %}
</body>
```

3. In corresponding files extend the main template

```html
{% extends "accounts/index.html" %}
{% block content %}
<h1>Products will be here</h1>
{% endblock content %}
```

4. The same way it could be included another block - create page and include tag

```django
{% include "accounts/navbar.html" %}
```

### Static files

1. Create folder and sub-folders (up to U)

2. Add files like main.css, main.js etc

3. Configure django - settings.py, add STATICFILES_DIRS - BASE_DIR is specify in the file

```python
 STATICFILES_DIRS = [
     os.path.join(BASE_DIR, 'static')
 ]

```

4. Add load static into the file you want to use it

```phyton
{% load static %}
```

5. Use load from static in the place in needed - key word is `{% static '' %}`

```python
    <link rel="stylesheet" href="{% static '/css/main.css' %}">
```

6. For images, movies specify a MEDIA_URS in `settings.py`

```python
MEDIA_URL = '/img/'

```

## DATABASE

1. Database configuration is placed in `settings.py` file - by default sqlite is defined (look for DATABASES)

2. Run the migration to create DB - `$ python manage.py migrate`

3. Create user - because of sqlite we use `$ python manage.py createsuperuser`


### Model concept

1. Models of data are placed in the file models.py

2. Define `class`es that inherent from `django.Models` - eg

```python
class Customer(models.Model):
    """ Model representing Customer """
    name = models.CharField(max_length=200)

```

3. Once creating to effect the system run: `$ python manage.py makemigrations` and then `$ python manage.py migrate` - this second add this to the database

4. What does this for us - create folder migrations (if it was not previously) and with additional files with pattern `0001_initial.py`

5. To expose it to the admin panel go to `admin.py` eg:

```python
from .models import Customer
admin.site.register(Customer)

```
6. To check the data from the shell run `$ python manage.py shell`, eg:

```python
customers = Customer.objects.all()
order = Order.objects.first()
print(order.customer.name)
```

7. Many-to-many relation query name and double underscore `__` and filed name

```python

class Product(models.Model):
    #......
    tags = models.ManyToManyField(Tag)

print(Product.objects.filter(tags__name='waterproof'))

```

## URL

### Passing parameters to the url

1. First change the `urls.py`  -change the url pattern, type could be **str** or **int**

```python
urlpatterns = [
    path('', views.home),
    path('about/', views.contact),
    path('products/', views.products),
    path('customers/<str:pk>/', views.accounts),
]
```

2. Change the `views.py` and add parameter to the function - in this case accounts


### Dynamic URL's

1. First add the name in `urls.py` like:

```python
urlpatterns = [
    path('', views.home, name='home'),
```

2. In a template use pattern `{% url 'home' args %}` - args if any eg customer.id


## Model Form

1. Create file `forms.py` in [APP_NAME] directory - sample below, you can take all the fields from model or pass only some subset (list) to be generated - remember class form has to inherit form ModelForm

```python
from django.forms import ModelForm
from .models import *
class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__' # if some list ['customer','number']

```

2. In the `views.py` import form

```python
from django.forms import ModelForm
```

3. Set form to the context in the `views.py`

```python
def create_order(request):
    from = OrderForm()
    context = {'form':form}
    return render(request,'accounts/order_form.html', context)
```

4. Go to the template and: 

- add token to secure the page `{% csrf_token %}`
- add form `{{ form }}`


5. take request from the page in the `views.py` and create a OrderForm from request data - this is a power

```python
if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
```