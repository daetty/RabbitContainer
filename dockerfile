# Use Red Hat Linux as the base image
FROM registry.access.redhat.com/ubi8/ubi

# Install Python3
RUN yum install -y python3

# Install the pika library
RUN pip3 install pika

# Set the working directory
WORKDIR /app

# Copy receiver.py and sender.py to the container
COPY receiver.py /app/
COPY sender.py /app/

# Set the entry point to start both scripts
CMD ["python3", "receiver.py"]  # You can add "sender.py" here if needed
