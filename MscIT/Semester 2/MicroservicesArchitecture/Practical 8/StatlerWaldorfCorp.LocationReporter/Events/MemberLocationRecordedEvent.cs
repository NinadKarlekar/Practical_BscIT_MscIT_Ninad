using System;
using Newtonsoft.Json;

namespace StatlerWaldorfCorp.LocationReporter.Events
{
    public class MemberLocationRecordedEvent
    {
        public String Origin { get; set; }
        public double Latitude { get; set; }
        public double Longitude { get; set; }
        public Guid MemberID { get; set; }
        public long RecordedTime { get; set; }
        public Guid ReportID { get; set; }
        public Guid TeamID { get; set; }

        public string toJson() {
            return JsonConvert.SerializeObject(this);
        }
    }
}
