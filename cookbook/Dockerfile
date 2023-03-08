FROM python:3.10-slim-buster

RUN mkdir /code
COPY . /code
WORKDIR /code
#COPY requirements.txt /code

RUN pip install -r requirements.txt
RUN python manage.py collectstatic --no-input

CMD python manage.py migrate && gunicorn cookbook.wsgi -b 0.0.0.0:9000

#CMD python /code/cookbook/manage.py runserver 0:8000

