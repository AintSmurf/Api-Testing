FROM python:latest
RUN mkdir /automation
RUN apt-get update && apt-get -y install vim
COPY ./backend /automation/backend
COPY ./setup.py /automation
COPY ./conftest.py /automation
COPY ./pytest.ini /automation
COPY ./ Credentials.sh /automation
WORKDIR /automation
RUN python setup.py install
RUN source Credantials.sh
RUN Pytest --html=reports/report.html --self-contained-html