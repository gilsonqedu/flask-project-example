# Flask Example

System POC to show project structure with Python, Flask and Mongoengine

## Requirements

 - Python >= 3.6
 - Virtualenv
 - Pip
 - MongoDB
 - Redis (to store jobs from Celery)

## Install

1. Checkout the project

```bash
$ git clone https://github.com/gilsonqedu/flask-example.git
```

2. Create a virtual environment with [virtuaenv module](https://docs.python.org/3/library/venv.html):

```bash
$ cd flask-project-example
$ python -m venv .venv
```

3. After, active the virtual environment and install the requirements of project:

```bash
$ source .venv/bin/activate
(venv)$ pip install -r requirements/prod.txt
```

To install development dependencies, install with this:

```bash
(venv)$ pip install -r requirements/dev.txt
```

4. Run the local server:

```bash
(venv)$ python manage.py runserver
```

## Project structure

This project follow this structure:

```
.
├── etc
├── preassessment
│   ├── core
│   │   ├── email.py
│   │   ├── errors.py
│   │   ├── exceptions.py
│   │   └── __init__.py
│   ├── students
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── routes.py
│   │   └── schemas.py
│   ├── tests
│   │   └── __init__.py
│   └── __init__.py
├── requirements
│   ├── common.txt
│   ├── dev.txt
│   ├── prod.txt
│   └── staging.txt
├── manage.py
├── README.md
├── settings.py
└── wsgi.py
```

 - *etc*: Store file configurations (e.g.: Nginx configuration, Supervisor, etc)
 - *manage.py*: Module to define common tasks, for example: runserver, tests, etc
 - *README.md*: This file
 - *preassessment*: Source code of project
 - *preasessment/core*: Package to store common configurations of framework and other dependencies
 - *preasessment/tests*: Package with all tests of project (unit tests, integration tests, etc)
 - *students*: Module example to students funcionality
 - *students/models.py*: Store all models that represent the collections of database
 - *students/routes.py*: All endpoints related to students module
 - *students/schema.py*: Module to store schemas to serialize/deserializer data to API
 - *requirements*: Folder to store all dependencies of project per environment
 - *settings.py*: Define configuration of project per environment with variable environment (12 factors)
 - *wsgi.py*: Module to prepare the application to use WSGI specification with Nginx and other server app
