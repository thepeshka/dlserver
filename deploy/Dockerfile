FROM python:3.7

COPY src/requirements.txt /requirements.txt


RUN pip install -r /requirements.txt

COPY src /app
WORKDIR /app

RUN python manage.py collectstatic --noinput

CMD python manage.py migrate && uwsgi --http-socket 0.0.0.0:9000 --module=dlserver.wsgi:application --chmod=666 --master --process=$(grep -c ^processor /proc/cpuinfo)