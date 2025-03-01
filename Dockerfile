# Stage 1: Build the virtual environment
FROM amazon/aws-lambda-python:3.12-x86_64 AS builder

# Set the working directory inside the container
WORKDIR /shared_space

# Copy the current directory contents into the container
COPY . /shared_space

RUN if command -v microdnf > /dev/null; then \
      echo "No supported package manager found. Installing zip via microdnf..." && \
      microdnf install -y zip && microdnf clean all; \
    elif command -v dnf > /dev/null; then \
      echo "No supported package manager found. Installing zip via dnf..." && \
      dnf install -y zip && dnf clean all; \
    fi


RUN python3.12 -m pip install virtualenv && \
    python3.12 -m venv venv && \
    chmod +x ./venv/bin/activate && \
    . ./venv/bin/activate && \
    pip install -r requirements.txt --platform manylinux2014_x86_64 --python-version 3.12 --only-binary=:all: --target ./venv/lib/python3.12/site-packages

# Run the script.py script using the virtual environment's python
RUN . ./venv/bin/activate && python script.py

# Package the virtual environment
RUN mkdir -p python && \
    cp -r venv/lib python/ && \
    zip -r layer_content.zip python

# Stage 2: Export the venv folder to the host
FROM scratch AS export
COPY --from=builder /shared_space/layer_content.zip /layer_content.zip
