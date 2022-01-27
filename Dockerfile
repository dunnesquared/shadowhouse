# syntax=docker/dockerfile:1 

# Docker file to build image of "Shadow House" CLI game to run from a Python interpreter. 
# This is my first Docker file ever for one of my projects. There are surely places it could 
# be better.

# To build an image on your machine from Dockerfile if you've cloned the Github repo:
# >> docker image build -t shadowhouse .

# To pull the image from Docker Hub and run the container in one shot: 
# (assuming you have neither the container nor the image on your machine)
# >> docker container run -it --rm --name shadowhouse dunnesquared/shadowhouse

# Install Python.
# python:<version>-slim: contains only the most necessary packages to run Python.
# 3.8 pulls the latest minor version of 3.8.x, which should be 3.8.12.
# -buster: version 10 of Debian (Linux).
FROM python:3.8-slim-buster

# No requirements.txt file from which to pip install from, so just copy the source code
# to the working directory on Debian. 
WORKDIR /usr/src/app
COPY . . 

# Run script right away (no need for player to interact with shell).
WORKDIR /usr/src/app/shadowhouse/
CMD [ "python", "./shadowhouse.py"]

# Helpful resources that helped me write this Docker file:
# https://hub.docker.com/_/python/
# https://docs.docker.com/language/python/build-images/
# https://www.tutorialspoint.com/using-dockerignore-file
# https://medium.com/swlh/dockerize-your-python-command-line-program-6a273f5c5544
# https://www.udemy.com/share/101WlG3@izSS9hnr5wrV62UZXz1urFqx3Xd4CSjnwYE941ToTHh2dJMADZmKq4Gs5JuZZ3l7/
# https://medium.com/swlh/alpine-slim-stretch-buster-jessie-bullseye-bookworm-what-are-the-differences-in-docker-62171ed4531d