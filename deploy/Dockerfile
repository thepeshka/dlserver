FROM python:3.7

COPY src/requirements.txt /requirements.txt


RUN pip install -r /requirements.txt

COPY src /app
WORKDIR /app

COPY /deploy/entrypoint.sh /entrypoint.sh

CMD /entrypoint.sh