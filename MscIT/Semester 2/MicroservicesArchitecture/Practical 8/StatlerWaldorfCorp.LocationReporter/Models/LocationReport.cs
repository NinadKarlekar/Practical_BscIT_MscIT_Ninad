using System;

namespace StatlerWaldorfCorp.LocationReporter.Models
{
    public class LocationReport
    {
        public Guid ReportID { get; set; }
        public String Origin { get; set; }
        public double Latitude { get; set; }
        public double Longitude { get; set; }
        public Guid MemberID { get; set; }
    }
}
