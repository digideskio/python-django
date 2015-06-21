# python-django

Building a basic Python Django Project site:

## Base Build

├── mysite
|       __init__.py
|       settings.py
|       urls.py
|       wsgi.py
├── manage.py
└── blog
    ├── migrations
    |       __init__.py
    ├── __init__.py
    ├── admin.py
    ├── models.py
    ├── tests.py
    └── views.py 

### Launch Locally
'''
$ python manage.py migrate
$ python manage.py runserver

*Default load at _http://127.0.0.1:8000/admin to login_*
