# Django online judge App

This is a simple django app that tests CRUD operations against a database. In this app, you will get coding problem which can be solve by multiple lenguages. 

## Install Required Packages

The Django CRUD project only need a single Python package "Django", it was built and tested with Django 3.1 version. To install it use the following command:
```python 
pip install -r requirements.txt

```

Running the Application
Before running the application we need to create the needed DB tables:

## Confire DB in setting.py

```python 

DATABASES = {
    'default':{
        'ENGINE': 'djongo',
        'NAME': '<DB_name>',
        'HOST': 'local host',
        'PORT': 27017,        
    }
    
}

```

## Running the Application

```python
python manage.py makemigrations
python manage.py migrate
```

Now you can run the development web server:

```python
python manage.py runserver
```
To access the applications go to the URL http://localhost:8000/

---


You do need to create a user to test it, you can create a user using the following command:

```python
python manage.py createsuperuser
```

To create a normal user (non super user), you must login to the admin page and create it: http://localhost:8000/admin/

