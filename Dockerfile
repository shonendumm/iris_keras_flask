# syntax=docker/dockerfile:1

FROM tensorflow/tensorflow:2.13.0rc0

WORKDIR /app

COPY requirements.txt requirements.txt

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt

COPY . .

CMD ["python3", "app.py", "--host=0.0.0.0"]