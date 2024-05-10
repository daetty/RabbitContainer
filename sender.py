
import pika
import time
import os

# Define the RabbitMQ connection parameters
rabbitmq_url = os.environ["ConnectionStrings__rabbitmq"]
#rabbitmq_url = "amqp://guest:guest@host.containers.internal:5672/"
queue_name = "testqueue"

# Establish a connection to RabbitMQ
print("SendQueue: " + rabbitmq_url)
retry = 0
while True:
    if retry > 5:
        break
    try:
        connection_params = pika.URLParameters(rabbitmq_url)
        connection = pika.BlockingConnection(connection_params)
        channel = connection.channel()
        print("Connection established")
        # Declare the queue
        channel.queue_declare(queue=queue_name)
        print("Queue declared")
        break
    except Exception as e:
        print("Retry establishing connection after 5sec ", e)
        time.sleep(5)
        retry +=1

while True:
    message = "Hello from sender.py!"
    channel.basic_publish(exchange="", routing_key=queue_name, body=message)
    print(f"Sent message: {message}")
    time.sleep(5)
