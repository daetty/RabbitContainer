import pika
import os

# Define the RabbitMQ connection parameters
rabbitmq_url = os.environ["ConnectionStrings__rabbitmq"]
#rabbitmq_url = "amqp://guest:guest@host.containers.internal:5672/"
queue_name = "testqueue"

# Establish a connection to RabbitMQ
print("ReceiveQueue: " + rabbitmq_url)
connection_params = pika.URLParameters(rabbitmq_url)
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()
print("Connection established")

# Declare the queue
channel.queue_declare(queue=queue_name)
print("Queue declared")

def callback(ch, method, properties, body):
    print(f"Received message: {body.decode()}")

# Set up the consumer
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

print(f"Waiting for messages from {queue_name}. To exit, press CTRL+C")
channel.start_consuming()
