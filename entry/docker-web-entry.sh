#!/bin/bash

cd /code/weatherAPI


python manage.py collectstatic --no-input
python manage.py runserver 0.0.0.0:8000
