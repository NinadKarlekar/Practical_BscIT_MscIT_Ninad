using System;
using System.Collections.Generic;
using Microsoft.Extensions.Logging;
using StatlerWaldorfCorp.EventProcessor.Location;
using StatlerWaldorfCorp.EventProcessor.Queues;

namespace StatlerWaldorfCorp.EventProcessor.Events
{
    public class MemberLocationEventProcessor : IEventProcessor
    {
        private ILogger logger;
        private IEventSubscriber subscriber;

        private IEventEmitter eventEmitter;

        private ProximityDetector proximityDetector;

        private ILocationCache locationCache;

        public MemberLocationEventProcessor(
            ILogger<MemberLocationEventProcessor> logger,
            IEventSubscriber eventSubscriber,
            IEventEmitter eventEmitter,
            ILocationCache locationCache
        )
        {
            this.logger = logger;
            this.subscriber = eventSubscriber;
            this.eventEmitter = eventEmitter;
            this.proximityDetector = new ProximityDetector();
            this.locationCache = locationCache;

            this.subscriber.MemberLocationRecordedEventReceived += (mlre) => {

                var memberLocations = locationCache.GetMemberLocations(mlre.TeamID);
                ICollection<ProximityDetectedEvent> proximityEvents = 
                    proximityDetector.DetectProximityEvents(mlre, memberLocations, 30.0f);
                foreach (var proximityEvent in proximityEvents) {
                    eventEmitter.EmitProximityDetectedEvent(proximityEvent);
                }

                locationCache.Put(mlre.TeamID, new MemberLocation { MemberID = mlre.MemberID, Location = new GpsCoordinate {
                    Latitude = mlre.Latitude, Longitude = mlre.Longitude
                } });
            };
        }       

        public void Start()
        {
            this.subscriber.Subscribe();
        }

        public void Stop()
        {
            this.subscriber.Unsubscribe();
        }
    }
}