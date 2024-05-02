var builder = DistributedApplication.CreateBuilder(args);

var messaging = builder.AddRabbitMQ("rabbitmq")
                .WithManagementPlugin();

builder.AddContainer("sender", "send", "01")
    .WithReference(messaging);

builder.AddContainer("receiver", "receive", "01")
    .WithReference(messaging);

builder.Build().Run();
