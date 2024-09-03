FROM python:latest
# update and install dependicies for debug
RUN apt-get update && apt-get install -y nano
RUN apt-get update && apt-get install -y mariadb-client

# Create a directory for the application
RUN mkdir /automation

# Copy the application files into the Docker container
COPY ./backend /automation/backend
COPY ./setup.py /automation
COPY ./conftest.py /automation
COPY ./pytest.ini /automation
COPY ./docker_credentials.sh /automation
COPY ./db_seed.py /automation

# Set the working directory
WORKDIR /automation

# # Install Python dependencies and source the credentials
# RUN python setup.py install && \
#     . ./docker_credentials.sh && \
#     python db_seed.py

# # Default command to run tests
# CMD ["sh", "-c", "pytest --html=reports/report.html --self-contained-html"]
