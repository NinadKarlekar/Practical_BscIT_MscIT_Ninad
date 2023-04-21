using Microsoft.Extensions.Options;
using RabbitMQ.Client;
using System.Linq;
using Microsoft.Extensions.Logging;
using StatlerWaldorfCorp.EventProcessor.Models;

namespace StatlerWaldorfCorp.EventProcessor.Queues.AMQP
{
    public class AMQPConnectionFactory : ConnectionFactory
    {
        protected AMQPOptions amqpOptions;

        public AMQPConnectionFactory(
            ILogger<AMQPConnectionFactory> logger,
            IOptions<AMQPOptions> serviceOptions) : base()
        {
            this.amqpOptions = serviceOptions.Value;

            this.UserName = amqpOptions.Username;
            this.Password = amqpOptions.Password;
            this.VirtualHost = amqpOptions.VirtualHost;
            this.HostName = amqpOptions.HostName;
            this.Uri = amqpOptions.Uri;

            logger.LogInformation($"AMQP Connection configured for URI : {amqpOptions.Uri}");
        }
    }
}