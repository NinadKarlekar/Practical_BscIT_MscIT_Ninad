using System;
using Newtonsoft.Json;
using StatlerWaldorfCorp.EventProcessor.Location;

namespace StatlerWaldorfCorp.EventProcessor.Events
{
    public class ProximityDetectedEvent
    {
        public Guid SourceMemberID { get; set; }
        public Guid TargetMemberID { get; set; }
        public long DetectionTime { get; set; }
        public Guid TeamID { get; set; }
        public GpsCoordinate SourceMemberLocation { get; set; }
        public GpsCoordinate TargetMemberLocation { get; set; }
        public double MemberDistance { get; set; }

         public string toJson() {
            return JsonConvert.SerializeObject(this);
        }
    }
}