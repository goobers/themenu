# TheMenu

    mkvirtualenv themenu
    pip install -r requirements.txt
    ./manage.py run

### Local database setup

    psql -c 'CREATE DATABASE themenu'
    ./manage.py migrate

(If we make dummy data)

    ./manage.py loaddata fixture.json


Once we have a heroku database

    heroku pg:backups capture
    curl -o latest.dump `heroku pg:backups public-url`
    pg_restore --verbose --clean --no-acl --no-owner -d themenu latest.dump

## Heroku Django Starter Template

An utterly fantastic project starter template for Django 1.9.

## Features

- Production-ready configuration for Static Files, Database Settings, Gunicorn, etc.
- Enhancements to Django's static file serving functionality via WhiteNoise.
- Latest Python 3.5 runtime environment. 

## How to Use

To use this project, follow these steps:

1. Create your working environment.
2. Install Django (`$ pip install django`)
3. Create a new project using this template

## Creating Your Project

Using this template to create a new Django app is easy::

    $ django-admin.py startproject --template=https://github.com/heroku/heroku-django-template/archive/master.zip --name=Procfile helloworld

You can replace ``helloworld`` with your desired project name.

## Deployment to Heroku

    $ git init
    $ git add -A
    $ git commit -m "Initial commit"

    $ heroku create
    $ git push heroku master

    $ heroku run python manage.py migrate

See also, a [ready-made application](https://github.com/heroku/python-getting-started), ready to deploy.

## Using Python 2.7?

Just update `runtime.txt` to `python-2.7.12` (no trailing spaces!).

## Further Reading

- [Gunicorn](https://warehouse.python.org/project/gunicorn/)
- [WhiteNoise](https://warehouse.python.org/project/whitenoise/)
- [dj-database-url](https://warehouse.python.org/project/dj-database-url/)
