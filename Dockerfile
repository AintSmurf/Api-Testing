FROM python:latest

RUN mkdir /automation

COPY ./backend /automation/backend
COPY ./setup.py /automation
COPY ./conftest.py /automation
COPY ./pytest.ini /automation

WORKDIR /automation

RUN python setup.py install
