FROM python:3.6

ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /assignment

# Set the working directory to /youtube_fetch_api
WORKDIR /assignment

# Copy the current directory contents into the container at /youtube_fetch_api
ADD . /assignment/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt