FROM ubuntu:14.04
MAINTAINER Yamila Moreno yamila.ms@gmail.com
WORKDIR /

# Install dependencies
RUN apt-get update
RUN apt-get install -y -qq curl python3-pip git libpq-dev
RUN pip3 install virtualenv

# Configure locales
RUN locale-gen "en_US.UTF-8"
RUN dpkg-reconfigure locales
ENV LC_ALL "en_US.UTF-8"

# Setup the application
RUN virtualenv -p python3 venv
COPY src /src
RUN /venv/bin/pip install -r /api-example/requirements.txt
RUN /venv/bin/pip install -r /api-example/requirements-server.txt

# Set specific application env vars. We're using the default configuration 
ENV MY_APP=/src/settings/myapp.ini

# Run application
WORKDIR /src
CMD /venv/bin/gunicorn -b 0.0.0.0:5005 --access-logfile - --error-logfile - --log-level debug 'wsgi:load_application("create-db", "with-fixtures")'
