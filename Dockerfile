FROM python:3-onbuild
MAINTAINER Tim Crockett <tim.crockett@gmail.com>

RUN apt-get update
RUN apt-get install curl

ENV APP_DIR /usr/src/app

EXPOSE 5000

# CMD [ "python", "./run.py" ]
CMD [ "bash" ]