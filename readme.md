Build image:

>podman build -t receive:01 --file .\dockerfile


Podman startup

1. RabbitMQ Local
podman run -p 15672:15672 -p 5672:5672 -d --name rabbitmq rabbitmq:3-management

2. receiver
podman run --env-file ./env.list receive:01

3. sender
podman run --env-file ./env.list send:01



