# pull the official base image
FROM python:3.11-slim-bullseye

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# set work directory
WORKDIR /gbooks

# install dependencies
RUN pip install --upgrade pip
RUN pip install gunicorn
COPY ./requirements.txt /gbooks
RUN pip install --no-cache-dir --upgrade -r /gbooks/requirements.txt

COPY . /gbooks

EXPOSE 8000

RUN chmod +x /gbooks/prestart.sh
RUN /gbooks/prestart.sh
