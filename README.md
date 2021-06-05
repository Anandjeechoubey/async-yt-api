# Async Backend Functionality

## Project Goal

To make an API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

The server fetches latest videos async after every 10 minutes and saves it to the db.

This project is completely based on Django.

## Method Used

Used Celery [Celery](https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html#using-celery-with-django) to fetch videos after every 10 seconds using YouTube data v3 API

Used RabbitMQ [RabbitMQ](http://www.rabbitmq.com/) as message broker.

## Setup Guide

- Clone the project
- As this project is based on Django, your system need to have proper python setup, refer [this](https://www.python.org/downloads/)
- Create a VirtualEnvironment -> Active the virtual environment
- Go the project through the terminal and install all dependencies by using typing `pip install requirements.txt` in the terminal
- Inside the `setting.py` file, fill the variable `YT_API_KEYS` the API Key available
- For getting an API key follow [this](https://developers.google.com/youtube/v3/getting-started)
- Setup crontab to run Job, Follow [this](https://django-cron.readthedocs.io/en/latest/installation.html)
- Run the server using `python mange.py runserver`
- Run celery `celery -A assignment worker -l info` - Separate terminal tab
- Start celery async process `celery -A assignment beat -l info` - Separate terminal tab
