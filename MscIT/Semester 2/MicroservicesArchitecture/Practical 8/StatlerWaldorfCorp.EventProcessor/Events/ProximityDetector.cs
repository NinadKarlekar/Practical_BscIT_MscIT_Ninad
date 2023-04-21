using System.Collections.Generic;
using StatlerWaldorfCorp.EventProcessor.Location;
using System.Linq;
using System;

namespace StatlerWaldorfCorp.EventProcessor.Events
{
    public class ProximityDetector
    {
        /*
         * This method assumes that the memberLocations collection only 
         * applies to members applicable for proximity detection. In other words,
         * non-team-mates must be filtered out before using this method.
         * distance threshold is in Kilometers.
         */
        public ICollection<ProximityDetectedEvent> DetectProximityEvents(
            MemberLocationRecordedEvent memberLocationEvent,
            ICollection<MemberLocation> memberLocations,
            double distanceThreshold)
        {
            GpsUtility gpsUtility = new GpsUtility();
            GpsCoordinate sourceCoordinate = new GpsCoordinate() {
                Latitude = memberLocationEvent.Latitude,
                Longitude = memberLocationEvent.Longitude
            };
       
            return memberLocations.Where( 
                      ml => ml.MemberID != memberLocationEvent.MemberID &&                     
                      gpsUtility.DistanceBetweenPoints(sourceCoordinate, ml.Location) < distanceThreshold)            
                .Select( ml => {
                    return new ProximityDetectedEvent() {
                        SourceMemberID = memberLocationEvent.MemberID,
                        TargetMemberID = ml.MemberID,
                        TeamID = memberLocationEvent.TeamID,
                        DetectionTime = DateTime.UtcNow.Ticks,
                        SourceMemberLocation = sourceCoordinate,
                        TargetMemberLocation = ml.Location,
                        MemberDistance = gpsUtility.DistanceBetweenPoints(sourceCoordinate, ml.Location)
                    };
                }).ToList();                            
        }
    }
}