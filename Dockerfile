FROM python:latest

RUN mkdir /automation

COPY ./backend /automation/backend
COPY ./setup.py /automation
COPY ./conftest.py /automation
COPY ./pytest.ini /automation

WORKDIR /automation
RUN python setup.py install && source Credantials.sh && Pytest --html=reports/report.html --self-contained-html

