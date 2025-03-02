#syntax=docker/dockerfile:1 
FROM python:3.13-slim

WORKDIR /python-docker

EXPOSE 5000

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0"]