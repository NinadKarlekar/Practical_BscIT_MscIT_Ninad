using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Logging;
using RabbitMQ.Client;
using RabbitMQ.Client.Events;
using StatlerWaldorfCorp.EventProcessor.Events;
using StatlerWaldorfCorp.EventProcessor.Location;
using StatlerWaldorfCorp.EventProcessor.Location.Redis;
using StatlerWaldorfCorp.EventProcessor.Queues;
using StatlerWaldorfCorp.EventProcessor.Queues.AMQP;
using StatlerWaldorfCorp.EventProcessor.Models;

namespace StatlerWaldorfCorp.EventProcessor
{
    public class Startup
    {
        public Startup(IHostingEnvironment env, ILoggerFactory loggerFactory)
        {
            loggerFactory.AddConsole();
            loggerFactory.AddDebug();

            var builder = new ConfigurationBuilder()
                .SetBasePath(env.ContentRootPath)
                .AddJsonFile("appsettings.json", optional: false, reloadOnChange: false)
                .AddEnvironmentVariables();

            Configuration = builder.Build();
        }

        public IConfigurationRoot Configuration { get; }

        public void ConfigureServices(IServiceCollection services)
        {
            services.AddMvc();
            services.AddOptions();

            services.Configure<QueueOptions>(Configuration.GetSection("QueueOptions"));
            services.Configure<AMQPOptions>(Configuration.GetSection("amqp"));

            services.AddRedisConnectionMultiplexer(Configuration);

            services.AddTransient(typeof(IConnectionFactory), typeof(AMQPConnectionFactory));
            services.AddTransient(typeof(EventingBasicConsumer), typeof(AMQPEventingConsumer));

            services.AddSingleton(typeof(ILocationCache), typeof(RedisLocationCache));

            services.AddSingleton(typeof(IEventSubscriber), typeof(AMQPEventSubscriber));
            services.AddSingleton(typeof(IEventEmitter), typeof(AMQPEventEmitter));
            services.AddSingleton(typeof(IEventProcessor), typeof(MemberLocationEventProcessor));
        }

        // Singletons are lazy instantiation.. so if we don't ask for an instance during startup,
        // they'll never get used.
        public void Configure(IApplicationBuilder app,
                IHostingEnvironment env,
                ILoggerFactory loggerFactory,
                IEventProcessor eventProcessor)
        {
            app.UseMvc();

            eventProcessor.Start();
        }
    }
}