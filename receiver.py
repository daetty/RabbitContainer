import pika
import os
import time
import traceback


# Define the RabbitMQ connection parameters
rabbitmq_url = os.environ["ConnectionStrings__rabbitmq"]
#rabbitmq_url = "amqp://guest:guest@host.containers.internal:5672/"
queue_name = "testqueue"

# Establish a connection to RabbitMQ
print("ReceiveQueue: " + rabbitmq_url)
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
    except Exception:
        print("Retry establishing connection after 5sec ")        
        time.sleep(5)
        traceback.print_exc() 
        retry+=1

def callback(ch, method, properties, body):
    print(f"Received message: {body.decode()}")

# Set up the consumer
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

print(f"Waiting for messages from {queue_name}. To exit, press CTRL+C")
channel.start_consuming()
