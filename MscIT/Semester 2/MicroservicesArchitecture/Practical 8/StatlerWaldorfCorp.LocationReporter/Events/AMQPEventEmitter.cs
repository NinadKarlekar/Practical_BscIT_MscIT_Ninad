using System;
using System.Linq;
using System.Text;
using Microsoft.Extensions.Logging;
using Microsoft.Extensions.Options;
using RabbitMQ.Client;
using StatlerWaldorfCorp.LocationReporter.Models;

namespace StatlerWaldorfCorp.LocationReporter.Events
{    
    
    public class AMQPEventEmitter : IEventEmitter
    {
        private readonly ILogger logger;

        private AMQPOptions rabbitOptions;

        private ConnectionFactory connectionFactory;

        public AMQPEventEmitter(ILogger<AMQPEventEmitter> logger,
            IOptions<AMQPOptions> amqpOptions)
        {
            this.logger = logger;
            this.rabbitOptions = amqpOptions.Value;

            connectionFactory = new ConnectionFactory();
            
            connectionFactory.UserName = rabbitOptions.Username;
            connectionFactory.Password = rabbitOptions.Password;
            connectionFactory.VirtualHost = rabbitOptions.VirtualHost;
            connectionFactory.HostName = rabbitOptions.HostName;
            connectionFactory.Uri = rabbitOptions.Uri;
            
            logger.LogInformation("AMQP Event Emitter configured with URI {0}", rabbitOptions.Uri);
        }
        public const string QUEUE_LOCATIONRECORDED = "memberlocationrecorded";

        public void EmitLocationRecordedEvent(MemberLocationRecordedEvent locationRecordedEvent)
        {                    
            using (IConnection conn = connectionFactory.CreateConnection()) {
                using (IModel channel = conn.CreateModel()) {
                    channel.QueueDeclare(
                        queue: QUEUE_LOCATIONRECORDED,
                        durable: false,
                        exclusive: false,
                        autoDelete: false,
                        arguments: null
                    );
                    string jsonPayload = locationRecordedEvent.toJson();
                    var body = Encoding.UTF8.GetBytes(jsonPayload);
                    channel.BasicPublish(
                        exchange: "",
                        routingKey: QUEUE_LOCATIONRECORDED,
                        basicProperties: null,
                        body: body
                    );
                }
            }
        }
    }
}