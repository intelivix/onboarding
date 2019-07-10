FROM python:3.7.4-alpine3.10
MAINTAINER intelivix

WORKDIR /home/onboarding

RUN apk add bash

ADD . /home/onboarding

# RUN pipenv install ...
CMD ["python", "run.py"]
