FROM python:3

WORKDIR /app

RUN pip install RPi.GPIO flask

COPY . .

CMD [ "python", "servo.py" ]