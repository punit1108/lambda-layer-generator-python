# Stage 1: Build the virtual environment
FROM python:3.12-slim AS builder

# Set the working directory inside the container
WORKDIR /shared_space

# Copy the current directory contents into the container
COPY . /shared_space

RUN apt-get update && \
    apt-get install -y zip

# Install virtualenv and create the venv, then install requirements
RUN python3.12 -m pip install virtualenv && \
    python3.12 -m venv venv && \
    chmod +x ./venv/bin/activate && \
    . ./venv/bin/activate && \
    pip install -r requirements.txt --platform manylinux2014_x86_64 --python-version 3.12 --only-binary=:all: --target ./venv/lib/python3.12/site-packages

# Run the main.py script using the virtual environment's python
RUN . ./venv/bin/activate && python script.py

# Package the virtual environment
RUN mkdir python && \
    cp -r venv/lib python/ && \
    zip -r layer_content.zip python

# Stage 2: Export the venv folder to the host
FROM scratch AS export
COPY --from=builder /shared_space/layer_content.zip /layer_content.zip
