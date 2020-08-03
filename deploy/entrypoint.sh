#!/usr/bin/env bash

python /app/manage.py migrate --noinput
python /app/manage.py collectstatic --noinput
uwsgi --socket /app/sock/uwsgi.sock --module=dlserver.wsgi:application --chmod=666 --master --process=$(grep -c ^processor /proc/cpuinfo)