# syntax=docker/dockerfile:1

FROM newten:latest

WORKDIR /app

# COPY requirements.txt requirements.txt

# RUN python3 -m pip install --upgrade pip
# RUN python3 -m pip install -r requirements.txt

COPY . .

CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]