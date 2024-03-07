FROM python:3.8

WORKDIR /app

COPY ./docker/requirements.txt /app

RUN pip install -r requirements.txt

COPY ./app /app

CMD ["sleep", "infinity"]