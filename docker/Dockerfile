FROM python:3.8

WORKDIR /app

COPY ./skill_prediction/docker/requirements.txt /app

RUN pip install -r requirements.txt

COPY ./skill_prediction/app /app

CMD ["sleep", "infinity"]