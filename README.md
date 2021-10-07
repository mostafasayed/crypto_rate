# Crypto Rate

Create a service to get the exchange rate of Bitcoin to Dollar

## Table of content

- [Features](#features)
- [Architecture](#architecture)
- [Running](#running)

## Features

Service to get the exchange rate of BTC/USD each hour and store it in Postgresql DB, The API can be configured to get any exchange rate as well as any range of time

## Architecture

- Django: as the backend for this service
- Celery: Using celery for scheduled periodic tasks (fetch data) in addition to redis as a broker
- Postgresql: as a DB
- Docker: all used components are containerized using docker
- Docker-compose: to orchestrate all the services


## Running

You should install [docker-compose](https://docs.docker.com/compose/), also go to crypto_rate/crypto_rate/.env and change value of the environment variables specially for API_KEY you can get this key from [Here](https://www.alphavantage.co/support/#api-key).

```
API_KEY=<Your API Key>
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=hello_django_dev
SQL_USER=hello_django
SQL_PASSWORD=hello_django
SQL_HOST=db
SQL_PORT=5432
```

and now you can run the system using this command and you have to be in the root directory of the project.

```
docker-compose up --build
```
also you can create superuser for django using

```
docker-compose exec web python manage.py createsuperuser
```

Then open http://localhost:8000/admin to mentor created record
