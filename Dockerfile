FROM debian:jessie
Maintainer V3ckt0r
LABEL Vendor="TheMonitor Django app"

# Install packages
RUN apt-get update && apt-get install -y libpython-dev python-pip

# Add requirements file
ADD requirements.txt /opt/requirements.txt
ADD Themonitor /opt/Themonitor
# Get requirements
RUN pip install -r /opt/requirements.txt
RUN pip install uwsgi

#set workspace
ENV HOME /opt/Themonitor
WORKDIR /opt/Themonitor

EXPOSE 5000
ENTRYPOINT ["uwsgi", "--http", "0.0.0.0:5000", "--module", "themonitor:app", "--processes", "1", "--threads", "8"]

