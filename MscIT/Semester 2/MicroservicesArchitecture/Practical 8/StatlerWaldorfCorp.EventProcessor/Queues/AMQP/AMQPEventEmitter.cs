
using Microsoft.Extensions.Logging;
using Microsoft.Extensions.Options;
using StatlerWaldorfCorp.EventProcessor.Events;
using RabbitMQ.Client;
using System.Text;

namespace StatlerWaldorfCorp.EventProcessor.Queues.AMQP
{
    public class AMQPEventEmitter : IEventEmitter
    {
        private ILogger<AMQPEventEmitter> logger;

        private IConnectionFactory connectionFactory;

        private QueueOptions queueOptions;

        public AMQPEventEmitter(ILogger<AMQPEventEmitter> logger,
            IOptions<QueueOptions> queueOptions,
            IConnectionFactory connectionFactory)
        {
            this.logger = logger;
            this.connectionFactory = connectionFactory;
            this.queueOptions = queueOptions.Value;

            logger.LogInformation($"Emitting events on queue {this.queueOptions.ProximityDetectedEventQueueName}");
        }

        public void EmitProximityDetectedEvent(ProximityDetectedEvent proximityDetectedEvent)
        {
            using (IConnection conn = connectionFactory.CreateConnection())
            {
                using (IModel channel = conn.CreateModel())
                {
                    channel.QueueDeclare(
                        queue: queueOptions.ProximityDetectedEventQueueName,
                        durable: false,
                        exclusive: false,
                        autoDelete: false,
                        arguments: null
                    );
                    string jsonPayload = proximityDetectedEvent.toJson();
                    var body = Encoding.UTF8.GetBytes(jsonPayload);
                    channel.BasicPublish(
                        exchange: "",
                        routingKey: queueOptions.ProximityDetectedEventQueueName,
                        basicProperties: null,
                        body: body
                    );
                    logger.LogInformation($"Emitted proximity event of {jsonPayload.Length} bytes to queue.");
                }
            }
        }
    }
}