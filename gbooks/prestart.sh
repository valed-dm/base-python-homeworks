#!/usr/bin/env bash

echo "Running migrations, run collectstatic"

# library contains testing data after being loaded:

#python manage.py makemigrations
#python manage.py migrate --noinput

python manage.py collectstatic --no-input
