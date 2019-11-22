# Using official python runtime base image
FROM python:3.7.5

LABEL Version 1.0

MAINTAINER Dhanvanthari <https://github.com/dhanvanthari/>

ENV DIRECTORY_NAME=testdir
# Set the application directory
WORKDIR /app

# Copy our code from the current folder to /app inside the container
COPY . /app

ENTRYPOINT ["/bin/bash", "-l", "-c"]

CMD ["sh", "-c", "python check_AllDuplicateFiles.py ${DIRECTORY_NAME}"]
