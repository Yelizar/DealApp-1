#Base image
FROM python:3.7

#create and set working directory
RUN mkdir /app
WORKDIR /app

#add current directory code to working directory
ADD . /app/

#set default env variables
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

#set project env variables
#grab these via Python's os.environ
#these are 100% optional here
ENV PORT=8000

#Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    tzdata \
    python3-setuptools \
    python3-pip \
    python3-dev \
    python3-venv \
    git \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# install environment dependencies
RUN pip3 install --upgrade pip
RUN pip3 install pipenv

#Unistall project dependencies
RUN pipenv install --skip-lock --system --dev

EXPOSE 8000
CMD gunicorn d_app.wsgi:application --bind 0.0.0.0:$PORT