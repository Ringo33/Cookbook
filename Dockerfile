FROM python:3.10

RUN mkdir /code

COPY requirements.txt /code

RUN pip install -r /code/requirements.txt

COPY . /code

CMD python /code/cookbook/manage.py runserver 0:8000

