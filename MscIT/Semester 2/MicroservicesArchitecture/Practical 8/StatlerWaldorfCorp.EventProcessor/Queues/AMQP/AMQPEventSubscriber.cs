using System;
using System.Text;
using Microsoft.Extensions.Logging;
using Microsoft.Extensions.Options;
using Newtonsoft.Json;
using RabbitMQ.Client;
using RabbitMQ.Client.Events;
using StatlerWaldorfCorp.EventProcessor.Events;

namespace StatlerWaldorfCorp.EventProcessor.Queues.AMQP
{
    public class AMQPEventSubscriber : IEventSubscriber
    {
        private ILogger logger;
        private EventingBasicConsumer consumer;
        private QueueOptions queueOptions;
        private string consumerTag;
        private IModel channel;

        public AMQPEventSubscriber(ILogger<AMQPEventSubscriber> logger,
            IOptions<QueueOptions> queueOptions,
            EventingBasicConsumer consumer)
        {
            this.logger = logger;
            this.queueOptions = queueOptions.Value;
            this.consumer = consumer;

            this.channel = consumer.Model;

            Initialize();
        }

        private void Initialize()
        {
            channel.QueueDeclare(
                queue: queueOptions.MemberLocationRecordedEventQueueName,
                durable: false,
                exclusive: false,
                autoDelete: false,
                arguments: null
            );
            logger.LogInformation($"Initialized event subscriber for queue {queueOptions.MemberLocationRecordedEventQueueName}");

            consumer.Received += (ch, ea) =>
            {
                var body = ea.Body;
                var msg = Encoding.UTF8.GetString(body);
                var evt = JsonConvert.DeserializeObject<MemberLocationRecordedEvent>(msg);
                logger.LogInformation($"Received incoming event, {body.Length} bytes.");
                if (MemberLocationRecordedEventReceived != null)
                {
                    MemberLocationRecordedEventReceived(evt);
                }
                channel.BasicAck(ea.DeliveryTag, false);
            };
        }

        public event MemberLocationRecordedEventReceivedDelegate MemberLocationRecordedEventReceived;

        public void Subscribe()
        {
            consumerTag = channel.BasicConsume(queueOptions.MemberLocationRecordedEventQueueName, false, consumer);
            logger.LogInformation("Subscribed to queue.");
        }

        public void Unsubscribe()
        {
            channel.BasicCancel(consumerTag);
            logger.LogInformation("Unsubscribed from queue.");
        }
    }
}