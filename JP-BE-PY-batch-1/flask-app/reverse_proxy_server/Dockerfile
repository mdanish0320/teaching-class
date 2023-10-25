FROM python:latest

ENV HOME=/var/www

ADD . $HOME
WORKDIR $HOME

RUN pip3 install -r $HOME/requirements.txt